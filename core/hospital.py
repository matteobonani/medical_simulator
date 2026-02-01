from medical_simulator.core.case_result import CaseResult
from medical_simulator.core.clock import Clock
from medical_simulator.core.disease import Disease
from medical_simulator.core.patient import Patient
from medical_simulator.core.treatment import Treatment
from medical_simulator.core.waiting_room import WaitingRoom


class Hospital:
    """
    Central orchestrator of the clinical simulation.

    Coordinates time progression, patient management, clinical actions,
    and scoring logic for a single simulation run.

    Parameters
    ----------
    clock : Clock
        Global simulation clock handling hours and days.
    waiting_room : WaitingRoom
        Container of all active patients.
    diseases : list[Disease]
        A list of all disease.
    treatments : list[Treatment]
        A list of all available diagnostic and therapeutic treatments.
    max_days : int, optional (default=5)
        Maximum number of days for the simulation.

    Attributes
    ----------
    total_score : int
        Total score accumulated during the simulation.
    daily_case_results : list[CaseResult]
        List of patient results for the current day.
    """

    def __init__(self, clock: Clock, waiting_room: WaitingRoom, diseases: list[Disease], treatments: list[Treatment], max_days=5):

        self.clock = clock
        self.waiting_room = waiting_room

        self.treatments = treatments
        self.diseases = diseases
        self.max_days = max_days
        self.total_score = 0

        self.daily_case_results: list[CaseResult] = []

    # -------------------------
    # Simulation flow
    # -------------------------

    def visit_patient(self, patient: Patient) -> None:
        """
        Handles the visit of a single patient.

        It runs a loop until the player returns to the waiting room, or the hospital day is over.
        """

        while not self.clock.is_day_over():

            if patient.is_dead():
                return

            patient.show_patient_status()
            self.show_available_actions()

            print("0) Back to waiting room")

            choice = input("\nChoose action: ").strip()

            if choice == "0":
                return

            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            choice_num = int(choice)
            total_actions = len(self.treatments) + 1

            if choice == total_actions:
                guess = input("Enter the disease name: ").strip()
                correct = patient.disease.name.lower() == guess.lower()
                patient.diagnosis_correct = correct
                if correct:
                    print(f"Correct! The patient had {patient.disease.name}.")
                    patient.health = min(100, patient.health + 10)
                    self.discharge_patient(patient)
                    self.waiting_room.remove_patient(patient)
                else:
                    print(f"Incorrect.")
                    patient.health -= 30
                    patient.health = max(0, patient.health)


            elif 1 <= choice_num < total_actions:
                for f in self.perform_action(patient, self.treatments[choice_num - 1]):
                    if not patient.is_dead():
                        print(f"- {f}")

    def start_new_day(self) -> None:
        self.clock.start_new_day()

    def is_simulation_over(self) -> bool:
        return self.clock.day >= self.max_days

    # -------------------------
    # Patient status
    # -------------------------

    def discharge_patient(self, patient: Patient) -> None:

        base_score = 100
        health_bonus = int(patient.health * 0.3)

        score = base_score + health_bonus

        self.daily_case_results.append(
            CaseResult(
                patient_name=patient.name,
                outcome="Discharged",
                score=score,
                notes=f"Health at discharge: {patient.health}"
            )
        )

    def unresolved_patient(self, patient: Patient) -> None:
        score = int(patient.health * 0.8)

        self.daily_case_results.append(
            CaseResult(
                patient_name=patient.name,
                outcome="Not discharged",
                score=score,
                notes="Patient still under observation"
            )
        )

    def patient_died(self, patient: Patient) -> None:
        self.daily_case_results.append(
            CaseResult(
                patient_name=patient.name,
                outcome="Died",
                score=-100,
                notes="Critical deterioration"
            )
        )
        self.waiting_room.remove_patient(patient)


    # -------------------------
    # Actions
    # -------------------------

    def advance_time(self, hours: int) -> None:
        for _ in range(hours):
            self.clock.advance(1)
            self.waiting_room.maybe_add_new_patients(self.clock.hour, self.diseases)

            for patient in list(self.waiting_room.patients):
                patient.advance_time(1)

                if patient.is_dead():
                    print(f"\nPatient {patient.name} has died.")
                    self.patient_died(patient)


    def show_available_actions(self) -> None:
        print("\nAvailable actions:")
        for i, t in enumerate(self.treatments, start=1):
            print(f"{i}) {t.name} ({t.time_cost}h) – {t.description}")

        print(f"{len(self.treatments) + 1}) Guess Disease")

    def perform_action(self, patient: Patient, treatment: Treatment):

        self.advance_time(treatment.time_cost)

        if patient.is_dead():
            return []

        t = treatment.test_type

        if t == "blood":
            print("\nBlood findings:")
            return patient.apply_blood_test()

        if t == "xray":
            print("\nX-Ray findings:")
            return patient.apply_xray()

        if t == "vitals":
            print("\nVital signs:")
            return patient.apply_vital_signs_test()

        if t == "ecg":
            print("\nECG findings:")
            return patient.apply_ecg()


        if treatment.effect > 0 or treatment.penalty > 0:
            if patient.disease.is_correct_treatment(treatment.name):
                patient.health += treatment.effect
                result = ["treatment effective"]
            else:
                patient.health -= treatment.penalty
                result = ["treatment ineffective"]

            patient.health = max(0, min(100, patient.health))
            return result

    def wait_and_observe(self, hours: int) -> None:
        print(f"\nWaiting for {hours} hour...")
        self.advance_time(hours)

    # -------------------------
    # Day end & scoring
    # -------------------------

    def end_day(self) -> None:

        # iterate over a copy of the patients to avoid skipping elements
        for p in list(self.waiting_room.patients):
            self.unresolved_patient(p)
            self.waiting_room.remove_patient(p)

        day_score = sum(r.score for r in self.daily_case_results)

        print("\n--- Day Summary ---")

        for r in self.daily_case_results:
            print(f"{r.patient_name}: {r.outcome} → {r.score} points")

        print(f"Total day score: {day_score}")

        self.total_score += day_score

        self.daily_case_results.clear()

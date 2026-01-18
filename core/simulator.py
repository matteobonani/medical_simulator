import random
from medical_simulator.core.patient import Patient


class Simulator:
    def __init__(self, diseases, treatments, max_days=5):
        self.diseases = diseases
        self.treatments = treatments
        self.max_days = max_days

        self.current_day = 0
        self.current_hour = 0
        self.patient = None

        self.daily_scores = []

    # -------------------------
    # Simulation flow
    # -------------------------

    def start_new_day(self):
        self.current_day += 1
        self.current_hour = 0

        disease = random.choice(self.diseases)
        self.patient = Patient(disease)

        print(f"\n=== Day {self.current_day} ===")

    def is_day_over(self):
        return self.current_hour >= 12 or not self.patient_is_stable()

    def is_simulation_over(self):
        return self.current_day >= self.max_days

    # -------------------------
    # Patient status
    # -------------------------

    def patient_is_stable(self):
        return self.patient.health > 0

    def show_patient_status(self):
        print("\nPatient status:")
        print(f"Health: {self.patient.health}")
        print(f"Hours elapsed: {self.current_hour}/12")

        print("\nClinical symptoms:")
        for s in self.patient.visible_symptoms:
            print(f"- {s}")

        if self.patient.discovered_blood_findings:
            print("\nBlood test findings:")
            for f in self.patient.discovered_blood_findings:
                print(f"- {f}")

        if self.patient.discovered_xray_findings:
            print("\nX-Ray findings:")
            for f in self.patient.discovered_xray_findings:
                print(f"- {f}")

    # -------------------------
    # Actions
    # -------------------------

    def show_available_actions(self):
        print("\nAvailable actions:")
        for i, t in enumerate(self.treatments, start=1):
            print(f"{i}) {t.name} ({t.time_cost}h) – {t.description}")

        print(f"{len(self.treatments) + 1}) Guess Disease and end day")

    def perform_action_by_index(self, index):
        if index < 1 or index > len(self.treatments):
            print("Invalid action.")
            return

        treatment = self.treatments[index - 1]
        self.perform_action(treatment)

    def perform_action(self, treatment):
        self.current_hour += treatment.time_cost
        self.patient.advance_time(treatment.time_cost)

        t = treatment.test_type

        if t == "blood":
            findings = self.patient.apply_blood_test()
            print("Blood test findings:" if findings else "Blood test normal.")
            for f in findings:
                print(f"- {f}")
            return

        if t == "xray":
            findings = self.patient.apply_xray()
            print("X-Ray findings:" if findings else "X-Ray normal.")
            for f in findings:
                print(f"- {f}")
            return

        if t == "vitals":
            vitals = self.patient.apply_vital_signs_test()
            print("Vital signs:")
            print(f"- Temperature: {vitals['temperature']} °C")
            print(f"- Systolic BP: {vitals['systolic_bp']} mmHg")
            return

        if t == "ecg":
            findings = self.patient.apply_ecg()
            print("ECG findings:" if findings else "ECG normal.")
            for f in findings:
                print(f"- {f}")
            return

        # Therapeutic actions
        if self.patient.disease.is_correct_treatment(treatment.name):
            self.patient.health += treatment.effect
            print("Treatment effective.")
        else:
            self.patient.health -= treatment.penalty
            print("Treatment ineffective.")

        self.patient.health = max(0, min(100, self.patient.health))

    # -------------------------
    # Day end & scoring
    # -------------------------

    def end_day(self):
        score = self.calculate_score()
        self.daily_scores.append(score)

        print("\n--- Day Summary ---")
        print(f"Final health: {self.patient.health}")
        print(f"Diagnosis correct: {self.patient.diagnosis_correct}")
        print(f"Score for the day: {score}")

    def calculate_score(self):
        score = 0

        # Health contribution (0–50)
        score += int(self.patient.health / 2)

        # Diagnosis bonus
        if self.patient.diagnosis_correct:
            score += 30

        # Efficiency bonus (less time = higher score)
        score += max(0, 20 - self.current_hour)

        return score

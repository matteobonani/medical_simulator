import random
from medical_simulator.core.disease import Disease


class Patient:

    """
    Patient obj in the clinical simulation.

    Health and symptoms evolve as simulation time advances.

    Parameters
    ----------
    disease : Disease
        The disease affecting the patient.

    Attributes
    ----------
    sex : str | None
        Patient's sex ('M' or 'F'), can be None initially.
    name : str | None
        Patient's name, can be None initially.
    age : int | None
        Patient's age, can be None initially.
    health : int
        Current health of the patient (0–100).
    time_elapsed : int
        Number of hours elapsed since patient arrival.
    visible_symptoms : list[str]
        Symptoms currently visible to the doctor.
    _revealed_symptoms : set[str]
        Internal set of symptoms that have already been revealed; used to avoid duplicating symptoms.
    discovered_blood_findings : list[str]
        Blood test findings discovered so far.
    discovered_xray_findings : list[str]
        X-ray findings discovered so far.
    discovered_ecg_findings : list[str]
        ECG findings discovered so far.
    vital_signs : dict
        Latest vital signs readings (temperature, systolic_bp).
    """

    def __init__(self, disease: Disease):
        self.sex = None
        self.name = None
        self.age = None

        self.disease = disease
        self.health = random.randint(
            disease.initial_health_range[0],
            disease.initial_health_range[1]
        )

        self.time_elapsed = 0
        self.visible_symptoms = []
        self._revealed_symptoms = set()

        self.discovered_blood_findings = []
        self.discovered_xray_findings = []
        self.discovered_ecg_findings = []
        self.vital_signs = {}

    # -------------------------
    # Patient status
    # -------------------------

    def is_dead(self) -> bool:
        return self.health <= 0

    def show_patient_status(self)  -> None:
        print(f"\n=== Visit {self.name} ===")
        print(f"Health: {self.health}")

    def show_patient_record(self)  -> None:

        print("\n=== Patient Record ===")
        print(f"Name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")

        print("\nSymptoms:")
        if self.visible_symptoms:
            for s in self.visible_symptoms:
                print(f"- {s}")
        else:
            print("- None")

        if self.vital_signs:
            print("\nVital signs:")
            print(f"- Temperature: {self.vital_signs['temperature']} °C")
            print(f"- Systolic BP: {self.vital_signs['systolic_bp']} mmHg")

        if self.discovered_blood_findings:
            print("\nBlood findings:")
            for f in self.discovered_blood_findings:
                print(f"- {f}")

        if self.discovered_xray_findings:
            print("\nX-Ray findings:")
            for f in self.discovered_xray_findings:
                print(f"- {f}")

        if self.discovered_ecg_findings:
            print("\nECG findings:")
            for f in self.discovered_ecg_findings:
                print(f"- {f}")

    # -------------------------
    # Time progression
    # -------------------------

    def advance_time(self, hours: int) -> None:
        self.time_elapsed += hours

        self._update_symptoms()

        decay = self.disease.severity * hours * random.uniform(0.5, 1.0)
        self.health -= decay
        self.health = max(0, int(self.health))



    def _update_symptoms(self)  -> None:

        for symptom in self.disease.symptoms_timeline:
            name = symptom["name"]
            from_hour = symptom["from_hour"]

            if self.time_elapsed >= from_hour and name not in self._revealed_symptoms:
                self.visible_symptoms.append(name)
                self._revealed_symptoms.add(name)

    # -------------------------
    # Diagnostic tests
    # -------------------------

    def apply_vital_signs_test(self)  -> dict[str, float]:

        # print("\nVital signs:")
        # print(f"- Temperature: {self.disease.base_temperature}")
        # print(f"- Systolic BP: {self.disease.base_systolic_bp}")

        self.vital_signs = {
            "temperature": self.disease.base_temperature,
            "systolic_bp": self.disease.base_systolic_bp
        }
        return self.vital_signs

    def apply_blood_test(self) -> list[str]:

        # print("\nBlood findings:")


        findings = self.disease.blood_findings.copy()
        if not findings:
            # print(f"normal blood test")
            findings = ["normal blood test"]

        for f in findings:
            if f not in self.discovered_blood_findings:
                # print(f"- {f}")
                self.discovered_blood_findings.append(f)

        return findings

    def apply_xray(self) -> list[str]:

        # print("\nX-Ray findings:")

        findings = self.disease.xray_findings.copy()
        if not findings:
            # print(f"normal chest x-ray")
            findings = ["normal chest x-ray"]

        for f in findings:
            if f not in self.discovered_xray_findings:
                # print(f"- {f}")
                self.discovered_xray_findings.append(f)

        return findings

    def apply_ecg(self) -> list[str]:

        # print("\nECG findings:")

        findings = getattr(self.disease, "ecg_findings", []).copy()
        if not findings:
            # print(f"normal ECG")
            findings = ["normal ECG"]

        for f in findings:
            if f not in self.discovered_ecg_findings:
                # print(f"- {f}")
                self.discovered_ecg_findings.append(f)

        return findings

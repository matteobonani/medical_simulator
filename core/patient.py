import random


class Patient:
    def __init__(self, disease):
        self.disease = disease

        self.health = random.randint(
            disease.initial_health_range[0],
            disease.initial_health_range[1]
        )

        self.time_elapsed = 0

        # Symptoms that are currently visible
        self.visible_symptoms = []

        # Track which symptoms have already appeared
        self._revealed_symptoms = set()

        self.discovered_blood_findings = []
        self.discovered_xray_findings = []
        self.discovered_ecg_findings = []
        self.vital_signs = {}

        # Initialize symptoms at time 0
        self._update_symptoms()

    # -------------------------
    # Time progression
    # -------------------------

    def advance_time(self, hours):
        self.time_elapsed += hours

        # Health decay depends on severity
        decay = self.disease.severity * hours * random.uniform(0.5, 1.0)
        self.health -= decay
        self.health = max(0, int(self.health))

        # Update symptoms as time passes
        self._update_symptoms()

    # -------------------------
    # Symptom progression
    # -------------------------

    def _update_symptoms(self):
        """
        Reveal symptoms whose activation time has been reached.
        """
        for symptom in self.disease.symptoms_timeline:
            name = symptom["name"]
            from_hour = symptom["from_hour"]

            if self.time_elapsed >= from_hour and name not in self._revealed_symptoms:
                self.visible_symptoms.append(name)
                self._revealed_symptoms.add(name)

    # -------------------------
    # Diagnostic tests
    # -------------------------

    def apply_vital_signs_test(self):
        if random.random() < 0.75:
            temperature = self.disease.base_temperature
            bp = self.disease.base_systolic_bp
        else:
            temperature = round(random.normalvariate(37, 0.8), 1)
            bp = random.randint(100, 140)

        self.vital_signs = {
            "temperature": temperature,
            "systolic_bp": bp
        }
        return self.vital_signs

    def apply_blood_test(self):
        findings = []

        if random.random() < 0.8 and self.disease.blood_findings:
            findings.append(random.choice(self.disease.blood_findings))

        if random.random() < 0.25:
            findings.append("non-specific inflammation")

        self.discovered_blood_findings.extend(
            f for f in findings if f not in self.discovered_blood_findings
        )
        return findings

    def apply_xray(self):
        findings = []

        if random.random() < 0.75 and self.disease.xray_findings:
            findings.append(random.choice(self.disease.xray_findings))

        if random.random() < 0.2:
            findings.append("non-specific shadow")

        self.discovered_xray_findings.extend(
            f for f in findings if f not in self.discovered_xray_findings
        )
        return findings

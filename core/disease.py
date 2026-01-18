class Disease:
    def __init__(
        self,
        name,
        symptoms_timeline,
        blood_findings,
        xray_findings,
        base_temperature,
        base_systolic_bp,
        severity,
        initial_health_range,
        correct_treatments
    ):
        self.name = name
        self.symptoms_timeline = symptoms_timeline
        self.blood_findings = blood_findings
        self.xray_findings = xray_findings
        self.base_temperature = base_temperature
        self.base_systolic_bp = base_systolic_bp
        self.severity = severity
        self.initial_health_range = initial_health_range
        self.correct_treatments = correct_treatments

    def is_correct_treatment(self, treatment_name):
        return treatment_name in self.correct_treatments

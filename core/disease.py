
class Disease:

    """
    Object that represents a disease.

    Attributes
    ----------
    name : str
        The name of the disease.
    symptoms_timeline : list[dict]
        List of symptom dictionaries with 'name' and 'from_hour', indicating when symptoms appear.
    blood_findings : list[str]
        List of blood test findings associated with the disease.
    xray_findings : list[str]
        List of X-ray findings associated with the disease.
    ecg_findings : list[str]
        List of ECG findings associated with the disease.
    base_temperature : float
        Base body temperature for patients with this disease.
    base_systolic_bp : float
        Base systolic blood pressure for patients with this disease.
    severity : float
        Severity factor affecting patient health decay over time.
    initial_health_range : tuple[int, int]
        Min and max initial health for a patient with this disease.
    correct_treatments : list[str]
        List of treatment names considered effective for this disease.
    """

    def __init__(
        self,
        name: str,
        symptoms_timeline: list[dict],
        blood_findings: list[str],
        xray_findings: list[str],
        ecg_findings: list[str],
        base_temperature: float,
        base_systolic_bp: float,
        severity: float,
        initial_health_range: tuple[int, int],
        correct_treatments: list[str]
    ):
        self.name = name
        self.symptoms_timeline = symptoms_timeline
        self.blood_findings = blood_findings
        self.xray_findings = xray_findings
        self.ecg_findings = ecg_findings
        self.base_temperature = base_temperature
        self.base_systolic_bp = base_systolic_bp
        self.severity = severity
        self.initial_health_range = initial_health_range
        self.correct_treatments = correct_treatments


    def is_correct_treatment(self, treatment_name: str) -> bool:
        return treatment_name in self.correct_treatments

class CaseResult:
    """
    Represents the result of a patient's case in the simulation, including outcome, score, and notes.

    Parameters
    ----------
    patient_name : str
        The name of the patient.
    outcome : str
        Outcome of the case (e.g., "Discharged", "Not discharged", "Died").
    score : int
        Points earned or lost for this case.
    notes : str
        Optional notes or comments about the case.
    """
    def __init__(self, patient_name: str, outcome: str, score: int, notes: str = ""):
        self.patient_name = patient_name
        self.outcome = outcome
        self.score = score
        self.notes = notes

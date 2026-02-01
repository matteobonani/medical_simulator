from typing import Any


class Treatment:
    """
    Object that represents a treatment or diagnostic action that can be performed on a patient.

    Attributes
    ----------
    name : str
        The name of the treatment or test.
    effect : int, optional (default=0)
        The positive effect on patient health if the treatment is correct.
    penalty : int, optional (default=0)
        The negative effect on patient health if the treatment is incorrect.
    time_cost : int, optional (default=1)
        The number of hours the treatment or test takes to perform.
    description : str, optional (default="")
        A brief description of the treatment or test.
    test_type : str or None, optional (default=None)
        The type of diagnostic test, e.g., "blood", "xray", "vitals", or "ecg".
    """
    def __init__(
        self,
        name,
        effect=0,
        penalty=0,
        time_cost=1,
        description="",
        test_type=None
    ):
        self.name = name
        self.effect = effect
        self.penalty = penalty
        self.time_cost = time_cost
        self.description = description
        self.test_type = test_type

    def info(self) -> dict[str, Any]:
        return {
            "Name": self.name,
            "Effect": self.effect,
            "Penalty": self.penalty,
            "Time cost (hours)": self.time_cost,
            "Test type": self.test_type,
            "Description": self.description
        }

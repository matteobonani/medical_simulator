class Treatment:
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

    def info(self):
        """
        Return a dictionary with the treatment's details.
        """
        return {
            "Name": self.name,
            "Effect": self.effect,
            "Penalty": self.penalty,
            "Time cost (hours)": self.time_cost,
            "Test type": self.test_type,
            "Description": self.description
        }

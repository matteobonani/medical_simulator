class Clock:
    """
    Represents the simulation clock, tracking days and hours in the hospital.

    Attributes
    ----------
    day : int
        The current day of the simulation.
    hour : int
        The current hour within the day (0–12).
    """
    def __init__(self):
        self.day = 0
        self.hour = 0

    def start_new_day(self) -> None:
        self.day += 1
        self.hour = 0

    def advance(self, hours: int) -> None:
        self.hour += hours

    def is_day_over(self) -> bool:
        return self.hour >= 12
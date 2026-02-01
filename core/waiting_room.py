from medical_simulator.core.disease import Disease
from medical_simulator.core.patient import Patient
import random
from medical_simulator.utils.utils import generate_random_patient
from typing import Optional


class WaitingRoom:

    """
    Hospital waiting room that holds patients.

    Parameters
    ----------
    capacity : int
        Maximum number of patients that can be in the waiting room.

    Attributes
    ----------
    patients : list[Patient]
        List of patients currently in the waiting room.
    """

    def __init__(self, capacity: int):
        self.patients = []
        self.capacity = capacity

    def show_patients(self) -> None:
        print("\n--- Waiting Room ---")
        for i, p in enumerate(self.patients, start=1):
            print(f"{i}) {p.name}")

    def get_patient(self, index: int) -> Optional[Patient]:
        if 0 <= index < len(self.patients):
            return self.patients[index]
        return None

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def remove_patient(self, patient: Patient) -> None:
        self.patients.remove(patient)

    def maybe_add_new_patients(self, current_hour: int, diseases: list[Disease]) -> None:

        if current_hour < 1:
            return

        max_add = self.capacity - len(self.patients)
        if max_add <= 0:
            return

        if current_hour < 7 and random.random() < 0.5:
            new_patient = generate_random_patient(diseases)
            self.add_patient(new_patient)
            print(f"New patient arrived: {new_patient.name}")




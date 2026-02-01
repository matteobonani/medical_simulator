from medical_simulator.core.hospital import Hospital
from medical_simulator.utils.utils import generate_random_patient


class SimulatorController:

    """
    Controls the flow of the clinical decision-making simulation.

    This class manages the day-to-day simulation, user interactions, and actions to the Hospital instance.

    Attributes
    ----------
    hospital : Hospital
        The hospital instance for the simulation.
    """

    def __init__(self, hospital: Hospital):
        self.hospital = hospital

    def run(self) -> None:
        print("Clinical Decision-Making Simulator")
        print("---------------------------------")

        while not self.hospital.is_simulation_over():
            self.run_day()

        print("\nSimulation finished.")
        print(f"Total score: {self.hospital.total_score}")

    def run_day(self) -> None:
        self.hospital.start_new_day()
        self.hospital.waiting_room.add_patient(generate_random_patient(self.hospital.diseases))
        try:
            while not self.hospital.clock.is_day_over():
                self.show_status()
                self.handle_user_choice()
        except StopIteration:
            pass

        self.hospital.end_day()

    def show_status(self) -> None:
        print(f"\n=== Day {self.hospital.clock.day} | Hour {self.hospital.clock.hour}/12 ===")
        self.hospital.waiting_room.show_patients()
        print("9) Wait and Observe")
        print("0) End day")

    def handle_user_choice(self) -> None:
        choice = input("\nSelect patient or action: ").strip()

        if choice == "0":
            raise StopIteration

        if choice == "9":
            self.hospital.wait_and_observe(1)
            return

        if not choice.isdigit():
            print("Invalid input.")
            return

        patient = self.hospital.waiting_room.get_patient(int(choice) - 1)
        if not patient:
            print("Invalid patient.")
            return

        patient.show_patient_record()
        input("\nPress ENTER to start visit...")
        self.hospital.visit_patient(patient)




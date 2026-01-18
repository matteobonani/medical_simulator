from medical_simulator.utils.loaders import load_diseases_from_json
from medical_simulator.core.simulator import Simulator
from medical_simulator.core.treatment import Treatment

import sys
import os

sys.path.append(os.path.dirname(__file__))


def build_treatments():
    return [
        Treatment("Observation", effect=0, penalty=0, time_cost=1, description="Wait and observe"),
        Treatment("IV Fluids", effect=10, penalty=2, time_cost=1, description="Hydration support"),
        Treatment("Antibiotics", effect=20, penalty=15, time_cost=1, description="Broad-spectrum antibiotics"),
        Treatment("Vital Signs Check", time_cost=1, test_type="vitals", description="Measure temperature and blood pressure"),
        Treatment("Blood Test", time_cost=2, test_type="blood", description="Laboratory analysis"),
        Treatment("X-Ray", time_cost=2, test_type="xray", description="Chest imaging"),
        Treatment("ECG", time_cost=1, test_type="ecg", description="Electrocardiogram")
    ]



def main():
    print("Clinical Decision-Making Simulator (Advanced Mode)")
    print("--------------------------------------------------")

    diseases = load_diseases_from_json("data/diseases.json")
    treatments = build_treatments()

    simulator = Simulator(diseases=diseases, treatments=treatments, max_days=5)

    while not simulator.is_simulation_over():
        simulator.start_new_day()

        while not simulator.is_day_over():
            simulator.show_patient_status()
            simulator.show_available_actions()

            choice = input("\nChoose an action (number): ").strip()
            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice_num = int(choice)
            total_actions = len(treatments) + 1  # +1 for Guess Disease

            if choice_num < 1 or choice_num > total_actions:
                print("Invalid choice number.")
                continue

            # Guess Disease
            if choice_num == total_actions:
                guess = input("Enter the disease name: ").strip()
                correct = simulator.patient.disease.name.lower() == guess.lower()
                simulator.patient.diagnosis_correct = correct
                if correct:
                    print(f"Correct! The patient had {simulator.patient.disease.name}.")
                    simulator.patient.health = min(100, simulator.patient.health + 10)
                else:
                    print(f"Incorrect. The patient actually had {simulator.patient.disease.name}.")
                    simulator.patient.health -= 5
                    simulator.patient.health = max(0, simulator.patient.health)
                # termina il giorno dopo diagnosi
                simulator.current_hour = 8
            else:
                treatment = treatments[choice_num - 1]
                simulator.perform_action(treatment)

            if simulator.patient.health <= 0:
                print("\nThe patient has deteriorated critically!")
                break

        simulator.end_day()

    print("\nSimulation finished. Thank you for playing!")

if __name__ == "__main__":
    main()

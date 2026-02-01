from medical_simulator.core.clock import Clock
from medical_simulator.utils.utils import load_diseases_from_json
from medical_simulator.core.hospital import Hospital
from medical_simulator.core.treatment import Treatment
from medical_simulator.core.waiting_room import WaitingRoom
from medical_simulator.core.simulator_controller import SimulatorController
import sys
import os

sys.path.append(os.path.dirname(__file__))


def build_treatments():
    return [
        Treatment("IV Fluids", effect=10, penalty=2, time_cost=1, description="Hydration support"),
        Treatment("Antibiotics", effect=20, penalty=15, time_cost=1, description="Broad-spectrum antibiotics"),
        Treatment("Vital Signs Check", time_cost=1, test_type="vitals", description="Measure temperature and blood pressure"),
        Treatment("Blood Test", time_cost=2, test_type="blood", description="Laboratory analysis"),
        Treatment("X-Ray", time_cost=2, test_type="xray", description="Chest imaging"),
        Treatment("ECG", time_cost=1, test_type="ecg", description="Electrocardiogram")
    ]


def main():
    diseases = load_diseases_from_json("data/diseases.json")
    treatments = build_treatments()

    hospital = Hospital(
        clock=Clock(),
        waiting_room=WaitingRoom(4),
        diseases=diseases,
        treatments=treatments,
        max_days=5
    )

    SimulatorController(hospital).run()


if __name__ == "__main__":
    main()

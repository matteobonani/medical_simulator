import random
from medical_simulator.core.patient import Patient
from medical_simulator.core.disease import Disease
import json


NAMES = {
    "M": ["Luca", "Marco", "Giovanni", "Andrea", "Paolo"],
    "F": ["Anna", "Giulia", "Francesca", "Maria", "Elena"]
}

def generate_random_patient(diseases: list[Disease]) -> Patient:

    disease = random.choice(diseases)
    patient = Patient(disease)

    patient.sex = random.choice(["M", "F"])
    patient.name = random.choice(NAMES[patient.sex])
    patient.age = random.randint(18, 85)

    return patient


def load_diseases_from_json(path: str) -> list:
    with open(path, "r") as file:
        data = json.load(file)

    diseases = []
    for item in data:
        disease = Disease(
            name=item["name"],
            symptoms_timeline=item["symptoms_timeline"],
            blood_findings=item["blood_findings"],
            xray_findings=item["xray_findings"],
            ecg_findings=item["ecg_findings"],
            base_temperature=item["base_temperature"],
            base_systolic_bp=item["base_systolic_bp"],
            severity=item["severity"],
            initial_health_range=item["initial_health_range"],
            correct_treatments=item["correct_treatments"]
        )
        diseases.append(disease)

    return diseases
from medical_simulator.core.disease import Disease
import json


def load_diseases_from_json(path):
    with open(path, "r") as file:
        data = json.load(file)

    diseases = []
    for item in data:
        disease = Disease(
            name=item["name"],
            symptoms_timeline=item["symptoms_timeline"],
            blood_findings=item["blood_findings"],
            xray_findings=item["xray_findings"],
            base_temperature=item["base_temperature"],
            base_systolic_bp=item["base_systolic_bp"],
            severity=item["severity"],
            initial_health_range=item["initial_health_range"],
            correct_treatments=item["correct_treatments"]
        )
        diseases.append(disease)

    return diseases

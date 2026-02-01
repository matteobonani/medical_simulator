# Clinical Decision-Making Simulator

A text-based clinical decision-making simulator where the player takes on the role of a hospital doctor. Each day, new patients arrive, time passes, patients may deteriorate, and your medical decisions directly impact outcomes and the final score.

---

## Goal of the Simulator

* Manage patients in the **waiting room**
* Perform **diagnostic tests** and **treatments**
* Identify the **correct disease**
* Manage **time and priorities** effectively
* Maximize the **overall score** while keeping patients alive

The simulation ends after a fixed number of days.

---

## How to Start

1. Start the simulator

Execute the following command from the folder containing the medical_simulator package
```bash
python -m medical_simulator.main
```
2. Play

To choose an action, enter the number shown next to the action description.
    
At the beginning of each day:

   * The current day and hour are displayed
   * Patients in the waiting room are shown

   You can:

   * Select a patient and start a visit
   * **Wait and Observe** (advance time)
   * End the current day

During a patient visit you can:

   * Perform diagnostic tests
   * Apply treatments
   * Attempt a diagnosis
   * Return to the waiting room



Time always advances and patients may worsen while you wait.

---

## Project Structure

```
medical_simulator/
│
├── core/
│   ├── case_result.py
│   ├── clock.py
│   ├── disease.py
│   ├── hospital.py
│   ├── patient.py
│   ├── simulator_controller.py
│   ├── treatment.py
│   └── waiting_room.py
│
├── data/
│   └── diseases.json
│
├── utils/
│   └── utils.py
│
└── main.py
```



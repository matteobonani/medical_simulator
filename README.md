```text
medical_simulator/
│
├── core/                     # Core domain logic of the simulator
│   ├── disease.py            # Disease model and clinical parameters
│   ├── patient.py            # Patient state and time progression
│   ├── simulator.py          # Simulation engine and game loop logic
│   └── treatment.py          # Treatments, tests, and clinical actions
│
├── data/                     
│   └── diseases.json         # Disease definitions (data-driven design)
│
├── utils/                    
│   └── loaders.py            # Load JSON data into disease objects
│
├── main.py                   
└── README.md                
```
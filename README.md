# QLearn — Quantum Computing Animations

Animated quantum computing curriculum built with [Manim Community Edition](https://www.manim.community/), designed for engineers and managers learning quantum computing from scratch.

## Curriculum

### Module 1: Foundations
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 1.1 | What Is a Qubit? | `WhatIsAQubit` |
| 1.2 | The Bloch Sphere | `BlochSphereScene` |
| 1.3 | Superposition | `SuperpositionScene` |
| 1.4 | Measurement | `MeasurementScene` |

### Module 2: Quantum Gates
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 2.1 | Pauli Gates (X, Y, Z) | `PauliGatesScene` |
| 2.2 | The Hadamard Gate | `HadamardGateScene` |
| 2.3 | Phase & Rotation Gates | `PhaseGatesScene` |
| 2.4 | Multi-Qubit Gates | `MultiQubitGatesScene` |

### Module 3: Entanglement
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 3.1 | Bell States | `BellStatesScene` |
| 3.2 | Quantum Teleportation | `QuantumTeleportationScene` |
| 3.3 | Superdense Coding | `SuperdenseCodingScene` |

### Module 4: Quantum Algorithms
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 4.1 | Deutsch-Jozsa Algorithm | `DeutschJozsaScene` |
| 4.2 | Grover's Search | `GroversSearchScene` |
| 4.3 | Quantum Fourier Transform | `QFTScene` |
| 4.4 | Shor's Algorithm | `ShorsAlgorithmScene` |

## Setup

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

> **Note:** Manim requires [FFmpeg](https://ffmpeg.org/) and a LaTeX distribution (e.g. [MiKTeX](https://miktex.org/) on Windows or TeX Live on Linux/macOS).

## Rendering

```bash
# Preview all (480p, fast)
python render_all.py --low

# Web quality (1080p)
python render_all.py --hd

# 4K
python render_all.py --4k

# Single module
python render_all.py --hd --module 1

# Single scene
python render_all.py --hd --scene GroversSearchScene

# List all available scenes
python render_all.py --list
```

Output videos are saved to `media/videos/`.

## Project Structure

```
qlearn/
├── common/                             # Shared utilities
│   ├── styles.py                       # Colors, fonts, title cards, info boxes
│   ├── quantum.py                      # Bloch sphere, state vector display
│   └── circuit.py                      # Quantum circuit diagram builder
├── module1_foundations/                 # Lessons 1.1–1.4
├── module2_gates/                      # Lessons 2.1–2.4
├── module3_entanglement/               # Lessons 3.1–3.3
├── module4_algorithms/                 # Lessons 4.1–4.4
├── render_all.py                       # Batch render script
└── requirements.txt
```

## License

MIT

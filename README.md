# QLearn — Quantum Computing Animations

Animated quantum computing curriculum designed for engineers and managers learning quantum computing from scratch. 32 scenes across 8 modules, from quantum mechanics foundations to NISQ applications.

## Curriculum

### Module 1: Foundations (Quantum Mechanics)
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 1.1 | Wave-Particle Duality | `WaveParticleDualityScene` |
| 1.2 | Quantum States & Probability | `QuantumStatesScene` |
| 1.3 | Uncertainty Principle | `UncertaintyPrincipleScene` |
| 1.4 | Spin & Stern-Gerlach | `SpinScene` |
| 1.5 | Schrödinger Equation | `SchrodingerEquationScene` |
| 1.6 | Dirac Notation | `DiracNotationScene` |
| 1.7 | Observables & Operators | `ObservablesOperatorsScene` |

### Module 2: Quantum Computing Basics
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 2.1 | What Is a Qubit? | `WhatIsAQubit` |
| 2.2 | The Bloch Sphere | `BlochSphereScene` |
| 2.3 | Superposition | `SuperpositionScene` |
| 2.4 | Measurement | `MeasurementScene` |

### Module 3: Quantum Circuits
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 3.1 | What Is a Circuit? | `WhatIsACircuitScene` |
| 3.2 | Circuit Notation | `CircuitNotationScene` |
| 3.3 | Circuit Depth & Complexity | `CircuitDepthScene` |

### Module 4: Quantum Gates
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 4.1 | Pauli Gates (X, Y, Z) | `PauliGatesScene` |
| 4.2 | Hadamard Gate | `HadamardGateScene` |
| 4.3 | Phase & Rotation Gates | `PhaseGatesScene` |
| 4.4 | Multi-Qubit Gates | `MultiQubitGatesScene` |

### Module 5: Entanglement
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 5.1 | Bell States | `BellStatesScene` |
| 5.2 | Quantum Teleportation | `QuantumTeleportationScene` |
| 5.3 | Superdense Coding | `SuperdenseCodingScene` |

### Module 6: Algorithms
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 6.1 | Deutsch-Jozsa Algorithm | `DeutschJozsaScene` |
| 6.2 | Grover's Search | `GroversSearchScene` |
| 6.3 | Quantum Fourier Transform | `QFTScene` |
| 6.4 | Shor's Algorithm | `ShorsAlgorithmScene` |

### Module 7: Hardware & Errors
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 7.1 | Noise & Decoherence | `NoiseDecoherenceScene` |
| 7.2 | Error Correction | `ErrorCorrectionScene` |
| 7.3 | Hardware Platforms | `HardwarePlatformsScene` |

### Module 8: NISQ Applications
| Lesson | Topic | Scene Class |
|--------|-------|-------------|
| 8.1 | VQE | `VQEScene` |
| 8.2 | QAOA | `QAOAScene` |
| 8.3 | BB84 Cryptography | `BB84Scene` |
| 8.4 | Quantum ML | `QuantumMLScene` |

## Setup

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

> **Note:** Requires [FFmpeg](https://ffmpeg.org/) and a LaTeX distribution (e.g. [MiKTeX](https://miktex.org/) on Windows or TeX Live on Linux/macOS).

## Rendering

```bash
# Preview (480p, fast)
python render_and_publish.py --low

# 720p
python render_and_publish.py --medium

# 1080p
python render_and_publish.py --hd

# 1440p (QHD)
python render_and_publish.py --1440p

# 4K (default)
python render_and_publish.py --4k

# Single module
python render_and_publish.py --1440p --module 1

# Single scene
python render_and_publish.py --1440p --scene GroversSearchScene

# Force re-render (skip cache)
python render_and_publish.py --1440p --force
```

Output videos are saved to `docs/videos/` (for web) and cached in `media/videos/`.

## Project Structure

```
qlearn/
├── common/                             # Shared utilities
│   ├── styles.py                       # Colors, fonts, timing constants
│   ├── scene_base.py                   # QScene base class
│   ├── quantum.py                      # Bloch sphere helper
│   └── circuit.py                      # Quantum circuit diagram builder
├── modules/
│   ├── foundations/                     # Module 1 — Lessons 1.1–1.7
│   ├── qc_basics/                      # Module 2 — Lessons 2.1–2.4
│   ├── circuits/                       # Module 3 — Lessons 3.1–3.3
│   ├── gates/                          # Module 4 — Lessons 4.1–4.4
│   ├── entanglement/                   # Module 5 — Lessons 5.1–5.3
│   ├── algorithms/                     # Module 6 — Lessons 6.1–6.4
│   ├── hardware/                       # Module 7 — Lessons 7.1–7.3
│   └── nisq/                           # Module 8 — Lessons 8.1–8.4
├── docs/videos/                        # Published MP4s
├── render_and_publish.py               # Batch render & publish script
└── requirements.txt
```

Each module folder contains a `SCENE.md` with scene specifications, beat-by-beat plans, and binding rules.

## License

MIT

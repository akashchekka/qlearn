# QLearn — Module & Lesson Index

This file defines the canonical ordering of all modules and lessons.
All scene files live under `modules/<topic>/`.

---

## Module 1 — Foundations (`modules/foundations/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 1.1 | `modules/foundations/scene01_wave_particle_duality.py` | `WaveParticleDualityScene` | Double-slit experiment, wave-particle duality |
| 1.2 | `modules/foundations/scene02_quantum_states.py` | `QuantumStatesScene` | Quantum states, amplitudes, Born rule |
| 1.3 | `modules/foundations/scene03_uncertainty_principle.py` | `UncertaintyPrincipleScene` | Heisenberg uncertainty, position-momentum tradeoff |
| 1.4 | `modules/foundations/scene04_spin.py` | `SpinScene` | Intrinsic spin, Stern-Gerlach, bridge to qubits |
| 1.5 | `modules/foundations/scene05_schrodinger_equation.py` | `SchrodingerEquationScene` | Schrodinger equation, time evolution, Hamiltonian |
| 1.6 | `modules/foundations/scene06_dirac_notation.py` | `DiracNotationScene` | Bras, kets, inner products, probability connection |
| 1.7 | `modules/foundations/scene07_observables_operators.py` | `ObservablesOperatorsScene` | Hermitian operators, eigenvalues, measurement outcomes |

## Module 2 — Quantum Computing Basics (`modules/qc_basics/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 2.1 | `modules/qc_basics/scene01_what_is_a_qubit.py` | `WhatIsAQubit` | Classical bit vs. qubit, normalization |
| 2.2 | `modules/qc_basics/scene02_bloch_sphere.py` | `BlochSphereScene` | Bloch sphere geometry, basis states |
| 2.3 | `modules/qc_basics/scene03_superposition.py` | `SuperpositionScene` | Coin analogy, probability bars |
| 2.4 | `modules/qc_basics/scene04_measurement.py` | `MeasurementScene` | Measurement collapse, histogram |

## Module 3 — Quantum Circuits (`modules/circuits/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 3.1 | `modules/circuits/scene01_what_is_a_circuit.py` | `WhatIsACircuitScene` | Classical vs. quantum circuit, time flow |
| 3.2 | `modules/circuits/scene02_circuit_notation.py` | `CircuitNotationScene` | Wire labels, gate notation, step-by-step |
| 3.3 | `modules/circuits/scene03_circuit_depth.py` | `CircuitDepthScene` | Width, depth, decoherence budget |

## Module 4 — Quantum Gates (`modules/gates/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 4.1 | `modules/gates/scene01_pauli_gates.py` | `PauliGatesScene` | X, Y, Z gates, Bloch rotations |
| 4.2 | `modules/gates/scene02_hadamard_gate.py` | `HadamardGateScene` | H matrix, self-inverse, circuit |
| 4.3 | `modules/gates/scene03_phase_gates.py` | `PhaseGatesScene` | Z/S/T hierarchy, Rx/Ry/Rz |
| 4.4 | `modules/gates/scene04_multi_qubit_gates.py` | `MultiQubitGatesScene` | CNOT, SWAP, Toffoli |

## Module 5 — Entanglement (`modules/entanglement/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 5.1 | `modules/entanglement/scene01_bell_states.py` | `BellStatesScene` | Bell circuit, four Bell states |
| 5.2 | `modules/entanglement/scene02_quantum_teleportation.py` | `QuantumTeleportationScene` | Teleportation protocol |
| 5.3 | `modules/entanglement/scene03_superdense_coding.py` | `SuperdenseCodingScene` | Encoding table, decode circuit |

## Module 6 — Algorithms (`modules/algorithms/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 6.1 | `modules/algorithms/scene01_deutsch_jozsa.py` | `DeutschJozsaScene` | Constant vs balanced, speedup |
| 6.2 | `modules/algorithms/scene02_grovers_search.py` | `GroversSearchScene` | Amplitude amplification, geometric view |
| 6.3 | `modules/algorithms/scene03_quantum_fourier_transform.py` | `QFTScene` | QFT equation, roots of unity, circuit |
| 6.4 | `modules/algorithms/scene04_shors_algorithm.py` | `ShorsAlgorithmScene` | Factoring, period finding, speedup |

## Module 7 — Hardware & Errors (`modules/hardware/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 7.1 | `modules/hardware/scene01_noise_decoherence.py` | `NoiseDecoherenceScene` | T1, T2, noise models, fidelity |
| 7.2 | `modules/hardware/scene02_error_correction.py` | `ErrorCorrectionScene` | No-cloning, bit-flip code, surface code |
| 7.3 | `modules/hardware/scene03_hardware_platforms.py` | `HardwarePlatformsScene` | Superconducting, ions, photonic |

## Module 8 — NISQ Applications (`modules/nisq/`)

| Lesson | File | Scene Class | Topic |
|--------|------|-------------|-------|
| 8.1 | `modules/nisq/scene01_vqe.py` | `VQEScene` | Hybrid loop, energy convergence |
| 8.2 | `modules/nisq/scene02_qaoa.py` | `QAOAScene` | Max-Cut, QAOA layers |
| 8.3 | `modules/nisq/scene03_bb84.py` | `BB84Scene` | BB84 protocol, eavesdropper detection |
| 8.4 | `modules/nisq/scene04_quantum_ml.py` | `QuantumMLScene` | Feature maps, PQC classifier, caveats |

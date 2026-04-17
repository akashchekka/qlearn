# Module 8 — NISQ Applications · SCENE.md

## Overview
- **Topic**: Near-term quantum applications — VQE, QAOA, BB84, and quantum ML
- **Hook**: "We can't wait for fault-tolerant quantum computers. What can today's noisy machines do?"
- **Target Audience**: Completed Modules 1-7; full quantum computing background
- **Estimated Length**: ~22 minutes (4 scenes × ~5.5 min each)
- **Key Insight**: NISQ algorithms use hybrid quantum-classical loops to work around noise, with real applications in chemistry, optimization, cryptography, and machine learning — but honest caveats about current limitations

## Narrative Arc
We explore four NISQ-era applications: VQE for chemistry, QAOA for combinatorial optimization, BB84 for quantum cryptography, and QML. Each includes the required caveat about current limitations.

## Transitions & Flow
- Scene 1: VQE — hybrid loop for ground-state energy
- Scene 2: QAOA — layered ansatz for Max-Cut
- Scene 3: BB84 — quantum key distribution (detects, not prevents)
- Scene 4: QML — feature maps and PQC classifiers
- Recurring motif: quantum + classical hybrid loop

## Color Palette
- Primary: `QTEAL` (#009688) — module accent, convergence curves
- Quantum side: `QBLUE` (#4FC3F7), Classical side: `QORANGE` (#FFA726)
- Alice: `QBLUE`, Bob: `QRED` (#EF5350), Eve: `QPURPLE` (#AB47BC)
- Success/match: `QGREEN` (#66BB6A)

## Mathematical Content
- ⟨ψ(θ)|H|ψ(θ)⟩ (VQE energy expectation)
- U_C(γ), U_B(β) alternating layers (QAOA)
- BB84 bases {Z, X}, 25% error rate on eavesdropping
- U_φ(x) feature maps, U(θ) parameterized circuits (QML)

## Implementation Order
1. scene01 (VQE — introduces hybrid loop pattern)
2. scene02 (QAOA — similar hybrid pattern, different application)
3. scene03 (BB84 — standalone protocol)
4. scene04 (QML — combines loop + pipeline patterns)

Scene specifications for `modules/nisq/`. Copilot MUST read the **RULES**
section at the bottom of this file before generating or editing any scene
in this module. Every rule is binding.

Shared imports for every scene in this module:

```python
from manim import *
from common.scene_base import QScene
from common.circuit import build_wire, place_gate, place_cnot
from common.styles import (
    QBLUE, QRED, QGREEN, QPURPLE, QORANGE, QYELLOW,
    QCYAN, QTEAL, QWHITE, QGRAY, QDARK,
    STEP_PAUSE, LONG_PAUSE,
)
```

Module accent color: **`QTEAL`** (`#009688`). Module number: **8**.

---

## 8.1 — Variational Quantum Eigensolver (`scene01_vqe.py`)

- **Class name:** `VQEScene`
- **Teaching objective:** Hybrid quantum/classical loop: parameterized
  ansatz circuit prepares trial state, quantum hardware estimates
  energy ⟨ψ(θ)|H|ψ(θ)⟩, classical optimizer updates θ. Show energy
  convergence on a small example (H₂ ground state).
- **Beats:**
  1. Title card.
  2. Loop diagram: a circle with four nodes — "ansatz `|ψ(θ)⟩`",
     "measure ⟨H⟩", "classical optimizer", "update θ" — arrows
     forming the cycle.
  3. Ansatz circuit example (2 qubits): R_y(θ_0), R_y(θ_1), CNOT,
     R_y(θ_2), R_y(θ_3). Label parameters explicitly.
  4. Energy convergence plot: x-axis iteration, y-axis ⟨H⟩. Curve
     descends and asymptotes to a dashed line `E_0` (true ground
     state).
  5. H₂ context: one line "VQE finds the ground-state energy of the
     hydrogen molecule" with a small molecule icon.
- **Color mapping:** quantum side → `QBLUE`, classical side → `QORANGE`,
  energy curve → `QTEAL`, target line → `QGREEN`.
- **Pitfalls:**
  - The variational principle gives an *upper bound* on `E_0`; the
    curve must approach from above, never cross below.

## 8.2 — QAOA (`scene02_qaoa.py`)

- **Class name:** `QAOAScene`
- **Teaching objective:** Max-Cut as a sample combinatorial problem,
  QAOA layered ansatz alternating cost (`U_C(γ)`) and mixer (`U_B(β)`),
  classical optimization of (γ, β), simple energy landscape view.
- **Beats:**
  1. Title card.
  2. Small graph (4 nodes, 5 edges) drawn cleanly. Show one Max-Cut
     partition by coloring nodes blue/red; count cut edges.
  3. QAOA circuit: H^n initial layer, then p alternating
     (`U_C(γ_k)`, `U_B(β_k)`) layers, then measure. Use abstract
     blocks for U_C and U_B; do not unroll.
  4. Optimization landscape: a 2D surface or contour over (γ, β)
     with a path descending toward a minimum. Keep it stylized.
  5. Recap line: "more layers → closer to optimum, but harder to
     train."
- **Color mapping:** graph node sets → `QBLUE`/`QRED`, cut edges →
  `QYELLOW`, U_C blocks → `QPURPLE`, U_B blocks → `QORANGE`.
- **Pitfalls:**
  - Max-Cut is NP-hard; do not claim QAOA solves it optimally for all
    cases. Frame it as approximation.
  - Block layers must visually alternate U_C → U_B p times; do not
    reorder.

## 8.3 — BB84 Quantum Key Distribution (`scene03_bb84.py`)

- **Class name:** `BB84Scene`
- **Teaching objective:** BB84 protocol — Alice sends qubits prepared in
  random bases, Bob measures in random bases, they sift on matching
  bases, eavesdropper Eve introduces detectable errors.
- **Beats:**
  1. Title card.
  2. Alice and Bob characters (Alice left, Bob right). Eve in the
     middle, dimmed, introduced later.
  3. Protocol table with columns: bit · Alice basis · sent state · Bob
     basis · Bob outcome · keep? Fill row by row for ~6 rows. Use
     bases {Z (rectilinear), X (diagonal)}.
  4. Sifting: highlight rows where bases matched; those bits form the
     shared key.
  5. Eve attack scenario: re-do a row with Eve intercepting and
     re-sending. Show that on basis-mismatch she introduces a 25%
     error rate detectable by Alice and Bob comparing a key sample.
- **Color mapping:** Alice → `QBLUE`, Bob → `QRED`, Eve → `QPURPLE`,
  matching-basis rows → `QGREEN` highlight, mismatched/eve rows →
  `QORANGE`.
- **Pitfalls:**
  - Use consistent basis names (Z/X) and consistent state symbols
    (|0⟩,|1⟩,|+⟩,|−⟩). Match Modules 1–3.
  - Do not claim BB84 prevents eavesdropping — it *detects* it.

## 8.4 — Quantum Machine Learning (`scene04_quantum_ml.py`)

- **Class name:** `QuantumMLScene`
- **Teaching objective:** Big-picture QML: feature maps that embed
  classical data into a quantum state, parameterized quantum circuit
  (PQC) classifier, classical training loop, brief mention of three
  approaches (variational classifiers, quantum kernels, quantum
  generative models).
- **Beats:**
  1. Title card.
  2. Pipeline diagram: classical data → "feature map `U_φ(x)`" →
     "PQC `U(θ)`" → "measurement" → prediction → loss → classical
     optimizer → update θ. Arrows forming a training loop on θ.
  3. Toy example: a 2D dataset of two classes, encoded into 2 qubits.
     Show decision-boundary forming over training iterations as a
     simple background-color shading.
  4. Three-approach panel: short cards labeled "Variational
     classifiers", "Quantum kernels", "Quantum generative models"
     with one-line descriptions.
  5. Caveat line: "no proven QML advantage on broad problems yet."
- **Color mapping:** classical pipeline arrows → `QORANGE`, quantum
  blocks → `QBLUE`, optimizer → `QPURPLE`, decision boundary →
  `QTEAL`.
- **Pitfalls:**
  - Do not overclaim quantum advantage. Include the caveat.
  - Do not depict feature maps as deterministic embeddings without a
    quantum block — the key is the quantum-state embedding.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "VQE"). Do NOT show the module number or
  lesson number on screen. Call `self.show_title_card("<Topic Name>")`.
- End with a one-line "what we learned" recap before fading.

### R2. Imports and constants
- All colors/sizes/timings from `common.styles`. No literals.
- Reuse `common.circuit` helpers for any circuit drawings.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Hybrid loop diagrams
- Hybrid (quantum + classical) loops are drawn as a circular flow.
  Quantum side `QBLUE`, classical side `QORANGE`. Arrows always
  unidirectional in a single loop direction (clockwise).
- Optimizer node always sits on the classical side.

### R4. Algorithm decomposition
- Each NISQ algorithm is taught as: **problem → hybrid loop → ansatz
  circuit → outcome → caveat**. Do not skip a step, especially the
  caveat.
- Ansatz blocks (`U_C`, `U_B`, `U_φ`, `U(θ)`) are drawn as labeled
  blocks, not unrolled, unless the lesson is the unrolling.

### R5. Layout
- Two-zone layout: pipeline/loop diagram on the left, plot/table on
  the right. Keep zones fixed.
- Tables (BB84) use uniform row height and bold column headers.
  Reveal one row at a time (0.5s per row).

### R6. Color discipline
- Quantum vs classical contrast: `QBLUE` vs `QORANGE` everywhere in
  this module. Do not swap.
- `QGREEN` reserved for "matching/keep/success"; `QRED` for "discard
  /error/Eve mismatch".
- Maximum 4 accent colors on screen.
- Inactive panels dim to opacity 0.35 when focus shifts.

### R7. Quantum accuracy and honesty
- VQE: variational principle = upper bound on ground state. Curve
  approaches from above, never below `E_0`.
- QAOA: approximation algorithm; Max-Cut is NP-hard; "more layers,
  harder to train" must be stated.
- BB84: detects, not prevents, eavesdropping. State 25% error rate
  on Eve interception when doing intercept-and-resend in the wrong
  basis.
- QML: include the "no proven broad advantage yet" caveat.

### R8. Motion
- Loop diagrams: animate the cycle once with a moving dot or pulsing
  arrows (one full cycle, ~3s), then hold static.
- Convergence plots: animate the curve with `Create` over 2.5s; the
  asymptote/target line appears first as a dashed reference.
- Tables: row-by-row reveal, 0.5s per row.

### R9. Timing
- Title hold 2s. Section header fade 0.6s.
- Each major beat ends with `LONG_PAUSE`.

### R10. Validation
- All hybrid diagrams have both quantum and classical sides clearly
  labeled.
- No graph or curve violates the algorithm's mathematical bounds
  (VQE energy lower bound, fidelity ≤ 1, probabilities ≥ 0).
- Caveats are present where required (QAOA, QML, BB84 detection).
- Notation matches Modules 1–6 exactly (kets, basis names, gate
  symbols).

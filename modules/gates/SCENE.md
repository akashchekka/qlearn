# Module 4 — Quantum Gates · SCENE.md

## Overview
- **Topic**: Single-qubit and multi-qubit quantum gates — the operations that manipulate qubits
- **Hook**: "Classical computers have NOT, AND, OR. Quantum computers have X, H, CNOT — and they're far more powerful"
- **Target Audience**: Completed Modules 1-3; can read quantum circuits
- **Estimated Length**: ~20 minutes (4 scenes × ~5 min each)
- **Key Insight**: Every quantum gate is a unitary matrix; multi-qubit gates like CNOT create entanglement

## Narrative Arc
From Pauli gates (X/Y/Z) through Hadamard to phase gates, we build the single-qubit toolkit. Then multi-qubit gates (CNOT, SWAP, Toffoli) unlock entanglement and universal computation.

## Transitions & Flow
- Scene 1: Pauli gates — the building blocks (bit-flip, phase-flip)
- Scene 2: Hadamard — the superposition creator
- Scene 3: Phase gates — the Z→S→T hierarchy
- Scene 4: Multi-qubit gates — where entanglement happens
- Each gate scene follows: matrix → action → Bloch view → circuit

## Color Palette
- Primary: `QPURPLE` (#AB47BC) — module accent, Y gate, phase gates
- X gate: `QRED` (#EF5350), Z gate: `QBLUE` (#4FC3F7), H gate: `QGREEN` (#66BB6A)
- Phase: `QORANGE` (#FFA726), CNOT control: `QCYAN` (#00E5FF)
- Highlight: `QYELLOW` (#FFEE58) — angle labels, active elements

## Mathematical Content
- Pauli matrices X, Y, Z (2×2)
- H = (1/√2)[[1,1],[1,-1]]
- Z = S² = T⁴ hierarchy
- CNOT 4×4 matrix, SWAP, Toffoli truth tables
- Rz(θ), Ry(θ), Rx(θ) generalized rotations

## Implementation Order
1. scene01 (Pauli — foundational)
2. scene02 (Hadamard — uses Bloch sphere)
3. scene03 (Phase — builds Z→S→T)
4. scene04 (Multi-qubit — uses QuantumCircuit helper)

---

Scene specifications for `modules/gates/`. Copilot MUST read the **RULES**
section at the bottom of this file before generating or editing any scene in
this module. Every rule is binding.

Shared imports for every scene in this module:

```python
from manim import *
from common.scene_base import QScene
from common.circuit import build_wire, place_gate, place_cnot
from common.styles import (
    QBLUE, QRED, QGREEN, QPURPLE, QORANGE, QYELLOW,
    QCYAN, QWHITE, QGRAY, QDARK,
    STEP_PAUSE, LONG_PAUSE,
)
```

Module accent color: **`QPURPLE`** (`#AB47BC`). Module number: **4**.

---

## 4.1 — Pauli Gates (`scene01_pauli_gates.py`)

- **Class name:** `PauliGatesScene`
- **Teaching objective:** Introduce X, Y, Z gates via their matrices,
  action on computational basis states, and Bloch-sphere rotations by π
  around the corresponding axis.
- **Beats:**
  1. Title card.
  2. Gate-by-gate in order X → Y → Z. For each:
     - Show matrix (2×2) to the left.
     - Show action: e.g., `X|0⟩ = |1⟩` and `X|1⟩ = |0⟩`.
     - Show a small Bloch sphere rotating the state vector by π around
       the named axis (one rotation only, slow).
  3. Summary table with three rows (X/Y/Z) and three columns (matrix,
     axis, effect on |0⟩).
- **Color mapping:**
  - X → `QRED` (bit-flip intuition), Y → `QPURPLE`, Z → `QBLUE`
    (phase-flip intuition).
- **Pitfalls:**
  - Y|0⟩ = i|1⟩: do NOT drop the phase factor i.
  - Do NOT rotate the Bloch sphere continuously; one π rotation, then
    hold.

---

## 4.2 — Hadamard Gate (`scene02_hadamard_gate.py`)

- **Class name:** `HadamardGateScene`
- **Teaching objective:** Introduce H: matrix, action `H|0⟩ = |+⟩` and
  `H|1⟩ = |−⟩`, self-inverse property `H² = I`, and its circuit role.
- **Beats:**
  1. Title card.
  2. H matrix `(1/√2) [[1,1],[1,−1]]` revealed in chunks.
  3. Action equations `H|0⟩ = (|0⟩+|1⟩)/√2 = |+⟩` and `H|1⟩ = |−⟩`.
  4. Bloch view: state vector rotates from +z to +x (for |0⟩ → |+⟩).
     Single rotation, slow.
  5. Self-inverse demo: `H(H|0⟩) = |0⟩`. Use `ReplacementTransform` to
     bring the state back.
  6. Tiny circuit `|0⟩ — H — measure` with probability bars 0.5/0.5.
- **Color mapping:** `|+⟩` → `QGREEN`, `|−⟩` → `QORANGE`.
- **Pitfalls:**
  - Probability bars must be exactly equal for the |+⟩ measurement.
  - Do NOT skip the `1/√2` normalization factor.

---

## 4.3 — Phase Gates (`scene03_phase_gates.py`)

- **Class name:** `PhaseGatesScene`
- **Teaching objective:** Build the Z → S → T hierarchy of phase gates,
  show their Bloch-sphere rotations about the z-axis (π, π/2, π/4), and
  generalize to `Rx(θ)`, `Ry(θ)`, `Rz(θ)`.
- **Beats:**
  1. Title card.
  2. Z gate: matrix, `Z|1⟩ = −|1⟩`, π rotation about z on the Bloch
     sphere.
  3. S gate: matrix `diag(1, i)`, π/2 rotation.
  4. T gate: matrix `diag(1, e^{iπ/4})`, π/4 rotation.
  5. Hierarchy diagram: Z = S², S = T². Show the nesting explicitly.
  6. Generalized rotations `Rx(θ)`, `Ry(θ)`, `Rz(θ)` with one matrix
     form and a Bloch illustration for an arbitrary `θ`.
- **Color mapping:** phase axis (z) → `QBLUE`, rotation arc → `QPURPLE`,
  angle label → `QYELLOW`.
- **Pitfalls:**
  - Z, S, T act only on |1⟩; |0⟩ is unchanged. Make this visible.
  - Rotations on the Bloch sphere are about the specified axis only —
    do not drift.

---

## 4.4 — Multi-Qubit Gates (`scene04_multi_qubit_gates.py`)

- **Class name:** `MultiQubitGatesScene`
- **Teaching objective:** Introduce CNOT (truth table + matrix), SWAP,
  and Toffoli (CCX). Emphasize that entangling capability requires
  multi-qubit gates.
- **Beats:**
  1. Title card.
  2. CNOT: circuit symbol, 4-row truth table `|ab⟩ → |a, a⊕b⟩`, and
     4×4 matrix. Highlight that only rows with a=1 differ from identity.
  3. SWAP: circuit symbol (×—×), action `|ab⟩ → |ba⟩`, matrix.
  4. Toffoli (CCX): circuit symbol with two controls + one target,
     truth table, statement "universal for classical reversible logic".
  5. Short recap table comparing the three gates.
- **Color mapping:** control dots → `QCYAN`, target ⊕ → `QPURPLE`,
  SWAP × → `QORANGE`.
- **Pitfalls:**
  - CNOT matrix ordering must match the stated basis ordering `|q_1 q_0⟩`
    (or whichever the project uses) — keep it consistent with Module 2.
  - Toffoli: both controls must be 1 for the target to flip. Make the
    truth table explicit.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "Pauli Gates"). Do NOT show the module
  number or lesson number on screen. Call
  `self.show_title_card("<Topic Name>")`.
- Structure each scene as: matrix → action on basis → Bloch view →
  circuit. Do not skip steps.

### R2. Imports and constants
- Pull all colors, sizes, and timings from `common.styles`. No literals.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Matrix presentation
- Matrices are 2×2 (single-qubit) or 4×4/8×8 (multi-qubit) with explicit
  basis ordering labeled above or beside the matrix on first appearance.
- Reveal matrix entries in logical chunks, not all at once, when the
  entries themselves are the lesson.
- Keep matrix font size consistent across the module.

### R4. Bloch sphere usage (see Foundations R6 as well)
- Reuse the Bloch-sphere helper if present; keep axis colors identical
  to Module 1 (x=`QORANGE`, y=`QGREEN`, z=`QBLUE`).
- One rotation per beat, slow (`run_time` ≥ 1.5s), then hold.
- Angle arcs in `QPURPLE`, angle labels in `QYELLOW`, placed so they do
  NOT intersect the state vector.
- Do not rotate the sphere camera while the state vector is rotating.
- External state labels MUST NOT overlap the sphere's built-in pole
  labels (`|0⟩` north, `|1⟩` south). Place them in a separate equation
  zone (e.g., fixed right column) — see Foundations R4a.

### R5. Gate color mapping (module-wide)
- Pauli-X: `QRED` (bit-flip). Pauli-Y: `QPURPLE`. Pauli-Z: `QBLUE`
  (phase-flip). Hadamard: `QGREEN`. Phase (S/T): `QORANGE`.
- CNOT control dot: `QCYAN`. CNOT target: `QPURPLE`. SWAP ×: `QORANGE`.
- Keep these mappings identical across all four scenes and all later
  modules that show gates.

### R6. Equations and kets
- Use the ket → ket form `Gate |input⟩ = |output⟩` (no prose in the
  equation). Prose goes in a separate label below the equation.
- Normalization factors (`1/√2`, etc.) must be visible in every
  equation; never silently drop them.
- Phase factors (`e^{iφ}`, `i`, `−1`) must be visible in every
  equation; never silently drop them.

### R7. Motion
- Prefer `Write` for equations, `Create` for matrix brackets, `FadeIn`
  for boxes, `TransformMatchingTex` for derivation steps.
- Highlight the changed matrix entries (e.g., S vs T vs Z) with color
  or `Indicate`, not with flashing.
- Pause `STEP_PAUSE` after each equation line; `LONG_PAUSE` after a key
  insight (e.g., "Z = S²").

### R8. Layout
- Three zones per gate beat: matrix (left), action equation (center),
  Bloch/circuit (right). Keep these zones fixed; do not cross them.
- Summary tables: rows equal height, columns equal width, labels bold.

### R9. Quantum accuracy
- Every gate shown must be unitary. Do not depict non-unitary effects
  (measurement comes in Module 1/4 only).
- Phase is physical: a gate that differs only by a global phase from
  another gate must be explicitly labeled as such.
- Multi-qubit gate truth tables must match the matrix exactly.

### R10. Validation
- Bloch vector never leaves the unit sphere.
- Matrix dimensions and basis ordering match the circuit ordering used
  in Module 2.
- No two gates share a color accidentally.
- Gate boxes across the scene have identical dimensions.

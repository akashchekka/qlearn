# Module 5 — Entanglement · SCENE.md

## Overview
- **Topic**: Quantum entanglement — Bell states, teleportation, and superdense coding
- **Hook**: "Einstein called it 'spooky action at a distance.' Here's what it really is — and what it can do"
- **Target Audience**: Completed Modules 1-4; knows gates and circuits
- **Estimated Length**: ~15 minutes (3 scenes × ~5 min each)
- **Key Insight**: Entanglement creates correlations with no classical explanation, enabling teleportation and superdense coding — but never faster-than-light communication

## Narrative Arc
We build a Bell state from scratch (H + CNOT), then show two killer applications: teleporting a quantum state and sending 2 classical bits through 1 qubit. Both require a classical channel — no FTL.

## Transitions & Flow
- Scene 1: Bell states — the foundation of entanglement
- Scene 2: Teleportation — using entanglement + classical bits
- Scene 3: Superdense coding — the reverse direction
- Alice is always left/blue, Bob always right/red across all three scenes

## Color Palette
- Primary: `QORANGE` (#FFA726) — module accent, entangled pair indicators
- Alice: `QBLUE` (#4FC3F7), Bob: `QRED` (#EF5350)
- Classical channel: `QGRAY` (#B0BEC5) double lines
- Corrections: `QYELLOW` (#FFEE58)
- Success/key: `QGREEN` (#66BB6A)

## Mathematical Content
- |Φ+⟩ = (|00⟩+|11⟩)/√2, |Φ-⟩, |Ψ+⟩, |Ψ-⟩ (four Bell states)
- Teleportation: Bell measurement → 2 classical bits → conditional X/Z
- Superdense coding: {I, X, Z, XZ} encoding → Bell measurement → 2 bits

## Implementation Order
1. scene01 (Bell states — foundation)
2. scene02 (Teleportation — uses Bell states)
3. scene03 (Superdense coding — reverse of teleportation)

---

Scene specifications for `modules/entanglement/`. Copilot MUST read the
**RULES** section at the bottom of this file before generating or editing
any scene in this module. Every rule is binding.

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

Module accent color: **`QORANGE`** (`#FFA726`). Module number: **5**.

---

## 5.1 — Bell States (`scene01_bell_states.py`)

- **Class name:** `BellStatesScene`
- **Teaching objective:** Build the Bell circuit `H ⊗ I` then `CNOT` on
  `|00⟩`, derive `|Φ+⟩ = (|00⟩+|11⟩)/√2`, and enumerate the four Bell
  states.
- **Beats:**
  1. Title card.
  2. Circuit: two wires initialized to `|0⟩`; H on q_0; CNOT (control q_0,
     target q_1). Build left→right.
  3. State evolution: reveal `|00⟩ → (|0⟩+|1⟩)|0⟩/√2 → (|00⟩+|11⟩)/√2`
     step by step, aligned to circuit progress (highlight the active
     gate as each step appears).
  4. Table of four Bell states `|Φ±⟩`, `|Ψ±⟩` with initial input noted
     (`|00⟩`, `|01⟩`, `|10⟩`, `|11⟩`).
  5. Correlation beat: show two qubits far apart; measuring one forces
     the other's outcome. Use simple icons, no distances/speeds implied
     beyond what the math gives.
- **Color mapping:** q_0 → `QBLUE`, q_1 → `QRED`, entangled pair bracket
  → `QORANGE`, correlation link → `QPURPLE`.
- **Pitfalls:**
  - Do NOT depict entanglement as a literal string between qubits that
    transmits information faster than light.
  - Keep normalization `1/√2` visible at each step.

---

## 5.2 — Quantum Teleportation (`scene02_quantum_teleportation.py`)

- **Class name:** `QuantumTeleportationScene`
- **Teaching objective:** Walk through the teleportation protocol: shared
  Bell pair between Alice and Bob, Alice's Bell-basis measurement, two
  classical bits sent to Bob, Bob's conditional corrections.
- **Beats:**
  1. Title card.
  2. Character setup: Alice (left), Bob (right), shared Bell pair drawn
     as the entangled middle. Alice holds an unknown `|ψ⟩` to teleport.
  3. Circuit form: 3 wires (ψ, Alice-half, Bob-half). Place CNOT and H to
     perform Bell measurement on ψ and Alice-half.
  4. Measurement boxes on Alice's two wires emit two classical bits.
     Draw classical double-lines to Bob.
  5. Bob applies conditional X and/or Z depending on the 2 classical
     bits. Display the four cases as a small table.
  6. Final state on Bob's wire is `|ψ⟩`. Emphasize: original `|ψ⟩` is
     gone from Alice's side (no-cloning).
- **Color mapping:** Alice → `QBLUE`, Bob → `QRED`, classical wires →
  `QGRAY` double-lines, conditional corrections → `QYELLOW`.
- **Pitfalls:**
  - Do NOT suggest teleportation sends information faster than light —
    classical bits must travel classically.
  - Do NOT leave `|ψ⟩` drawn on Alice's wire after measurement.

---

## 5.3 — Superdense Coding (`scene03_superdense_coding.py`)

- **Class name:** `SuperdenseCodingScene`
- **Teaching objective:** Show how a shared Bell pair lets Alice send 2
  classical bits by transmitting 1 qubit, via the encoding `{I, X, Z,
  XZ}`.
- **Beats:**
  1. Title card.
  2. Start from a shared `|Φ+⟩` between Alice and Bob.
  3. Encoding table: `00→I`, `01→X`, `10→Z`, `11→XZ` (or whichever
     convention the project uses — document it in the table).
  4. Alice applies her gate conditioned on her 2 bits; send her qubit to
     Bob.
  5. Bob performs the Bell measurement circuit (CNOT then H) and reads
     off the 2 bits.
  6. Recap line: 1 qubit + prior entanglement = 2 classical bits.
- **Color mapping:** Alice gates → `QBLUE`, Bob's decoder → `QRED`,
  transmitted qubit path → `QORANGE`, classical output → `QGREEN`.
- **Pitfalls:**
  - The encoding table convention must match the code. State it
    explicitly in the scene.
  - Do NOT claim "2 bits transmitted in 1 qubit" without the caveat of
    prior shared entanglement.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "Bell States"). Do NOT show the module
  number or lesson number on screen. Call
  `self.show_title_card("<Topic Name>")`.
- Section flow: setup → circuit build → state evolution → interpretation
  → recap.

### R2. Imports and constants
- Use `common.styles` for all colors/sizes/pauses.
- Use `common.circuit` helpers for wires, gates, CNOT, measurement.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Multi-qubit visual conventions
- Basis ordering is `|q_1 q_0⟩` with `q_0` the top wire — keep this
  consistent with Modules 2 and 3. State it in the scene if it matters
  for the math.
- Entangled pairs are marked with a soft `QORANGE` bracket or brace,
  not a straight line that looks like a wire.
- Classical wires after measurement are `QGRAY` double lines.

### R4. State evolution display
- Anchor state-vector text in a fixed zone (right or below the circuit)
  so it does not move with the circuit.
- Use `TransformMatchingTex` when going from one state line to the
  next so common symbols stay anchored.
- Every evolution step shows normalization (`1/√2`, `1/2`, etc.)
  explicitly.

### R5. Alice/Bob visual language
- Alice is always on the left, Bob on the right. Do not swap sides.
- Alice-blue (`QBLUE`), Bob-red (`QRED`). Keep this mapping across
  every scene that uses characters.
- Classical communication channel is a `QGRAY` double-line with a small
  arrow pointing from sender to receiver.

### R6. Motion
- Build the circuit wires first, then gates, then measurements, then
  classical channels, then conditional corrections.
- Animate the "transmission" of a qubit as a slow `MoveAlongPath` or
  `Transform` with `run_time` ≥ 1.2s; do not make it dart across.
- Pause `LONG_PAUSE` after each completed protocol phase.

### R7. Color discipline
- Max 4 accent colors on screen. Dim inactive wires to opacity 0.35.
- `QORANGE` is the entanglement accent for this module — reserve it
  for entangled-pair indicators.

### R8. Quantum accuracy
- Entanglement correlations do not transmit information on their own.
  Always pair any "spooky" visual with a classical channel when
  information transfer is implied.
- Teleportation destroys the original `|ψ⟩` — remove it from Alice's
  side after measurement.
- Superdense coding requires prior entanglement — never show "1 qubit →
  2 bits" without the pre-shared pair.
- Bell measurement is `CNOT` then `H` on the control, then measurement.
  Do not reorder.

### R9. Timing
- Title hold: 2s. Circuit build per gate: 0.8–1.2s.
- Protocol phases (setup / measure / classical-send / correct): each
  followed by `LONG_PAUSE`.

### R10. Validation
- Every state line normalized.
- Classical double-lines clearly distinguishable from quantum wires.
- Alice always left, Bob always right.
- No entangled qubit appears on both sides after teleportation.

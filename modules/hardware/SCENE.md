# Module 7 — Hardware & Errors · SCENE.md

## Overview
- **Topic**: Real quantum hardware — noise, decoherence, error correction, and platform comparison
- **Hook**: "Quantum computers are incredibly fragile. How do we protect quantum information from the environment?"
- **Target Audience**: Completed Modules 1-6; understands algorithms and circuits
- **Estimated Length**: ~16 minutes (3 scenes × ~5.5 min each)
- **Key Insight**: Noise is the biggest obstacle; quantum error correction is possible despite no-cloning, and different hardware platforms make different engineering tradeoffs

## Narrative Arc
We face the reality of noise (T1/T2 decoherence), then show how quantum error correction works despite no-cloning (3-qubit code), and finally compare the three leading hardware platforms.

## Transitions & Flow
- Scene 1: Noise — the enemy (T1, T2, noise models, fidelity)
- Scene 2: Error correction — the defense (no-cloning → repetition code → surface code teaser)
- Scene 3: Hardware platforms — the implementations (superconducting, ions, photonic)

## Color Palette
- Primary: `QGREEN` (#66BB6A) — module accent, correction success, fidelity
- Error: `QRED` (#EF5350) — injected errors, no-cloning ✗
- Data qubits: `QBLUE` (#4FC3F7), Ancilla: `QPURPLE` (#AB47BC)
- T1 curve: `QORANGE` (#FFA726), T2 curve: `QPURPLE`
- Ideal state: `QYELLOW` (#FFEE58)

## Mathematical Content
- T1 (energy relaxation), T2 (dephasing), T2 ≤ 2T1
- F = ⟨ψ|ρ|ψ⟩ (fidelity)
- 3-qubit bit-flip code: |ψ⟩|0⟩|0⟩ → α|000⟩ + β|111⟩
- F = e^{-d/dc} (fidelity vs circuit depth)

## Implementation Order
1. scene01 (Noise — uses BlochSphere)
2. scene02 (Error correction — uses QuantumCircuit)
3. scene03 (Hardware — standalone comparison)

Scene specifications for `modules/hardware/`. Copilot MUST read the
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

Module accent color: **`QGREEN`** (`#66BB6A`). Module number: **7**.

---

## 7.1 — Noise & Decoherence (`scene01_noise_decoherence.py`)

- **Class name:** `NoiseDecoherenceScene`
- **Teaching objective:** Define `T_1` (energy relaxation) and `T_2`
  (dephasing), introduce common noise models (bit-flip, phase-flip,
  depolarizing) at a high level, and define fidelity.
- **Beats:**
  1. Title card.
  2. Bloch sphere with state on the equator. Show `T_2` decoherence as
     the in-plane vector spiraling toward the z-axis (loss of phase).
     One smooth animation, then hold.
  3. Bloch sphere with excited state at south pole. Show `T_1`
     relaxation as the vector decaying toward the north pole. Hold.
  4. Plot decay curves: amplitude vs time for `e^{-t/T_1}` and
     `e^{-t/T_2}`. Annotate the time constants.
  5. Three boxes labeled "bit-flip", "phase-flip", "depolarizing" with
     a one-line definition each. No matrices needed at this depth.
  6. Fidelity definition `F = ⟨ψ| ρ |ψ⟩` revealed once, with a short
     plain-language gloss "how close is the noisy state to the ideal".
- **Color mapping:** ideal state vector → `QYELLOW`, noisy state →
  `QRED`, T_1 curve → `QORANGE`, T_2 curve → `QPURPLE`.
- **Pitfalls:**
  - Do NOT depict noise as random teleportation — show smooth decay.
  - `T_2 ≤ 2 T_1` always; do not draw `T_2 > T_1` curves.

---

## 7.2 — Error Correction (`scene02_error_correction.py`)

- **Class name:** `ErrorCorrectionScene`
- **Teaching objective:** Motivate quantum error correction, state the
  no-cloning theorem as the obstacle, present the 3-qubit bit-flip
  repetition code (encode + error + syndrome + recover), and gesture
  toward the surface code.
- **Beats:**
  1. Title card.
  2. No-cloning callout: `|ψ⟩ → |ψ⟩|ψ⟩` with a red ✗ over it. One-line
     statement.
  3. Bit-flip code circuit:
     - Encode `|ψ⟩|0⟩|0⟩ → α|000⟩ + β|111⟩` with two CNOTs.
     - Inject a single bit-flip error on one of the three qubits
       (visualized as an X gate appearing in red).
     - Syndrome measurement using two ancillas. Show the 4 syndrome
       outcomes mapping to "no error / error on q_0 / q_1 / q_2".
     - Apply the corresponding X correction.
  4. Statement: "corrects 1 bit-flip; does not correct phase-flip" —
     remind viewer that real codes (Shor, surface) handle both.
  5. Surface-code teaser: a small grid of data qubits with ancilla
     stabilizers. Do not animate logic — just show the lattice and
     label "data" vs "syndrome" qubits.
- **Color mapping:** data qubits → `QBLUE`, ancilla qubits → `QPURPLE`,
  injected error → `QRED`, correction gate → `QGREEN`.
- **Pitfalls:**
  - Do NOT show the encoding as cloning. The CNOTs entangle, not copy.
  - Make clear the bit-flip code does NOT protect against arbitrary
    errors.

---

## 7.3 — Hardware Platforms (`scene03_hardware_platforms.py`)

- **Class name:** `HardwarePlatformsScene`
- **Teaching objective:** Compare three current platforms —
  superconducting, trapped ions, photonic — across qubit type, gate
  speed, connectivity, and main challenge. Present a comparison table.
- **Beats:**
  1. Title card.
  2. Superconducting panel: schematic of a transmon (capacitor +
     Josephson junction icon, simplified). One-line description.
  3. Trapped-ion panel: chain of ion icons in a linear trap with laser
     arrows. One-line description.
  4. Photonic panel: photon paths through beam splitters and detectors.
     One-line description.
  5. Comparison table with columns: Platform · Qubit type · Gate speed
     · Connectivity · Main challenge.
- **Color mapping:** superconducting → `QBLUE`, trapped ions →
  `QORANGE`, photonic → `QPURPLE`.
- **Pitfalls:**
  - Schematics are stylized; label them as "schematic, not to scale".
  - Do NOT make claims about which platform is "best".

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "Noise & Decoherence"). Do NOT show the
  module number or lesson number on screen. Call
  `self.show_title_card("<Topic Name>")`.
- Each major topic is a section with a header.

### R2. Imports and constants
- All colors/sizes/timings from `common.styles`. No literals.
- Reuse `common.circuit` helpers for any circuit drawings.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Hardware schematics
- Schematics are educational stylizations. Always label them
  "schematic" once on first appearance.
- Use uniform icon sizes within a panel (all ions same size, all
  beam-splitter boxes same size).
- Keep arrows short and straight; never curve laser arrows around
  ions.

### R4. Decay & noise visualizations
- Smooth `MoveAlongPath` or parametric updaters for Bloch decoherence.
- Decay curves animated with `Create` over the time axis; never
  appearing all at once.
- Always label the time constant on the curve at its `1/e` point.
- External state labels near a Bloch sphere MUST NOT overlap the
  sphere's built-in pole labels — see Foundations R4a.

### R5. Layout
- Three-panel comparison scenes (7.3) use equal-width columns with a
  fixed top header row. Do not let one panel overflow into another.
- Comparison tables use uniform row height and bold column headers.

### R6. Color discipline
- Module accent `QGREEN` is reserved for "correction succeeded" /
  "good outcome" states.
- Errors injected on circuits are always `QRED`.
- Inactive panels in a comparison view dim to opacity 0.35 while one
  panel is being explained.

### R7. Quantum accuracy
- No-cloning theorem is mentioned wherever the audience might think
  encoding = copying.
- 3-qubit repetition code only protects against bit-flips. State this
  explicitly.
- T_2 ≤ 2 T_1 always; never draw curves violating this.
- Fidelity is between 0 and 1; never animate a curve outside that
  range.
- Real hardware comparison: state numbers as orders of magnitude or
  ranges, not exact values that go stale.

### R8. Motion
- Decay animations: `run_time` ≥ 2.5s so the viewer can track the
  decay.
- Error-correction circuit beats: 1.0–1.5s per gate, `LONG_PAUSE`
  after each protocol phase (encode / error / syndrome / correct).

### R9. Timing
- Title hold 2s. Section header fade 0.6s.
- Comparison table reveal: row by row, 0.5s per row.

### R10. Validation
- Decay curves correctly ordered (`T_2` ≤ `2 T_1`).
- All schematics labeled.
- No claim about platform superiority.
- Repetition code limitations stated explicitly.
- Bloch vector never escapes the unit sphere even during decoherence.

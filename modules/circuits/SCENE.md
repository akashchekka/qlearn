# Module 3 — Quantum Circuits · SCENE.md

## Overview
- **Topic**: Quantum circuit model — the programming language of quantum computers
- **Hook**: "Classical circuits have AND gates and wires. Quantum circuits have something fundamentally different"
- **Target Audience**: Completed Modules 1-2; knows qubits and superposition
- **Estimated Length**: ~14 minutes (3 scenes × ~4.5 min each)
- **Key Insight**: A quantum circuit is a sequence of unitary operations on qubits — reversible, probabilistic, and read left-to-right

## Narrative Arc
From classical circuits to quantum circuits, we learn to read the notation (wires, gates, measurements), then understand why depth matters for real hardware.

## Transitions & Flow
- Scene 1: classical vs quantum contrast sets the stage
- Scene 2: hands-on reading of a Bell circuit
- Scene 3: width/depth/decoherence connects to hardware reality
- Recurring motif: circuits build left-to-right with stepping cursor

## Color Palette
- Primary: `QCYAN` (#00E5FF) — quantum wires, control dots
- Secondary: `QBLUE` (#4FC3F7) — gate fills
- Accent: `QGREEN` (#66BB6A) — measurement symbols
- Highlight: `QYELLOW` (#FFEE58) — active gate highlight
- Classical: `QGRAY` (#B0BEC5) — classical wires, secondary text

## Mathematical Content
- F = e^{-d/d_c} (fidelity vs depth)
- Circuit width (qubits) and depth (layers)

## Implementation Order
1. scene01 (foundational contrast)
2. scene02 (uses QuantumCircuit helper)
3. scene03 (extends circuit concepts)

Scene specifications for `modules/circuits/`. Copilot MUST read the
**RULES** section at the bottom of this file before generating or editing any
scene in this module. Every rule is binding.

Shared imports for every scene in this module:

```python
from manim import *
from common.scene_base import QScene
from common.circuit import (
    build_wire, place_gate, place_cnot,
)  # use project circuit helpers when present
from common.styles import (
    QBLUE, QRED, QGREEN, QPURPLE, QORANGE, QYELLOW,
    QCYAN, QWHITE, QGRAY, QDARK,
    STEP_PAUSE, LONG_PAUSE,
)
```

Module accent color: **`QCYAN`** (`#00E5FF`). Module number: **3**.

---

## 2.1 — What Is a Circuit? (`scene01_what_is_a_circuit.py`)

- **Class name:** `WhatIsACircuitScene`
- **Teaching objective:** Contrast a classical logic circuit with a quantum
  circuit, establish time-flow direction (left → right), and list the
  essential differences (reversibility, superposition, measurement).
- **Beats:**
  1. Title card.
  2. Classical circuit panel: two input bits, an AND gate, a single output
     bit. Use rectangles + labels. Keep wires orthogonal.
  3. Quantum circuit panel (right-hand side or swapped-in): two horizontal
     qubit wires, a gate box (e.g., H), and a measurement symbol at the
     end.
  4. Side-by-side comparison table with exactly three rows: "Reversible?",
     "State space", "Output". Keep to 3 rows; do not overload.
  5. Fade the comparison, then show a single arrow labeled "time" running
     left → right beneath a quantum wire.
- **Color mapping:**
  - Classical wires / bits → `QGRAY`.
  - Quantum wires → `QCYAN`.
  - Gates → `QBLUE` fill with `QWHITE` label.
  - Measurement symbol → `QGREEN`.
- **Pitfalls:**
  - Do NOT mix quantum and classical wires on the same rail.
  - Do NOT imply a quantum circuit has "inputs/outputs" like a classical
    logic gate — frame it as state evolution.

---

## 2.2 — Circuit Notation (`scene02_circuit_notation.py`)

- **Class name:** `CircuitNotationScene`
- **Teaching objective:** Teach how to read a quantum circuit: wire labels
  (q₀, q₁, …), single-qubit gate boxes, control/target conventions, and
  measurement. Walk through a small circuit step-by-step.
- **Beats:**
  1. Title card.
  2. Draw two wires with labels `q_0` and `q_1` on the left margin and the
     initial state `|0⟩` next to each wire end.
  3. Place an H on `q_0`. Highlight, label "Hadamard — creates
     superposition", then pause.
  4. Place a CNOT with control on `q_0`, target on `q_1`. Highlight the
     control dot + target ⊕ + connecting line. Label "entangles the two
     qubits".
  5. Place a measurement on each wire. Explain double-line = classical
     result.
  6. Step through execution: highlight each gate in sequence using
     `Indicate` or a moving cursor.
- **Color mapping:**
  - Wires → `QCYAN`; control dot → `QCYAN`; target ⊕ → `QPURPLE`.
  - Active gate highlight → `QYELLOW`.
- **Pitfalls:**
  - Control and target MUST be perfectly vertically aligned.
  - Never leave a partial circuit on screen when transitioning to the
    next beat.

---

## 2.3 — Circuit Depth (`scene03_circuit_depth.py`)

- **Class name:** `CircuitDepthScene`
- **Teaching objective:** Define circuit **width** (number of qubits) and
  **depth** (number of sequential layers), show a short vs deep circuit,
  and connect depth to the decoherence/error budget.
- **Beats:**
  1. Title card.
  2. Display a 4-wire circuit with gates grouped into visible layers
     separated by faint vertical gridlines.
  3. Animate `width = 4` with a vertical brace on the left; `depth = N`
     with a horizontal brace on the bottom counting the layers.
  4. Contrast: a shallow circuit (depth 3) vs a deep circuit (depth 15)
     side-by-side. Same width.
  5. Overlay a decoherence fidelity curve `F = e^{-d/d_c}` decreasing with
     depth. Annotate "decoherence budget".
- **Color mapping:**
  - Layer gridlines → `QGRAY` at opacity 0.3.
  - Width brace → `QBLUE`, depth brace → `QPURPLE`.
  - Fidelity curve → `QORANGE`.
- **Pitfalls:**
  - Gates in the "same layer" must share the same x-coordinate.
  - Do NOT let gates overlap wires that they do not act on.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "What Is a Circuit?"). Do NOT show the
  module number or lesson number on screen. Call
  `self.show_title_card("<Topic Name>")`.
- Use `self.show_section(...)` per major section; fade sections out
  before starting the next.

### R2. Imports and constants
- Pull colors/sizes/pauses from `common.styles`. No hardcoded literals.
- Reuse circuit helpers from `common.circuit` when available (wires,
  gate boxes, CNOT, measurement) instead of re-drawing from primitives.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Circuit construction
- Always draw **wires first**, then gates, then annotations/highlights.
- Build circuits left → right. Do not move the whole circuit to make
  room — plan the final layout before placing the first gate.
- Gate boxes must be uniform size across the scene (use one size
  constant per scene).
- Wire spacing must be uniform across all wires in a circuit.
- Gate labels must be centered inside the gate box.
- Controlled operations: control dot and target symbol share an exact
  x-coordinate; the connecting line is straight and terminates at their
  centers.
- Measurement symbols are visually distinct from unitary gates (use the
  meter icon or `M` style consistently).

### R4. Layout
- Reserve a title area (top), main visualization area (center), and
  explanation area (bottom or right). Do not cross these zones.
- Maintain ≥ 0.3-unit margins from frame edges.
- Labels sit close to their target but never overlap it.
- If a circuit is wider than the frame, chunk it into sections; do not
  scroll unless scrolling is the explicit lesson.

### R5. Motion
- Introduce gates with `FadeIn` or `Create`; highlight the active gate
  with `Indicate` or a soft outline in `QYELLOW`.
- Animate a stepping cursor left → right when walking through execution.
- Never animate gates and wires simultaneously on first reveal — wires
  come first.
- Pause (`STEP_PAUSE`) after each gate placement.

### R6. Notation
- Wire labels: `q_0`, `q_1`, … from top to bottom.
- Initial states shown as `|0⟩` on the left of each wire.
- Double-line = classical wire after measurement.
- Gate names inside boxes: `H`, `X`, `Y`, `Z`, `S`, `T`, `Rx`, `Ry`,
  `Rz`. Use LaTeX for subscripts.

### R7. Color discipline
- Quantum wires: `QCYAN`. Classical wires: `QGRAY` (double line).
- Single-qubit gate fill: `QBLUE` or `QPURPLE`. Controls/targets:
  `QCYAN` dot, `QPURPLE` ⊕.
- Active highlight: `QYELLOW` only, and only on the currently discussed
  element.
- Dim inactive elements to 0.35 opacity when focus shifts.

### R8. Timing
- Title card hold: 2s. Section fade: 0.6s.
- Gate placement: 0.8–1.2s. Step-through cursor: 0.6s per step.
- Final pause on completed circuit: `LONG_PAUSE`.

### R9. Quantum accuracy
- Quantum wires carry states, not classical bits. Do not label them with
  `0/1` (use `|0⟩`).
- Gates are unitary. Do not depict "splitting" or "merging" of wires
  except for measurements and classical fan-out.
- CNOT control never changes; only the target flips — if animating,
  make this explicit.

### R10. Validation
- Control/target alignment verified.
- Wire spacing uniform.
- All gate boxes same size.
- No label overlaps wire or gate body.
- Scene parses as a valid circuit if paused at any frame.

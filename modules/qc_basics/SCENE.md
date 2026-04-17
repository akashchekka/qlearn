# Module 2 — Quantum Computing Basics · SCENE.md

## Overview
- **Topic**: Core quantum computing concepts — qubits, Bloch sphere, superposition, measurement
- **Hook**: "A classical bit is 0 or 1. A qubit can be both — and here's exactly what that means"
- **Target Audience**: Beginners with Module 1 foundations; no programming needed
- **Estimated Length**: ~18 minutes (4 scenes × ~4.5 min each)
- **Key Insight**: A qubit isn't magic — it's a precisely defined mathematical object with measurable probabilities

## Narrative Arc
We start by contrasting bits with qubits, then visualize the qubit geometrically on the Bloch sphere, build intuition for superposition with probability bars, and finally show what happens when we measure — collapse and statistics.

## Transitions & Flow
- Scene 1→2: from abstract equation to geometric picture
- Scene 2→3: from single state to probability interpretation
- Scene 3→4: from theory to what actually happens in the lab
- Recurring motif: probability bars track state changes across scenes

## Color Palette
- Primary: `QBLUE` (#4FC3F7) — |0⟩, α, classical 0
- Secondary: `QRED` (#EF5350) — |1⟩, β, classical 1
- Accent: `QGREEN` (#66BB6A) — measurement, Born rule
- Supporting: `QPURPLE` (#AB47BC) — superposition section headers
- Highlight: `QYELLOW` (#FFEE58) — state vector on Bloch sphere
- Neutral: `QGRAY` (#B0BEC5) — secondary text

## Mathematical Content
- |ψ⟩ = α|0⟩ + β|1⟩ (superposition)
- |α|² + |β|² = 1 (normalization)
- |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩ (Bloch parametrization)
- P(0) = |α|², P(1) = |β|² (Born rule)

## Implementation Order
1. scene01 (no dependencies)
2. scene02 (uses BlochSphere from common/quantum.py)
3. scene03 (references superposition from scene01)
4. scene04 (depends on concepts from scenes 01-03)

---

Scene specifications for `modules/qc_basics/`. Copilot MUST read the
**RULES** section at the bottom of this file before generating or editing any
scene in this module. Every rule is binding.

Shared imports for every scene in this module:

```python
from manim import *
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QGREEN, QPURPLE, QORANGE, QYELLOW,
    QWHITE, QGRAY, QDARK,
    STEP_PAUSE, LONG_PAUSE, TITLE_HOLD,
)
```

Module accent color: **`QBLUE`** (`#4FC3F7`). Module number: **2**.

---

## 1.1 — What Is a Qubit? (`scene01_what_is_a_qubit.py`)

- **Class name:** `WhatIsAQubit`
- **Teaching objective:** Contrast a classical bit (0 OR 1) with a qubit
  (α|0⟩ + β|1⟩), and introduce the normalization constraint |α|² + |β|² = 1.
- **Beats (in order):**
  1. Title card — show only the topic name "What Is a Qubit?" (no module or lesson number on screen).
  2. Classical bit: two boxes labeled `0` (blue) and `1` (red) with "OR"
     between them; show a switch arrow from 0 → 1.
  3. Clear. Show `|0⟩` and `|1⟩` kets with an explicit "AND" between them.
  4. Superposition equation `|ψ⟩ = α|0⟩ + β|1⟩` written in chunks
     (state symbol → α|0⟩ → +β|1⟩). Label α and β as complex amplitudes.
  5. Normalization constraint `|α|² + |β|² = 1` revealed below the equation,
     with a short explanatory label ("probability amplitudes sum to 1").
  6. Brief recap beat: bit = one of two values, qubit = superposition.
- **Color mapping (must stay consistent):**
  - `|0⟩`, α, "classical 0" → `QBLUE`
  - `|1⟩`, β, "classical 1" → `QRED`
  - Secondary text / hints → `QGRAY`
- **Key mobjects to keep named:** `bit_0`, `bit_1`, `ket_0`, `ket_1`,
  `superposition_eq`, `norm_eq`.
- **Pitfalls:**
  - Do NOT draw the qubit as "both 0 and 1 at the same time" blobs.
  - Do NOT conflate amplitude magnitude with probability in this scene.

---

## 1.2 — The Bloch Sphere (`scene02_bloch_sphere.py`)

- **Class name:** `BlochSphereScene`
- **Teaching objective:** Introduce the Bloch sphere as the geometric picture
  of a single-qubit pure state, identify basis poles, and show how arbitrary
  states are parameterized by `θ` and `φ`.
- **Beats:**
  1. Title card.
  2. Draw a clean 3D sphere with three labeled axes (x, y, z). Use
     consistent axis colors across the module (x=QORANGE, y=QGREEN, z=QBLUE).
  3. Mark the north pole as `|0⟩` and south pole as `|1⟩`. Label them
     outside the sphere; do not place text on the sphere surface.
  4. Show the `|+⟩` and `|−⟩` states on the x-axis; `|+i⟩`, `|−i⟩` on
     the y-axis (introduce only the ones needed for this lesson).
  5. Introduce an arbitrary state vector. Reveal the angles `θ` (polar from
     +z) and `φ` (azimuthal from +x) with small labeled arcs.
  6. Write the parametric form
     `|ψ⟩ = cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩` off to the side.
  7. Short hold, then fade out.
- **Color mapping:**
  - `|0⟩`/+z → `QBLUE`, `|1⟩`/−z → `QRED`.
  - State vector → `QYELLOW`.
  - Angle arcs → `QGRAY` or `QPURPLE` (choose one and keep it).
- **Pitfalls:**
  - Do NOT rotate the sphere continuously while explaining.
  - Do NOT let the state arrow, angle arcs, and axis labels pile on top of
    one another — stagger their introduction.
  - Do NOT swap north/south pole conventions mid-scene.

---

## 1.3 — Superposition (`scene03_superposition.py`)

- **Class name:** `SuperpositionScene`
- **Teaching objective:** Build intuition for superposition via a coin
  analogy, then move to equal and unequal superpositions with probability
  bars driven by |α|² and |β|².
- **Beats:**
  1. Title card.
  2. Spinning-coin analogy (short, labeled "intuition only"). Remove it
     before the formal content.
  3. Equal superposition `|+⟩ = (|0⟩ + |1⟩)/√2`. Show two equal-height
     probability bars (0.5 and 0.5) next to the equation.
  4. Unequal superposition example
     `|ψ⟩ = √0.8 |0⟩ + √0.2 |1⟩`. Bars update to 0.8 / 0.2.
  5. Explicit statement: "bar height = |amplitude|², not the amplitude."
  6. Short recap.
- **Color mapping:** `|0⟩` bar → `QBLUE`, `|1⟩` bar → `QRED`.
- **Pitfalls:**
  - Do NOT let probability bars exceed the axis or sum ≠ 1.
  - Do NOT imply the coin analogy is literally what happens physically.
  - Bar ket labels (`|0⟩`, `|1⟩`) MUST sit on the same horizontal line
    (see **R4b**). Use a fixed `LABEL_Y`, not `next_to(bar, DOWN)`.

---

## 1.4 — Measurement (`scene04_measurement.py`)

- **Class name:** `MeasurementScene`
- **Teaching objective:** Show measurement collapse (one shot) and the
  statistical distribution that emerges from many shots.
- **Beats:**
  1. Title card.
  2. Start with a state `|ψ⟩ = α|0⟩ + β|1⟩` and its probability bars.
  3. Single measurement: highlight one outcome, collapse bars to a single
     bar of height 1 (0 or 1), label the collapse explicitly as
     irreversible.
  4. Reset to the original state.
  5. Repeated-measurement histogram: animate N shots accumulating into two
     bins approaching |α|² and |β|².
  6. Annotate that the histogram approximates the Born-rule probabilities.
- **Color mapping:** outcome 0 → `QBLUE`, outcome 1 → `QRED`,
  measurement icon → `QGREEN`.
- **Pitfalls:**
  - Do NOT animate collapse as a smooth reversible rotation.
  - Do NOT label the histogram as "the state" — it is outcome statistics.
  - State labels near the Bloch sphere MUST NOT overlap the sphere's
    built-in `|0⟩`/`|1⟩` pole labels. Place them in a fixed equation
    zone (see **R4a**).
  - Histogram bars MUST share a fixed baseline. Ket labels below bars
    MUST share a fixed y-coordinate (see **R4b**).

---

## RULES (binding — Copilot must follow strictly)

These rules are derived from the project-wide `copilot-instructions.md` and
apply to every scene file in this module.

### R1. Scene scaffolding
- Every scene class inherits from `QScene`.
- The first beat must be a title card that displays **only the topic name**
  (e.g., "What Is a Qubit?"). Do NOT show the module number or lesson
  number on screen. Call `self.show_title_card("<Topic Name>")`.
- Use `self.show_section(...)` for each major section header.
- End each section with `self.fade_out_group(...)` or `self.clear_scene()`
  before starting the next section. No leftover mobjects between sections.

### R2. Imports and constants
- Import colors, sizes, and pauses from `common.styles`. Do NOT hardcode
  hex colors, font sizes, or run-times inside a scene.
- Use the module accent color (`QBLUE`) for module-level emphasis only.
- `common/quantum.py` exposes only `BlochSphere`. Scene-specific helpers
  (bar charts, ket displays, probability bars) MUST be defined locally
  inside the scene file that needs them so that one scene's changes cannot
  break another scene.

### R3. One idea per beat
- Each beat teaches exactly one concept. Split large ideas into multiple
  beats or multiple scenes instead of stacking them on screen.
- Never introduce new text while a major transform is still playing,
  unless that text is part of the transform.

### R4. Layout and spacing
- Maintain clear margins from screen edges; never place mobjects within
  0.3 units of the frame edge.
- Labels must be anchored near their target but must not touch or overlap
  it. Re-anchor labels after objects move.
- Check collisions along the entire animation path, not just the final
  frame.
- Use `VGroup`, `.arrange(...)`, `.next_to(...)`, and `.align_to(...)` for
  layout; do not rely on accidental placement.

#### R4a. Bloch sphere + external labels
- When a scene places text above or near a `BlochSphere`, the text MUST
  NOT overlap the sphere's built-in pole labels (`|0⟩` at north, `|1⟩`
  at south). Place external state labels in a **separate zone** (e.g.,
  top-left equation area or a fixed right-hand column) rather than using
  `next_to(bloch, UP)`, which collides after the state arrow moves to
  the north pole.
- After collapse to `|0⟩`, the state label must remain in its fixed zone
  and never drift into the sphere's `|0⟩` label.

#### R4b. Probability bar charts
- All bars MUST share a **fixed baseline y-coordinate** (`BASELINE_Y`).
  Position bar bottoms with explicit coordinates, NOT with
  `align_to(ORIGIN, DOWN)` followed by `next_to(ORIGIN, LEFT/RIGHT)`.
- Ket labels (`|0⟩`, `|1⟩`, …) below the bars MUST share a **fixed
  label y-coordinate** (`LABEL_Y`) so they remain on the same horizontal
  line regardless of bar height.
- When bar height is near zero (e.g., `p ≈ 0`), the bar is still
  anchored at `BASELINE_Y`; labels never float up.
- Percentage text above bars uses `.next_to(bar, UP, buff=0.1)` and
  updates when the bar animates.

### R5. Motion
- Prefer `FadeIn`, `FadeOut`, `Write`, `Create`, `Transform`,
  `ReplacementTransform`. Avoid elastic, bouncing, flashing, or
  decorative spinning.
- Sequential animation is preferred over many simultaneous ones.
- Pause with `self.pause()` (STEP_PAUSE) after each meaningful
  transformation; use `LONG_PAUSE` after a key insight.
- Highlight first → transform second → explain third.

### R6. Camera
- Keep the camera static unless teaching 3D geometry (scene 1.2).
- Never use camera motion to compensate for poor layout.
- If the Bloch sphere is rotated, rotate it only once, slowly, and only
  when geometrically necessary.

### R7. Notation
- Use consistent ket notation (`|0⟩`, `|1⟩`, `|+⟩`, `|−⟩`, `|ψ⟩`).
- Basis ordering, symbol choices, and phase conventions MUST match the
  rest of the project (see `MODULES.md` and other modules' SCENE.md).
- `|0⟩` is always `QBLUE`; `|1⟩` is always `QRED`. Do not swap.
- Amplitudes use α, β. Do not silently rename them mid-scene.

### R8. Equations
- Reveal derivations in chunks using `Write` or `TransformMatchingTex`.
  Never dump a wall of math in one frame.
- Keep equations aligned; use `MathTex(..., substrings_to_isolate=[...])`
  when components must be colored or animated independently.

### R9. Color discipline
- Colors have semantic meaning (basis states, measurement, phase).
  Do not reuse a semantic color for decoration.
- Maximum of 4 distinct accent colors on screen at once.
- Inactive elements are dimmed via `set_opacity(0.35)`, not removed, when
  they still provide context.

### R10. Quantum accuracy
- Measurement is not reversible — never animate collapse as a smooth
  two-way rotation.
- Bar heights representing probabilities must sum to 1.
- Distinguish amplitude magnitude from probability explicitly when both
  appear.
- Normalization must hold for every displayed state.

### R11. Timing
- Titles: ≤ 2s hold. Section headers: fade out before next section.
- Standard transforms: `run_time` between 0.8s and 1.5s.
- Long builds (e.g., superposition equation): chunk into ≤ 1.5s steps.
- After every major insight: `self.pause(LONG_PAUSE)`.

### R12. Validation before committing a scene
- No unintentional overlaps at any frame.
- All text readable at 1080p.
- Every mobject is either explained, labeled, or removed.
- Scene makes sense without narration.
- Notation and colors match every other scene in the project.

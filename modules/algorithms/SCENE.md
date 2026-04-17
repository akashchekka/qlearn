# Module 6 — Algorithms · SCENE.md

## Overview
- **Topic**: Landmark quantum algorithms — Deutsch-Jozsa, Grover's search, QFT, Shor's factoring
- **Hook**: "One quantum query vs millions of classical ones. Here's how quantum algorithms achieve exponential speedups"
- **Target Audience**: Completed Modules 1-5; understands circuits, gates, entanglement
- **Estimated Length**: ~22 minutes (4 scenes × ~5.5 min each)
- **Key Insight**: Quantum algorithms exploit superposition and interference to solve specific problems exponentially faster than classical algorithms

## Narrative Arc
We progress from the simplest oracle algorithm (Deutsch-Jozsa) through the most practical (Grover's search), to the most impactful (Shor's factoring via QFT). Each scene follows: problem → idea → circuit → outcome → speedup.

## Transitions & Flow
- Scene 1: DJ — simplest proof of quantum advantage
- Scene 2: Grover — amplitude amplification (most visual)
- Scene 3: QFT — the engine inside Shor's algorithm
- Scene 4: Shor — the algorithm that threatens RSA
- Each scene has a speedup comparison beat at the end

## Color Palette
- Primary: `QRED` (#EF5350) — module accent, quantum speedup bars
- Oracle: `QORANGE` (#FFA726) — oracle blocks and highlights
- Input register: `QBLUE` (#4FC3F7), Work register: `QRED` (#EF5350)
- Measurement: `QGREEN` (#66BB6A)
- Geometric/phase: `QPURPLE` (#AB47BC)
- Classical comparison: `QGRAY` (#B0BEC5)

## Mathematical Content
- f: {0,1}^n → {0,1}, constant vs balanced (DJ)
- Amplitude amplification: oracle + diffusion about mean (Grover)
- |x⟩ → (1/√N) Σ e^{2πixk/N} |k⟩ (QFT)
- f(x) = a^x mod N, period finding, continued fractions (Shor)
- Speedups: 1 vs 2^{n-1}+1 (DJ), O(√N) vs O(N) (Grover), O((log N)³) vs sub-exponential (Shor)

## Implementation Order
1. scene01 (DJ — standalone)
2. scene02 (Grover — standalone)
3. scene03 (QFT — needed before Shor)
4. scene04 (Shor — references QFT)

---

Scene specifications for `modules/algorithms/`. Copilot MUST read the
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

Module accent color: **`QRED`** (`#EF5350`). Module number: **6**.

---

## 6.1 — Deutsch–Jozsa (`scene01_deutsch_jozsa.py`)

- **Class name:** `DeutschJozsaScene`
- **Teaching objective:** Define constant vs balanced functions, show the
  DJ circuit (n + 1 qubits, oracle, H layers), and emphasize the
  exponential speedup (1 query vs 2^{n−1} + 1 classical queries worst
  case).
- **Beats:**
  1. Title card.
  2. Define f: {0,1}^n → {0,1}; show small truth tables for one constant
     example and one balanced example.
  3. DJ circuit (n=2 for clarity): top n wires init to `|0⟩`, ancilla to
     `|1⟩`, H on every wire, oracle `U_f`, H on top n wires, measure top
     n wires.
  4. Walk through state evolution at four checkpoints. Keep evolution
     text in a fixed right zone; circuit on the left.
  5. Outcome rule: top register all-zero ⇒ constant; otherwise balanced.
  6. Speedup comparison: classical worst case `2^{n−1}+1` queries vs
     quantum `1`. Bar comparison.
- **Color mapping:** input register → `QBLUE`, ancilla → `QRED`, oracle
  → `QORANGE`, measurement → `QGREEN`.

## 6.2 — Grover's Search (`scene02_grovers_search.py`)

- **Class name:** `GroversSearchScene`
- **Teaching objective:** Database search problem, amplitude
  amplification per Grover iteration, geometric (2D) view with rotation
  by 2θ per iteration, optimal iteration count `≈ (π/4)√N`.
- **Beats:**
  1. Title card.
  2. Database of N=8 items as a row of small squares; mark one as the
     "target" with `QORANGE`.
  3. Amplitude bar chart over the 8 items, all heights `1/√8`. Apply
     oracle: target amplitude flips sign.
  4. Apply diffusion (inversion about the mean): show the mean line,
     reflect each bar across it.
  5. Repeat the (oracle + diffusion) cycle 2 times; target amplitude
     visibly grows.
  6. 2D geometric view: vector in the plane spanned by `|good⟩`/`|bad⟩`,
     rotating by `2θ` per iteration toward `|good⟩`.
  7. State the optimal count `≈ (π/4)√N`.
- **Color mapping:** non-target → `QGRAY` bars, target → `QORANGE`,
  mean line → `QYELLOW`, geometric vector → `QPURPLE`.

## 6.3 — Quantum Fourier Transform (`scene03_quantum_fourier_transform.py`)

- **Class name:** `QFTScene`
- **Teaching objective:** State the QFT equation `|x⟩ → (1/√N) Σ_k
  e^{2πi xk/N} |k⟩`, visualize roots of unity on the unit circle, and
  build a 3-qubit QFT circuit (H + controlled-phase + SWAPs).
- **Beats:**
  1. Title card.
  2. QFT formula displayed in chunks; label each piece (sum, phase,
     normalization).
  3. Roots of unity on the unit circle (N = 8). Highlight one `e^{2πi k
     /N}` arrow at a time as k advances.
  4. 3-qubit QFT circuit: H on q_0, controlled-`R_2` and `R_3` from
     q_1/q_2 to q_0, recurse on q_1, then SWAP at the end.
  5. Note: inverse QFT reverses the order; just state it, do not draw.
- **Color mapping:** roots of unity arrows → `QPURPLE`, phase rotations
  in circuit → `QORANGE`, SWAP → `QYELLOW`.

## 6.4 — Shor's Algorithm (`scene04_shors_algorithm.py`)

- **Class name:** `ShorsAlgorithmScene`
- **Teaching objective:** Factoring problem framed as period finding;
  high-level steps (classical preprocessing, quantum period finding via
  modular exponentiation + QFT, classical post-processing); exponential
  speedup over best-known classical algorithms.
- **Beats:**
  1. Title card.
  2. Problem statement: "factor N = p · q". Small worked example
     `N = 15`.
  3. Reduction: factoring → finding period r of `f(x) = a^x mod N`.
  4. Plot `f(x)` for `a = 7, N = 15` showing periodicity.
  5. High-level circuit: input register (n qubits) + work register;
     blocks labeled "H^n", "U_f (modular exp)", "QFT^{−1}", measure.
     Do NOT draw internals — keep blocks abstract.
  6. Classical post-processing: continued fractions → r → factors.
  7. Speedup line: `O((log N)^3)` quantum vs `~exp((log N)^{1/3})`
     classical (general number field sieve).
- **Color mapping:** registers → `QBLUE` (input) and `QRED` (work),
  block boundaries → `QORANGE`, classical step → `QGREEN`.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Inherit from `QScene`. The first beat must be a title card that displays
  **only the topic name** (e.g., "Deutsch–Jozsa"). Do NOT show the module
  number or lesson number on screen. Call
  `self.show_title_card("<Topic Name>")`.
- Always end with a one-line "what we learned" recap before fading.

### R2. Imports and constants
- Pull every color/size/timing from `common.styles`.
- Reuse `common.circuit` helpers when drawing circuits.
- `common/quantum.py` exposes only `BlochSphere`. Any other visualization
  helper (bar charts, ket displays) must be defined locally inside the
  scene file that needs it.

### R3. Algorithm decomposition
- Each algorithm is taught as: **problem → idea → circuit → outcome →
  speedup**. Do not skip a step.
- Black-box subroutines (oracle, modular exponentiation, QFT inside
  Shor) are drawn as labeled blocks, not unrolled. Reserve unrolling
  for its dedicated scene (e.g., QFT in 6.3).

### R4. Layout
- Three zones: circuit (left), state/derivation (right), recap line
  (bottom). Keep these zones fixed across the scene.
- Bar charts and 2D geometric views: keep axes labeled and scales
  stable across iterations so the change is comparable frame-to-frame.

### R5. Iteration animations (Grover, QFT, etc.)
- Each iteration is animated identically (same gestures, same timing).
  After 2–3 iterations, ellipsis or "× k" label takes over.
- Do not animate more than 4 iterations explicitly; summarize the rest.

### R6. Color discipline
- Oracle blocks: `QORANGE` border. Measurement: `QGREEN`. Speedup
  comparison bars: classical `QGRAY`, quantum `QRED`.
- Maximum 4 accent colors on screen at once.
- Inactive parts of the circuit dim to opacity 0.35 when focus shifts.

### R7. Equations
- Reveal long sums (QFT, DJ evolution) one term at a time using
  `Write` or `TransformMatchingTex`.
- Always show normalization factors and phase factors.
- Big-O speedup expressions live in their own zone; never overlay them
  on the circuit.

### R8. Quantum accuracy
- Speedups must be stated correctly (DJ: 1 vs `2^{n−1}+1` worst case;
  Grover: `O(√N)` vs `O(N)`; Shor: polynomial vs sub-exponential).
- Grover diffusion is "inversion about the mean", not "negation". Show
  the mean line.
- Shor's algorithm requires both the quantum subroutine (period
  finding) and classical post-processing — both must appear.

### R9. Timing
- Title 2s. Each algorithmic phase: build 1.0–1.5s, then `LONG_PAUSE`.
- Speedup comparison bar growth animation: 1.5s.

### R10. Validation
- Probability/amplitude bars sum/normalize correctly at every frame
  shown.
- Iterations look identical except for the changing data.
- All blocks labeled; no anonymous boxes.
- Speedup numbers match what's in the recap line.

# Module 1 — Foundations (Quantum Mechanics) · SCENE.md

## Overview
- **Topic**: Quantum mechanics fundamentals — the physics that underpins quantum computing
- **Hook**: "Before building quantum computers, we need to understand the strange rules of quantum mechanics"
- **Target Audience**: Absolute beginners; high-school math assumed, no physics prerequisites
- **Estimated Length**: ~25 minutes (7 scenes × ~3.5 min each)
- **Key Insight**: Quantum objects follow fundamentally different rules than classical objects — superposition, uncertainty, and spin are not limitations of our tools but properties of nature itself

## Narrative Arc
We begin with the mystery of wave-particle duality, then progressively build the mathematical language (states, uncertainty, spin, Schrödinger equation, Dirac notation, operators) needed to describe quantum systems. Each scene adds one conceptual layer, ending with the full operator/eigenvalue framework that quantum computing relies on.

## Transitions & Flow
- Scenes 1–3 build physical intuition (duality → states → uncertainty)
- Scene 4 bridges to computation (spin → qubits)
- Scenes 5–7 introduce the math framework (Schrödinger → Dirac → operators)
- Recurring motif: "classical analogy → quantum reality → key difference"

## Color Palette
- Primary: `QBLUE` (#4FC3F7) — |0⟩, position, spin-up, kets, eigenstates
- Secondary: `QRED` (#EF5350) — |1⟩, momentum, spin-down, bras
- Accent: `QGREEN` (#66BB6A) — key insights, Born rule, eigenvalues
- Supporting: `QPURPLE` (#AB47BC) — phase, inner products, operators
- Highlight: `QORANGE` (#FFA726) — time derivative, apparatus, oracles
- Neutral: `QGRAY` (#B0BEC5) — secondary text, explanatory labels

## Mathematical Content
- Δx·Δp ≥ ℏ/2 (uncertainty principle)
- |ψ⟩ = α|A⟩ + β|B⟩, P(A) = |α|², |α|²+|β|²=1 (Born rule)
- iℏ ∂/∂t |ψ(t)⟩ = Ĥ|ψ(t)⟩ and Ĥ|ψ⟩ = E|ψ⟩ (Schrödinger)
- ⟨φ|ψ⟩, P = |⟨φ|ψ⟩|² (Dirac notation)
- Â|a⟩ = a|a⟩ (eigenvalue equation)
- Ŝ_z = (ℏ/2)diag(1,−1) (spin-z operator)

## Implementation Order
1. scene01 (no dependencies)
2. scene02 (references Born rule from scene01 conceptually)
3. scene03 (builds on states from scene02)
4. scene04 (bridges to qubits — can be done in parallel with scene03)
5. scene05 (standalone equation scene)
6. scene06 (uses kets introduced in earlier scenes)
7. scene07 (builds on Dirac notation from scene06)

---

Scene specifications for `modules/foundations/`. Copilot MUST read the
**RULES** section at the bottom of this file before generating or editing any
scene in this module. Every rule is binding.

Module accent color: **`QBLUE`** (`#4FC3F7`). Module number: **1**.

---

## 1.1 — Wave-Particle Duality (`scene01_wave_particle_duality.py`)

- **Class name:** `WaveParticleDualityScene`
- **Duration**: ~4 minutes
- **Purpose**: Hook the viewer with the most famous quantum experiment
- **Teaching objective:** Show that quantum objects exhibit both wave and
  particle behavior. Use the double-slit experiment as the central example.

### Visual Elements
- Barrier with two slits, screen, source dot
- Animated particles traveling source → slit → screen
- Ghost-copy particles splitting through both slits (quantum case)
- Interference fringe pattern on screen

### Technical Notes
- Use `FadeIn(mob, shift=LEFT)` for directional particle entry
- Particle travel: `animate.move_to()` with `rate_func=linear`
- Fringes: `Rectangle` with `fill_opacity` proportional to cos²
- Use `Indicate()` on insight text for emphasis

### Narration Notes
- Emphasize "each particle interferes with itself" — not with other particles
- The observation beat should feel dramatic: pattern destruction = quantum weirdness

- **Beats:**
  1. Title card — topic name only.
  2. Classical particles through two slits: two bands on the screen.
  3. Quantum particles: interference pattern (wave behavior).
  4. Key insight: each particle goes through both slits.
  5. Observation destroys the pattern.
- **Color mapping:** classical dots → `QORANGE`, interference → `QBLUE`,
  insight → `QGREEN`, observation warning → `QRED`.

---

## 1.2 — Quantum States & Probability (`scene02_quantum_states.py`)

- **Class name:** `QuantumStatesScene`
- **Duration**: ~3 minutes
- **Purpose**: Establish the mathematical language of quantum states
- **Teaching objective:** Introduce quantum states as combinations of
  possibilities, probability amplitudes as complex numbers, and the Born rule.

### Visual Elements
- State equation with color-coded amplitudes
- Born rule equation with normalization box

### Technical Notes
- Use `TransformMatchingTex` when evolving from state eq to Born rule
- `SurroundingRectangle` for normalization highlight
- `Indicate()` on the normalization equation

### Narration Notes
- "Amplitude" is the new word; "probability = |amplitude|²" is the punchline

- **Beats:**
  1. Title card.
  2. Quantum state equation |ψ⟩ = α|A⟩ + β|B⟩.
  3. Amplitudes are complex numbers.
  4. Born rule: P(A) = |α|², normalization |α|²+|β|²=1.
- **Color mapping:** state A → `QBLUE`, state B → `QRED`, Born rule → `QGREEN`.

---

## 1.3 — Uncertainty Principle (`scene03_uncertainty_principle.py`)

- **Class name:** `UncertaintyPrincipleScene`
- **Duration**: ~3.5 minutes
- **Purpose**: Shatter the classical intuition that everything can be measured precisely
- **Teaching objective:** Explain Heisenberg's uncertainty principle as a
  fundamental limit of nature, not a measurement flaw.

### Visual Elements
- Heisenberg equation centered
- Side-by-side Axes plots: narrow Gaussian (position) vs wide Gaussian (momentum)
- Strikethrough on "instrument limitation" text

### Technical Notes
- Axes with `x_length=4.2` spread at `LEFT*3.3` / `RIGHT*3.3` for spacing
- Use `MathTex` inside `get_x_axis_label()` for axis labels
- `Create(cross)` over the misconception text for dramatic effect

### Narration Notes
- Build to the reveal: "NOT instruments — nature itself"

- **Beats:**
  1. Title card.
  2. The equation Δx·Δp ≥ ℏ/2.
  3. Visual: narrow position → wide momentum (and vice versa).
  4. Key point: fundamental property, not instrument limitation.
- **Color mapping:** position → `QBLUE`, momentum → `QRED`, key point → `QGREEN`.

---

## 1.4 — Spin & Stern-Gerlach (`scene04_spin.py`)

- **Class name:** `SpinScene`
- **Duration**: ~4 minutes
- **Purpose**: Bridge from physics to computing — spin IS a qubit
- **Teaching objective:** Introduce intrinsic spin, the Stern-Gerlach
  experiment (beam splits into exactly two), and the bridge to qubits.

### Visual Elements
- Stern-Gerlach apparatus: source, magnet (N/S), screen
- Beam splitting into up/down paths with arrows
- Spin-to-qubit correspondence equations

### Technical Notes
- Use `GrowArrow` for beam paths
- `Indicate()` on the "only 2 outcomes" text
- `FadeIn(mob, shift=DOWN)` for the bridge equations

### Narration Notes
- The key surprise: only TWO spots, never a continuum
- The bridge to qubits should feel like a natural conclusion

- **Beats:**
  1. Title card.
  2. Spin-1/2: |↑⟩ or |↓⟩, not classical rotation.
  3. Stern-Gerlach apparatus: source → magnet → two spots on screen.
  4. Connection: |↑⟩ ↔ |0⟩, |↓⟩ ↔ |1⟩ — spin systems are natural qubits.
- **Color mapping:** spin-up → `QBLUE`, spin-down → `QRED`, apparatus → `QORANGE`.

---

## 1.5 — Schrödinger Equation (`scene05_schrodinger_equation.py`)

- **Class name:** `SchrodingerEquationScene`
- **Duration**: ~3.5 minutes
- **Purpose**: Show that quantum mechanics has its own "F = ma"
- **Teaching objective:** Introduce the Schrödinger equation as the rule
  governing how quantum states evolve. Show both time-dependent and
  time-independent forms. Compare to F = ma conceptually.

### Visual Elements
- Color-coded equation with labeled parts below
- Time-independent form with energy label
- Classical vs quantum comparison text

### Technical Notes
- Use `MathTex` with multi-part splitting for independent coloring
- `FadeIn(lbl)` row-by-row for equation labels
- `Circumscribe()` on the key insight comparison

### Narration Notes
- Don't solve anything — just name the parts and explain the analogy

- **Beats:**
  1. Title card.
  2. Time-dependent equation iℏ ∂/∂t |ψ(t)⟩ = Ĥ|ψ(t)⟩, labeled part by part.
  3. Time-independent form Ĥ|ψ⟩ = E|ψ⟩.
  4. Key insight: "F = ma for classical, Schrödinger for quantum."
- **Color mapping:** iℏ → `QPURPLE`, time derivative → `QORANGE`,
  state → `QBLUE`, Hamiltonian → `QRED`, energy → `QGREEN`.

---

## 1.6 — Dirac Notation (`scene06_dirac_notation.py`)

- **Class name:** `DiracNotationScene`
- **Duration**: ~3.5 minutes
- **Purpose**: Equip the viewer with the notation used everywhere in QC
- **Teaching objective:** Teach bra-ket notation practically: kets as
  column vectors, bras as row vectors, inner products, and the connection
  to measurement probability.

### Visual Elements
- Ket ↔ column vector correspondence
- Bra ↔ row vector correspondence
- Orthogonality examples in a row
- Probability formula

### Technical Notes
- Use `TransformMatchingTex` when going from ket definition to examples
- `Indicate()` on orthogonality result ⟨0|1⟩ = 0
- Arrange orthogonality examples with `buff=1.0` for spacing

### Narration Notes
- Keep it practical: "this is just a compact way to write column vectors"

- **Beats:**
  1. Title card.
  2. Kets |ψ⟩ as column vectors; examples |0⟩, |1⟩.
  3. Bras ⟨ψ| as conjugate-transpose row vectors.
  4. Inner product ⟨φ|ψ⟩ = overlap; orthogonality examples.
  5. Probability: P = |⟨φ|ψ⟩|².
- **Color mapping:** kets → `QBLUE`, bras → `QRED`, inner product →
  `QPURPLE`, probability → `QGREEN`.

---

## 1.7 — Observables & Operators (`scene07_observables_operators.py`)

- **Class name:** `ObservablesOperatorsScene`
- **Duration**: ~3.5 minutes
- **Purpose**: Complete the QM framework — everything measurable is an operator
- **Teaching objective:** Physical quantities are represented by Hermitian
  operators; measurements yield eigenvalues. Show the eigenvalue equation
  and a concrete spin-z example.

### Visual Elements
- Observable list → operator equation → eigenvalue equation
- Labeled eigenstate/eigenvalue breakdown
- Spin-z matrix with eigenvalue results

### Technical Notes
- Use `FadeIn(lbl, shift=LEFT)` for row-by-row label reveal
- `Circumscribe()` on the eigenvalue equation as the key takeaway
- `Indicate()` on eigenvalue results ±ℏ/2

### Narration Notes
- The spin-z example ties back to Scene 4 — full circle

- **Beats:**
  1. Title card.
  2. List of observables (position, momentum, energy, spin).
  3. Operators as matrices acting on states; Hermitian = real eigenvalues.
  4. Eigenvalue equation Â|a⟩ = a|a⟩; label eigenstate and eigenvalue.
  5. Example: spin-z matrix, eigenvalues ±ℏ/2.
- **Color mapping:** operator → `QPURPLE`, eigenstate → `QBLUE`,
  eigenvalue → `QGREEN`, spin-up → `QBLUE`, spin-down → `QRED`.

---

## RULES (binding — Copilot must follow strictly)

### R1. Scene scaffolding
- Every scene class inherits from `QScene`.
- Title card shows **only the topic name**. Call `self.show_title_card("<Topic>")`.
- Use `self.show_section(...)` for each section. Fade out before next section.

### R2. Imports and constants
- All colors/sizes/pauses from `common.styles`. No hardcoded hex or font sizes.
- Scene-specific helpers defined locally, not in shared modules.

### R3. Simplicity
- These scenes target absolute beginners. Keep language simple.
- One idea per beat. No dense equations. Short text blocks.
- Use analogies but label them as analogies.

### R4. Layout
- Margins ≥ 0.3 units from frame edges.
- Labels near targets but never overlapping.
- Use explicit coordinates for bar/label alignment (see R4b in qc_basics).

### R5. Motion
- Prefer `FadeIn`, `FadeOut`, `Write`, `Create`. No decorative spinning.
- Sequential animations preferred. Pause after each insight.

### R6. Color discipline
- Max 4 accent colors on screen at once.
- `QBLUE` and `QRED` for paired concepts (up/down, A/B, position/momentum).
- `QGREEN` for key insights and confirmed results.

### R7. Physics accuracy
- Wave-particle duality: each particle interferes with itself, not with others.
- Uncertainty principle: fundamental, not an instrument limitation.
- Spin: intrinsic property, not classical rotation.
- Born rule: probability = |amplitude|², always state this.

### R8. Validation
- No overlapping text at any frame.
- All text readable at 1080p.
- Scene makes sense without narration.

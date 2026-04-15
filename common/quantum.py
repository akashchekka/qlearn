"""Quantum visualization helpers — Bloch sphere, state vectors, ket displays."""
from __future__ import annotations
import numpy as np
from manim import *
from .styles import QBLUE, QRED, QGRAY, QWHITE, QPURPLE, MATH_FONT_SIZE


# ── Bloch Sphere ──────────────────────────────────────────────

class BlochSphere(VGroup):
    """Wireframe Bloch sphere with axis labels & a state‑vector arrow."""

    def __init__(
        self,
        radius: float = 1.8,
        theta: float = 0.0,
        phi: float = 0.0,
        show_axes: bool = True,
        show_labels: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.radius = radius
        self._theta = theta
        self._phi = phi

        # Main sphere (circle)
        self.sphere_circle = Circle(radius=radius, color=QGRAY, stroke_opacity=0.3)
        self.add(self.sphere_circle)

        # Equator ellipse
        self.equator = Ellipse(
            width=2 * radius, height=0.6 * radius,
            color=QGRAY, stroke_opacity=0.25,
        )
        self.add(self.equator)

        if show_axes:
            # Z axis
            self.z_axis = DashedLine(
                radius * DOWN, radius * UP, color=QGRAY, stroke_opacity=0.4
            )
            # X axis
            self.x_axis = DashedLine(
                radius * LEFT, radius * RIGHT, color=QGRAY, stroke_opacity=0.4
            )
            self.add(self.z_axis, self.x_axis)

        if show_labels:
            self.label_0 = MathTex(r"|0\rangle", font_size=24, color=QBLUE).next_to(
                radius * UP, UP, buff=0.15
            )
            self.label_1 = MathTex(r"|1\rangle", font_size=24, color=QRED).next_to(
                radius * DOWN, DOWN, buff=0.15
            )
            self.label_plus = MathTex(r"|+\rangle", font_size=20, color=QGRAY).next_to(
                radius * RIGHT, RIGHT, buff=0.15
            )
            self.label_minus = MathTex(r"|-\rangle", font_size=20, color=QGRAY).next_to(
                radius * LEFT, LEFT, buff=0.15
            )
            self.add(self.label_0, self.label_1, self.label_plus, self.label_minus)

        # State vector arrow
        self.state_arrow = Arrow(
            ORIGIN,
            self._state_point(),
            buff=0,
            color=QWHITE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        self.state_dot = Dot(self._state_point(), color=QWHITE, radius=0.06)
        self.add(self.state_arrow, self.state_dot)

    def _state_point(self) -> np.ndarray:
        """Convert (θ, φ) to 2‑D projection on the Bloch sphere."""
        x = self.radius * np.sin(self._theta) * np.cos(self._phi)
        y = self.radius * np.cos(self._theta)
        return np.array([x, y, 0])

    def animate_to_state(self, theta: float, phi: float, run_time: float = 1.5):
        """Return an AnimationGroup that moves the state vector."""
        self._theta = theta
        self._phi = phi
        new_point = self._state_point()
        return AnimationGroup(
            self.state_arrow.animate.put_start_and_end_on(ORIGIN, new_point),
            self.state_dot.animate.move_to(new_point),
            run_time=run_time,
        )

    def get_state_point(self) -> np.ndarray:
        return self._state_point()


# ── State Vector Bar Chart ────────────────────────────────────

class StateVectorDisplay(VGroup):
    """Bar chart showing probability amplitudes for |0⟩ and |1⟩."""

    def __init__(self, alpha: complex = 1, beta: complex = 0, bar_height: float = 2.0, **kwargs):
        super().__init__(**kwargs)
        self.bar_height = bar_height
        self._alpha = alpha
        self._beta = beta

        p0 = abs(alpha) ** 2
        p1 = abs(beta) ** 2

        self.bar0 = Rectangle(
            width=0.6, height=bar_height * p0,
            fill_color=QBLUE, fill_opacity=0.8, stroke_width=0,
        ).align_to(ORIGIN, DOWN)
        self.bar1 = Rectangle(
            width=0.6, height=bar_height * p1,
            fill_color=QRED, fill_opacity=0.8, stroke_width=0,
        ).align_to(ORIGIN, DOWN)

        self.bar0.next_to(ORIGIN, LEFT, buff=0.3)
        self.bar1.next_to(ORIGIN, RIGHT, buff=0.3)

        self.lbl0 = MathTex(r"|0\rangle", font_size=22, color=QBLUE).next_to(self.bar0, DOWN, buff=0.15)
        self.lbl1 = MathTex(r"|1\rangle", font_size=22, color=QRED).next_to(self.bar1, DOWN, buff=0.15)

        self.prob0 = Text(f"{p0:.0%}", font_size=20, color=QWHITE).next_to(self.bar0, UP, buff=0.1)
        self.prob1 = Text(f"{p1:.0%}", font_size=20, color=QWHITE).next_to(self.bar1, UP, buff=0.1)

        self.add(self.bar0, self.bar1, self.lbl0, self.lbl1, self.prob0, self.prob1)

    def update_probs(self, alpha: complex, beta: complex):
        """Return animations to smoothly update probabilities."""
        p0 = abs(alpha) ** 2
        p1 = abs(beta) ** 2
        self._alpha = alpha
        self._beta = beta

        new_bar0 = Rectangle(
            width=0.6, height=max(self.bar_height * p0, 0.02),
            fill_color=QBLUE, fill_opacity=0.8, stroke_width=0,
        ).align_to(self.bar0, DOWN).move_to(self.bar0, aligned_edge=DOWN)

        new_bar1 = Rectangle(
            width=0.6, height=max(self.bar_height * p1, 0.02),
            fill_color=QRED, fill_opacity=0.8, stroke_width=0,
        ).align_to(self.bar1, DOWN).move_to(self.bar1, aligned_edge=DOWN)

        new_prob0 = Text(f"{p0:.0%}", font_size=20, color=QWHITE).next_to(new_bar0, UP, buff=0.1)
        new_prob1 = Text(f"{p1:.0%}", font_size=20, color=QWHITE).next_to(new_bar1, UP, buff=0.1)

        return AnimationGroup(
            Transform(self.bar0, new_bar0),
            Transform(self.bar1, new_bar1),
            Transform(self.prob0, new_prob0),
            Transform(self.prob1, new_prob1),
        )


# ── Ket / State Label Helpers ─────────────────────────────────

def state_label(alpha_str: str, beta_str: str, color=QWHITE) -> MathTex:
    """Render  α|0⟩ + β|1⟩  as a single MathTex."""
    return MathTex(
        rf"{alpha_str}|0\rangle + {beta_str}|1\rangle",
        color=color,
        font_size=MATH_FONT_SIZE,
    )


def ket_colored(state: str) -> MathTex:
    """Return a ket with color based on state."""
    c = QBLUE if state == "0" else QRED if state == "1" else QPURPLE
    return MathTex(rf"|{state}\rangle", color=c, font_size=MATH_FONT_SIZE)

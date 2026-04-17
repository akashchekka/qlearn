"""Quantum visualization helpers — Bloch sphere."""
from __future__ import annotations
import numpy as np
from manim import *
from .styles import QBLUE, QRED, QGRAY, QWHITE


# ── Bloch Sphere ──────────────────────────────────────────────

class BlochSphere(VGroup):
    """Wireframe Bloch sphere with axis labels and a state-vector arrow.

    This is the only shared visualization in quantum.py.  Scene-specific
    helpers (bar charts, ket displays, etc.) should live in the scene
    file that needs them, so changes to one scene never break another.
    """

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

        # Main circle
        self.sphere_circle = Circle(
            radius=radius, color=QGRAY, stroke_opacity=0.3
        )
        self.add(self.sphere_circle)

        # Equator ellipse
        self.equator = Ellipse(
            width=2 * radius, height=0.6 * radius,
            color=QGRAY, stroke_opacity=0.25,
        )
        self.add(self.equator)

        if show_axes:
            self.z_axis = DashedLine(
                radius * DOWN, radius * UP,
                color=QGRAY, stroke_opacity=0.4,
            )
            self.x_axis = DashedLine(
                radius * LEFT, radius * RIGHT,
                color=QGRAY, stroke_opacity=0.4,
            )
            self.add(self.z_axis, self.x_axis)

        if show_labels:
            self.label_0 = MathTex(
                r"|0\rangle", font_size=24, color=QBLUE
            ).next_to(radius * UP, UP, buff=0.15)
            self.label_1 = MathTex(
                r"|1\rangle", font_size=24, color=QRED
            ).next_to(radius * DOWN, DOWN, buff=0.15)
            self.label_plus = MathTex(
                r"|+\rangle", font_size=20, color=QGRAY
            ).next_to(radius * RIGHT, RIGHT, buff=0.15)
            self.label_minus = MathTex(
                r"|-\rangle", font_size=20, color=QGRAY
            ).next_to(radius * LEFT, LEFT, buff=0.15)
            self.add(
                self.label_0, self.label_1,
                self.label_plus, self.label_minus,
            )

        # State vector arrow
        self.state_arrow = Arrow(
            ORIGIN, self._state_point(), buff=0,
            color=QWHITE, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        self.state_dot = Dot(
            self._state_point(), color=QWHITE, radius=0.06,
        )
        self.add(self.state_arrow, self.state_dot)

    # ── helpers ───────────────────────────────────────────────

    def _state_point(self) -> np.ndarray:
        """Convert (theta, phi) to 2-D projection on the Bloch sphere."""
        x = self.radius * np.sin(self._theta) * np.cos(self._phi)
        y = self.radius * np.cos(self._theta)
        return np.array([x, y, 0])

    def animate_to_state(
        self, theta: float, phi: float, run_time: float = 1.5
    ):
        """Return an AnimationGroup that moves the state vector."""
        self._theta = theta
        self._phi = phi
        new_point = self._state_point()
        # Use the sphere circle's center so the arrow stays anchored
        # correctly even after the VGroup has been moved.
        center = self.sphere_circle.get_center()
        return AnimationGroup(
            self.state_arrow.animate.put_start_and_end_on(
                center, center + new_point
            ),
            self.state_dot.animate.move_to(center + new_point),
            run_time=run_time,
        )

    def get_state_point(self) -> np.ndarray:
        return self._state_point()

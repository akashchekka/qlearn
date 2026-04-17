"""1.2 - The Bloch Sphere

Teaching objective: introduce the Bloch sphere as the geometric
picture of a single-qubit pure state. Identify |0>/|1> poles,
|+>/|-> on the x-axis, and parameterize arbitrary states with theta, phi.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE, QORANGE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
    LABEL_FONT_SIZE, SMALL_MATH_SIZE,
)
from common.quantum import BlochSphere

# Layout constants
SPHERE_CENTER = LEFT * 2.5 + DOWN * 0.3
EQ_CENTER_X = 3.2
SPHERE_RADIUS = 1.6


class BlochSphereScene(QScene):
    """Scene 1.2 - The Bloch Sphere."""

    def construct(self):
        # Beat 1 - Title card
        self.show_title_card("The Bloch Sphere")

        # Beat 2 - Draw sphere with labeled axes
        sec = self.show_section("Bloch Sphere", QBLUE)

        bloch = BlochSphere(radius=SPHERE_RADIUS, theta=0, phi=0)
        bloch.move_to(SPHERE_CENTER)

        self.play(FadeIn(bloch, scale=0.85), run_time=1.5)
        self.pause()

        # Beat 3 - Identify |0> (north) and |1> (south)
        pole_notes = VGroup(
            MathTex(r"|0\rangle", r"\;\text{-- north pole}",
                    font_size=SMALL_MATH_SIZE),
            MathTex(r"|1\rangle", r"\;\text{-- south pole}",
                    font_size=SMALL_MATH_SIZE),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        pole_notes[0][0].set_color(QBLUE)
        pole_notes[0][1].set_color(QGRAY)
        pole_notes[1][0].set_color(QRED)
        pole_notes[1][1].set_color(QGRAY)
        pole_notes.move_to(RIGHT * EQ_CENTER_X + UP * 1.5)

        self.play(
            Indicate(bloch.label_0, color=QBLUE, scale_factor=1.4),
            Write(pole_notes[0]),
            run_time=1.5,
        )
        self.pause()

        self.play(bloch.animate_to_state(np.pi, 0), run_time=1.5)
        self.play(
            Indicate(bloch.label_1, color=QRED, scale_factor=1.4),
            Write(pole_notes[1]),
            run_time=1.5,
        )
        self.wait(LONG_PAUSE)
        self.play(FadeOut(pole_notes))

        # Beat 4 - |+> on +x, |-> on -x
        plus_eq = MathTex(
            r"|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}",
            font_size=SMALL_MATH_SIZE, color=QGREEN,
        ).move_to(RIGHT * EQ_CENTER_X + UP * 1.8)

        self.play(bloch.animate_to_state(np.pi / 2, 0), run_time=1.5)
        self.play(Write(plus_eq), run_time=1.5)
        self.play(
            Indicate(bloch.label_plus, color=QGREEN, scale_factor=1.3),
            run_time=0.6,
        )
        self.pause()

        minus_eq = MathTex(
            r"|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}",
            font_size=SMALL_MATH_SIZE, color=QPURPLE,
        ).move_to(RIGHT * EQ_CENTER_X + UP * 0.6)

        self.play(bloch.animate_to_state(np.pi / 2, np.pi), run_time=1.5)
        self.play(Write(minus_eq), run_time=1.5)
        self.play(
            Indicate(bloch.label_minus, color=QPURPLE, scale_factor=1.3),
            run_time=0.6,
        )
        self.wait(LONG_PAUSE)
        self.play(FadeOut(plus_eq), FadeOut(minus_eq))

        # Beat 5 - Arbitrary state with theta and phi arcs
        arb_theta = np.pi / 3
        arb_phi = np.pi / 4

        self.play(bloch.animate_to_state(arb_theta, arb_phi), run_time=1.5)
        self.pause()

        state_pt = bloch._state_point()
        state_angle_from_x = np.arctan2(state_pt[1], state_pt[0])
        theta_sweep = state_angle_from_x - PI / 2

        theta_arc = Arc(
            radius=0.5,
            start_angle=PI / 2,
            angle=theta_sweep,
            color=QPURPLE, stroke_width=3,
        ).shift(SPHERE_CENTER)

        mid_angle = PI / 2 + theta_sweep / 2
        theta_lbl = MathTex(
            r"\theta", font_size=LABEL_FONT_SIZE, color=QPURPLE,
        ).move_to(
            SPHERE_CENTER
            + 0.8 * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
        )

        state_abs = SPHERE_CENTER + state_pt
        equator_proj = np.array([state_abs[0], SPHERE_CENTER[1], 0])
        drop_line = DashedLine(
            state_abs, equator_proj,
            color=QGRAY, stroke_width=2, stroke_opacity=0.5,
        )
        phi_lbl = MathTex(
            r"\phi", font_size=LABEL_FONT_SIZE, color=QGRAY,
        ).next_to(equator_proj, DOWN + RIGHT * 0.3, buff=0.15)

        self.play(Create(theta_arc), Write(theta_lbl), run_time=1.5)
        self.pause()
        self.play(Create(drop_line), Write(phi_lbl), run_time=1.2)
        self.pause()

        # Beat 6 - Parametric equation
        param_eq = MathTex(
            r"|\psi\rangle = \cos\!\frac{\theta}{2}\,|0\rangle"
            r" + e^{i\phi}\!\sin\!\frac{\theta}{2}\,|1\rangle",
            font_size=26, color=QWHITE,
        ).move_to(RIGHT * EQ_CENTER_X + UP * 1.5)

        self.play(Write(param_eq), run_time=1.5)
        self.wait(LONG_PAUSE)

        # Beat 7 - Summary, hold, clean up
        summary = Text(
            "Every point on the sphere is a valid qubit state",
            font_size=26, color=QGRAY,
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(summary), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()

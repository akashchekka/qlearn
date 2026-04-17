"""1.5 - Schrodinger Equation

Teaching objective: introduce the Schrodinger equation as the rule for
how quantum states change over time. Keep it conceptual — show the
equation, explain each part, and animate a simple time-evolving state.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE, QORANGE,
    STEP_PAUSE, LONG_PAUSE, SMALL_MATH_SIZE,
)


class SchrodingerEquationScene(QScene):
    def construct(self):
        self.show_title_card("Schrodinger Equation")

        # Beat 2 - The equation
        sec = self.show_section("The Equation", QPURPLE)
        eq = MathTex(
            r"i\hbar", r"\frac{\partial}{\partial t}",
            r"|\psi(t)\rangle", r"=", r"\hat{H}", r"|\psi(t)\rangle",
            font_size=40,
        )
        eq[0].set_color(QPURPLE)   # i*hbar
        eq[1].set_color(QORANGE)   # time derivative
        eq[2].set_color(QBLUE)     # state
        eq[4].set_color(QRED)      # Hamiltonian
        eq[5].set_color(QBLUE)     # state
        eq.move_to(UP * 1.5)
        self.play(Write(eq), run_time=2.5)
        self.wait(LONG_PAUSE)

        # Beat 3 - Label each part
        labels = VGroup(
            VGroup(
                MathTex(r"i\hbar \frac{\partial}{\partial t}", font_size=24, color=QORANGE),
                Text("=  how the state changes", font_size=22, color=QGRAY),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"\hat{H}", font_size=24, color=QRED),
                Text("=  Hamiltonian  (energy operator)", font_size=22, color=QGRAY),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(r"|\psi(t)\rangle", font_size=24, color=QBLUE),
                Text("=  quantum state at time t", font_size=22, color=QGRAY),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(DOWN * 1.0)

        for lbl in labels:
            self.play(FadeIn(lbl), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(eq, labels, sec)

        # Beat 4 - Time-independent version
        sec2 = self.show_section("Time-Independent", QBLUE)
        ti_eq = MathTex(
            r"\hat{H}", r"|\psi\rangle", r"=", r"E", r"|\psi\rangle",
            font_size=44,
        )
        ti_eq[0].set_color(QRED)
        ti_eq[1].set_color(QBLUE)
        ti_eq[3].set_color(QGREEN)
        ti_eq[4].set_color(QBLUE)
        ti_eq.move_to(UP * 1.0)
        self.play(Write(ti_eq), run_time=2.0)

        ti_note = Text("energy E  determines  allowed states", font_size=24,
                       color=QGRAY).next_to(ti_eq, DOWN, buff=0.6)
        self.play(Write(ti_note))
        self.wait(LONG_PAUSE)
        self.fade_out_group(ti_eq, ti_note, sec2)

        # Beat 5 - Key insight
        sec3 = self.show_section("Key Insight", QGREEN)
        insight = VGroup(
            Text("Classical:   F = ma  tells objects how to move", font_size=26, color=QGRAY),
            Text("Quantum:   Schrodinger equation  tells states how to evolve",
                 font_size=26, color=QGREEN),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        self.play(Write(insight[0]), run_time=1.5)
        self.play(Write(insight[1]), run_time=1.5)
        self.play(Circumscribe(insight[1], color=QGREEN, run_time=1.5))
        self.wait(LONG_PAUSE)
        self.clear_scene()

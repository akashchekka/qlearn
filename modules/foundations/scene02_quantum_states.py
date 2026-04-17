"""1.2 - Quantum States & Probability

Teaching objective: introduce wavefunctions, probability amplitudes, and
the Born rule in simple terms.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QPURPLE,
    STEP_PAUSE, LONG_PAUSE,
)


class QuantumStatesScene(QScene):
    def construct(self):
        self.show_title_card("Quantum States & Probability")

        # Beat 2 - What is a quantum state?
        sec = self.show_section("Quantum State", QBLUE)
        state_eq = MathTex(
            r"|\psi\rangle", r" = ", r"\alpha", r"|A\rangle", r" + ", r"\beta", r"|B\rangle",
            font_size=44,
        )
        state_eq[0].set_color(QWHITE)
        state_eq[2].set_color(QBLUE)
        state_eq[3].set_color(QBLUE)
        state_eq[5].set_color(QRED)
        state_eq[6].set_color(QRED)
        state_eq.move_to(UP * 1.5)
        self.play(Write(state_eq), run_time=2.0)

        explain = Text("a quantum state is a combination of possibilities",
                       font_size=24, color=QGRAY).next_to(state_eq, DOWN, buff=0.6)
        self.play(Write(explain), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(state_eq, explain, sec)

        # Beat 3 - Probability amplitudes
        sec2 = self.show_section("Amplitudes", QPURPLE)
        amp_eq = MathTex(
            r"\alpha, \beta", r" \in \mathbb{C}", r"\quad\text{(complex numbers)}",
            font_size=32, color=QWHITE,
        ).move_to(UP * 1.5)
        self.play(Write(amp_eq), run_time=1.5)
        self.pause()

        amp_note = Text("amplitudes encode both  probability  and  phase",
                        font_size=24, color=QGRAY).next_to(amp_eq, DOWN, buff=0.6)
        self.play(Write(amp_note), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.fade_out_group(amp_eq, amp_note, sec2)

        # Beat 4 - Born rule
        sec3 = self.show_section("Born Rule", QGREEN)
        born = MathTex(
            r"P(A) = |\alpha|^2", r"\qquad", r"P(B) = |\beta|^2",
            font_size=36, color=QWHITE,
        ).move_to(UP * 1.0)
        born[0].set_color(QBLUE)
        born[2].set_color(QRED)
        self.play(Write(born), run_time=2.0)

        born_note = Text("probability  =  |amplitude|²", font_size=26, color=QGREEN
                         ).next_to(born, DOWN, buff=0.6)
        self.play(Write(born_note), run_time=1.5)
        self.pause()

        # Normalization
        norm = MathTex(r"|\alpha|^2 + |\beta|^2 = 1", font_size=32, color=QGREEN
                       ).next_to(born_note, DOWN, buff=0.6)
        norm_box = SurroundingRectangle(norm, color=QGREEN, corner_radius=0.1, buff=0.15)
        self.play(Write(norm), Create(norm_box))
        self.play(Indicate(norm, color=QGREEN, scale_factor=1.1))
        self.wait(LONG_PAUSE)
        self.clear_scene()

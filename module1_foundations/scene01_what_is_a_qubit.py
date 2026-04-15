"""1.1 — What Is a Qubit? (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE


class WhatIsAQubit(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Classical bit: two squares, 0 or 1 ───────────────
        bit_0 = VGroup(
            Square(side_length=1.2, color=QBLUE, fill_opacity=0.3),
            Text("0", font_size=48, color=QBLUE, weight=BOLD),
        ).move_to(2 * LEFT)
        bit_1 = VGroup(
            Square(side_length=1.2, color=QRED, fill_opacity=0.3),
            Text("1", font_size=48, color=QRED, weight=BOLD),
        ).move_to(2 * RIGHT)
        or_label = Text("OR", font_size=28, color=QGRAY)

        self.play(FadeIn(bit_0, shift=LEFT * 0.3), FadeIn(bit_1, shift=RIGHT * 0.3))
        self.play(Write(or_label))
        self.wait(1)

        switch_arrow = Arrow(bit_0.get_right(), bit_1.get_left(), color=QGRAY, buff=0.3)
        self.play(GrowArrow(switch_arrow))
        self.wait(1)
        self.play(FadeOut(bit_0), FadeOut(bit_1), FadeOut(or_label), FadeOut(switch_arrow))

        # ── Qubit: |0⟩ AND |1⟩ ───────────────────────────────
        ket_0 = MathTex(r"|0\rangle", font_size=56, color=QBLUE).move_to(2.5 * LEFT)
        ket_1 = MathTex(r"|1\rangle", font_size=56, color=QRED).move_to(2.5 * RIGHT)
        and_label = Text("AND", font_size=28, color=QGREEN)

        self.play(Write(ket_0), Write(ket_1))
        self.play(FadeIn(and_label, scale=1.3))
        self.wait(1.5)
        self.play(FadeOut(ket_0), FadeOut(ket_1), FadeOut(and_label))

        # ── Superposition equation ────────────────────────────
        state_eq = MathTex(
            r"|\psi\rangle", "=", r"\alpha", r"|0\rangle", "+", r"\beta", r"|1\rangle",
            font_size=52,
        )
        state_eq[0].set_color(QWHITE)
        state_eq[2].set_color(QBLUE)
        state_eq[3].set_color(QBLUE)
        state_eq[5].set_color(QRED)
        state_eq[6].set_color(QRED)
        self.play(Write(state_eq), run_time=2)
        self.wait(1.5)

        # ── Normalization constraint ──────────────────────────
        norm = MathTex(
            r"|\alpha|^2 + |\beta|^2 = 1",
            font_size=40, color=QGREEN,
        ).next_to(state_eq, UP, buff=1.0)
        norm_box = SurroundingRectangle(norm, color=QGREEN, corner_radius=0.1, buff=0.2)
        self.play(Write(norm), Create(norm_box))
        self.wait(2)
        self.play(FadeOut(state_eq), FadeOut(norm), FadeOut(norm_box))

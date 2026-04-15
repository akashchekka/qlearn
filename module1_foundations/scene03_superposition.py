"""1.3 — Superposition (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE
from common.quantum import StateVectorDisplay


class SuperpositionScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Spinning coin analogy ─────────────────────────────
        coin = Circle(radius=1.0, color=QGRAY, fill_opacity=0.2, stroke_width=3)
        heads = Text("H", font_size=64, color=QBLUE, weight=BOLD).move_to(coin)
        tails = Text("T", font_size=64, color=QRED, weight=BOLD).move_to(coin)
        self.play(FadeIn(VGroup(coin, heads)))
        self.wait(0.8)

        # Rapid flicker H ↔ T
        for _ in range(6):
            self.play(Transform(heads, tails.copy().move_to(coin)), run_time=0.12)
            self.play(Transform(heads, Text("H", font_size=64, color=QBLUE, weight=BOLD).move_to(coin)), run_time=0.12)
        qmark = Text("?", font_size=72, color=QPURPLE, weight=BOLD).move_to(coin)
        self.play(Transform(heads, qmark))
        self.wait(1.5)
        self.play(FadeOut(coin), FadeOut(heads))

        # ── State equation + probability bars ─────────────────
        eq = MathTex(r"|\psi\rangle = ", r"|0\rangle", font_size=44)
        eq[1].set_color(QBLUE)
        eq.move_to(UP * 2.8)

        bars = StateVectorDisplay(alpha=1, beta=0, bar_height=2.0)
        bars.move_to(DOWN * 1.0)
        self.play(Write(eq), FadeIn(bars))
        self.wait(1)

        # → equal superposition
        eq_plus = MathTex(
            r"|\psi\rangle = ", r"\tfrac{1}{\sqrt{2}}", r"|0\rangle", r"+", r"\tfrac{1}{\sqrt{2}}", r"|1\rangle",
            font_size=40,
        )
        eq_plus[1].set_color(QBLUE); eq_plus[2].set_color(QBLUE)
        eq_plus[4].set_color(QRED); eq_plus[5].set_color(QRED)
        eq_plus.move_to(UP * 2.8)

        a = 1 / np.sqrt(2)
        self.play(Transform(eq, eq_plus), bars.update_probs(a, a), run_time=1.5)
        self.wait(1.5)

        # → unequal superposition
        eq_uneq = MathTex(
            r"|\psi\rangle = ", r"\tfrac{1}{2}", r"|0\rangle", r"+", r"\tfrac{\sqrt{3}}{2}", r"|1\rangle",
            font_size=40,
        )
        eq_uneq[1].set_color(QBLUE); eq_uneq[2].set_color(QBLUE)
        eq_uneq[4].set_color(QRED); eq_uneq[5].set_color(QRED)
        eq_uneq.move_to(UP * 2.8)

        self.play(Transform(eq, eq_uneq), bars.update_probs(0.5, np.sqrt(3) / 2), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(eq), FadeOut(bars))

"""1.3 - Superposition

Teaching objective: build intuition for superposition using a spinning-
coin analogy, then show equal and unequal superpositions with
probability bars driven by |alpha|^2 and |beta|^2.
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

# R4b: all bars share a fixed baseline and label y.
BAR_WIDTH = 0.7
BAR_MAX_H = 2.2
BAR_GAP = 1.6
BASELINE_Y = -1.6
LABEL_Y = BASELINE_Y - 0.35
EQ_Y = 2.6


def _make_bar(prob, color, cx):
    h = max(BAR_MAX_H * prob, 0.02)
    bar = Rectangle(
        width=BAR_WIDTH, height=h,
        fill_color=color, fill_opacity=0.8, stroke_width=0,
    )
    bar.move_to(np.array([cx, BASELINE_Y + h / 2, 0]))
    return bar


def _prob_text(prob, bar):
    return Text(f"{prob:.0%}", font_size=24, color=QWHITE).next_to(bar, UP, buff=0.1)


def build_bars(p0, p1):
    x0, x1 = -BAR_GAP / 2, BAR_GAP / 2
    bar0 = _make_bar(p0, QBLUE, x0)
    bar1 = _make_bar(p1, QRED, x1)
    lbl0 = MathTex(r"|0\rangle", font_size=26, color=QBLUE)
    lbl0.move_to(np.array([x0, LABEL_Y, 0]))
    lbl1 = MathTex(r"|1\rangle", font_size=26, color=QRED)
    lbl1.move_to(np.array([x1, LABEL_Y, 0]))
    pct0 = _prob_text(p0, bar0)
    pct1 = _prob_text(p1, bar1)
    return VGroup(bar0, bar1, lbl0, lbl1, pct0, pct1)


def bars_update_anims(bars_group, p0, p1):
    bar0, bar1, _l0, _l1, pct0, pct1 = bars_group
    x0 = bar0.get_center()[0]
    x1 = bar1.get_center()[0]
    new_bar0 = _make_bar(p0, QBLUE, x0)
    new_bar1 = _make_bar(p1, QRED, x1)
    new_pct0 = _prob_text(p0, new_bar0)
    new_pct1 = _prob_text(p1, new_bar1)
    return AnimationGroup(
        Transform(bar0, new_bar0),
        Transform(bar1, new_bar1),
        Transform(pct0, new_pct0),
        Transform(pct1, new_pct1),
    )


class SuperpositionScene(QScene):
    """Scene 1.3 - Superposition."""

    def construct(self):
        self.show_title_card("Superposition")

        # Beat 2 - Spinning-coin analogy
        sec = self.show_section("Coin Analogy", QGRAY)

        coin = Circle(radius=1.0, color=QGRAY, fill_opacity=0.2, stroke_width=3)
        coin_letter = Text("H", font_size=64, color=QBLUE, weight=BOLD).move_to(coin)
        intuition_tag = Text(
            "(intuition only)", font_size=22, color=QGRAY,
        ).next_to(coin, DOWN, buff=0.5)

        self.play(FadeIn(VGroup(coin, coin_letter)), Write(intuition_tag))
        self.wait(0.8)

        tails = Text("T", font_size=64, color=QRED, weight=BOLD).move_to(coin)
        self.play(Transform(coin_letter, tails), run_time=0.6)
        self.wait(0.4)

        heads = Text("H", font_size=64, color=QBLUE, weight=BOLD).move_to(coin)
        self.play(Transform(coin_letter, heads), run_time=0.6)
        self.wait(0.4)

        qmark = Text("?", font_size=72, color=QPURPLE, weight=BOLD).move_to(coin)
        hort = Text("H or T", font_size=28, color=QGRAY).move_to(intuition_tag)
        self.play(Transform(coin_letter, qmark), Transform(intuition_tag, hort))
        self.wait(LONG_PAUSE)
        self.fade_out_group(coin, coin_letter, intuition_tag, sec)

        # Beat 3 - Equal superposition with bars
        sec2 = self.show_section("State Vector", QBLUE)

        eq = MathTex(r"|\psi\rangle = ", r"|0\rangle", font_size=44)
        eq[1].set_color(QBLUE)
        eq.move_to(UP * EQ_Y)

        bars = build_bars(1.0, 0.0)
        self.play(Write(eq), FadeIn(bars))
        self.pause()

        eq_plus = MathTex(
            r"|\psi\rangle = ",
            r"\frac{1}{\sqrt{2}}", r"|0\rangle", r"+",
            r"\frac{1}{\sqrt{2}}", r"|1\rangle",
            font_size=40,
        )
        eq_plus[1].set_color(QBLUE)
        eq_plus[2].set_color(QBLUE)
        eq_plus[4].set_color(QRED)
        eq_plus[5].set_color(QRED)
        eq_plus.move_to(UP * EQ_Y)

        self.play(
            Transform(eq, eq_plus),
            bars_update_anims(bars, 0.5, 0.5),
            run_time=1.5,
        )
        self.wait(LONG_PAUSE)

        # Beat 4 - Unequal superposition
        eq_uneq = MathTex(
            r"|\psi\rangle = ",
            r"\sqrt{0.8}", r"|0\rangle", r"+",
            r"\sqrt{0.2}", r"|1\rangle",
            font_size=40,
        )
        eq_uneq[1].set_color(QBLUE)
        eq_uneq[2].set_color(QBLUE)
        eq_uneq[4].set_color(QRED)
        eq_uneq[5].set_color(QRED)
        eq_uneq.move_to(UP * EQ_Y)

        self.play(
            Transform(eq, eq_uneq),
            bars_update_anims(bars, 0.8, 0.2),
            run_time=1.5,
        )
        self.wait(LONG_PAUSE)

        # Beat 5 - Clarification label
        clarify = Text(
            "bar height  =  |amplitude|^2,  not  the  amplitude",
            font_size=26, color=QGREEN,
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(clarify), run_time=1.5)
        self.play(Indicate(clarify, color=QGREEN, scale_factor=1.1))
        self.wait(LONG_PAUSE)

        # Beat 6 - Recap
        self.clear_scene()

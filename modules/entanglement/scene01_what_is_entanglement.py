"""5.1 - What Is Entanglement?

Teaching objective: explain quantum entanglement as correlated measurement
outcomes that cannot be explained by classical hidden variables. Introduce
the EPR thought experiment and emphasize that entanglement does NOT allow
faster-than-light communication.
"""
from manim import *
import numpy as np
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from common.scene_base import QScene
from common.styles import (
    QBLUE, QRED, QWHITE, QGRAY, QGREEN, QORANGE, QPURPLE, QYELLOW,
    STEP_PAUSE, LONG_PAUSE,
)


class WhatIsEntanglementScene(QScene):
    def construct(self):
        self.show_title_card("What Is Entanglement?")

        # ── Beat 2: Einstein quote hook ─────────────────────────
        quote = Text(
            '"Spooky action at a distance"',
            font_size=34, color=QPURPLE, slant=ITALIC,
        ).move_to(UP * 0.5)
        attribution = Text(
            "— Albert Einstein, 1935",
            font_size=22, color=QGRAY,
        ).next_to(quote, DOWN, buff=0.4)
        self.play(Write(quote), run_time=2.0)
        self.play(FadeIn(attribution, shift=UP * 0.2), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.play(FadeOut(quote), FadeOut(attribution))

        # ── Beat 3: Classical analogy — paired gloves ───────────
        sec = self.show_section("Classical Analogy", QGRAY)

        box_a = VGroup(
            RoundedRectangle(width=1.8, height=1.4, color=QGRAY, fill_opacity=0.15,
                             corner_radius=0.12),
            Text("Box A", font_size=24, color=QGRAY),
        ).arrange(DOWN, buff=0.25).move_to(LEFT * 3)
        box_b = VGroup(
            RoundedRectangle(width=1.8, height=1.4, color=QGRAY, fill_opacity=0.15,
                             corner_radius=0.12),
            Text("Box B", font_size=24, color=QGRAY),
        ).arrange(DOWN, buff=0.25).move_to(RIGHT * 3)

        # Question marks before reveal
        qmark_a = Text("?", font_size=48, color=QGRAY, weight=BOLD).move_to(box_a[0])
        qmark_b = Text("?", font_size=48, color=QGRAY, weight=BOLD).move_to(box_b[0])

        self.play(
            FadeIn(box_a, shift=LEFT * 0.3),
            FadeIn(box_b, shift=RIGHT * 0.3),
            run_time=1.5,
        )
        self.play(FadeIn(qmark_a), FadeIn(qmark_b), run_time=0.8)
        self.pause()

        # Open box A — reveal left glove
        glove_l = Text("L", font_size=44, color=QBLUE, weight=BOLD).move_to(box_a[0])
        self.play(ReplacementTransform(qmark_a, glove_l), run_time=1.0)
        self.pause()

        # Instantly know box B
        glove_r = Text("R", font_size=44, color=QRED, weight=BOLD).move_to(box_b[0])
        self.play(ReplacementTransform(qmark_b, glove_r), run_time=1.0)

        classical_note = Text(
            "Open one  \u2192  instantly know the other",
            font_size=24, color=QGRAY,
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(classical_note), run_time=1.5)
        self.pause()

        # Label this as boring classical correlation
        hidden_lbl = Text(
            "(values decided in advance  \u2014  no mystery)",
            font_size=22, color=QORANGE,
        ).next_to(classical_note, UP, buff=0.4)
        self.play(FadeIn(hidden_lbl, shift=UP * 0.2), run_time=1.2)
        self.wait(LONG_PAUSE)

        # Explicit label: "not quite right" for quantum
        caveat = Text(
            "But quantum entanglement is  NOT  like this...",
            font_size=26, color=QPURPLE, weight=BOLD,
        ).move_to(UP * 2.2)
        self.play(Write(caveat), run_time=1.5)
        self.wait(STEP_PAUSE)
        self.fade_out_group(
            box_a, box_b, glove_l, glove_r,
            classical_note, hidden_lbl, caveat, sec,
        )

        # ── Beat 4: Quantum entanglement — the real thing ──────
        sec2 = self.show_section("Quantum Entanglement", QORANGE)

        # Two qubits close together
        qubit_a = VGroup(
            Circle(radius=0.55, color=QBLUE, fill_opacity=0.15, stroke_width=3),
            Text("?", font_size=36, color=QBLUE, weight=BOLD),
        )
        qubit_a[1].move_to(qubit_a[0])
        qubit_b = VGroup(
            Circle(radius=0.55, color=QRED, fill_opacity=0.15, stroke_width=3),
            Text("?", font_size=36, color=QRED, weight=BOLD),
        )
        qubit_b[1].move_to(qubit_b[0])
        qubit_a.move_to(LEFT * 1.5)
        qubit_b.move_to(RIGHT * 1.5)

        lbl_a = MathTex(r"\text{Qubit A}", font_size=22, color=QBLUE
                        ).next_to(qubit_a, DOWN, buff=0.3)
        lbl_b = MathTex(r"\text{Qubit B}", font_size=22, color=QRED
                        ).next_to(qubit_b, DOWN, buff=0.3)

        self.play(
            FadeIn(qubit_a, scale=0.8), FadeIn(qubit_b, scale=0.8),
            Write(lbl_a), Write(lbl_b),
            run_time=1.5,
        )
        self.pause()

        # Entanglement link — wavy line, NOT a solid wire
        wave_pts = [
            qubit_a[0].get_right() + RIGHT * 0.1 + UP * 0.0,
            LEFT * 0.5 + UP * 0.15,
            ORIGIN + DOWN * 0.1,
            RIGHT * 0.5 + UP * 0.15,
            qubit_b[0].get_left() + LEFT * 0.1,
        ]
        entangle_wave = CubicBezier(
            wave_pts[0], wave_pts[1], wave_pts[3], wave_pts[4],
            color=QORANGE, stroke_width=3,
        ).set_stroke(opacity=0.6)
        entangle_lbl = Text("entangled", font_size=20, color=QORANGE
                            ).next_to(entangle_wave, DOWN, buff=0.2)

        self.play(Create(entangle_wave), Write(entangle_lbl), run_time=1.5)
        self.pause()

        # State equation above
        state_eq = MathTex(
            r"|\Phi^+\rangle", r"=",
            r"\frac{1}{\sqrt{2}}", r"\big(",
            r"|00\rangle", r"+", r"|11\rangle",
            r"\big)",
            font_size=36,
        ).move_to(UP * 2.0)
        state_eq[0].set_color(QORANGE)
        state_eq[4].set_color(QBLUE)
        state_eq[6].set_color(QRED)
        self.play(Write(state_eq), run_time=2.0)

        neither_note = Text(
            "Neither qubit has a definite value yet",
            font_size=24, color=QORANGE,
        ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(neither_note, shift=UP * 0.2), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.play(FadeOut(neither_note))

        # ── Separate them — emphasize distance ──
        sep_note = Text(
            "Separate them by any distance...",
            font_size=24, color=QGRAY,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(sep_note), run_time=1.2)

        self.play(
            qubit_a.animate.move_to(LEFT * 4.5),
            lbl_a.animate.next_to(LEFT * 4.5 + DOWN * 0.55, DOWN, buff=0.15),
            qubit_b.animate.move_to(RIGHT * 4.5),
            lbl_b.animate.next_to(RIGHT * 4.5 + DOWN * 0.55, DOWN, buff=0.15),
            FadeOut(entangle_wave), FadeOut(entangle_lbl),
            run_time=2.0, rate_func=smooth,
        )

        # Dashed line showing they're still entangled
        dist_line = DashedLine(
            LEFT * 3.9, RIGHT * 3.9,
            color=QORANGE, stroke_width=2, dash_length=0.15,
        ).move_to(UP * 0.5)
        still_lbl = Text("still entangled", font_size=20, color=QORANGE
                         ).next_to(dist_line, UP, buff=0.15)
        self.play(Create(dist_line), FadeIn(still_lbl), run_time=1.2)
        self.wait(STEP_PAUSE)
        self.play(FadeOut(sep_note))

        # ── Measure qubit A ──
        measure_note = Text(
            "Measure Qubit A...", font_size=24, color=QGREEN,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(measure_note), run_time=1.0)

        # Flash on A
        flash = Circle(radius=0.05, color=QGREEN, fill_opacity=1
                       ).move_to(qubit_a[0])
        self.play(flash.animate.scale(30).set_opacity(0), run_time=0.5)
        self.remove(flash)

        # A collapses to |0⟩
        result_a = MathTex(r"|0\rangle", font_size=40, color=QBLUE
                           ).move_to(qubit_a[0])
        self.play(
            FadeOut(qubit_a[1]),
            FadeIn(result_a, scale=1.3),
            run_time=1.0,
        )
        self.pause()

        # B instantly determined — |0⟩
        self.play(FadeOut(measure_note))
        instant_note = Text(
            "Qubit B is  instantly  determined!",
            font_size=24, color=QGREEN,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(instant_note), run_time=1.2)

        result_b = MathTex(r"|0\rangle", font_size=40, color=QRED
                           ).move_to(qubit_b[0])
        self.play(
            FadeOut(qubit_b[1]),
            FadeIn(result_b, scale=1.3),
            run_time=1.0,
        )
        self.play(Indicate(result_b, color=QRED, scale_factor=1.3))
        self.wait(STEP_PAUSE)

        # Show both outcomes
        self.play(FadeOut(instant_note))
        outcomes = VGroup(
            VGroup(
                MathTex(r"|0\rangle_A", font_size=28, color=QBLUE),
                Text("and", font_size=20, color=QGRAY),
                MathTex(r"|0\rangle_B", font_size=28, color=QRED),
            ).arrange(RIGHT, buff=0.4),
            Text("or", font_size=22, color=QGRAY),
            VGroup(
                MathTex(r"|1\rangle_A", font_size=28, color=QBLUE),
                Text("and", font_size=20, color=QGRAY),
                MathTex(r"|1\rangle_B", font_size=28, color=QRED),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.0)

        never_note = MathTex(
            r"\text{always correlated --- never } |01\rangle \text{ or } |10\rangle",
            font_size=28, color=QGREEN,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(outcomes, shift=UP * 0.2), run_time=1.5)
        self.play(Write(never_note), run_time=1.2)
        self.play(Indicate(never_note, color=QGREEN, scale_factor=1.05))
        self.wait(LONG_PAUSE)

        self.fade_out_group(
            qubit_a[0], qubit_b[0], lbl_a, lbl_b,
            result_a, result_b, dist_line, still_lbl,
            state_eq, outcomes, never_note, sec2,
        )

        # ── Beat 5: Why it's NOT like gloves — visual contrast ──
        sec3 = self.show_section("Beyond Classical", QPURPLE)

        # Side-by-side comparison boxes — build each with arrange
        c_title = Text("Classical Gloves", font_size=22, color=QGRAY, weight=BOLD)
        c_icons = VGroup(
            Text("L", font_size=44, color=QBLUE, weight=BOLD),
            Text("R", font_size=44, color=QRED, weight=BOLD),
        ).arrange(RIGHT, buff=1.0)
        c_desc = Text("Values fixed from the start", font_size=18, color=QGRAY)
        c_content = VGroup(c_title, c_icons, c_desc).arrange(DOWN, buff=0.35)
        c_rect = SurroundingRectangle(
            c_content, color=QGRAY, fill_opacity=0.06,
            corner_radius=0.15, buff=0.35,
        )
        classical_box = VGroup(c_rect, c_content).move_to(LEFT * 3.2)

        q_title = Text("Quantum Qubits", font_size=22, color=QORANGE, weight=BOLD)
        q_icons = VGroup(
            Text("?", font_size=44, color=QBLUE, weight=BOLD),
            Text("?", font_size=44, color=QRED, weight=BOLD),
        ).arrange(RIGHT, buff=1.0)
        q_desc = Text("No value until measured", font_size=18, color=QORANGE)
        q_content = VGroup(q_title, q_icons, q_desc).arrange(DOWN, buff=0.35)
        q_rect = SurroundingRectangle(
            q_content, color=QORANGE, fill_opacity=0.06,
            corner_radius=0.15, buff=0.35,
        )
        quantum_box = VGroup(q_rect, q_content).move_to(RIGHT * 3.2)

        self.play(FadeIn(classical_box, shift=LEFT * 0.3), run_time=1.5)
        self.pause()
        self.play(FadeIn(quantum_box, shift=RIGHT * 0.3), run_time=1.5)
        self.play(Circumscribe(quantum_box, color=QORANGE, run_time=1.5))
        self.wait(LONG_PAUSE)

        bell_note = Text(
            "Bell tests prove:  no  hidden  variables  can  explain  quantum  correlations",
            font_size=24, color=QPURPLE,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(bell_note), run_time=2.0)
        self.play(Indicate(bell_note, color=QPURPLE, scale_factor=1.05))
        self.wait(LONG_PAUSE)
        self.fade_out_group(classical_box, quantum_box, bell_note, sec3)

        # ── Beat 6: No FTL communication ────────────────────────
        sec4 = self.show_section("No Faster-Than-Light", QRED)

        alice = VGroup(
            Circle(radius=0.4, color=QBLUE, fill_opacity=0.2, stroke_width=2),
            Text("Alice", font_size=24, color=QBLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 4 + UP * 1.0)
        bob = VGroup(
            Circle(radius=0.4, color=QRED, fill_opacity=0.2, stroke_width=2),
            Text("Bob", font_size=24, color=QRED, weight=BOLD),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 4 + UP * 1.0)

        self.play(FadeIn(alice, shift=DOWN * 0.2), FadeIn(bob, shift=DOWN * 0.2),
                  run_time=1.2)

        steps = VGroup(
            Text("\u2460  Alice measures \u2192 random result", font_size=22, color=QWHITE),
            Text("\u2461  Bob measures \u2192 also random", font_size=22, color=QWHITE),
            Text("\u2462  Compare notes via classical channel", font_size=22, color=QYELLOW),
            Text("\u2463  Only then are correlations visible", font_size=22, color=QGREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 0.8)

        for step in steps:
            self.play(FadeIn(step, shift=LEFT * 0.3), run_time=1.2)
            self.pause()

        # Crossed-out FTL arrow between Alice and Bob
        ftl_arrow = Arrow(LEFT * 2.5 + UP * 1.0, RIGHT * 2.5 + UP * 1.0,
                          color=QRED, stroke_width=4)
        ftl_lbl = Text("FTL?", font_size=22, color=QRED).next_to(ftl_arrow, UP, buff=0.15)
        cross1 = Line(
            ftl_arrow.get_center() + LEFT * 0.8 + UP * 0.3,
            ftl_arrow.get_center() + RIGHT * 0.8 + DOWN * 0.3,
            color=QRED, stroke_width=8,
        )
        cross2 = Line(
            ftl_arrow.get_center() + LEFT * 0.8 + DOWN * 0.3,
            ftl_arrow.get_center() + RIGHT * 0.8 + UP * 0.3,
            color=QRED, stroke_width=8,
        )

        self.play(GrowArrow(ftl_arrow), Write(ftl_lbl), run_time=1.2)
        self.play(Create(cross1), Create(cross2), run_time=0.8)
        self.play(Indicate(VGroup(cross1, cross2), color=QRED, scale_factor=1.1))
        self.wait(LONG_PAUSE)
        self.fade_out_group(alice, bob, steps, ftl_arrow, ftl_lbl, cross1, cross2, sec4)

        # ── Beat 7: Key properties recap ────────────────────────
        sec5 = self.show_section("Entanglement Is a Resource", QGREEN)

        props = VGroup(
            VGroup(
                Text("\u2022", font_size=26, color=QORANGE),
                Text("Non-local  correlations  beyond  classical  limits", font_size=24, color=QWHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("\u2022", font_size=26, color=QORANGE),
                Text("Cannot  be  cloned  (no-cloning  theorem)", font_size=24, color=QWHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("\u2022", font_size=26, color=QORANGE),
                Text("Monogamy:  maximum  entanglement  is  pairwise", font_size=24, color=QWHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("\u2022", font_size=26, color=QGREEN),
                Text("A  resource  consumed  by  quantum  protocols", font_size=24, color=QGREEN),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.3)

        for prop in props:
            self.play(FadeIn(prop, shift=LEFT * 0.3), run_time=1.2)

        self.play(Circumscribe(props[-1], color=QGREEN, run_time=1.5))

        recap = Text(
            "Entanglement  powers  teleportation,  cryptography,  and  quantum  speedups",
            font_size=22, color=QGRAY,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(recap, shift=UP * 0.2), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.clear_scene()

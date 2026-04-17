"""1.1 - Wave-Particle Duality

Teaching objective: show that quantum objects behave as both waves and
particles, using the double-slit experiment as the central example.
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
)


class WaveParticleDualityScene(QScene):
    def construct(self):
        self.show_title_card("Wave-Particle Duality")

        # Beat 2 - Classical particles: two slits, two bands
        sec = self.show_section("Classical Particles", QGRAY)

        # Experiment setup — shifted down so header never overlaps
        SETUP_Y = DOWN * 0.3
        barrier = Rectangle(width=0.3, height=3.5, color=QGRAY, fill_opacity=0.6
                            ).move_to(LEFT * 1 + SETUP_Y)
        slit1 = Rectangle(width=0.35, height=0.5, color=QDARK, fill_opacity=1
                          ).move_to(LEFT * 1 + UP * 0.8 + SETUP_Y)
        slit2 = Rectangle(width=0.35, height=0.5, color=QDARK, fill_opacity=1
                          ).move_to(LEFT * 1 + DOWN * 0.8 + SETUP_Y)
        screen = Rectangle(width=0.15, height=3.5, color=QGRAY, fill_opacity=0.3
                           ).move_to(RIGHT * 3.5 + SETUP_Y)
        source_dot = Dot(LEFT * 4.5 + SETUP_Y, color=QORANGE, radius=0.08)
        source_lbl = Text("source", font_size=18, color=QGRAY
                          ).next_to(source_dot, DOWN, buff=0.25)

        self.play(FadeIn(barrier), FadeIn(slit1), FadeIn(slit2),
                  FadeIn(screen), FadeIn(source_dot), Write(source_lbl),
                  run_time=1.5)
        self.pause()

        # Animate particles traveling through slits to screen
        landed_dots = VGroup()
        for i in range(6):
            slit = slit1 if i % 2 == 0 else slit2
            y_offset = (0.8 if i % 2 == 0 else -0.8) + np.random.uniform(-0.15, 0.15)
            end_pos = RIGHT * 3.5 + UP * y_offset + SETUP_Y

            p = Dot(source_dot.get_center(), color=QORANGE, radius=0.05)
            self.add(p)
            self.play(p.animate.move_to(slit.get_center()), run_time=0.4, rate_func=linear)
            self.play(p.animate.move_to(end_pos), run_time=0.4, rate_func=linear)
            landed_dots.add(p)

        # Fill remaining pattern
        extra_dots = VGroup(*[
            Dot(RIGHT * 3.5 + UP * (0.8 + np.random.uniform(-0.2, 0.2)) + SETUP_Y,
                color=QORANGE, radius=0.04) for _ in range(12)
        ] + [
            Dot(RIGHT * 3.5 + DOWN * (0.8 + np.random.uniform(-0.2, 0.2)) + SETUP_Y,
                color=QORANGE, radius=0.04) for _ in range(12)
        ])
        self.play(FadeIn(extra_dots, lag_ratio=0.05), run_time=1.5)

        classical_lbl = Text("two bands  (classical particles)", font_size=24,
                             color=QGRAY).to_edge(DOWN, buff=0.5)
        self.play(Write(classical_lbl), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(landed_dots, extra_dots, classical_lbl, sec)

        # Beat 3 - Quantum: interference pattern
        sec2 = self.show_section("Quantum Particles", QBLUE)

        # Animate quantum particles — they appear to pass through BOTH slits
        for i in range(3):
            p = Dot(source_dot.get_center(), color=QBLUE, radius=0.06)
            self.add(p)
            self.play(p.animate.move_to(LEFT * 1.3 + SETUP_Y), run_time=0.4, rate_func=linear)
            # Split into two ghost copies through both slits
            ghost_up = p.copy().set_opacity(0.4)
            ghost_dn = p.copy().set_opacity(0.4)
            p.set_opacity(0)
            self.add(ghost_up, ghost_dn)
            self.play(
                ghost_up.animate.move_to(slit1.get_center()),
                ghost_dn.animate.move_to(slit2.get_center()),
                run_time=0.35, rate_func=linear,
            )
            # Both converge to an interference-pattern position
            fringe_y = np.random.choice(np.arange(-6, 7)) * 0.3
            target = RIGHT * 3.5 + UP * fringe_y + SETUP_Y
            self.play(
                ghost_up.animate.move_to(target).set_opacity(0.8),
                ghost_dn.animate.move_to(target).set_opacity(0),
                run_time=0.4, rate_func=linear,
            )
            self.remove(ghost_dn)

        # Full interference fringes
        fringes = VGroup()
        for k in range(-6, 7):
            intensity = np.cos(k * np.pi / 3) ** 2
            fringe = Rectangle(
                width=0.12, height=0.25, fill_opacity=intensity * 0.9,
                fill_color=QBLUE, stroke_width=0,
            ).move_to(RIGHT * 3.5 + UP * k * 0.3 + SETUP_Y)
            fringes.add(fringe)
        self.play(FadeIn(fringes, lag_ratio=0.03), run_time=1.5)

        quantum_lbl = Text("interference pattern  (wave behavior!)", font_size=24,
                           color=QBLUE).to_edge(DOWN, buff=0.5)
        self.play(Write(quantum_lbl), run_time=1.2)
        self.wait(LONG_PAUSE)
        self.fade_out_group(fringes, quantum_lbl, source_dot, source_lbl,
                            barrier, slit1, slit2, screen, sec2)

        # Remove any leftover ghost particles
        self.clear_scene()

        # Beat 4 - Key insight
        sec3 = self.show_section("Key Insight", QGREEN)
        insight = VGroup(
            Text("Each particle goes through  BOTH  slits", font_size=28, color=QWHITE),
            Text("and interferes with itself", font_size=28, color=QBLUE),
        ).arrange(DOWN, buff=0.5).move_to(UP * 0.5)
        self.play(Write(insight[0]), run_time=1.5)
        self.play(Write(insight[1]), run_time=1.5)
        self.wait(LONG_PAUSE)

        # Beat 5 - Observation collapses
        obs_note = Text("Observing which slit  destroys  the pattern", font_size=24,
                        color=QRED).next_to(insight, DOWN, buff=0.6)
        self.play(Write(obs_note), run_time=1.5)
        self.wait(LONG_PAUSE)
        self.clear_scene()

from common.styles import QDARK

"""4.2 — Grover's Search Algorithm (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE


class GroversSearchScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Database with marked item ─────────────────────────
        N = 8
        target_idx = 5
        items = VGroup()
        for i in range(N):
            color = QORANGE if i == target_idx else QGRAY
            opacity = 0.3 if i == target_idx else 0.1
            box = VGroup(
                Square(side_length=0.7, color=color, fill_opacity=opacity, stroke_width=1.5),
                Text(str(i), font_size=20, color=color),
            )
            items.add(box)
        items.arrange(RIGHT, buff=0.2).move_to(UP * 2.5)
        self.play(FadeIn(items))
        self.wait(1)

        # ── Amplitude amplification bars ──────────────────────
        n_states = 8
        target = 5
        amps = np.ones(n_states) / np.sqrt(n_states)
        bar_max_h = 3.0
        bar_w = 0.6
        bar_spacing = 0.8
        base_y = -1.5

        def make_bars(amplitudes):
            bars = VGroup()
            for i in range(n_states):
                h = bar_max_h * abs(amplitudes[i])
                color = QORANGE if i == target else QBLUE
                bar = Rectangle(width=bar_w, height=max(h, 0.01),
                                fill_color=color, fill_opacity=0.7, stroke_width=0)
                bar.move_to(np.array([(i - n_states / 2 + 0.5) * bar_spacing, base_y + h / 2, 0]))
                bars.add(bar)
            return bars

        labels = VGroup()
        for i in range(n_states):
            lbl = MathTex(rf"|{i}\rangle", font_size=16, color=QGRAY)
            lbl.move_to(np.array([(i - n_states / 2 + 0.5) * bar_spacing, base_y - 0.3, 0]))
            labels.add(lbl)

        bars = make_bars(amps)
        self.play(FadeIn(bars), FadeIn(labels))
        self.wait(0.8)

        # Grover iterations
        for iteration in range(1, 3):
            # Oracle: flip target
            amps[target] *= -1
            new_bars = make_bars(amps)
            self.play(Transform(bars, new_bars), run_time=0.8)
            self.wait(0.3)

            # Diffusion: reflect about mean
            mean_amp = np.mean(amps)
            amps = 2 * mean_amp - amps
            new_bars2 = make_bars(amps)
            self.play(Transform(bars, new_bars2), run_time=0.8)
            self.wait(0.5)

        self.wait(1.5)
        self.play(FadeOut(bars), FadeOut(labels), FadeOut(items))

        # ── Geometric interpretation ──────────────────────────
        axes_origin = DOWN * 0.5
        w_axis = Arrow(axes_origin, axes_origin + 2.5 * UP, color=QORANGE, buff=0, stroke_width=2)
        w_lbl = MathTex(r"|w\rangle", font_size=24, color=QORANGE).next_to(w_axis, RIGHT, buff=0.15)
        s_axis = Arrow(axes_origin, axes_origin + 3.5 * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        s_lbl = MathTex(r"|s^\perp\rangle", font_size=24, color=QGRAY).next_to(s_axis, DOWN, buff=0.15)
        self.play(GrowArrow(w_axis), GrowArrow(s_axis), Write(w_lbl), Write(s_lbl))

        theta0 = np.arcsin(1 / np.sqrt(n_states))
        r = 2.5

        # Initial |s⟩ arrow
        s_arrow = Arrow(axes_origin, axes_origin + r * np.array([np.cos(theta0), np.sin(theta0), 0]),
                        color=QBLUE, buff=0, stroke_width=3)
        s_lbl2 = MathTex(r"|s\rangle", font_size=24, color=QBLUE).next_to(s_arrow.get_end(), UR, buff=0.1)
        self.play(GrowArrow(s_arrow), Write(s_lbl2))

        theta_arc = Arc(radius=0.8, start_angle=0, angle=theta0, color=QGREEN, arc_center=axes_origin)
        theta_lbl = MathTex(r"\theta", font_size=22, color=QGREEN)
        theta_lbl.move_to(axes_origin + 1.0 * np.array([np.cos(theta0 / 2), np.sin(theta0 / 2), 0]))
        self.play(Create(theta_arc), Write(theta_lbl))

        # Rotation steps — create fresh arrows for each step
        current_angle = theta0
        all_arrows = [s_arrow]
        all_labels = [s_lbl2]
        for i in range(1, 3):
            new_angle = theta0 + 2 * theta0 * i
            new_end = axes_origin + r * np.array([np.cos(new_angle), np.sin(new_angle), 0])
            new_arrow = Arrow(axes_origin, new_end, color=QPURPLE, buff=0, stroke_width=3)

            # Arc showing the 2θ rotation for this step
            rot_arc = Arc(
                radius=0.5 + 0.3 * i,
                start_angle=current_angle,
                angle=2 * theta0,
                color=QPURPLE,
                arc_center=axes_origin,
            )
            rot_lbl = MathTex(r"2\theta", font_size=18, color=QPURPLE)
            mid_angle = current_angle + theta0
            rot_lbl.move_to(
                axes_origin + (0.5 + 0.3 * i + 0.3) * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
            )

            # Fade old arrow, show new one
            self.play(FadeIn(new_arrow), Create(rot_arc), Write(rot_lbl), run_time=1)
            if i > 0:
                self.play(all_arrows[-1].animate.set_opacity(0.3), run_time=0.3)
            all_arrows.append(new_arrow)
            current_angle = new_angle
            self.wait(0.3)

        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

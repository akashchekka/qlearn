"""2.3 — Phase & Rotation Gates (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.quantum import BlochSphere


class PhaseGatesScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Phase gate hierarchy: Z → S → T ───────────────────
        hierarchy_title = Text("Phase Gate Family", font_size=32, color=QWHITE, weight=BOLD)
        hierarchy_title.to_edge(UP, buff=0.4)
        self.play(Write(hierarchy_title))

        # Show hierarchy with arrows
        z_box = VGroup(
            RoundedRectangle(width=2.4, height=1.0, corner_radius=0.1,
                             color=QBLUE, fill_opacity=0.15, stroke_width=2),
            MathTex(r"Z", font_size=28, color=QBLUE),
            MathTex(r"\phi = \pi", font_size=18, color=QGRAY).shift(DOWN * 0.25),
        ).move_to(LEFT * 4 + DOWN * 0.3)
        z_box[1].shift(UP * 0.15)

        s_box = VGroup(
            RoundedRectangle(width=2.4, height=1.0, corner_radius=0.1,
                             color=QPURPLE, fill_opacity=0.15, stroke_width=2),
            MathTex(r"S = \sqrt{Z}", font_size=24, color=QPURPLE),
            MathTex(r"\phi = \pi/2", font_size=18, color=QGRAY).shift(DOWN * 0.25),
        ).move_to(ORIGIN + DOWN * 0.3)
        s_box[1].shift(UP * 0.15)

        t_box = VGroup(
            RoundedRectangle(width=2.4, height=1.0, corner_radius=0.1,
                             color=QORANGE, fill_opacity=0.15, stroke_width=2),
            MathTex(r"T = \sqrt{S}", font_size=24, color=QORANGE),
            MathTex(r"\phi = \pi/4", font_size=18, color=QGRAY).shift(DOWN * 0.25),
        ).move_to(RIGHT * 4 + DOWN * 0.3)
        t_box[1].shift(UP * 0.15)

        arrow1 = Arrow(z_box.get_right(), s_box.get_left(), color=QGRAY, buff=0.15, stroke_width=2)
        arrow2 = Arrow(s_box.get_right(), t_box.get_left(), color=QGRAY, buff=0.15, stroke_width=2)
        sq_lbl1 = MathTex(r"\sqrt{}", font_size=18, color=QGRAY).next_to(arrow1, UP, buff=0.05)
        sq_lbl2 = MathTex(r"\sqrt{}", font_size=18, color=QGRAY).next_to(arrow2, UP, buff=0.05)

        self.play(FadeIn(z_box, scale=0.9))
        self.play(GrowArrow(arrow1), Write(sq_lbl1), FadeIn(s_box, scale=0.9))
        self.play(GrowArrow(arrow2), Write(sq_lbl2), FadeIn(t_box, scale=0.9))

        # Common property
        common = MathTex(
            r"\text{All leave } |0\rangle \text{ unchanged, add phase to } |1\rangle",
            font_size=22, color=QGRAY,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(common))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── S and T on Bloch sphere with angle labels ─────────
        for name, matrix_str, color, end_phi, angle_str in [
            ("S", r"S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}",
             QPURPLE, np.pi / 2, r"90°"),
            ("T", r"T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}",
             QORANGE, np.pi / 4, r"45°"),
        ]:
            gate_title = Text(f"{name} Gate", font_size=30, color=color, weight=BOLD)
            gate_title.to_edge(UP, buff=0.4)
            self.play(Write(gate_title))

            mat = MathTex(matrix_str, font_size=30, color=color).move_to(RIGHT * 3 + UP * 0.3)
            bloch = BlochSphere(radius=1.3, theta=np.pi / 2, phi=0)
            bloch.move_to(LEFT * 3)

            start_lbl = MathTex(r"|+\rangle", font_size=24, color=QGREEN)
            start_lbl.next_to(bloch, DOWN, buff=0.5)

            self.play(Write(mat), FadeIn(bloch, scale=0.8), Write(start_lbl))

            # Show the rotation angle
            angle_label = MathTex(
                rf"\text{{Phase rotation: }} {angle_str}",
                font_size=22, color=color,
            ).move_to(RIGHT * 3 + DOWN * 1.2)
            self.play(Write(angle_label))
            self.play(bloch.animate_to_state(np.pi / 2, end_phi), run_time=2)
            self.wait(1)
            self.play(FadeOut(mat), FadeOut(bloch), FadeOut(gate_title),
                      FadeOut(start_lbl), FadeOut(angle_label))

        # ── General rotations with clear labels ───────────────
        rot_title = Text("General Rotation Gates", font_size=30, color=QWHITE, weight=BOLD)
        rot_title.to_edge(UP, buff=0.4)
        self.play(Write(rot_title))

        # Show Rx, Ry, Rz with descriptions
        rotations = VGroup(
            VGroup(
                MathTex(r"R_x(\theta)", font_size=30, color=QRED),
                MathTex(r"\text{Rotates around X-axis}", font_size=18, color=QGRAY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                MathTex(r"R_y(\theta)", font_size=30, color=QGREEN),
                MathTex(r"\text{Rotates around Y-axis}", font_size=18, color=QGRAY),
            ).arrange(DOWN, buff=0.15),
            VGroup(
                MathTex(r"R_z(\theta)", font_size=30, color=QBLUE),
                MathTex(r"\text{Rotates around Z-axis}", font_size=18, color=QGRAY),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.0).move_to(RIGHT * 1.5)

        bloch = BlochSphere(radius=1.3, theta=np.pi / 3, phi=0)
        bloch.move_to(LEFT * 3.5)

        self.play(Write(rotations), FadeIn(bloch, scale=0.8), run_time=1.5)

        # Label: show Rz sweep
        rz_lbl = MathTex(r"R_z \text{ sweep}", font_size=22, color=QBLUE)
        rz_lbl.next_to(bloch, DOWN, buff=0.5)
        self.play(Write(rz_lbl))

        # Smoother continuous Rz rotation
        n_steps = 30
        for i in range(n_steps):
            angle = 2 * np.pi * i / n_steps
            self.play(bloch.animate_to_state(np.pi / 3, angle), run_time=0.1, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(bloch), FadeOut(rotations), FadeOut(rot_title), FadeOut(rz_lbl))

        # ── Universality statement ────────────────────────────
        universal = MathTex(
            r"\text{Any single-qubit gate} = R_z(\alpha) \cdot R_y(\beta) \cdot R_z(\gamma)",
            font_size=28, color=QGREEN,
        )
        universal_box = SurroundingRectangle(universal, color=QGREEN, corner_radius=0.1, buff=0.2)
        self.play(Write(universal), Create(universal_box))
        self.wait(2)
        self.play(FadeOut(universal), FadeOut(universal_box))

"""6.1 — Variational Quantum Eigensolver (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class VQEScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Hybrid loop diagram ───────────────────────────────
        # Quantum processor box
        q_box = VGroup(
            RoundedRectangle(width=3.0, height=2.0, corner_radius=0.15,
                             color=QBLUE, fill_opacity=0.12, stroke_width=2),
            MathTex(r"\text{Quantum}", font_size=22, color=QBLUE).shift(UP * 0.3),
            MathTex(r"|\psi(\vec\theta)\rangle", font_size=20, color=QWHITE).shift(DOWN * 0.2),
        ).move_to(LEFT * 3)

        # Classical optimizer box
        c_box = VGroup(
            RoundedRectangle(width=3.0, height=2.0, corner_radius=0.15,
                             color=QORANGE, fill_opacity=0.12, stroke_width=2),
            MathTex(r"\text{Classical}", font_size=22, color=QORANGE).shift(UP * 0.3),
            MathTex(r"\text{optimizer}", font_size=20, color=QWHITE).shift(DOWN * 0.2),
        ).move_to(RIGHT * 3)

        # Arrows forming a loop
        top_arrow = Arrow(q_box.get_right() + UP * 0.3, c_box.get_left() + UP * 0.3,
                          color=QGREEN, buff=0.15, stroke_width=2)
        top_lbl = MathTex(r"\langle E \rangle", font_size=20, color=QGREEN).next_to(top_arrow, UP, buff=0.1)

        bot_arrow = Arrow(c_box.get_left() + DOWN * 0.3, q_box.get_right() + DOWN * 0.3,
                          color=QPURPLE, buff=0.15, stroke_width=2)
        bot_lbl = MathTex(r"\vec\theta'", font_size=20, color=QPURPLE).next_to(bot_arrow, DOWN, buff=0.1)

        self.play(FadeIn(q_box, shift=RIGHT * 0.2), FadeIn(c_box, shift=LEFT * 0.2))
        self.play(GrowArrow(top_arrow), Write(top_lbl))
        self.play(GrowArrow(bot_arrow), Write(bot_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Parametric circuit (ansatz) ───────────────────────
        circ = QuantumCircuit(num_qubits=2, num_cols=7, wire_length=9, labels=["0", "0"])
        circ.move_to(0.5 * UP)
        self.play(FadeIn(circ))

        # Ry rotations (parametric)
        ry0 = circ.add_single_gate(r"R_y", 0, 1, color=QPURPLE)
        ry1 = circ.add_single_gate(r"R_y", 1, 1, color=QPURPLE)
        self.play(FadeIn(ry0, scale=1.2), FadeIn(ry1, scale=1.2))

        # Entangling CNOT
        cnot = circ.add_cnot(0, 1, 3, color=QBLUE)
        self.play(FadeIn(cnot, scale=1.2))

        # Another round of Ry
        ry2 = circ.add_single_gate(r"R_y", 0, 5, color=QPURPLE)
        ry3 = circ.add_single_gate(r"R_y", 1, 5, color=QPURPLE)
        self.play(FadeIn(ry2, scale=1.2), FadeIn(ry3, scale=1.2))

        # Params annotation
        theta_lbl = MathTex(r"\theta_1, \theta_2, \theta_3, \theta_4", font_size=22, color=QPURPLE)
        theta_lbl.next_to(circ, DOWN, buff=0.6)
        self.play(Write(theta_lbl))
        self.wait(2)
        self.play(FadeOut(circ), FadeOut(ry0), FadeOut(ry1), FadeOut(cnot),
                  FadeOut(ry2), FadeOut(ry3), FadeOut(theta_lbl))

        # ── Energy landscape convergence ──────────────────────
        axes_o = LEFT * 4 + DOWN * 1.0
        x_ax = Arrow(axes_o, axes_o + 8 * RIGHT, color=QGRAY, buff=0, stroke_width=2)
        y_ax = Arrow(axes_o, axes_o + 3.5 * UP, color=QGRAY, buff=0, stroke_width=2)
        x_lbl = MathTex(r"\text{iteration}", font_size=18, color=QGRAY).next_to(x_ax, DOWN, buff=0.1)
        y_lbl = MathTex(r"\langle E \rangle", font_size=18, color=QGRAY).next_to(y_ax, LEFT, buff=0.1)
        self.play(GrowArrow(x_ax), GrowArrow(y_ax), Write(x_lbl), Write(y_lbl))

        # Simulated convergence curve
        rng = np.random.default_rng(7)
        energies = []
        e = 3.0
        for i in range(40):
            e = e * 0.93 + rng.uniform(-0.1, 0.05)
            energies.append(max(e, 0.4))

        dx = 8 / 40
        dy = 1.0
        dots = VGroup()
        for i, en in enumerate(energies):
            pos = axes_o + (i + 1) * dx * RIGHT + en * dy * UP
            dots.add(Dot(pos, radius=0.04, color=QGREEN))

        self.play(FadeIn(dots, lag_ratio=0.05), run_time=2)

        # Ground state line
        gs_line = DashedLine(
            axes_o + 0.4 * dy * UP, axes_o + 8 * RIGHT + 0.4 * dy * UP,
            color=QORANGE, stroke_opacity=0.5, stroke_width=1.5,
        )
        gs_lbl = MathTex(r"E_0", font_size=20, color=QORANGE).next_to(gs_line, RIGHT, buff=0.15)
        self.play(Create(gs_line), Write(gs_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Molecule visualization (H₂) ──────────────────────
        atom1 = VGroup(
            Circle(radius=0.4, color=QBLUE, fill_opacity=0.3),
            MathTex(r"\text{H}", font_size=24, color=QBLUE),
        ).move_to(LEFT * 1.5)
        atom2 = VGroup(
            Circle(radius=0.4, color=QBLUE, fill_opacity=0.3),
            MathTex(r"\text{H}", font_size=24, color=QBLUE),
        ).move_to(RIGHT * 1.5)
        bond = Line(atom1[0].get_right(), atom2[0].get_left(), color=QWHITE, stroke_width=3)

        # Electron cloud
        cloud = Ellipse(width=4.5, height=1.5, color=QPURPLE, stroke_opacity=0.3, fill_opacity=0.05)

        mol_lbl = MathTex(r"H_2 \text{ molecule}", font_size=26, color=QWHITE).shift(DOWN * 1.5)
        find_lbl = MathTex(r"\text{Find ground state energy } E_0", font_size=22, color=QGREEN)
        find_lbl.shift(DOWN * 2.2)

        self.play(FadeIn(atom1), FadeIn(atom2), Create(bond), FadeIn(cloud))
        self.play(Write(mol_lbl), Write(find_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

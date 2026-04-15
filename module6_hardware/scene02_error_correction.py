"""5.2 — Quantum Error Correction (animation only)"""
from manim import *
import numpy as np
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE
from common.circuit import QuantumCircuit


class ErrorCorrectionScene(Scene):
    def construct(self):
        self.camera.background_color = QDARK

        # ── Classical repetition: 0 → 000, 1 → 111 ──────────
        classical = VGroup(
            MathTex(r"0 \to 000", font_size=36, color=QBLUE),
            MathTex(r"1 \to 111", font_size=36, color=QRED),
        ).arrange(DOWN, buff=0.5)

        majority_lbl = MathTex(r"\text{majority vote}", font_size=26, color=QGRAY)
        majority_lbl.next_to(classical, DOWN, buff=0.6)

        self.play(Write(classical), run_time=1.5)
        self.play(Write(majority_lbl))
        self.wait(1)

        # Error example: 000 → 010 → vote → 0 ✓
        error_ex = VGroup(
            MathTex(r"000", font_size=32, color=QBLUE),
            MathTex(r"\xrightarrow{\text{error}}", font_size=24, color=QORANGE),
            MathTex(r"010", font_size=32, color=QORANGE),
            MathTex(r"\xrightarrow{\text{vote}}", font_size=24, color=QGREEN),
            MathTex(r"0\;\checkmark", font_size=32, color=QGREEN),
        ).arrange(RIGHT, buff=0.3).next_to(majority_lbl, DOWN, buff=0.5)

        self.play(Write(error_ex), run_time=2)
        self.wait(1.5)
        self.play(FadeOut(classical), FadeOut(majority_lbl), FadeOut(error_ex))

        # ── Quantum problem: no cloning ──────────────────────
        no_clone = VGroup(
            MathTex(r"|\psi\rangle \not\to |\psi\rangle|\psi\rangle|\psi\rangle",
                    font_size=36, color=QRED),
            MathTex(r"\text{No-Cloning Theorem}", font_size=24, color=QGRAY),
        ).arrange(DOWN, buff=0.4)
        self.play(Write(no_clone))
        self.wait(1.5)
        self.play(FadeOut(no_clone))

        # ── 3-qubit bit flip code circuit ─────────────────────
        circ = QuantumCircuit(num_qubits=3, num_cols=8, wire_length=10,
                              labels=[r"\psi", "0", "0"])
        circ.move_to(0.3 * UP)
        self.play(FadeIn(circ))

        # Encoding: CNOT from q0→q1, CNOT from q0→q2
        c1 = circ.add_cnot(0, 1, 1, color=QBLUE)
        c2 = circ.add_cnot(0, 2, 2, color=QBLUE)
        self.play(FadeIn(c1, scale=1.2), FadeIn(c2, scale=1.2))
        circ.add_barrier(3)

        encode_lbl = MathTex(r"\text{encode}", font_size=20, color=QBLUE)
        encode_lbl.next_to(circ, DOWN, buff=0.4).shift(LEFT * 3)
        self.play(Write(encode_lbl))

        # Error on qubit 1 (X gate)
        err = circ.add_single_gate("E", 1, 4, color=QRED)
        self.play(FadeIn(err, scale=1.3))
        circ.add_barrier(5)

        # Syndrome measurement: CNOT q0→q1, CNOT q0→q2, then measure ancillas
        c3 = circ.add_cnot(0, 1, 6, color=QGREEN)
        c4 = circ.add_cnot(0, 2, 7, color=QGREEN)
        self.play(FadeIn(c3, scale=1.2), FadeIn(c4, scale=1.2))

        syndrome_lbl = MathTex(r"\text{detect \& correct}", font_size=20, color=QGREEN)
        syndrome_lbl.next_to(encode_lbl, RIGHT, buff=3.0)
        self.play(Write(syndrome_lbl))
        self.wait(2)

        self.play(FadeOut(circ), FadeOut(c1), FadeOut(c2), FadeOut(err),
                  FadeOut(c3), FadeOut(c4), FadeOut(encode_lbl), FadeOut(syndrome_lbl))

        # ── Surface code grid ─────────────────────────────────
        grid_size = 5
        dot_spacing = 0.7
        data_dots = VGroup()
        ancilla_x = VGroup()
        ancilla_z = VGroup()

        for r in range(grid_size):
            for c in range(grid_size):
                pos = np.array([c * dot_spacing, -r * dot_spacing, 0])
                d = Dot(pos, radius=0.1, color=QBLUE)
                data_dots.add(d)

        # Place X-type ancillas (between rows)
        for r in range(grid_size - 1):
            for c in range(grid_size - 1):
                if (r + c) % 2 == 0:
                    pos = np.array([(c + 0.5) * dot_spacing, -(r + 0.5) * dot_spacing, 0])
                    a = Square(side_length=0.2, color=QRED, fill_opacity=0.5, stroke_width=0)
                    a.move_to(pos)
                    ancilla_x.add(a)
                else:
                    pos = np.array([(c + 0.5) * dot_spacing, -(r + 0.5) * dot_spacing, 0])
                    a = Square(side_length=0.2, color=QGREEN, fill_opacity=0.5, stroke_width=0)
                    a.move_to(pos)
                    ancilla_z.add(a)

        grid = VGroup(data_dots, ancilla_x, ancilla_z)
        grid.move_to(LEFT * 2.5)

        surface_lbl = MathTex(r"\text{Surface Code}", font_size=30, color=QGREEN)
        surface_lbl.to_edge(UP, buff=0.5)

        legend = VGroup(
            VGroup(Dot(radius=0.08, color=QBLUE), MathTex(r"\text{data}", font_size=18, color=QBLUE)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.16, color=QRED, fill_opacity=0.5, stroke_width=0),
                   MathTex(r"\text{X check}", font_size=18, color=QRED)).arrange(RIGHT, buff=0.2),
            VGroup(Square(side_length=0.16, color=QGREEN, fill_opacity=0.5, stroke_width=0),
                   MathTex(r"\text{Z check}", font_size=18, color=QGREEN)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(RIGHT * 3)

        self.play(Write(surface_lbl))
        self.play(FadeIn(data_dots, lag_ratio=0.02))
        self.play(FadeIn(ancilla_x, lag_ratio=0.05), FadeIn(ancilla_z, lag_ratio=0.05))
        self.play(FadeIn(legend))
        self.wait(1)

        # Highlight an error — flash a data qubit red
        err_qubit = data_dots[12]  # middle qubit
        self.play(err_qubit.animate.set_color(QRED).scale(1.5), run_time=0.5)
        self.wait(0.5)

        # Show syndrome detection — nearby ancillas light up
        flash_anc = VGroup(*ancilla_x[:2], *ancilla_z[:2])
        self.play(flash_anc.animate.set_opacity(1), run_time=0.5)
        self.wait(0.5)

        # Correct — qubit returns to blue
        self.play(err_qubit.animate.set_color(QBLUE).scale(1 / 1.5), run_time=0.5)
        self.wait(1.5)

        # Overhead stat
        overhead = MathTex(
            r"\sim 1000 \text{ physical} \to 1 \text{ logical qubit}",
            font_size=26, color=QORANGE,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(overhead))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

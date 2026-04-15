"""6.3 — Quantum Cryptography BB84 (animation only)"""
from manim import *
import numpy as np
import random
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.styles import QBLUE, QRED, QWHITE, QGRAY, QDARK, QGREEN, QPURPLE, QORANGE, QYELLOW


class BB84Scene(Scene):
    def construct(self):
        self.camera.background_color = QDARK
        random.seed(42)

        # ── Alice and Bob ─────────────────────────────────────
        alice = VGroup(
            RoundedRectangle(width=2.0, height=1.4, corner_radius=0.15,
                             color=QBLUE, fill_opacity=0.12, stroke_width=2),
            MathTex(r"\text{Alice}", font_size=22, color=QBLUE),
        ).move_to(LEFT * 5)
        bob = VGroup(
            RoundedRectangle(width=2.0, height=1.4, corner_radius=0.15,
                             color=QGREEN, fill_opacity=0.12, stroke_width=2),
            MathTex(r"\text{Bob}", font_size=22, color=QGREEN),
        ).move_to(RIGHT * 5)

        channel = Line(alice.get_right(), bob.get_left(), color=QGRAY, stroke_width=1.5, stroke_opacity=0.4)
        channel_lbl = MathTex(r"\text{quantum channel}", font_size=16, color=QGRAY).next_to(channel, UP, buff=0.1)

        self.play(FadeIn(alice), FadeIn(bob), Create(channel), Write(channel_lbl))
        self.wait(0.5)

        # ── Basis icons ───────────────────────────────────────
        # Rectilinear basis: + symbol, Diagonal basis: × symbol
        bases_legend = VGroup(
            VGroup(
                MathTex(r"+", font_size=24, color=QBLUE),
                MathTex(r"\{|0\rangle, |1\rangle\}", font_size=16, color=QGRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\times", font_size=24, color=QPURPLE),
                MathTex(r"\{|+\rangle, |-\rangle\}", font_size=16, color=QGRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=1.0).to_edge(UP, buff=0.4)
        self.play(FadeIn(bases_legend))

        # ── Send qubits ──────────────────────────────────────
        n_bits = 8
        alice_bits = [random.randint(0, 1) for _ in range(n_bits)]
        alice_bases = [random.choice(["+", "×"]) for _ in range(n_bits)]
        bob_bases = [random.choice(["+", "×"]) for _ in range(n_bits)]

        # Build table rows
        table_y = -0.5
        row_spacing = 0.55
        col_width = 0.8
        col_start = -3.5

        headers = ["Bit", "A basis", "Qubit", "B basis", "Match?", "Key"]
        header_row = VGroup()
        for j, h in enumerate(headers):
            txt = MathTex(r"\text{" + h + "}", font_size=16, color=QGRAY)
            txt.move_to(np.array([col_start + j * col_width + j * 0.15, table_y, 0]))
            header_row.add(txt)
        self.play(FadeIn(header_row))

        all_rows = VGroup()
        sifted_key = []
        for i in range(n_bits):
            y = table_y - (i + 1) * row_spacing
            a_bit = str(alice_bits[i])
            a_base = alice_bases[i]

            # Determine qubit sent
            if a_base == "+":
                qubit = f"|{alice_bits[i]}\\rangle"
                q_color = QBLUE
            else:
                qubit = "|+\\rangle" if alice_bits[i] == 0 else "|-\\rangle"
                q_color = QPURPLE

            b_base = bob_bases[i]
            match_sym = "Y" if a_base == b_base else "N"
            m_color = QGREEN if a_base == b_base else QRED

            key_val = ""
            if a_base == b_base:
                key_val = a_bit
                sifted_key.append(a_bit)

            cells = [
                MathTex(a_bit, font_size=18, color=QWHITE),
                MathTex(a_base, font_size=18, color=QBLUE if a_base == "+" else QPURPLE),
                MathTex(qubit, font_size=16, color=q_color),
                MathTex(b_base, font_size=18, color=QBLUE if b_base == "+" else QPURPLE),
                Text(match_sym, font_size=16, color=m_color, weight=BOLD),
                MathTex(key_val, font_size=18, color=QGREEN) if key_val else Text("", font_size=16),
            ]

            row = VGroup()
            for j, cell in enumerate(cells):
                cell.move_to(np.array([col_start + j * col_width + j * 0.15, y, 0]))
                row.add(cell)

            all_rows.add(row)
            self.play(FadeIn(row), run_time=0.3)

            # Animate qubit flying from Alice to Bob
            photon = Dot(alice.get_right() + RIGHT * 0.2, radius=0.06, color=q_color)
            self.play(
                photon.animate.move_to(bob.get_left() + LEFT * 0.2),
                run_time=0.2, rate_func=linear,
            )
            self.remove(photon)

        self.wait(1)

        # Show sifted key
        key_str = "".join(sifted_key)
        key_display = MathTex(
            r"\text{Sifted Key: }" + key_str,
            font_size=24, color=QGREEN,
        ).to_edge(DOWN, buff=0.3)
        key_box = SurroundingRectangle(key_display, color=QGREEN, corner_radius=0.1, buff=0.15)
        self.play(Write(key_display), Create(key_box))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ── Eavesdropper detection ────────────────────────────
        eve = VGroup(
            RoundedRectangle(width=1.8, height=1.2, corner_radius=0.15,
                             color=QRED, fill_opacity=0.15, stroke_width=2),
            MathTex(r"\text{Eve}", font_size=22, color=QRED),
        ).move_to(ORIGIN)

        alice2 = VGroup(
            Circle(radius=0.5, color=QBLUE, fill_opacity=0.2),
            MathTex(r"A", font_size=22, color=QBLUE),
        ).move_to(LEFT * 4)
        bob2 = VGroup(
            Circle(radius=0.5, color=QGREEN, fill_opacity=0.2),
            MathTex(r"B", font_size=22, color=QGREEN),
        ).move_to(RIGHT * 4)

        line_ae = Line(alice2.get_right(), eve.get_left(), color=QGRAY, stroke_width=1.5)
        line_eb = Line(eve.get_right(), bob2.get_left(), color=QGRAY, stroke_width=1.5)

        self.play(FadeIn(alice2), FadeIn(bob2), FadeIn(eve), Create(line_ae), Create(line_eb))
        self.wait(0.5)

        # Eve measures → disturbs state
        disturb = MathTex(r"\sim 25\% \text{ errors introduced}", font_size=26, color=QRED)
        disturb.shift(DOWN * 1.5)
        flash = Circle(radius=0.01, color=QRED, fill_opacity=1).move_to(eve)
        self.play(flash.animate.scale(80).set_opacity(0), run_time=0.4)
        self.play(Write(disturb))
        self.wait(1)

        detect = MathTex(r"\text{Alice \& Bob compare sample} \to \text{detect Eve!}",
                         font_size=22, color=QGREEN).shift(DOWN * 2.3)
        self.play(Write(detect))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

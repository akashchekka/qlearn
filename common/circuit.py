"""Quantum circuit drawing helpers — wires, gates, measurements."""
from __future__ import annotations
import numpy as np
from manim import *
from .styles import QCYAN, QBLUE, QRED, QGREEN, QWHITE, QGRAY, QORANGE, QPURPLE

# ── Constants ─────────────────────────────────────────────────
WIRE_SPACING = 1.0
GATE_SIZE = 0.7
GATE_SPACING = 1.2


class QuantumWire(VGroup):
    """A single horizontal qubit wire with an optional label."""

    def __init__(
        self, length: float = 8.0, label: str | None = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.wire = Line(ORIGIN, length * RIGHT, color=QCYAN, stroke_width=2)
        self.add(self.wire)
        if label:
            lbl = MathTex(rf"|{label}\rangle", font_size=22, color=QCYAN)
            lbl.next_to(self.wire, LEFT, buff=0.25)
            self.add(lbl)


class QuantumCircuit(VGroup):
    """Build up a quantum circuit diagram incrementally."""

    def __init__(
        self,
        num_qubits: int,
        num_cols: int = 8,
        wire_length: float = 8.0,
        labels: list[str] | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.num_qubits = num_qubits
        self.wire_length = wire_length
        self.num_cols = num_cols
        self._col_x_start = -wire_length / 2 + 1.0
        self._col_spacing = (wire_length - 2.0) / max(num_cols - 1, 1)

        if labels is None:
            labels = [str(i) for i in range(num_qubits)]

        self.wires: list[QuantumWire] = []
        for i in range(num_qubits):
            w = QuantumWire(length=wire_length, label=labels[i])
            w.shift(i * WIRE_SPACING * DOWN)
            self.wires.append(w)
            self.add(w)

        self.center()

    # ── position helpers ──────────────────────────────────────

    def _qubit_y(self, qubit: int) -> float:
        return self.wires[qubit].wire.get_center()[1]

    def _col_x(self, col: int) -> float:
        return self._col_x_start + col * self._col_spacing + self.get_center()[0]

    def gate_position(self, qubit: int, col: int) -> np.ndarray:
        return np.array([self._col_x(col), self._qubit_y(qubit), 0])

    # ── gate builders ─────────────────────────────────────────

    def add_single_gate(
        self, name: str, qubit: int, col: int, color=QBLUE
    ) -> VGroup:
        pos = self.gate_position(qubit, col)
        box = Square(
            side_length=GATE_SIZE, color=color,
            fill_opacity=0.2, stroke_width=2,
        ).move_to(pos)
        lbl = MathTex(name, font_size=22, color=color).move_to(pos)
        gate = VGroup(box, lbl)
        self.add(gate)
        return gate

    def add_cnot(
        self, control: int, target: int, col: int, color=QBLUE
    ) -> VGroup:
        ctrl_pos = self.gate_position(control, col)
        tgt_pos = self.gate_position(target, col)
        ctrl_dot = Dot(ctrl_pos, color=color, radius=0.1)
        tgt_circle = Circle(
            radius=0.2, color=color, stroke_width=2,
        ).move_to(tgt_pos)
        tgt_plus = MathTex(r"+", font_size=18, color=color).move_to(tgt_pos)
        line = Line(ctrl_pos, tgt_pos, color=color, stroke_width=2)
        gate = VGroup(line, ctrl_dot, tgt_circle, tgt_plus)
        self.add(gate)
        return gate

    def add_swap(
        self, q1: int, q2: int, col: int, color=QBLUE
    ) -> VGroup:
        pos1 = self.gate_position(q1, col)
        pos2 = self.gate_position(q2, col)
        x1 = MathTex(r"\times", font_size=22, color=color).move_to(pos1)
        x2 = MathTex(r"\times", font_size=22, color=color).move_to(pos2)
        line = Line(pos1, pos2, color=color, stroke_width=2)
        gate = VGroup(line, x1, x2)
        self.add(gate)
        return gate

    def add_measurement(
        self, qubit: int, col: int, color=QGREEN
    ) -> VGroup:
        pos = self.gate_position(qubit, col)
        box = Square(
            side_length=GATE_SIZE, color=color,
            fill_opacity=0.15, stroke_width=2,
        ).move_to(pos)
        arc = Arc(
            radius=0.18, start_angle=PI, angle=-PI,
            color=color, stroke_width=2,
        ).move_to(pos + 0.05 * DOWN)
        needle = Line(
            pos + 0.05 * DOWN,
            pos + 0.22 * UP + 0.15 * RIGHT,
            color=color, stroke_width=2,
        )
        meter = VGroup(box, arc, needle)
        self.add(meter)
        return meter

    def add_controlled_gate(
        self, name: str, control: int, target: int, col: int,
        color=QPURPLE,
    ) -> VGroup:
        ctrl_pos = self.gate_position(control, col)
        tgt_pos = self.gate_position(target, col)
        ctrl_dot = Dot(ctrl_pos, color=color, radius=0.1)
        line = Line(ctrl_pos, tgt_pos, color=color, stroke_width=2)
        box = Square(
            side_length=GATE_SIZE, color=color,
            fill_opacity=0.2, stroke_width=2,
        ).move_to(tgt_pos)
        lbl = MathTex(name, font_size=22, color=color).move_to(tgt_pos)
        gate = VGroup(line, ctrl_dot, box, lbl)
        self.add(gate)
        return gate

    def add_barrier(self, col: int, color=QGRAY) -> VGroup:
        top = self.gate_position(0, col) + 0.4 * UP
        bottom = self.gate_position(self.num_qubits - 1, col) + 0.4 * DOWN
        line = DashedLine(
            top, bottom, color=color,
            stroke_opacity=0.5, stroke_width=1.5,
        )
        self.add(line)
        return VGroup(line)

    def add_multi_qubit_gate(
        self, name: str, qubits: list[int], col: int, color=QPURPLE
    ) -> VGroup:
        """Draw a gate box spanning multiple qubits."""
        positions = [self.gate_position(q, col) for q in qubits]
        top_y = max(p[1] for p in positions) + GATE_SIZE / 2
        bot_y = min(p[1] for p in positions) - GATE_SIZE / 2
        cx = positions[0][0]
        box = Rectangle(
            width=GATE_SIZE + 0.2,
            height=top_y - bot_y,
            color=color, fill_opacity=0.2, stroke_width=2,
        ).move_to(np.array([cx, (top_y + bot_y) / 2, 0]))
        lbl = MathTex(name, font_size=22, color=color).move_to(box)
        gate = VGroup(box, lbl)
        self.add(gate)
        return gate

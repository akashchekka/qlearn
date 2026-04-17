"""Shared color palette, fonts, and styling constants for all animations."""
from manim import *

# -- Color Palette --
QBLUE = "#4FC3F7"       # |0> state / primary accent
QRED = "#EF5350"        # |1> state / secondary accent
QGREEN = "#66BB6A"      # measurement / success
QPURPLE = "#AB47BC"     # entanglement / phase
QORANGE = "#FFA726"     # oracle / highlight
QYELLOW = "#FFEE58"     # annotations / active highlight
QDARK = "#1A1A2E"       # background
QGRAY = "#B0BEC5"       # secondary text / grid
QWHITE = "#ECEFF1"      # primary text
QCYAN = "#00E5FF"       # circuit wires
QTEAL = "#009688"       # NISQ / applications

# -- Module Accent Colors --
MODULE_COLORS = {
    1: QBLUE,
    2: QBLUE,
    3: QCYAN,
    4: QPURPLE,
    5: QORANGE,
    6: QRED,
    7: QGREEN,
    8: QTEAL,
}

# -- Module Names --
MODULE_NAMES = {
    1: "Foundations",
    2: "Quantum Computing Basics",
    3: "Quantum Circuits",
    4: "Quantum Gates",
    5: "Entanglement",
    6: "Algorithms",
    7: "Hardware & Errors",
    8: "NISQ Applications",
}

# -- Shared Sizing --
TITLE_FONT_SIZE = 48
SUBTITLE_FONT_SIZE = 32
BODY_FONT_SIZE = 28
LABEL_FONT_SIZE = 24
MATH_FONT_SIZE = 36
SMALL_MATH_SIZE = 28

# -- Timing Constants (seconds) --
TITLE_HOLD = 2.5
STEP_PAUSE = 1.5
LONG_PAUSE = 3.0
FAST_ANIM = 0.8
NORMAL_ANIM = 1.2

# -- LaTeX Preamble --
KET_TEX_TEMPLATE = TexTemplate()
KET_TEX_TEMPLATE.add_to_preamble(r"\usepackage{braket}")


# -- Text Factories --

def styled_title(text: str, color=QWHITE) -> Text:
    return Text(text, font_size=TITLE_FONT_SIZE, color=color, weight=BOLD)


def styled_subtitle(text: str, color=QGRAY) -> Text:
    return Text(text, font_size=SUBTITLE_FONT_SIZE, color=color)


def styled_body(text: str, color=QWHITE) -> Text:
    return Text(text, font_size=BODY_FONT_SIZE, color=color)


def styled_label(text: str, color=QGRAY) -> Text:
    return Text(text, font_size=LABEL_FONT_SIZE, color=color)


# -- Math Factories --

def ket(state: str, color=QWHITE) -> MathTex:
    return MathTex(rf"|{state}\rangle", color=color, font_size=MATH_FONT_SIZE)


def bra(state: str, color=QWHITE) -> MathTex:
    return MathTex(rf"\langle {state}|", color=color, font_size=MATH_FONT_SIZE)


def braket_tex(bra_s: str, ket_s: str, color=QWHITE) -> MathTex:
    return MathTex(
        rf"\langle {bra_s}|{ket_s}\rangle", color=color, font_size=MATH_FONT_SIZE
    )


def gate_matrix(matrix_str: str, color=QWHITE) -> MathTex:
    return MathTex(matrix_str, color=color, font_size=MATH_FONT_SIZE)


# -- Layout Components --

def title_card(topic_name: str) -> VGroup:
    """Title card showing only the topic name."""
    title = styled_title(topic_name, color=QWHITE)
    return VGroup(title)


def section_title(text: str, color=QBLUE) -> Text:
    """Small section header used within a scene."""
    return Text(text, font_size=SUBTITLE_FONT_SIZE, color=color, weight=BOLD)


def info_box(text: str, color=QBLUE, width=10) -> VGroup:
    """Rounded rectangle with centered text."""
    txt = styled_body(text, color=QWHITE)
    txt.width = min(txt.width, width - 0.6)
    box = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=txt.height + 0.8,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.15,
    )
    return VGroup(box, txt)


def math_info_box(
    tex_string: str, color=QBLUE, width=10, font_size=BODY_FONT_SIZE
) -> VGroup:
    """Rounded rectangle with centered MathTex."""
    txt = MathTex(tex_string, font_size=font_size, color=QWHITE)
    if txt.width > width - 0.6:
        txt.width = width - 0.6
    box = RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=txt.height + 0.8,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.15,
    )
    return VGroup(box, txt)

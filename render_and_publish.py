"""Render all scenes at 4K and place final MP4s in docs/videos/.

Each video is named after its scene class (e.g. BlochSphereScene.mp4).
Manim renders into media/videos/ first, then the script copies the
finished MP4 into docs/videos/ with the clean name.

Usage:
    python render_and_publish.py          # 4K (default)
    python render_and_publish.py --hd     # 1080p
    python render_and_publish.py --low    # 480p (fast preview)
    python render_and_publish.py --scene BlochSphereScene  # one scene
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DOCS_VIDEOS = ROOT / "docs" / "videos"
MEDIA = ROOT / "media" / "videos"

# ── Scene Registry ────────────────────────────────────────────
SCENES = [
    # (module, file, scene_class, display_name)
    # Module 1 — Foundations (Quantum Mechanics)
    (1, "modules/foundations/scene01_wave_particle_duality.py", "WaveParticleDualityScene", "1.1 Wave-Particle Duality"),
    (1, "modules/foundations/scene02_quantum_states.py", "QuantumStatesScene", "1.2 Quantum States & Probability"),
    (1, "modules/foundations/scene03_uncertainty_principle.py", "UncertaintyPrincipleScene", "1.3 Uncertainty Principle"),
    (1, "modules/foundations/scene04_spin.py", "SpinScene", "1.4 Spin & Stern-Gerlach"),
    (1, "modules/foundations/scene05_schrodinger_equation.py", "SchrodingerEquationScene", "1.5 Schrodinger Equation"),
    (1, "modules/foundations/scene06_dirac_notation.py", "DiracNotationScene", "1.6 Dirac Notation"),
    (1, "modules/foundations/scene07_observables_operators.py", "ObservablesOperatorsScene", "1.7 Observables & Operators"),
    # Module 2 — Quantum Computing Basics
    (2, "modules/qc_basics/scene01_what_is_a_qubit.py", "WhatIsAQubit", "2.1 What Is a Qubit"),
    (2, "modules/qc_basics/scene02_bloch_sphere.py", "BlochSphereScene", "2.2 The Bloch Sphere"),
    (2, "modules/qc_basics/scene03_superposition.py", "SuperpositionScene", "2.3 Superposition"),
    (2, "modules/qc_basics/scene04_measurement.py", "MeasurementScene", "2.4 Measurement"),
    # Module 3 — Quantum Circuits
    (3, "modules/circuits/scene01_what_is_a_circuit.py", "WhatIsACircuitScene", "3.1 What Is a Quantum Circuit"),
    (3, "modules/circuits/scene02_circuit_notation.py", "CircuitNotationScene", "3.2 Circuit Notation"),
    (3, "modules/circuits/scene03_circuit_depth.py", "CircuitDepthScene", "3.3 Circuit Depth & Complexity"),
    # Module 4 — Quantum Gates
    (4, "modules/gates/scene01_pauli_gates.py", "PauliGatesScene", "4.1 Pauli Gates"),
    (4, "modules/gates/scene02_hadamard_gate.py", "HadamardGateScene", "4.2 Hadamard Gate"),
    (4, "modules/gates/scene03_phase_gates.py", "PhaseGatesScene", "4.3 Phase & Rotation Gates"),
    (4, "modules/gates/scene04_multi_qubit_gates.py", "MultiQubitGatesScene", "4.4 Multi-Qubit Gates"),
    # Module 5 — Entanglement
    (5, "modules/entanglement/scene01_bell_states.py", "BellStatesScene", "5.1 Bell States"),
    (5, "modules/entanglement/scene02_quantum_teleportation.py", "QuantumTeleportationScene", "5.2 Quantum Teleportation"),
    (5, "modules/entanglement/scene03_superdense_coding.py", "SuperdenseCodingScene", "5.3 Superdense Coding"),
    # Module 6 — Algorithms
    (6, "modules/algorithms/scene01_deutsch_jozsa.py", "DeutschJozsaScene", "6.1 Deutsch-Jozsa Algorithm"),
    (6, "modules/algorithms/scene02_grovers_search.py", "GroversSearchScene", "6.2 Grover's Search"),
    (6, "modules/algorithms/scene03_quantum_fourier_transform.py", "QFTScene", "6.3 Quantum Fourier Transform"),
    (6, "modules/algorithms/scene04_shors_algorithm.py", "ShorsAlgorithmScene", "6.4 Shor's Algorithm"),
    # Module 7 — Hardware & Errors
    (7, "modules/hardware/scene01_noise_decoherence.py", "NoiseDecoherenceScene", "7.1 Noise & Decoherence"),
    (7, "modules/hardware/scene02_error_correction.py", "ErrorCorrectionScene", "7.2 Error Correction"),
    (7, "modules/hardware/scene03_hardware_platforms.py", "HardwarePlatformsScene", "7.3 Hardware Platforms"),
    # Module 8 — NISQ Applications
    (8, "modules/nisq/scene01_vqe.py", "VQEScene", "8.1 VQE"),
    (8, "modules/nisq/scene02_qaoa.py", "QAOAScene", "8.2 QAOA"),
    (8, "modules/nisq/scene03_bb84.py", "BB84Scene", "8.3 BB84 Cryptography"),
    (8, "modules/nisq/scene04_quantum_ml.py", "QuantumMLScene", "8.4 Quantum ML"),
]

QUALITY_MAP = {
    "low": ("-ql", "480p15"),
    "medium": ("-qm", "720p30"),
    "hd": ("-qh", "1080p60"),
    "1440p": ("-qh", "1440p60"),
    "4k": ("-qk", "2160p60"),
}


def render_and_copy(file_path, scene_class, quality_flag, quality_dir, display_name, extra_args=None, force=False):
    """Render one scene, then copy the MP4 to docs/videos/."""
    dest = DOCS_VIDEOS / f"{scene_class}.mp4"
    if dest.exists() and not force:
        size_mb = dest.stat().st_size / (1024 * 1024)
        print(f"  SKIP: {scene_class}.mp4 already exists ({size_mb:.1f} MB)")
        return True

    print(f"\n{'='*60}")
    print(f"  Rendering: {display_name}")
    print(f"{'='*60}")

    cmd = [
        sys.executable, "-m", "manim", "render",
        quality_flag, file_path, scene_class,
    ]
    if extra_args:
        cmd[4:4] = extra_args
    result = subprocess.run(cmd, cwd=str(ROOT))
    if result.returncode != 0:
        print(f"  FAILED: {display_name}")
        return False

    # Find the rendered MP4 — manim puts it under media/videos/<stem>/<quality>/
    stem = Path(file_path).stem  # e.g. scene01_what_is_a_qubit
    rendered = MEDIA / stem / quality_dir / f"{scene_class}.mp4"

    if not rendered.exists():
        # Fallback: search recursively
        matches = list(MEDIA.rglob(f"{scene_class}.mp4"))
        if matches:
            rendered = max(matches, key=lambda p: p.stat().st_mtime)
        else:
            print(f"  ERROR: Cannot find {scene_class}.mp4 in media/videos/")
            return False

    dest = DOCS_VIDEOS / f"{scene_class}.mp4"
    shutil.copy2(rendered, dest)
    size_mb = dest.stat().st_size / (1024 * 1024)
    print(f"  DONE: {scene_class}.mp4  ({size_mb:.1f} MB) → docs/videos/")
    return True


def main():
    parser = argparse.ArgumentParser(description="Render & publish quantum animations")
    parser.add_argument("--hd", action="store_true", help="1080p")
    parser.add_argument("--1440p", dest="qhd", action="store_true", help="1440p (QHD)")
    parser.add_argument("--4k", dest="four_k", action="store_true", help="4K (default)")
    parser.add_argument("--low", action="store_true", help="480p (fast preview)")
    parser.add_argument("--medium", action="store_true", help="720p")
    parser.add_argument("--module", type=int, help="Render only a specific module (1-7)")
    parser.add_argument("--scene", type=str, help="Render only a specific scene class name")
    parser.add_argument("--force", action="store_true", help="Re-render even if video exists")
    args = parser.parse_args()

    # Default to 4K
    extra_args = None
    if args.low:
        quality_flag, quality_dir = QUALITY_MAP["low"]
    elif args.medium:
        quality_flag, quality_dir = QUALITY_MAP["medium"]
    elif args.hd:
        quality_flag, quality_dir = QUALITY_MAP["hd"]
    elif args.qhd:
        quality_flag, quality_dir = QUALITY_MAP["1440p"]
        extra_args = ["--resolution", "2560,1440"]
    else:
        quality_flag, quality_dir = QUALITY_MAP["4k"]

    # Filter
    scenes = SCENES
    if args.module:
        scenes = [s for s in scenes if s[0] == args.module]
    if args.scene:
        scenes = [s for s in scenes if s[2] == args.scene]

    if not scenes:
        print("No matching scenes found.")
        return

    DOCS_VIDEOS.mkdir(parents=True, exist_ok=True)

    print(f"\n>>> Rendering {len(scenes)} scene(s) at {quality_dir}")
    print(f"    Output: docs/videos/\n")

    ok, fail = 0, 0
    for mod, file, cls, name in scenes:
        if render_and_copy(file, cls, quality_flag, quality_dir, name, extra_args, force=args.force):
            ok += 1
        else:
            fail += 1

    print(f"\n{'='*60}")
    print(f"  Results: {ok} succeeded, {fail} failed")
    print(f"  Videos in: docs/videos/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

"""Render all scenes and export web-ready MP4 files.

Usage:
    python render_all.py              # Render all at 720p (fast preview)
    python render_all.py --hd         # Render all at 1080p (web quality)
    python render_all.py --4k         # Render all at 4K
    python render_all.py --module 1   # Render only module 1
    python render_all.py --scene WhatIsAQubit  # Render a specific scene
"""
import argparse
import subprocess
import sys
from pathlib import Path

# ── Scene Registry ────────────────────────────────────────────
SCENES = [
    # (module, file, scene_class, display_name)
    (1, "module1_foundations/scene01_what_is_a_qubit.py", "WhatIsAQubit", "1.1 What Is a Qubit"),
    (1, "module1_foundations/scene02_bloch_sphere.py", "BlochSphereScene", "1.2 The Bloch Sphere"),
    (1, "module1_foundations/scene03_superposition.py", "SuperpositionScene", "1.3 Superposition"),
    (1, "module1_foundations/scene04_measurement.py", "MeasurementScene", "1.4 Measurement"),
    (2, "module2_circuits/scene01_what_is_a_circuit.py", "WhatIsACircuitScene", "2.1 What Is a Quantum Circuit"),
    (2, "module2_circuits/scene02_circuit_notation.py", "CircuitNotationScene", "2.2 Circuit Notation"),
    (2, "module2_circuits/scene03_circuit_depth.py", "CircuitDepthScene", "2.3 Circuit Depth & Complexity"),
    (3, "module3_gates/scene01_pauli_gates.py", "PauliGatesScene", "3.1 Pauli Gates"),
    (3, "module3_gates/scene02_hadamard_gate.py", "HadamardGateScene", "3.2 Hadamard Gate"),
    (3, "module3_gates/scene03_phase_gates.py", "PhaseGatesScene", "3.3 Phase & Rotation Gates"),
    (3, "module3_gates/scene04_multi_qubit_gates.py", "MultiQubitGatesScene", "3.4 Multi-Qubit Gates"),
    (4, "module4_entanglement/scene01_bell_states.py", "BellStatesScene", "4.1 Bell States"),
    (4, "module4_entanglement/scene02_quantum_teleportation.py", "QuantumTeleportationScene", "4.2 Quantum Teleportation"),
    (4, "module4_entanglement/scene03_superdense_coding.py", "SuperdenseCodingScene", "4.3 Superdense Coding"),
    (5, "module5_algorithms/scene01_deutsch_jozsa.py", "DeutschJozsaScene", "5.1 Deutsch-Jozsa Algorithm"),
    (5, "module5_algorithms/scene02_grovers_search.py", "GroversSearchScene", "5.2 Grover's Search"),
    (5, "module5_algorithms/scene03_quantum_fourier_transform.py", "QFTScene", "5.3 Quantum Fourier Transform"),
    (5, "module5_algorithms/scene04_shors_algorithm.py", "ShorsAlgorithmScene", "5.4 Shor's Algorithm"),
    (6, "module6_hardware/scene01_noise_decoherence.py", "NoiseDecoherenceScene", "6.1 Noise & Decoherence"),
    (6, "module6_hardware/scene02_error_correction.py", "ErrorCorrectionScene", "6.2 Error Correction"),
    (6, "module6_hardware/scene03_hardware_platforms.py", "HardwarePlatformsScene", "6.3 Hardware Platforms"),
    (7, "module7_nisq/scene01_vqe.py", "VQEScene", "7.1 VQE"),
    (7, "module7_nisq/scene02_qaoa.py", "QAOAScene", "7.2 QAOA"),
    (7, "module7_nisq/scene03_bb84.py", "BB84Scene", "7.3 BB84 Cryptography"),
    (7, "module7_nisq/scene04_quantum_ml.py", "QuantumMLScene", "7.4 Quantum ML"),
]

QUALITY_MAP = {
    "low": "-ql",     # 480p
    "medium": "-qm",  # 720p
    "hd": "-qh",      # 1080p
    "4k": "-qk",      # 4K
}


def render_scene(file_path: str, scene_class: str, quality_flag: str, display_name: str):
    """Render a single scene with manim."""
    print(f"\n{'='*60}")
    print(f"  Rendering: {display_name}")
    print(f"  File: {file_path}")
    print(f"{'='*60}")

    cmd = [
        sys.executable, "-m", "manim",
        "render",
        quality_flag,
        file_path,
        scene_class,
    ]

    result = subprocess.run(cmd, cwd=str(Path(__file__).parent))
    if result.returncode != 0:
        print(f"  FAILED: {display_name}")
        return False
    print(f"  DONE: {display_name}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Render quantum computing Manim animations")
    parser.add_argument("--hd", action="store_true", help="Render at 1080p")
    parser.add_argument("--4k", dest="four_k", action="store_true", help="Render at 4K")
    parser.add_argument("--low", action="store_true", help="Render at 480p (fastest)")
    parser.add_argument("--module", type=int, help="Render only a specific module (1-4)")
    parser.add_argument("--scene", type=str, help="Render only a specific scene class name")
    parser.add_argument("--list", action="store_true", help="List all scenes")
    args = parser.parse_args()

    if args.list:
        print("\nAvailable Scenes:")
        print("-" * 50)
        for mod, file, cls, name in SCENES:
            print(f"  {name:40s} [{cls}]")
        return

    # Determine quality
    if args.four_k:
        quality_flag = QUALITY_MAP["4k"]
    elif args.hd:
        quality_flag = QUALITY_MAP["hd"]
    elif args.low:
        quality_flag = QUALITY_MAP["low"]
    else:
        quality_flag = QUALITY_MAP["medium"]

    # Filter scenes
    scenes_to_render = SCENES
    if args.module:
        scenes_to_render = [s for s in SCENES if s[0] == args.module]
    if args.scene:
        scenes_to_render = [s for s in SCENES if s[2] == args.scene]

    if not scenes_to_render:
        print("No matching scenes found.")
        return

    print(f"\n>>> Rendering {len(scenes_to_render)} scene(s)...")
    print(f"   Quality: {quality_flag}")

    successes = 0
    failures = 0
    for mod, file, cls, name in scenes_to_render:
        if render_scene(file, cls, quality_flag, name):
            successes += 1
        else:
            failures += 1

    print(f"\n{'='*60}")
    print(f"  Results: {successes} succeeded, {failures} failed")
    print(f"  Output: media/videos/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()

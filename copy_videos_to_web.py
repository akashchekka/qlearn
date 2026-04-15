"""Copy rendered 4K videos into the website/videos/ folder with clean names."""
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
MEDIA = ROOT / "media" / "videos"
OUT = ROOT / "docs" / "videos"

# Map scene class names to output filenames
SCENE_MAP = {
    "WhatIsAQubit":               "WhatIsAQubit.mp4",
    "BlochSphereScene":           "BlochSphereScene.mp4",
    "SuperpositionScene":         "SuperpositionScene.mp4",
    "MeasurementScene":           "MeasurementScene.mp4",
    "WhatIsACircuitScene":        "WhatIsACircuitScene.mp4",
    "CircuitNotationScene":       "CircuitNotationScene.mp4",
    "CircuitDepthScene":          "CircuitDepthScene.mp4",
    "PauliGatesScene":            "PauliGatesScene.mp4",
    "HadamardGateScene":          "HadamardGateScene.mp4",
    "PhaseGatesScene":            "PhaseGatesScene.mp4",
    "MultiQubitGatesScene":       "MultiQubitGatesScene.mp4",
    "BellStatesScene":            "BellStatesScene.mp4",
    "QuantumTeleportationScene":  "QuantumTeleportationScene.mp4",
    "SuperdenseCodingScene":      "SuperdenseCodingScene.mp4",
    "DeutschJozsaScene":          "DeutschJozsaScene.mp4",
    "GroversSearchScene":         "GroversSearchScene.mp4",
    "QFTScene":                   "QFTScene.mp4",
    "ShorsAlgorithmScene":        "ShorsAlgorithmScene.mp4",
    "NoiseDecoherenceScene":      "NoiseDecoherenceScene.mp4",
    "ErrorCorrectionScene":       "ErrorCorrectionScene.mp4",
    "HardwarePlatformsScene":     "HardwarePlatformsScene.mp4",
    "VQEScene":                   "VQEScene.mp4",
    "QAOAScene":                  "QAOAScene.mp4",
    "BB84Scene":                  "BB84Scene.mp4",
    "QuantumMLScene":             "QuantumMLScene.mp4",
}

OUT.mkdir(parents=True, exist_ok=True)

found = 0
for scene_name, out_name in SCENE_MAP.items():
    # Search for the rendered mp4 in any quality subfolder
    matches = list(MEDIA.rglob(f"{scene_name}.mp4"))
    if matches:
        # Pick highest quality (largest file)
        best = max(matches, key=lambda p: p.stat().st_size)
        dest = OUT / out_name
        shutil.copy2(best, dest)
        size_mb = best.stat().st_size / (1024 * 1024)
        print(f"  ✅ {out_name:40s} ({size_mb:.1f} MB)")
        found += 1
    else:
        print(f"  ⚠️  {out_name:40s} NOT FOUND")

print(f"\n  Copied {found}/{len(SCENE_MAP)} videos to website/videos/")

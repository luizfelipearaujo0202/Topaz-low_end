import os
import argparse

from modules.extractor import extract_frames
from modules.analyzer import analyze_frames
from modules.enhancer import enhance_frames
from modules.renderer import render_video

from utils.paths import BASE_DIR, VIDEOS_DIR, FRAMES_DIR, OUTPUT_DIR, ensure_dirs
from utils.video_finder import find_video

ensure_dirs()

parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str, default="run")

args = parser.parse_args()

if args.mode == "train":
    print("Modo treino ativado.")

elif args.mode == "run":
    print("Modo execução ativado.")

VIDEO_PATH = find_video(VIDEOS_DIR)
FRAMES_PATH = "frames"
OUTPUT_PATH = "output/final.mp4"

print("__file__:", __file__)
print("BASE_DIR:", BASE_DIR)
os.chdir("/home/luiz412/Desktop/Treinos/Topaz low_end")
print("CWD:", os.getcwd())


def main():
    print("🔥 iniciando pipeline...")

    # 1. garantir pastas
    os.makedirs(FRAMES_PATH, exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # 2. extrair frames
    print("📥 extraindo frames...")
    frames = extract_frames(VIDEO_PATH, FRAMES_PATH)

    if not frames:
        print("💀 erro: nenhum frame extraído")
        return

    # 3. analisar frames
    print("🧠 analisando frames...")
    metrics = analyze_frames(frames)

    print("📊 métricas:", metrics)

    # 4. melhorar frames
    print("⚙️ melhorando frames...")
    enhanced_frames = enhance_frames(frames, metrics)

    # 5. renderizar vídeo final
    print("🎬 renderizando vídeo...")
    render_video(enhanced_frames, OUTPUT_PATH)

    print("✅ pronto: vídeo salvo em", OUTPUT_PATH)


if __name__ == "__main__":
    main()
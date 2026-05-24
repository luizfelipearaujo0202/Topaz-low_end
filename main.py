import os
from modules.extractor import extract_frames
from modules.analyzer import analyze_frames
from modules.enhancer import enhance_frames
from modules.renderer import render_video


VIDEO_PATH = "videos/input.mp4"
FRAMES_PATH = "frames"
OUTPUT_PATH = "output/final.mp4"


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
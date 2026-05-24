from utils.analyzer import analyze_frames
from utils.frame_extract import extrair_frames

VIDEO_PATH = "video"

for arquivo in VIDEO_PATH:
    if arquivo.endswith(".mp4"):
        extrair_frames(arquivo, "output/frames")
        
resultado = analyze_frames("output/frames")

print(resultado)
from utils.analyzer import analyze_frames
from utils.frame_extract import extrair_frames
from utils.rebuild import rebuild

VIDEO_PATH = "video"

for arquivo in VIDEO_PATH:
    if arquivo.endswith(".mp4"):
        extrair_frames(arquivo, "frames")
        
resultado = analyze_frames("frames")

rebuild("frames")

print(resultado)
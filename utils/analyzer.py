import os
import cv2
import numpy as np

def analyze_frames(frames_path):

    total_blur = 0
    total_brightness = 0
    frame_count = 0

    arquivos = sorted(os.listdir(frames_path))

    for arquivo in arquivos:

        if not arquivo.endswith(".png"):
            continue

        caminho = os.path.join(
            frames_path,
            arquivo
        )

        frame = cv2.imread(caminho)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(gray, cv2.CV_64F).var()

        brightness = np.mean(gray)

        total_blur += blur
        total_brightness += brightness

        frame_count += 1

        print(
            f"[{frame_count}] "
            f"blur={blur:.2f}"
            f"brightness={brightness:.2f}")

    avg_blur = total_blur / frame_count
    avg_brightness = total_brightness / frame_count

    return {
        "blur": avg_blur,
        "brightness": avg_brightness
    }
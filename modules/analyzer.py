import cv2
import numpy as np

def analyze_frames(frames):
    total_blur = 0
    total_brightness = 0

    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.Laplacian(gray, cv2.CV_64F).var()
        brightness = np.mean(gray)

        total_blur += blur
        total_brightness += brightness

    n = len(frames)

    return {
        "blur": total_blur / n,
        "brightness": total_brightness / n
    }

import cv2
import numpy as np

def enhance_frames(frames, metrics):
    enhanced = []

    blur = metrics["blur"]
    brightness = metrics["brightness"]

    # kernel sharpen simples
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    for frame in frames:

        # 🔥 sharpen se estiver borrado
        if blur < 80:
            frame = cv2.filter2D(frame, -1, kernel)

        # 🌫️ denoise leve se imagem ruim
        if blur < 60:
            frame = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)

        # 💡 ajuste simples de brilho
        if brightness < 100:
            frame = cv2.convertScaleAbs(frame, alpha=1.1, beta=10)

        enhanced.append(frame)

    return enhanced

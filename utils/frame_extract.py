import os
import cv2

def extrair_frames(video_path):
    os.makedirs("frames", exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_id = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        nome = os.path.join(
            "frames",
            f"frame_{frame_id:05d}.png"
        )

        cv2.imwrite(nome, frame)

        frame_id += 1

    cap.release()

    return frame_id
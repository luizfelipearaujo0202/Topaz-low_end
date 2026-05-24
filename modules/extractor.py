import cv2
import os

def extract_frames(video_path, frames_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("💀 erro abrindo vídeo")
        return []

    frames = []
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(frames_path, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, frame)

        frames.append(frame)
        count += 1

    cap.release()

    print(f"📦 {count} frames extraídos")
    return frames
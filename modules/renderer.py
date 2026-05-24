
import cv2

def render_video(frames, output_path):
    if not frames:
        print("💀 sem frames pra renderizar")
        return

    height, width, _ = frames[0].shape

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        30,
        (width, height)
    )

    for frame in frames:
        out.write(frame)

    out.release()

    print("🎬 vídeo gerado com sucesso")

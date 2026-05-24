import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VIDEOS_DIR = os.path.join(BASE_DIR, "videos")
FRAMES_DIR = os.path.join(BASE_DIR, "frames")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def ensure_dirs():
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
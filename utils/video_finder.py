import os

VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]

def find_video(video_dir):
    if not os.path.exists(video_dir):
        return None
    
    files = os.listdir(video_dir)
    
    for f in files:
        for ext in VIDEO_EXTENSIONS:
            if f.lower().endswith(ext):
                return os.path.join(video_dir, f)
            
    return None
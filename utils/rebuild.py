import cv2
import os

for frame in os.listdir("frames"):
    height, width, _ = frame.shape
    
    out = cv2.VideoWriter(
        "output.mp4",
        cv2.VIdeoWriter_fourcc(*"mp4v"),
        30,
        (width, height)
        )
    
    out.write(frame)
    
    out.release()
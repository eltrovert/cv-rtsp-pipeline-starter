import os
import time
import cv2

RTSP_URL = os.getenv("RTSP_URL", "")
GST = os.getenv("GST_PIPELINE", "")

if not RTSP_URL and not GST:
    raise SystemExit("Set RTSP_URL or provide GST_PIPELINE")

source = GST if GST else RTSP_URL
cap = cv2.VideoCapture(source, cv2.CAP_GSTREAMER if GST else 0)

if not cap.isOpened():
    raise SystemExit("Failed to open video source")

print("Streaming started. Press Ctrl+C to stop.")
frame_count = 0
try:
    while True:
        ok, frame = cap.read()
        if not ok:
            time.sleep(0.1)
            continue
        frame_count += 1
        if frame_count % 60 == 0:
            h, w = frame.shape[:2]
            print(f"Frames: {frame_count} Size: {w}x{h}")
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    print("Stopped.")

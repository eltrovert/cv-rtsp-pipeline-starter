# CV RTSP Pipeline Starter

Minimal starter to capture frames from an RTSP camera using Python + OpenCV, containerize it, and run on Kubernetes.

## Features
- RTSP input via OpenCV (FFmpeg backend)
- Optional GStreamer pipeline string for lower latency
- Dockerfile (slim) with OpenCV + runtime deps
- Kubernetes Deployment + Service manifest

## Quick start
```bash
export RTSP_URL="rtsp://user:pass@camera-host:554/stream"
python3 app.py
```

## GStreamer pipeline example
```bash
export GST_PIPELINE="rtspsrc location=$RTSP_URL latency=200 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink"
python3 app.py
```

## Docker
```bash
docker build -t ghcr.io/eltrovert/cv-rtsp-pipeline:dev .
docker run --rm -it -e RTSP_URL -e GST_PIPELINE ghcr.io/eltrovert/cv-rtsp-pipeline:dev
```

## Kubernetes
```bash
kubectl apply -f k8s/
```

## Notes
- For Jetson devices, consider GStreamer hardware decoders.
- Ensure ffmpeg build supports your RTSP codecs.

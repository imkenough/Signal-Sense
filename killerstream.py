import cv2
import torch
import warnings
import subprocess
import time

warnings.filterwarnings("ignore", category=FutureWarning)

# Load YOLOv5 model (pretrained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# YouTube live stream URL
youtube_url = 'https://youtu.be/DmSOFIkM5gY'

# Use streamlink to get the direct stream URL
command = ["streamlink", youtube_url, "360p", "--stream-url"]
try:
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)
    stream_url = result.stdout.strip()
    print(f"Stream URL: {stream_url}")
except subprocess.CalledProcessError as e:
    print(f"Error fetching stream URL: {e.stderr}")
    exit(1)

# Open the video stream
cap = cv2.VideoCapture(stream_url)

# Define vehicle-related class IDs
vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck

# skipping frames cus wtf
frame_skip = 5  # Process every 5th frame
frame_count = 0

# Frame processing loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to retrieve frame. Exiting...")
        break

    # Run YOLO inference
    results = model(frame)

    # Get the predictions
    detections = results.pred[0]

    # Filter detections for only vehicle classes
    filtered_detections = detections[torch.isin(
        detections[:, 5], torch.tensor(vehicle_classes))]

    # Draw bounding boxes for filtered detections (vehicles only)
    for *box, conf, cls in filtered_detections:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2),
                      (19, 220, 223), 2)  # Green box
        label = f'{model.names[int(cls)]} {conf:.2f}'
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the frame with vehicle detections
    cv2.imshow('YOLOv5 Vehicle Detection', frame)

    # Add a slight delay to reduce bottlenecks
    time.sleep(0.1)  # 100ms delay

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

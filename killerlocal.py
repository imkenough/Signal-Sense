import cv2
import torch
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# Load YOLOv5 model (pretrained on COCO dataset, which includes cars)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Local video file path
video_path = 'vid\carrs4.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Define vehicle-related class IDs
vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference
    results = model(frame)

    # Get the predictions
    detections = results.pred[0]

    # Filter detections for only vehicle classes
    filtered_detections = detections[torch.isin(
        detections[:, 5], torch.tensor(vehicle_classes))]

    # If you want to visualize the filtered results
    for *box, conf, cls in filtered_detections:
        # Draw bounding box for filtered detections (vehicles only)
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (19, 220, 223),
                      2)  # Green box for vehicles
        label = f'{model.names[int(cls)]} {conf:.2f}'
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the frame with vehicle detections
    cv2.imshow('YOLOv5 Vehicle Detection', frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

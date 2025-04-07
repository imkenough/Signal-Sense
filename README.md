# Signal Sense

This repository showcases a cutting-edge solution that leverages **YOLO (You Only Look Once)** and **OpenCV** to dynamically adjust traffic lights based on real-time vehicle detection at intersections. Designed to reduce congestion and improve traffic flow, this project highlights the practical application of AI in solving urban challenges.

---

## Key Features

- **Real-Time Vehicle Detection**: Utilizes the YOLO model to detect and count vehicles at intersections with high accuracy.
- **Dynamic Traffic Signal Adjustment**: Optimizes traffic light timing based on vehicle density, minimizing wait times.
- **Local Testing and Deployment**:
  - A script to run the model on local video files for easy testing.
  - A framework designed for real-world deployment using live camera feeds.
- **Scalable and Modular Design**: Ready to integrate with city-wide traffic management systems.

---

## Project Structure

```plaintext
├── killerlocal.py        # Script to run the model on local video files
├── killerstream.py       # Script for real-time processing from live camera feeds
├── yolov5/               # YOLOv5 model directory
├── yolov5s.pt            # YOLOv5 small model weights
├── yolov5m.pt            # YOLOv5 medium model weights
├── carrs.mp4             # Example video file
├── carrs2.mp4            # Example video file
├── carrs3.mp4            # Example video file
├── carrs4.mp4            # Example video file
├── chaos.mp4             # Example video file
├── README.md             # You're here! 🎉
└── tempCodeRunnerFile.py # Temporary file for testing
```

---

## 🛠️ How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/traffic-light-optimization.git
cd traffic-light-optimization
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed, then create a `requirements.txt` file with the following content:

```plaintext
opencv-python
opencv-python-headless
torch
torchvision
ultralytics
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Test Locally with Video Files
Run the model on local files to see the detection in action:
```bash
python killerlocal.py
```

### 4. Real-Time Deployment with Live Feeds
For real-world applications, integrate a live camera feed:
```bash
python killerstream.py --camera_url your_camera_feed_url
```

---

## Results and Insights
- **Efficiency**: Achieved significant reductions in average vehicle wait times during simulations.
- **Scalability**: Designed to work seamlessly with multiple intersections in complex urban environments.

---

## Contributions
We welcome contributions to enhance this project! Feel free to:
- Submit pull requests for new features or optimizations.
- Report issues or suggest improvements via the [Issues](https://github.com/yourusername/traffic-light-optimization/issues) tab.

---

## Why This Project?
Traffic congestion is a pressing issue in urban areas, costing billions in lost productivity and increased pollution. This project demonstrates how **AI and computer vision** can tackle such real-world challenges, showcasing your ability to build impactful, scalable solutions.

---

**Let’s revolutionize traffic management together! 🚦**

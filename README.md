---

# 🚧 Construction PPE Detection System  

A **real-time detection system** built with **YOLO (Ultralytics)** to identify Personal Protective Equipment (PPE) on construction sites. The system detects helmets, vests, gloves, boots, and humans in video streams, ensuring compliance with safety protocols.  

---

## 🚀 Features  
- **Real-Time Detection**: Processes video feeds to detect PPE (helmets, vests, gloves, boots) and humans.  
- **YOLO-Powered**: Uses a pre-trained YOLOv8 model (`best.pt`) for high accuracy.  
- **Bounding Box Visualization**: Draws labeled bounding boxes with `cvzone` for clear output.  
- **Multi-Class Detection**: Identifies 5 classes: `helmet`, `vest`, `gloves`, `boots`, and `human`.  

---

## 🛠️ Tech Stack  
- **YOLOv8 (Ultralytics)**: For object detection.  
- **OpenCV (`cv2`)**: Video processing and frame rendering.  
- **CVZone**: Enhanced visualization of bounding boxes.  
- **Python**: Core programming language.  

---

## 📦 Setup Instructions  

### 1. **Clone the Repository**  
```bash
git clone https://github.com/Rahul2201020931/Construction-PPE-Detection.git
cd Construction-PPE-Detection
```

### 2. **Install Dependencies**  
```bash
pip install ultralytics opencv-python cvzone
```

### 3. **Download the YOLO Model**  
Place your pre-trained model (`best.pt`) in the project root or specify its path in the script.  

### 4. **Run the Detection Script**  
```bash
safety_control.py
```
---

## 🌐 Deployment  

You can deploy this PPE detection system as:  

1. **Local Script**: Run directly using Python (as shown above).  
2. **Web App**: Use `Streamlit`/`Flask` to create a browser interface.  
3. **Cloud**: Deploy on **Hugging Face Spaces**, **Render**, or **AWS Lambda**.  

### 🚀 Try the Live Demo  
> 🔗 [![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Rahul9898/Construction-PPE-Detection)   

---

### **How to Deploy on Hugging Face Spaces**  
1. Create a `app.py` with Streamlit (example below).  
2. Upload `app.py`, `best.pt`, and `requirements.txt` to a new Hugging Face Space.  

#### Example `app.py` for Streamlit:  
```python
import streamlit as st
from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
st.title("PPE Detection")

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])
if uploaded_file:
    st.video(uploaded_file)
    cap = cv2.VideoCapture(uploaded_file.name)
    # Add YOLO detection logic here
    st.success("Detection Complete!")
```

---

Now your README has a clear **Deployment** section with a placeholder for the live link. Just replace it once deployed! 🎉  

Let me know if you need help with deployment scripts!

---

## 🧠 Model Details  
- **Model**: Custom YOLOv8 (`best.pt`).  
- **Classes**: `helmet`, `vest`, `gloves`, `boots`, `human`.  
- **Input Resolution**: Adjustable (default: 640x640).  

---

## 📂 Project Structure  
```
Construction-PPE-Detection/
├── detect_ppe.py          # Main detection script
├── best.pt                # YOLO model weights
├── README.md              # Project documentation
├── requirements.txt       # Dependencies list
└── test_videos/           # Sample videos for testing
    └── ppe-3-1.mp4        
```

---

## 🤝 How to Contribute  
1. Fork the repository.  
2. Add improvements (e.g., better model, UI integration with Streamlit).  
3. Submit a pull request!  

---

## 📜 License  
MIT © [Rahul Kumar Gupta](https://github.com/Rahul2201020931)  

---

## 🙌 Author  
**Rahul Kumar Gupta**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/Rahul2201020931)  

---

### 🔗 Links  
- [Ultralytics YOLO Docs](https://docs.ultralytics.com)  
- [CVZone GitHub](https://github.com/cvzone/cvzone)  

---

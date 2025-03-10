from ultralytics import YOLO
import cv2
import cvzone

# Load the YOLO model
model = YOLO(r"C:\Users\rg967\OneDrive\Desktop\best.pt")

# Define class names
classname = ['boots', 'gloves', 'helmet', 'human', 'vest']

# Open the video file
video_path = r"C:\ml1\yolo_projects\images\ppe-3-1.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file. Check the path.")
    exit()

# Process video frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends

    # Run YOLO detection on the frame
    results = model(frame)

    # Process detection results
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # Convert tensor to list
            w, h = x2 - x1, y2 - y1

            # Draw bounding box with cvzone
            cvzone.cornerRect(frame, (x1, y1, w, h), l=15, t=2)

    # Display the output frame
    cv2.imshow("YOLO Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

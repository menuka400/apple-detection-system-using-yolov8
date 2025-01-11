import cv2
from ultralytics import YOLO

def detect_weapons_from_camera():
    yolo_model = YOLO('C:\\Users\\menuk\\Desktop\\Human_model_v2\\train\\weights\\best.pt')

    # Open the default camera (usually the first one)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Failed to capture frame from the camera.")
            break

        # Detect objects in the frame
        results = yolo_model(frame)

        for result in results:
            classes = result.names
            cls = result.boxes.cls
            conf = result.boxes.conf
            detections = result.boxes.xyxy

            for pos, detection in enumerate(detections):
                if conf[pos] >= 0.5:
                    xmin, ymin, xmax, ymax = detection
                    label = f"{classes[int(cls[pos])]} {conf[pos]:.2f}"
                    color = (0, int(cls[pos]), 255)
                    cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, 2)
                    cv2.putText(frame, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Weapon Detection', frame)

        # Check if the user pressed 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Call the function to start weapon detection from the camera
detect_weapons_from_camera()
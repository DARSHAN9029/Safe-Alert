import cv2
import numpy as np
from tensorflow.keras.models import load_model
import requests

model_path = r"C:\Users\PINKY\OneDrive\Desktop\acc_det\accident_detection_model.h5"
model = load_model(model_path)

API_URL = "http://127.0.0.1:5000/send-alert"

def detection_acc():
    cap = cv2.VideoCapture(0)

    frame_count = 0
    accident_frames = 0

    text = "Processing...."
    color = (255, 255, 255)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (64, 64))                     # Resize & Normalize
        reshaped_frame = np.expand_dims(resized_frame, axis=0) / 255.0

        prediction = model.predict(reshaped_frame)[0][0]                    # Predict Accident
        print(f"Prediction score: {prediction}")

        frame_count += 1
        if prediction > 0.7:                                        # Prediction
            accident_frames += 1

        if frame_count >= 10:
            if accident_frames >= 5:
                text = "ACCIDENT DETECTED"
                color = (0, 0, 255)                         # red

                try:
                    response = requests.get(API_URL)                        # Call the API
                    print(f"API Response: {response.json()}")
                except Exception as e:
                    print(f"Error sending alert: {e}")
            else:
                text = "No Accident detected"
                color = (0, 255, 0)                                     # green

            frame_count = 0
            accident_frames = 0

        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow("Accident Detection", frame)

        if cv2.waitKey(25) & 0xFF == ord('x'):                  # Press 'x' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

detection_acc()

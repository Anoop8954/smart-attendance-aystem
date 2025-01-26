import cv2
import numpy as np
import os
from datetime import datetime

# Load pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to capture and store face data
def capture_face_data(name, roll_no):
    cam = cv2.VideoCapture(0)
    face_data = []
    while len(face_data) < 10:
        ret, frame = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_data.append(gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Capture Face Data", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    return np.mean(face_data, axis=0)

# Function for face recognition
def recognize_face(known_faces):
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            face_resized = cv2.resize(face, (100, 100))
            matched = False
            for user_id, known_face in known_faces.items():
                if np.mean((known_face - face_resized) ** 2) < 1000:
                    print(f"Attendance marked for User ID: {user_id}")
                    matched = True
                    break
            if not matched:
                print("Unknown face detected.")
        cv2.imshow("Recognize Face", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

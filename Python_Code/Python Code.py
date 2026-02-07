import cv2
import mediapipe as mp
import time
import numpy as np
import serial

# Establishing connection with Arduino
try:
    arduino = serial.Serial('COM7', 9600)
    time.sleep(2)
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    arduino = None

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

# Eye landmarks (Right and Left)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Calculation of  Euclidean distance
def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# EAR calculation
def calculate_ear(eye_points):
    # Vertical distances
    A = euclidean(eye_points[1], eye_points[5])
    B = euclidean(eye_points[2], eye_points[4])
    # Horizontal distance
    C = euclidean(eye_points[0], eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Thresholds limit, should be changed according to the size of the eyes
EAR_THRESHOLD = 0.30
CLOSED_EYES_DURATION = 2  # seconds of delay

# Initialize
cap = cv2.VideoCapture(0)
closed_eyes_start = None
alarm_triggered = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    h, w, _ = frame.shape
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Gets the coordinates of the landmarks
        left_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in LEFT_EYE]
        right_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in RIGHT_EYE]

        # Calculate EAR for both the eyes
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        # Display "JSCONNECT" text
        cv2.putText(frame, 'JSCONNECT', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

        # Display the value of EAR
        cv2.putText(frame, f'EAR Value: {avg_ear:.2f}', (30, 65), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)


        current_time = time.time()

        if avg_ear < EAR_THRESHOLD:
            if closed_eyes_start is None:
                closed_eyes_start = current_time
            elif current_time - closed_eyes_start >= CLOSED_EYES_DURATION:
                if not alarm_triggered:
                    print("Drowsiness Detected!")
                    if arduino:
                        arduino.write(b'A')
                    alarm_triggered = True
        else:
            closed_eyes_start = None
            if alarm_triggered:
                print("Driver Awake")
                if arduino:
                    arduino.write(b'R')
                alarm_triggered = False

        # Draw the eye landmarks
        for point in left_eye + right_eye:
            cv2.circle(frame, point, 2, (255, 0, 0), -1)

    cv2.imshow("Driver Drowsiness Detection Model by Md Jahin Sabur", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()

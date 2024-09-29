import cv2
import numpy as np

def estimate_gaze(eye_region, threshold=80):
    # Applying a binary threshold to find the darkest parts, typically the pupil
    _, thresh = cv2.threshold(eye_region, threshold, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            return (cx, cy), True
    return (0, 0), False

# Initialize the webcam
cap = cv2.VideoCapture(1)  # Adjust the index if necessary

# Load the pre-trained Haar Cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    for (ex, ey, ew, eh) in eyes:
        eye = gray[ey:ey+eh, ex:ex+ew]
        gaze_point, found = estimate_gaze(eye)
        if found:
            cv2.circle(frame, (ex + gaze_point[0], ey + gaze_point[1]), 2, (0, 255, 0), 2)
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    cv2.imshow('Gaze Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

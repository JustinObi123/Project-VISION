import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize video capture and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(
    refine_landmarks=True, 
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Get screen dimensions
screen_w, screen_h = pyautogui.size()

# Initialize variables for eye closure tracking
eye_closed_time = None
button_pressed = False
EYE_CLOSED_DURATION = 0.2  # Reduced to 0.2 seconds for quicker response
EYE_CLOSED_THRESHOLD_VALUE = 0.01  # Adjust based on your calibration

# Function to calculate Eye Aspect Ratio (EAR) for more robust detection
def calculate_EAR(upper, lower):
    return lower.y - upper.y

# Define left iris landmarks (using top and bottom points)
LEFT_IRIS_TOP = 476
LEFT_IRIS_BOTTOM = 477

# Main loop
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Track only the left iris top and bottom landmarks
        left_iris_landmarks = [LEFT_IRIS_TOP, LEFT_IRIS_BOTTOM]
        for idx, landmark_id in enumerate(left_iris_landmarks):
            landmark = landmarks[landmark_id]
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)  # Green dots for tracking

            # Use the top iris landmark to control the mouse
            if landmark_id == LEFT_IRIS_TOP:
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y, duration=0.01)  # Smooth mouse movement

        # Get landmarks for the left eye for closure detection
        left_upper = landmarks[159]
        left_lower = landmarks[145]
        eye_distance = calculate_EAR(left_upper, left_lower)

        # Draw eye landmarks
        upper_x = int(left_upper.x * frame_w)
        upper_y = int(left_upper.y * frame_h)
        lower_x = int(left_lower.x * frame_w)
        lower_y = int(left_lower.y * frame_h)
        cv2.circle(frame, (upper_x, upper_y), 3, (0, 255, 255), -1)  # Yellow dots
        cv2.circle(frame, (lower_x, lower_y), 3, (0, 255, 255), -1)  # Yellow dots

        # Display eye distance for debugging
        cv2.putText(frame, f'Eye distance: {eye_distance:.4f}', (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # Check if the eye is closed based on landmark positions
        if eye_distance < EYE_CLOSED_THRESHOLD_VALUE:
            if eye_closed_time is None:
                eye_closed_time = time.time()
                print("Eye closed detected, starting timer.")
            else:
                elapsed = time.time() - eye_closed_time
                cv2.putText(frame, f'Closed for: {elapsed:.2f}s', (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if elapsed >= EYE_CLOSED_DURATION and not button_pressed:
                    pyautogui.mouseDown(button='left')  # Press and hold the left mouse button
                    button_pressed = True
                    print("Mouse button pressed down.")
        else:
            if eye_closed_time is not None:
                print("Eye opened, resetting timer.")
            eye_closed_time = None
            if button_pressed:
                pyautogui.mouseUp(button='left')  # Release the mouse button
                button_pressed = False
                print("Mouse button released.")

    # Display the frame
    cv2.imshow('Eye Controlled Mouse', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release resources
cam.release()
cv2.destroyAllWindows()

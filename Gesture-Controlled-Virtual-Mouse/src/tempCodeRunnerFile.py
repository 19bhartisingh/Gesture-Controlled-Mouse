import cv2
import mediapipe as mp

class HandGestureController:
    def __init__(self):
        self.prev_hand = None  # To store the previous gesture

    def handle_controls(self, gesture_name, hand_result):
        if gesture_name:
            print(f"Gesture recognized: {gesture_name}")
            # Implement control logic based on the gesture name
            if gesture_name == "thumbs_up":
                print("Action: Move up")
            elif gesture_name == "fist":
                print("Action: Stop")
            # Add additional gesture actions as required

# Initialize MediaPipe hand solutions and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize the controller
Controller = HandGestureController()

# Start capturing video
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image for a selfie-view display
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and detect hands
        results = hands.process(image_rgb)

        # If hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Determine the gesture name based on landmarks (gesture detection logic)
                gesture_name = "some_detected_gesture"  # Replace with actual detection method
                Controller.handle_controls(gesture_name, hand_landmarks)

                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        else:
            Controller.prev_hand = None

        # Display the image
        cv2.imshow('Gesture Controller', image)

        # Exit when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
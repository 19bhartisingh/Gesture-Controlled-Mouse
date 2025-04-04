# Gesture-Controlled-Mouse
This project is a Gesture Controlled Virtual Mouse that uses your hand gestures to control the cursor, click, and perform basic operations—no physical mouse needed! It leverages computer vision and hand-tracking technology using OpenCV and MediaPipe.

# ✨ Features
Move the cursor with hand movements
Left click using finger gestures
Right click and double click support
Scroll functionality
Real-time hand tracking using webcam
Smooth and responsive interaction

# 🛠️ Technologies Used
Python
OpenCV
MediaPipe
PyAutoGUI
NumPy

# 📷 How It Works
The webcam captures real-time video.
MediaPipe detects and tracks your hand landmarks.
Specific finger combinations are mapped to mouse actions:
Index finger only: Move cursor
Index + Middle finger together: Click actions
Thumb + other fingers: Custom gestures like scroll
PyAutoGUI is used to simulate actual mouse movements and clicks.

# 📌 Use Cases
Hands-free interaction
Accessibility tool for people with disabilities
Contactless computer control
Cool AI-vision based mini project or portfolio item

# 💡 Future Improvements
Add custom gesture training
Multi-hand gesture control
GUI-based toggle features

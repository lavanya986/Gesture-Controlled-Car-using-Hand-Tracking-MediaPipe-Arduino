Gesture Controlled Car using Hand Tracking (MediaPipe) + Arduino
A simple AI-powered car that moves forward, backward, left, right, or stops based on hand gestures detected through a webcam using MediaPipe. Commands are sent to Arduino via serial communication to control motors.

🚗 Features
Real-time hand gesture recognition using MediaPipe
Serial communication between Python and Arduino
Controls car direction using DC motors via L298N Motor Driver
Touchless and intuitive control system
🧰 Technologies Used
Python (MediaPipe, OpenCV, PySerial)
Arduino UNO
L298N Motor Driver
DC Motors
MediaPipe Hand Tracking
OpenCV for camera input
PySerial for serial communication
📁 Project Structure
gesture-controlled-car/ ├── arduino/ │ └── gesture_car.ino ├── python/ │ └── gesture_control.py └── README.md

🔌 Circuit Connections
IN1 -> Arduino pin 8
IN2 -> Arduino pin 9
IN3 -> Arduino pin 10
IN4 -> Arduino pin 11
ENA & ENB connected to 5V
Motor A/B connected to L298N
Power supply to L298N and Arduino
See /images/circuit_diagram.png if you include an image.

✋ Gesture Mapping
Fingers Shown	Action	Command Sent
1 Finger	Forward	F
2 Fingers	Backward	B
3 Fingers	Turn Left	L
4 Fingers	Turn Right	R
5 Fingers	Stop	S
🛠 How to Run
1. Arduino Setup
Open gesture_car.ino in Arduino IDE
Select your COM port and board (e.g., Arduino UNO)
Upload the code
2. Python Setup
Install dependencies:

pip install opencv-python mediapipe pyserial

Run:

python gesture_control.py 

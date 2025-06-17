import cv2
import mediapipe as mp
import serial
import time

# Serial Communication with Arduino
ser = serial.Serial('COM3', 9600)  # Change COM port as per your system
time.sleep(2)  # Wait for Arduino to reset

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []

    # For thumb (check x-coordinates instead of y)
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # For other 4 fingers (index to pinky)
    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

def get_command(finger_count):
    if finger_count == 1:
        return 'F'  # Forward
    elif finger_count == 2:
        return 'B'  # Backward
    elif finger_count == 3:
        return 'L'  # Left
    elif finger_count == 4:
        return 'R'  # Right
    elif finger_count == 5:
        return 'S'  # Stop
    else:
        return 'S'  # Default to Stop

try:
    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                finger_count = count_fingers(hand_landmarks)
                cmd = get_command(finger_count)

                ser.write(cmd.encode())
                cv2.putText(frame, f'Fingers: {finger_count}  Command: {cmd}', (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    ser.close()
    cv2.destroyAllWindows()

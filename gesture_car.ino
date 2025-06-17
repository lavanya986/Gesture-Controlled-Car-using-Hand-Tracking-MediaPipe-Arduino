char command;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);  // Left motor IN1
  pinMode(9, OUTPUT);  // Left motor IN2
  pinMode(10, OUTPUT); // Right motor IN3
  pinMode(11, OUTPUT); // Right motor IN4
}

void loop() {
  if (Serial.available() > 0) {

    command = Serial.read();

    if (command == 'F') {
      // Forward
      digitalWrite(8, HIGH); digitalWrite(9, LOW);
      digitalWrite(10, HIGH); digitalWrite(11, LOW);
    } else if (command == 'B') {
      // Backward
      digitalWrite(8, LOW); digitalWrite(9, HIGH);
      digitalWrite(10, LOW); digitalWrite(11, HIGH);
    } else if (command == 'L') {
      // Turn Left
      digitalWrite(8, LOW); digitalWrite(9, HIGH);
      digitalWrite(10, HIGH); digitalWrite(11, LOW);
    } else if (command == 'R') {
      // Turn Right
      digitalWrite(8, HIGH); digitalWrite(9, LOW);
      digitalWrite(10, LOW); digitalWrite(11, HIGH);
    } else if (command == 'S') {
      // Stop
      digitalWrite(8, LOW); digitalWrite(9, LOW);
      digitalWrite(10, LOW); digitalWrite(11, LOW);
    }
  }
}

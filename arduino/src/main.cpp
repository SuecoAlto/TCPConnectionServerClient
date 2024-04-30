// Include any libraries needed
#include <Arduino.h>
#include <Servo.h>

// Define pin numbers and other constants
const int LED_GREEN = 6;
const int LED_BLUE = 7;
const int SERVO_PIN = 8;

Servo myServo; // Creates a Servo object that allows you to control a servo motor.

// Initialization code in setup()
void setup() {
  // Set pin modes
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  myServo.attach(SERVO_PIN); // Attaches the servo motor to the pin defined by SERVO_PIN.

  // Start serial communication if needed
  Serial.begin(9600); // Initializes serial communication at 9600 bits per second.
}


// Main code in loop()
void loop() {
  if (Serial.available()) {// Checks if there is any incoming data on the serial port.
    String command = Serial.readStringUntil('\n');
    Serial.print("Full command receiced: ");
    Serial.println(command);
    handleCommand(command); // Calls the handleCommand function with the received command string.
  }


// Additional functionality can be added here
void handleCommand(String command) {
  if (command.startsWith("green-on")) {
    digitalWrite(LED_GREEN, HIGH);
    Serial.println("GREEN LED ON");
  } 
  else if (command.startsWith("blue-on")) {
    digitalWrite(LED_BLUE, HIGH);
    Serial.println("BLUE LED ON")
  }
  else if (command.startsWith("green-off")) {
    digitalWrite(LED_GREEN, LOW);
    Serial.println("GREEN LED OFF");
  } 
  else if (command.startsWith("blue-off")) {
    digitalWrite(LED_BLUE, LOW);
    Serial.println("BLUE LED OFF");
  } 
  else if (command.startsWith("servo-")) {
    int pos = command.substring(6).toInt();
    myServo.write(pos);
    Serial.print("SERVO POSITION SET TO: ");
    Serial.println(pos);
  } 
  else {
    Serial.println("INVALID COMMAND RECEIVED");
  }
}


}
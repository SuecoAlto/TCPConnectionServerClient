// Include any libraries needed
#include <Arduino.h>
#include <Servo.h>

// Define pin numbers and other constants
const int LED_GREEN = 6;
const int LED_BLUE = 7;
const int SERVO_PIN = 8;

Servo myServo;               // Creates a Servo object that allows you to control a servo motor.

// Initialization code in setup()
void setup() {
  // Set pin modes
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  myServo.attach(SERVO_PIN); // Attaches the servo motor to the pin defined by SERVO_PIN.

  // Start serial communication if needed
  Serial.begin(9600);        // Initializes serial communication at 9600 bits per second.
}


// Main code in loop()
void loop() {
  if (Serial.available()) {  // Checks if there is any incoming data on the serial port.
    String command = Serial.readStringUntil('\n');
    Serial.print("Full command receiced: ");
    Serial.println(command);
    proccesCommand(command);
  }
}

// Split the command string and delegate to the appropriate function
void processCommand(String command) {
  int firstDash = command.indexOf('-'); // Find the position of the first dash '-' in the command string.
  if (firstDash == -1) {                // Check if the dash was not found.
    Serial.println("ERROR: Invalid commnd format.");
    return;
  }
}

String device = command.substring(0, firstDash);  // Extract the device part of the command (before the dash).
String action = command.substring(firstDash + 1); // Extract the action part of the command (after the dash).

  // Determine the type of device from the command and call the appropriate handler.
  if (device == "LED") {
    handleLEDCommand(action);   // Handle LED commands.
  } 
  else if (device == "servo") {
    handleServoCommand(action); // Handle servo commands.
  } 
  else {
    Serial.println("ERROR: Unknown device specified.");
  }


// Define the function to handle LED-related commands.
void handelLEDCommand(String action) {
int pin;                             // Declare a variable to store the pin number associated with the LED.
if (action.startsWith("green")) {     
  pin = LED_GREEN;                   // Assign the pin number for the green LED.
  prtcolor = print(f"GREEN")
  }
else if (action.startsWith("blue")) {
  pin = LED_BLUE;                    // Assign the pin number for the blue LED.
  prtcolor = print(f"BLUE")
  }
else {
  Serial.println("ERROR: Unknown LED color specified.");
return;
}
// Perform the action specified for the LED.
  if (action.endsWith("on")) {
    digitalWrite(pin, HIGH);
    Serial.println({prtcolor} + "LED ON");
  } 
  else if (action.endsWith("off")) {
    digitalWrite(pin, LOW);
    Serial.println({prtcolor} + "LED OFF")
  }
  else {
    Serial.println("ERROR: Unknown action specified for LED.");
  }
}


// Define the function to handle servo-related commands.
void handleServoCommand(String position) {
  if (position.toInt() < 0 || position.toInt() > 180) { // Convert position string to integer and check if it is within the valid range.
    Serial.println("ERROR: Servo position out of range (0-180).");
    return;
  }
  myServo.write(position.toInt());   // Set the servo to the specified position.
  Serial.print("SERVO POSITION SET TO: ");
  Serial.println(position);
}

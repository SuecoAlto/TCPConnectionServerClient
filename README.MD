# TCPServer-ArduinoRaspberryPi

## Overview
This project establishes a TCP connection between a Raspberry Pi server and an Arduino device. The Raspberry Pi acts as a bridge, facilitating communication between the Arduino and client machines over a network. This setup allows clients to send commands to the Arduino, which performs various functions based on these instructions.

## System Configuration
### Arduino (Serially Connected Device)
The Arduino is equipped with sensors and actuators to process both digital and analog signals. It features two LEDs (blue and green) and a SpringRC SM-S2309S Micro Analog Servo. The Arduino's firmware is responsible for:
- Managing the serial connection to the server securely and reliably.
- Executing commands received from clients through the server, such as toggling LEDs and controlling the servo.

### Raspberry Pi (Server)
The Raspberry Pi serves as the central server, managing connections from client machines. It handles:
- Establishing and maintaining a secure and reliable connection to the Arduino.
- Routing commands from clients to the Arduino.

### Local Machine (Client)
The client software on the local machine:
- Connects to the Raspberry Pi server.
- Sends commands securely and reliably, with payloads specifying actions for the Arduino to execute.

## Hardware Setup
- **LEDs**: Connect the green LED to pin designated as '6' and the blue LED to pin '7' on the Arduino.
- **Servo**: Attach the servo's control wire to the pin marked '8'.
- **Serial Connection**: Ensure the Arduino is connected to the Raspberry Pi via a USB cable for serial communication.

## Installation
To get started with this project, clone this repository to both your Raspberry Pi and the local machine. Follow the hardware setup instructions above to connect your Arduino appropriately. You should also send the main.cpp to be installed in the Arduino. 

## Usage
The system listens for specific commands sent from the client to the server, which are then forwarded to the Arduino. Commands should be sent in plain text followed by a newline character. Here are some examples of valid commands:
- `"LED_GREEN_ON"` - Turns the green LED on.
- `"LED_BLUE_OFF"` - Turns the blue LED off.
- `"SERVO 90"` - Moves the servo to 90 degrees.

Ensure your client implementation appends a newline character to each command for correct processing by the Arduino's serial interface.

## Code Overview
The provided Arduino code initializes the specified pins for output and attaches the servo. It listens for incoming serial commands and will include functionality to parse and execute these commands.


```cpp
// Include necessary libraries
#include <Arduino.h>
#include <Servo.h>

// Define pin numbers
const int LED_GREEN = 'g';
const int LED_BLUE = 'b';
const int SERVO_PIN = 's';

Servo myServo;

void setup() {
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  myServo.attach(SERVO_PIN);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    handleCommand(command);
  }
}

void handleCommand(String command) {
  // Command parsing logic will be implemented here
}
```


## Troubleshooting
- **LEDs Not Lighting Up**: Check if the LEDs are correctly connected to their respective pins and that they are functional.
- **Servo Not Responding**: Ensure that the servo is powered and connected to the correct pin. Also, check for any signs of mechanical jamming or electrical issues.

## References
- SpringRC SM-S2309S - Micro Analog Servo: [ServoDatabase](https://servodatabase.com/servo/springrc/sm-s2309s)
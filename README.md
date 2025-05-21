# MQTT Python Experiment
This is an experimental implementation of temperature sharing through the MQTT protocol in Python, using the paho-mqtt library.

----
## ❓ What is MQTT?
MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for constrained devices and low-bandwidth, high-latency or unreliable networks. It is ideal for IoT applications where data needs to be transmitted reliably and efficiently.
It uses a publish-subscribe model, where publishers send messages to a broker, and subscribers receive messages from the broker.

## Requirements
- Python 3.12 or higher
- poetry for dependency management
- an Arduino Uno or similar microcontroller with a temperature sensor
- an MQTT broker (e.g., Mosquitto (self-hosted), mqtt.eclipseprojects.io)

## 📚 How to Use
1. Connect your Arduino to your computer using a USB cable.
2. Ensure your Arduino is properly configured.
    - Set it up to communicate through Serial.setup() with a baud rate of 9600
    - Write a program that reads the temperature from the sensor and prints it to the serial connection, using Serial.println(temperature).
    - Upload the program to your Arduino.
3. Install the necessary libraries and dependencies using poetry.
4. Run the `index.py` script to start reading data from the Arduino and publishing it to the MQTT broker.
5. Subscribe to the MQTT topic to receive temperature updates, through a separate script or application.

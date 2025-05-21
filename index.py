import serial
import paho.mqtt.client as mqtt

# Initialize serial connection to Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)

# Initialize MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("mqtt.eclipseprojects.io", 1883, 60) #@users: This is merely an example, using a publicly available MQTT broker.
client.loop_start()

while True:
    temperature = arduino.readline()
    print("Temperature: " + temperature.decode('utf-8') + " °C")

    #@users: This schema shows the institution and room, in which the temperature was recorded, while writing this.
    #@users: Feel free to change it to something more fitting for your use-case.
    client.publish("institution/bwv-ahaus/room/A060/temperature", temperature.decode('utf-8'))

client.loop_stop()

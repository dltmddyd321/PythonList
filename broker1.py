import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(rc)
    if rc == 0:
        print("계정 서버 연결")

        client.subscribe("shingu/#")

def on_message(client, userdata, msg) :
    print(msg.topic + ": " + msg.payload.decode('utf-8'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_start()
while True:
    message = input(">")
    client.publish("shingu/2017132073", message, 1)
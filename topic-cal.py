import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("계산기 서비스 접속!")

        client.subscribe("shingu/calc/#")

def on_message(client, userdata, msg) :
    print("계산 결과 : " +msg.topic + "->" + msg.payload.decode('utf-8'))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_start()
while True:
    first = int(input("1 : "))
    second = int(input("2 : "))
    client.publish("shingu/calc/2017132073", first+second, 1)
client.loop_stop()
import random

from paho.mqtt import client as mqtt_client


index = 0
index2 = 0
broker = 'broker.emqx.io'
port = 1883
topic = "STOCK/ALERT"
# generate client ID with pub prefix randomly
client_id = [
    f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}']
username = ['kuvalsub1', 'kuvalsub2', 'kuvalsub3', 'kuvalsub4', 'kuvalsub5']
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("\n\nCONNECTED TO MQTT BROKER")
        else:
            print("FAILED TO CONNECT\nRETURN CODE %d\n", rc)

    global index
    client = mqtt_client.Client(client_id[index])
    client.username_pw_set(username[index], password)
    client.on_connect = on_connect
    client.connect(broker, port)
    index += 1
    return client


def subscribe(client: mqtt_client):
    global index2

    def on_message(client, userdata, msg):
        print(f"SUBSCRIBER {(index2)}")
        print(f"RECEIVED `{msg.payload.decode()}` FROM `{msg.topic}` TOPIC")
    index2 += 1
    client.subscribe(topic)
    client.on_message = on_message


def run():
    # subscriber authentication
    user1 = input("\n\nSUBSCRIBER 1\nENTER THE USERNAME: ")
    pass1 = input("ENTER THE PASSWORD: ")
    if(user1 == username[0] and pass1 == password):
        client1 = connect_mqtt()
        subscribe(client1)
        client1.loop_forever()
    else:
        print(
            f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user1}\nPASSWORD: {pass1}")

    user2 = input("\nSUBSCRIBER 2\nENTER THE USERNAME: ")
    pass2 = input("ENTER THE PASSWORD: ")
    if(user2 == username[1] and pass2 == password):
        client2 = connect_mqtt()
        subscribe(client2)
        client2.loop_forever()
    else:
        print(
            f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user2}\nPASSWORD: {pass2}")

    user3 = input("\nSUBSCRIBER 3\nENTER THE USERNAME: ")
    pass3 = input("ENTER THE PASSWORD: ")
    if(user3 == username[2] and pass3 == password):
        client3 = connect_mqtt()
        subscribe(client3)
        client3.loop_forever()
    else:
        print(
            f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user3}\nPASSWORD: {pass3}")

    user4 = input("\nSUBSCRIBER 4\nENTER THE USERNAME: ")
    pass4 = input("ENTER THE PASSWORD: ")
    if(user4 == username[3] and pass4 == password):
        client4 = connect_mqtt()
        subscribe(client4)
        client4.loop_forever()
    else:
        print(
            f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user4}\nPASSWORD: {pass4}")

    user5 = input("\nSUBSCRIBER 5\nENTER THE USERNAME: ")
    pass5 = input("ENTER THE PASSWORD: ")
    if(user5 == username[4] and pass5 == password):
        client5 = connect_mqtt()
        subscribe(client5)
        client5.loop_forever()
    else:
        print(
            f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user5}\nPASSWORD: {pass5}")


if __name__ == '__main__':
    run()

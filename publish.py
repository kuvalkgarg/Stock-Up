import random
import time

from paho.mqtt import client as mqtt_client

import pandas as pd  # data manipulation and analysis package
# enables data pull from Alpha Vantage
from alpha_vantage.timeseries import TimeSeries


index = 0
broker = 'broker.emqx.io'
port = 1883
topic = "STOCK/ALERT"
# generate client ID with pub prefix randomly
client_id = [
    f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}', f'python-mqtt-{random.randint(0, 1000)}']
# list containing usernames and passwords to create separate threads
username = ['kuvalsub1', 'kuvalsub2', 'kuvalsub3', 'kuvalsub4', 'kuvalsub5']
password = 'public'
pusername = ['kuvalpub1']


def connect_mqtt():
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


def publish(client):
    msg_count = 1
    while msg_count != 4:
        time.sleep(1)
        msg = "THE STOCK IS AT A PRICE ABOVE WHAT YOU SET " + \
            "%.6f" % last_price  # The message you want to send
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        # Set the desired message you want to see once the stock price is at a certain level
        target_sell_price = 5  # enter the price you want to sell at
        if status == 0 and last_price > target_sell_price:
            print(f"SUBSCRIBER {(index)}")
            print(f"SEND `{msg}` TO TOPIC `{topic}`")
        else:
            print(f"FAILED TO SEND MESSAGE TO TOPIC {topic}")
        msg_count += 1


def run():
    client1 = connect_mqtt()
    client1.loop_start()
    publish(client1)

    client2 = connect_mqtt()
    client2.loop_start()
    publish(client2)

    client3 = connect_mqtt()
    client3.loop_start()
    publish(client3)

    client4 = connect_mqtt()
    client4.loop_start()
    publish(client4)

    client5 = connect_mqtt()
    client5.loop_start()
    publish(client5)


if __name__ == '__main__':
    ts = TimeSeries(key='H7NT63K7PAJL90BY', output_format='pandas')
    data, meta_data = ts.get_intraday(
        symbol='MSFT', interval='1min', outputsize='full')
    # We are currently interested in the latest price
    close_data = data['4. close']  # The close data column
    # Selecting the last price from the close_data column
    last_price = close_data[0]

    i = 1
    # publisher authentication with 3 allowed login attempts
    while(i < 4):
        user = input("\n\nPUBLISHER 1\nENTER THE USERNAME: ")
        passw = input("ENTER THE PASSWORD: ")
        if(user == pusername[0] and passw == password):
            i = 4
            run()
        else:
            print(
                f"INVALID USERNAME / PASSWORD\nYOU ENTERED\nUSERNAME: {user}\nPASSWORD: {passw}")
        i += 1
    if(i == 4):
        print("\n\nTOO MANY INCORRECT LOGIN ATTEMPTS\n\n")

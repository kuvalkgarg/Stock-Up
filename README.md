# StockUp
Real-Time Stock Price Alert System and MQTT Subscriber. This project combines two components: Real-Time Stock Price Alert System and MQTT Subscriber. The Real-Time Stock Price Alert System retrieves real-time stock prices using the Alpha Vantage API and publishes alerts to an MQTT broker when the stock prices exceed a predetermined threshold. The MQTT Subscriber component connects to the MQTT broker, authenticates users, and subscribes to the topic for receiving stock price alerts. These components work together to provide real-time stock monitoring and alert functionality.

Languages and Frameworks/Libraries
The project is implemented in **Python**. It utilizes the following libraries:

1. For Real-Time Stock Price Alert System:
    * **paho.mqtt.client:** Used for MQTT communication with the broker and publishing messages.
    * **pandas:** Used for data manipulation and analysis.
    * **alpha_vantage.timeseries:** Used for retrieving real-time stock price data from the Alpha Vantage API.

2. For MQTT Subscriber:
* **paho.mqtt.client:** Used for MQTT communication with the broker and subscribing to topics.

# Installation and Execution
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.0 or above).
3. Install the required dependencies:
4. For Real-Time Stock Price Alert System: Install the pandas and alpha_vantage libraries by running the following command:
```
pip install pandas alpha_vantage
```

# Configuration
* For MQTT Subscriber: No additional dependencies required.
  - Open a terminal or command prompt and navigate to the project directory.
* For Real-Time Stock Price Alert System:
  - Open the publish.py script file.
  - Update the following variables as per your requirements:
      * **broker:** The MQTT broker address (e.g., 'broker.emqx.io').
      * **port:** The MQTT broker port (e.g., 1883).
      * **topic:** The topic to publish stock price alerts.
      * **username:** Update the list of usernames for authentication.
      * **password:** Set the password for authentication.
      * **client_id:** Generate unique client IDs for each publisher.
      * **pusername:** Set the publisher's username.
      * **last_price:** Set the initial last price of the stock.
  - Save the changes to the script file.
  - Run the Python script by executing the following command:
  ```
  python publish.py
  ```

* For MQTT Subscriber:
  - Open the subscribe.py script file.

  - Update the following variables as per your requirements:
      * **broker:** The MQTT broker address (e.g., 'broker.emqx.io').
      * **port:** The MQTT broker port (e.g., 1883).
      * **topic:** The topic to subscribe for stock price alerts.
      * **username:** Update the list of usernames for authentication.
      * **password:** Set the password for authentication.
      * **client_id:** Generate unique client IDs for each subscriber.
  - Save the changes to the script file.
  - Run the Python script by executing the following command:
  ```
  python subscribe.py
  ```

# Conclusion
This project integrates the Real-Time Stock Price Alert System and MQTT Subscriber components to provide real-time stock monitoring and alert functionality. The Real-Time Stock Price Alert System retrieves stock prices from the Alpha Vantage API and publishes alerts to an MQTT broker when the stock prices exceed the specified thresholds. The MQTT Subscriber component connects to the MQTT broker, authenticates users, and receives the stock price alerts by subscribing to the corresponding topic. Together, these components enable real-time stock monitoring and timely notifications for subscribed

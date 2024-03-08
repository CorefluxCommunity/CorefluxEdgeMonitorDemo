
# Coreflux Edge Monitor Demo

Coreflux Edge Monitor Demo is a demonstration project that visualizes real-time data from IoT edge devices. Utilizing Flask for the web interface and Paho MQTT for subscribing to topics, it showcases how data sent to a Coreflux MQTT broker can be securely received and displayed. This project is perfect for learning how to integrate IoT device data with web technologies for real-time monitoring and visualization.

## Features

- Real-time subscription to MQTT topics with Paho MQTT.
- Secure MQTT communication with TLS support.
- Dynamic data display in a Flask web application.
- Visualization of device data and images encoded in base64.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- Paho MQTT
- A Coreflux Cloud Broker get one free trial -> https://mqtt.coreflux.org

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/CorefluxIoTDataDisplay.git
   cd CorefluxIoTDataDisplay
   ```

2. Install the necessary Python packages:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Open `app.py` and configure the Cloud Coreflux MQTT broker settings:
   ```python
   MQTT_BROKER = "your_broker_address"
   MQTT_PORT = 8883  # or 1883 for non-TLS
   MQTT_TOPIC = "your_topic"
   ```

2. If your broker requires authentication or you're using TLS, ensure to configure `username_pw_set` and `tls_set` methods accordingly in `app.py`.

### Running the Application

Execute the following command from the project directory:

```
flask run
```

Access the web interface by navigating to `http://127.0.0.1:5000/` in your web browser.


## License

This project is licensed under   Apache License Version 2.0. You can use it no problem 🚀


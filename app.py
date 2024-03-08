from flask import Flask, render_template, Response
import paho.mqtt.client as mqtt
import base64
import json
import ssl

app = Flask(__name__)

# MQTT Configuration
MQTT_BROKER = #"broker address"
MQTT_PORT = 8883
MQTT_TOPIC = "PortoHotel/Floor1/Device1/$SYS/Coreflux/Assets"

latest_message = None
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global latest_message
    print(f"MQTT Message Received: {msg.topic}")
    try:
        # Assuming the payload is a JSON string
        message = json.loads(msg.payload)
        latest_message = message
    except Exception as e:
        print(f"Error processing message: {e}")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC)

# Setup MQTT Client with Authentication
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set('user', 'password')  # Set your MQTT username and password here
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)
# Enable TLS for secure connection
mqtt_client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                    tls_version=ssl.PROTOCOL_TLS, ciphers=None)
mqtt_client.tls_insecure_set(False) 
mqtt_client.loop_start()  # Start the loop in a non-blocking way




@app.route('/')
def index():
    return render_template('index.html', data=latest_message)

def generate_image_stream(image_data):
    """Converts base64 image data to binary and yields it"""
    if image_data:
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + base64.b64decode(image_data) + b'\r\n')

@app.route('/image/<image_key>')
def image(image_key):
    global latest_message
    if not latest_message:
        return "Waiting for MQTT data...", 503

    # Assuming latest_message contains the expected JSON structure
    image_data = latest_message[0].get(image_key, "")
    return Response(generate_image_stream(image_data), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
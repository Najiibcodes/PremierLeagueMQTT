import random
import json
import time
import paho.mqtt.client as mqtt

# Simulated top scorers data
top_scorers = [
    {"player": "Alan Shearer", "goals": 260, "team": "-"},
    {"player": "Harry Kane", "goals": 213, "team": "-"},
    {"player": "Wayne Rooney", "goals": 208, "team": "-"},
    {"player": "Andrew Cole", "goals": 187, "team": "-"},
    {"player": "Sergio Agüero", "goals": 184, "team": "-"},
    {"player": "Frank Lampard", "goals": 177, "team": "-"},
    {"player": "Thierry Henry", "goals": 175, "team": "-"},
    {"player": "Robbie Fowler", "goals": 163, "team": "-"},
    {"player": "Jermain Defoe", "goals": 162, "team": "-"},
    {"player": "Mohamed Salah", "goals": 161, "team": "Liverpool"},
    {"player": "Michael Owen", "goals": 150, "team": "-"},
    {"player": "Les Ferdinand", "goals": 149, "team": "-"},
    {"player": "Teddy Sheringham", "goals": 146, "team": "-"},
    {"player": "Robin van Persie", "goals": 144, "team": "-"},
    {"player": "Jamie Vardy", "goals": 138, "team": "Leicester City"},
    {"player": "Jimmy Floyd Hasselbaink", "goals": 127, "team": "-"},
    {"player": "Robbie Keane", "goals": 126, "team": "-"},
    {"player": "Nicolas Anelka", "goals": 125, "team": "-"},
    {"player": "Raheem Sterling", "goals": 123, "team": "Arsenal"},
    {"player": "Dwight Yorke", "goals": 123, "team": "-"}
]

# MQTT broker connection settings
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print(f"Failed to connect, return code {rc}")

# Function to simulate data publishing
def publish_data(client):
    scorer = random.choice(top_scorers)
    data = json.dumps(scorer)
    client.publish("premierleague/top_scorers", data)
    print(f"Published: {data}")

# Connect to AWS IoT Core MQTT endpoint with TLS/SSL
client = mqtt.Client()
client.on_connect = on_connect

# Set the path to your certificates and private key
ca_cert_path = "C:/Users/nejis/Downloads/AmazonRootCA1.pem"
client_cert_path = "C:/Users/..pem.crt"
private_key_path = "C:/Users/..pem.key"

# Configure TLS/SSL settings for the client
client.tls_set(ca_certs=ca_cert_path, certfile=client_cert_path, keyfile=private_key_path)

# AWS IoT Core endpoint
client.connect("ar7dykgmzgwtvi-ats.iot.eu-west-2.amazonaws.com", 8883, 60)

# Start loop to simulate data publishing every 10 seconds
client.loop_start()
while True:
    publish_data(client)
    time.sleep(10)

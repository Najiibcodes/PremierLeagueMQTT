# Premier League IoT Data Simulation with MQTT and AWS

## Project Overview

This project simulates real-time data publishing using **MQTT** protocol and **AWS IoT Core**. It streams Premier League top scorers' data continuously to an IoT endpoint, demonstrating the use of **secure communication channels**, **certificate-based authentication**, and **real-time data pipelines**.

## Key Features

- **MQTT Protocol**: Publishes live data at intervals using the lightweight MQTT messaging protocol, optimized for IoT applications.
- **AWS IoT Core**: Secure integration with AWS IoT, using X.509 certificates for authentication.
- **Python Automation**: Python script driving automated data publishing every 10 seconds, simulating a live feed.
- **Real-Time Streaming**: Simulated data stream of top Premier League scorers, published in real-time to an AWS IoT endpoint.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Najiibcodes/PremierLeagueMQTT.git

**Install necessary dependencies:**
pip install paho-mqtt

**Run the simulation:**
python iot_simulator.py

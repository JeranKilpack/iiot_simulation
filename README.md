IIoT Simulation and Visualization

This repository contains Python scripts for simulating and visualizing data from different sensors used in an IIoT (Industrial Internet of Things) environment. The simulation includes MQTT, CoAP, and OPC UA sensor data with real-time visualization for temperature and humidity.
Prerequisites

Before you begin, ensure you have the following installed on your system:

    Python 3.x

    pip (Python package installer)

    Git

    Visual Studio Code or any code editor of your choice

Setup
1. Clone the repository

Clone the repository to your local machine using the following command:

git clone https://github.com/your-username/iiot_simulation.git

2. Set up a Virtual Environment

Navigate to the project folder:

cd iiot_simulation

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

    On Windows:

.\venv\Scripts\activate

On Linux/macOS:

    source venv/bin/activate

3. Install the required packages

Install the necessary dependencies from the requirements.txt file:

pip install -r requirements.txt

If the requirements.txt is not provided, you can manually install the packages:

pip install paho-mqtt
pip install coapthon
pip install opcua
pip install matplotlib

4. Run the Sensor Simulations

To run the different sensor simulation scripts in separate terminals:
MQTT Sensor Simulation:

python mqtt_sensor_simulation.py

CoAP Sensor Simulation:

python coap_sensor_simulation.py

OPC UA Sensor Simulation:

python opcua_sensor_simulation.py

5. Visualize the Data

Once all three simulations are running, you can start the data visualization scripts to view real-time data for temperature and humidity:
MQTT Visualization:

python data_visualization_mqtt.py

CoAP Visualization:

python data_visualization_coap.py

OPC UA Visualization:

python data_visualization_opcua.py

6. Stop the Scripts

To stop any of the running scripts, you can press Ctrl + C in the terminal where they are running.
Repository Structure

    mqtt_sensor_simulation.py: Simulates sensor data using MQTT protocol.

    coap_sensor_simulation.py: Simulates sensor data using CoAP protocol.

    opcua_sensor_simulation.py: Simulates sensor data using OPC UA protocol.

    data_visualization_mqtt.py: Visualizes MQTT sensor data (temperature and humidity).

    data_visualization_coap.py: Visualizes CoAP sensor data (temperature and humidity).

    data_visualization_opcua.py: Visualizes OPC UA sensor data (temperature and humidity).

    requirements.txt: Contains the list of required Python packages.

    README.md: Instructions for setting up and running the project.

License

This project is licensed under the MIT License - see the LICENSE file for details.

You can modify the repository URL, file names, and any other details that match your specific project setup.

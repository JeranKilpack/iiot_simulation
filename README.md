IIoT Simulation and Visualization

This repository contains Python scripts for simulating and visualizing data from different sensors used in an IIoT (Industrial Internet of Things) environment. The simulation includes MQTT, CoAP, and OPC UA sensor data with real-time visualization for temperature and humidity.
Prerequisites

Before you begin, ensure you have the following installed on your system:

    Python 3.x: Download from python.org.

    pip (Python package installer): This should come with Python 3.x, but you can check by running pip --version in the command prompt.

    Git: Download from git-scm.com.

    Visual Studio Code (Optional): You can use any text editor, but Visual Studio Code is recommended.

Setup
1. Clone the repository

Clone the repository to your local machine using Git. Open a command prompt and run:

git clone https://github.com/your-username/iiot_simulation.git

2. Set up a Virtual Environment

Navigate to the project folder:

cd iiot_simulation

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

.\venv\Scripts\activate

You should now see (venv) in your command prompt, indicating that the virtual environment is active.
3. Install Required Packages

Install the necessary dependencies by running the following commands in your activated virtual environment:

pip install pandas numpy paho-mqtt aiocoap asyncua matplotlib

4. Run the Sensor Simulations

To run the different sensor simulation scripts, open three separate command prompt windows and run the following commands in each:
MQTT Sensor Simulation:

python mqtt_sensor_simulation.py

CoAP Sensor Simulation:

python coap_sensor_simulation.py

OPC UA Sensor Simulation:

python opcua_sensor_simulation.py

5. Visualize the Data

Once all three simulations are running, you can start the data visualization scripts to view real-time data for temperature and humidity.
MQTT Visualization:

Open a new command prompt and run:

python data_visualization_mqtt.py

CoAP Visualization:

Open another command prompt and run:

python data_visualization_coap.py

OPC UA Visualization:

Finally, open another command prompt and run:

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

    README.md: Instructions for setting up and running the project.

License

This project is licensed under the MIT License - see the LICENSE file for details.

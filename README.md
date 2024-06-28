ThreadSimulations

## Project description

The project is designed to simulate data flows from GNSS receivers in real time. It includes several scripts and services for loading, converting and publishing data, as well as an API for interacting with users.

## Installation

To install the project, follow these steps:

1. Clone the repository using the command:
```bash
git clone https://github.com/shokorev25/ThreadSimulations
```
2. Install MQTT:
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```
3. Go to the project directory:

```bash
cd ThreadSimulations
```
4. Make CRX2RNX executable:

```bash
cmod bin\CRX2RNX
```

### Creating a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installing dependencies

```bash
pip install -r requirements.txt
```

## Setting up the service system

1. **download_and_extract.service**
2. **convert_to_rnx.service**
3. **publish_data.service**
4. **subscribe_data.service**

Copy the service files to the `/etc/systemd/system/` directory and activate them:

```bash
sudo cp service/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable download_and_extract.service
sudo systemctl enable convert_to_rnx.service
sudo systemctl enable publish_data.service
sudo systemctl enable subscribe_data.service
sudo systemctl start download_and_extract.service
sudo systemctl start convert_to_rnx.service
sudo systemctl start publish_data.service
sudo systemctl start subscribe_data.service
```

## Launching the application

To launch the FastAPI application, run:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Make a duplicate in Putty.
```bash
mosquitto_sub -h localhost -t gnss_data -v
```
## Usage

Log in to your machine's address in Fast Api Swagger UI.
```bash
https://yourmachineaddress:8000/docs
```
Use POST to interact with the project.

## License

This project is licensed under the MIT license - see the LICENSE file for details.

## Authors

- **Shokorev Alexander** - [shokorev25](https://github.com/shokorev25)
- **Dmitry Kazmin** - [reikatto](https://github.com/reikatto)

# Safe Alert
# Accident Detection and SOS Alert System

## Overview
This project is an AI-powered accident detection system that analyzes video footage to detect accidents in real-time. Upon detecting an accident, the system automatically sends an SOS alert to the nearest authorities.

## Features
- **Accident Detection**: Uses video processing and AI models to identify accidents.
- **SOS Alerts**: Automatically sends an alert message upon accident detection.
- **Flask API**: Provides API endpoints for accident detection and alert notifications.

## Future Scope
- **Geolocation Integration**: Capturing and sending the exact accident location using geolocation services.
- **Database Storage**: Using **MongoDB** (via PyMongo) to store detected accident data for analysis.
- **Enhanced UI**: Building an interactive dashboard for real-time accident monitoring.

## Challenges Faced
- **False Positives**: Improving the model to reduce incorrect accident detections.
- **Network Latency**: Ensuring real-time alerts despite network delays.
- **Integration Issues**: Handling issues related to Twilio API for SMS alerts.

## Installation
```sh
git clone https://github.com/yourusername/accident-detection.git
cd accident-detection
pip install -r requirements.txt
```

## Usage
```sh
python app.py
```

## API Endpoints
- `GET /detect-accident` - Triggers accident detection.
- `GET /send-alert` - Sends an SOS alert.

## Dataset
https://www.kaggle.com/datasets/ckay16/accident-detection-from-cctv-footage/data

## Technologies Used
- Python, Flask
- OpenCV, Deep Learning (CNNs)
- Twilio API (for alerts)
- MongoDB (Future Scope)

## Contributors
- **Darshan Jain** (Project Lead)

## License
This project is licensed under the MIT License.

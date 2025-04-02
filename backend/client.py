import requests

response = requests.post("http://127.0.0.1:5000/start_detection")       # Send POST request to start detection
print(response.json())

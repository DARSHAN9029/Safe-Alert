from twilio.rest import Client
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
app = Flask(__name__)

def send_sos_alert():                                       # Function for sending alerts
    client = Client(TWILIO_SID , TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            from_='+13802702757',
            body='emergency, accident detected',
            to='+918451811559'
        )
        print(f"SOS Alert Sent! Message SID: {message.sid}")
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        print(f"Error sending SOS alert: {e}")
        return {"status": "failure", "error": str(e)}

@app.route("/send-alert", methods=["GET"])        
def alert():
    return send_sos_alert()

def run_app():
    app.run(host="127.0.0.1", port=5000)

if __name__ == "__main__":
    thread = Thread(target=run_app)       # Run the Flask app in a separate thread so that the accident detection code can
    thread.start()

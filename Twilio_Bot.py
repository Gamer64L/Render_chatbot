from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Tu Account SID
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')  # Tu Auth Token
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')  # Tu número de Twilio

@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()

    # Mensaje automático de bienvenida
    if 'hola' in incoming_msg:
        response_message = "Hola, soy tu bot automático de Twilio. ¿En qué puedo ayudarte hoy?"
    else:
        response_message = "Disculpa, no entendí tu mensaje. Puedes decir 'Hola' para empezar."

    resp.message(response_message)
    return str(resp)

if __name__ == "__main__":
    app.run()



from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

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
    # Configuración del puerto para Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



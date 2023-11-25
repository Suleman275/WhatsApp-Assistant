from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import google.generativeai as palm
import os

load_dotenv()

palm.configure(api_key=os.environ['palmkey'])
response = palm.chat(messages='Hello')

# Init the Flask App
app = Flask(__name__)

# Define a route to handle incoming requests
@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get('Body', '').lower()
    print("Message: ", incoming_message)
    
    global response
    response = response.reply(incoming_message)

    print("Response: ", response.last)

    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(response.last)

    return str(bot_resp)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
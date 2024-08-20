from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


# Your Auth Token from twilio.com/user/account
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

if auth_token is None:
    raise ValueError("The TWILIO_AUTH_TOKEN environment variable is not set.")

# Initialize the request validator
validator = RequestValidator(auth_token)

@app.route('/bot', methods=['POST'])
def bot():
    # Store Twilio's request URL (the url of your webhook) as a variable
    url = 'https://b016-194-35-99-114.ngrok-free.app/bot'
     # Assuming 'bot' is the endpoint Twilio will hit

    # Get the entire header object received from Twilio
    twilio_signature = request.headers.get('X-Twilio-Signature', '')

    # Get all form data
    form_data = request.form.to_dict()
    
    # Validate the request
    if not validator.validate(url, form_data, twilio_signature):
        # If request is not valid, return an error response
        return 'Validation failed', 403
    print(request.headers)
    print(request.values)
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    print("--------------------------")
    print(request.values.get('From'))
    print("--------------------------")

    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

if __name__ == '__main__':
    app.run(port=4000)

# Twilio-Whatsapp-Bot
This project is a simple chatbot built using Flask and Twilio. The bot responds to incoming WhatsApp messages with either a random quote or a cat picture, based on the content of the message.

## Features

- **Message Handling**: Responds to specific keywords in WhatsApp messages.
- **Quote Retrieval**: Fetches a random quote from an external API.
- **Cat Pictures**: Sends a random cat picture when prompted.
- **Request Validation**: Ensures that incoming requests are legitimately from Twilio.

## Requirements

- Python 3.7+
- Required Python packages: Install via `pip install -r requirements.txt`
  - `Flask`
  - `requests`
  - `twilio`
  - `python-dotenv`

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your Twilio Auth Token to the `.env` file:
     ```
     TWILIO_AUTH_TOKEN=your-twilio-auth-token
     ```

4. **Configure Twilio Webhook**:
   - Set the webhook URL for your Twilio number to point to the `/bot` endpoint of your server. If you're running locally, use a tunneling service like `ngrok` to expose your localhost to the internet. For example:
     ```
     https://<your-ngrok-url>/bot
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

## Code Overview

### File Structure

- **`app.py`**: Main application file that handles incoming requests and responses.
- **`.env`**: Environment file to store sensitive information like the Twilio Auth Token.

### Key Components

- **Flask**: The web framework used to handle incoming HTTP requests.
- **Twilio Request Validator**: Ensures that incoming requests are genuinely from Twilio by validating the `X-Twilio-Signature`.
- **Twilio MessagingResponse**: Used to generate responses to be sent back to the user via WhatsApp.
- **Requests Library**: Used to fetch random quotes from the external API.

### Application Logic

- **Webhook Endpoint**: The `/bot` endpoint is configured to receive POST requests from Twilio.
- **Request Validation**: Before processing, the request is validated to ensure it is from Twilio.
- **Message Handling**:
  - If the message contains the word "quote", the bot fetches a random quote from the Quotable API and sends it back.
  - If the message contains the word "cat", the bot sends back a random cat image.
  - If the message contains neither, the bot responds with a default message.

## Usage

1. Send a WhatsApp message to your Twilio number.
2. The bot will respond based on the content of your message:
   - Type "quote" to receive a random quote.
   - Type "cat" to receive a random cat picture.

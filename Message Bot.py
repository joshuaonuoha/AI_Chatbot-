from flask import Flask, request
import requests
import json
import instapi 

class MessageBot:
    app = Flask(__name__)

    # Instagram webhook endpoint
    @app.route('/instagram-webhook', methods=['POST'])
    def instagram_webhook():
        # Get incoming message text from Instagram
        data = request.get_json()
        # Extract the message text and sender ID
        message_text = data['message']['content']
        sender_id = data['sender_id']
        # Send the message to ChatGPT
        response = send_to_chatgpt(message_text)
        # Send the response back to Instagram
        send_response_to_instagram(sender_id, response)
        return "OK"

    def send_to_chatgpt(message):
        # ChatGPT API endpoint
        api_url = 'https://api.openai.com/v1/chat/completions'
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_OPENAI_API_KEY'}
        payload = {'messages': [{'role': 'system', 'content': 'Your USER_ID'}, {'role': 'user', 'content': message}]}
        # Make the API call to ChatGPT
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        # Extract and return the generated response from ChatGPT
        return response_data['choices'][0]['message']['content']

    def send_response_to_instagram(recipient_id, response):
        # Implement the necessary logic to send the response to the user with recipient ID
        pass  # Replace this line with your Instagram integration code

if __name__ == '__main__':
    MessageBot.app.run(debug=True)

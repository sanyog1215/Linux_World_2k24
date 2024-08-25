from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
import getpass
from twilio.rest import Client

import os
import pyttsx3
import requests
from bs4 import BeautifulSoup
import openai

app = Flask(__name__)
CORS(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    fromaddr = data['from']
    toaddrs = data['to']
    subject = data['subject']
    msg = data['message']
    app_password = data['password']

    email_message = f"From: {fromaddr}\nTo: {', '.join(toaddrs)}\nSubject: {subject}\n\n{msg}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, app_password)
        server.sendmail(fromaddr, toaddrs, email_message)
        server.quit()
        return jsonify({"status": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    to = data['to']
    message_body = data['message']

    account_sid = "AC898946107af3ee2f7f77e21feb3d3c18"
    auth_token = "bf6cc9dff76c9bf17dd0b9fced0c929d"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+12053031065",
        to=to,
        body=message_body
    )

    return jsonify({"status": "SMS sent successfully!", "sid": message.sid}), 200



@app.route('/open_chrome', methods=['GET'])
def open_chrome():
    os.system("chrome")
    return jsonify({"status": "Chrome opened successfully!"}), 200

@app.route('/open_notepad', methods=['GET'])
def open_notepad():
    os.system("notepad")
    return jsonify({"status": "Notepad opened successfully!"}), 200

@app.route('/speak_text', methods=['POST'])
def speak_text():
    data = request.json
    text = data['text']
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    return jsonify({"status": "Text spoken successfully!"}), 200

@app.route('/get_wikipedia_data', methods=['POST'])
def get_wikipedia_data():
    data = request.json
    topic = data['topic']
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(wikipedia_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = [p.text for p in soup.find_all('p')]
        return jsonify({"title": title, "content": paragraphs}), 200
    else:
        return jsonify({"error": f"Failed to retrieve data. Status code: {response.status_code}"}), 500

@app.route('/open_chatgpt', methods=['POST'])
def open_chatgpt():
    data = request.json
    user_message = data['message']

    openai.api_key = "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"
    messages = [{"role": "user", "content": user_message}]

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    chat_reply = chat.choices[0].message.content
    return jsonify({"reply": chat_reply}), 200

if __name__ == '__main__':
    app.run(debug=True)

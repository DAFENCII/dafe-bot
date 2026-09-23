from flask import Flask, request
import requests
import os
app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
@app.route('/', methods=['GET','POST'])
def home():
    return "Dafe Bot شغال", 200
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        if data and "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text","")
            reply = f"البوت اشتغل! رسالتك: {text}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": chat_id, "text": reply})
    return "ok", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

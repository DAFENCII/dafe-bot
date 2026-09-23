from flask import Flask, request
app = Flask(__name__)
VERIFY_TOKEN = "dafe_verify_2025"

@app.route('/webhook/whatsapp', methods=['GET'])
def verify():
    if request.args.get('hub.verify_token') == VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return "wrong", 403

@app.route('/webhook/whatsapp', methods=['POST'])
def webhook():
    print(request.json)
    return "ok", 200

@app.route('/')
def home():
    return "Dafe Bot شغال"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

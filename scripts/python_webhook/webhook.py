from flask import Flask, request, jsonify
import hmac
import os

WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    signature = request.headers.get('X-Hub-Signature')
    body = request.get_json()

    computed_sig = hmac.digest(WEBHOOK_SECRET, body, 'sha1').hexdigest()

    if hmac.compare_digest(computed_sig, signature):
        print('success')
    else:
        print('error')


if __name__ == '__main__':
    app.run()
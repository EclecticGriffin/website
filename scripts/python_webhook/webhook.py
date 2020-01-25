from flask import Flask, request, jsonify
import hmac
import os
import subprocess

WEBHOOK_SECRET = bytes(os.getenv('WEBHOOK_SECRET'), 'utf-8')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    signature = request.headers.get('X-Hub-Signature', '')
    body = request.get_data()

    computed_sig = 'sha1=' + hmac.HMAC(WEBHOOK_SECRET, body, 'sha1').hexdigest()

    if hmac.compare_digest(computed_sig, signature):
        print('success')
        subprocess.run(["git", "pull"])
        subprocess.run(["hugo"])
    else:
        print('error')

    return "200"

if __name__ == '__main__':
    app.run()
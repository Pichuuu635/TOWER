from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

# 📁 pega pasta controller
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📁 vai pra pasta data (irmã da controller)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.json

    temp = dados.get('temperatura')
    umid = dados.get('umidade')
    chuva = dados.get('chuva')
    esp_id = dados.get('id')
    solo_analogico = dados.get('solo_analogico') 
    solo_digital = dados.get('solo_digital')

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{esp_id}] {agora} | Temp: {temp}°C | Umid: {umid}% | Chuva: {chuva}")

    if esp_id == "ESP32_ESTUFA":
        caminho = os.path.join(DATA_DIR, "estufa_data.txt")
        with open(caminho, "a") as f:
            f.write(f"{agora},{temp},{umid},{chuva},{solo_analogico},{solo_digital}\n")

    elif esp_id == "ESP32_01":
        caminho = os.path.join(DATA_DIR, "torre_data.txt")
        with open(caminho, "a") as f:
            f.write(f"{agora},{temp},{umid},{chuva}\n")

    else:
        print("ESP desconhecido:", esp_id)

    return "Dados recebidos!", 200


def iniciar_servidor():
    app.run(host='0.0.0.0', port=5000)
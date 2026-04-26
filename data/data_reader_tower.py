import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ler_ultimo_estufa():
    caminho = os.path.join(BASE_DIR, "torre_data.txt")

    try:
        with open(caminho, "r") as f:
            linhas = f.readlines()

            if not linhas:
                return None

            ultima = linhas[-1].strip()
            dados = ultima.split(",")

            return {
                "data": dados[0],
                "temperatura": dados[1],
                "umidade": dados[2],
                "chuva": dados[3],
            }
    except:
        return None
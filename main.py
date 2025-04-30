from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho=12, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas

    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

@app.route("/")
def home():
    return "Gerador de Senhas - Acesse /gerar para gerar uma senha"

@app.route("/gerar")
def gerar():
    try:
        tamanho = int(request.args.get("tamanho", 12))
        usar_numeros = request.args.get("numeros", "true").lower() == "true"
        usar_simbolos = request.args.get("simbolos", "true").lower() == "true"

        senha = gerar_senha(tamanho, usar_numeros, usar_simbolos)
        return jsonify({"senha_gerada": senha})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

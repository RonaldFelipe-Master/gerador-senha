from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

def gerar_senha(tamanho=12, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

HTML = '''
<!doctype html>
<html>
<head>
  <title>Gerador de Senhas</title>
</head>
<body>
  <h1>Gerador de Senhas</h1>
  <form method="post">
    <label for="tamanho">Tamanho:</label>
    <input type="number" name="tamanho" value="12" min="4" max="50">
    <br><br>
    <label><input type="checkbox" name="numeros" checked> Incluir números</label><br>
    <label><input type="checkbox" name="simbolos" checked> Incluir símbolos</label><br><br>
    <button type="submit">Gerar Senha</button>
  </form>

  {% if senha %}
    <h2>Senha Gerada:</h2>
    <p><strong>{{ senha }}</strong></p>
  {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    senha = None
    if request.method == "POST":
        tamanho = int(request.form.get("tamanho", 12))
        usar_numeros = "numeros" in request.form
        usar_simbolos = "simbolos" in request.form
        senha = gerar_senha(tamanho, usar_numeros, usar_simbolos)
    return render_template_string(HTML, senha=senha)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

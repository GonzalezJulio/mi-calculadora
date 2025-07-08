from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"mensaje": "Bienvenido a la calculadora Flask"})

@app.route("/sumar/<int:a>/<int:b>")
def sumar(a, b):
    return jsonify({"resultado": a + b})

@app.route("/restar/<int:a>/<int:b>")
def restar(a, b):
    return jsonify({"resultado": a - b})

@app.route("/es-primo/<int:n>")
def es_primo(n):
    if n < 2:
        return jsonify({"es_primo": False})
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return jsonify({"es_primo": False})
    return jsonify({"es_primo": True})

@app.route("/dividir/<int:a>/<int:b>")
def dividir(a, b):
    if b == 0:
        return jsonify({"error": "División por cero"}), 400
    return jsonify({"resultado": a / b})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# funciones de utilidad
def potencia(base, exponente): return base ** exponente
def es_par(n): return n % 2 == 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

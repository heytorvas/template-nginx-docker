from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Servidor 1 - Porta 81"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
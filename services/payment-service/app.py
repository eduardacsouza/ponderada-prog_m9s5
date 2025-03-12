from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pagar', methods=['POST'])
def pagar():
    resposta = {"status": "Aprovado"}
    return jsonify(resposta)

if __name__ == '__main__':
    print("Serviço de Pagamento rodando na porta 8081")
    app.run(port=8081)

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/pedido', methods=['POST'])
def criar_pedido():
    dados = request.get_json()
    
    if not dados or "id" not in dados or "valor" not in dados:
        return jsonify({"erro": "ID e valor são obrigatórios"}), 400

    novo_pedido = {
        "id": dados["id"],
        "valor": dados["valor"],
        "status": "Pendente"
    }

    # Chamando o serviço de pagamento com timeout de 5s e cabeçalho com versão
    try:
        resposta = requests.post(
            "http://localhost:8081/pagar",
            headers={"Content-Type": "application/json", "X-API-Version": "1.0"},
            timeout=5
        )
        pagamento_status = resposta.json().get("status", "Falha")
    except requests.exceptions.Timeout:
        print("Erro: Timeout na chamada ao serviço de pagamento")
        pagamento_status = "Falha - Tempo excedido"
    except Exception as e:
        print("Erro ao chamar serviço de pagamento:", e)
        pagamento_status = "Falha"

    novo_pedido["status"] = pagamento_status
    return jsonify(novo_pedido)

if __name__ == '__main__':
    print("Serviço de Pedidos rodando na porta 8080")
    app.run(port=8080)
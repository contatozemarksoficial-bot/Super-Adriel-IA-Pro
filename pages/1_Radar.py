
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Simulador de Banco de Dados de Produtos / Lançamentos coletados da Gringa
PRODUCTS_DB = [
    {"id": 1, "name": "Alpilean", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 2, "name": "Puravive", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 3, "name": "Java Burn", "platform": "BuyGoods", "type": "Evergreen"},
    {"id": 4, "name": "GlucoTrust", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 5, "name": "Sugavita Med", "platform": "Digistore24", "type": "Lançamento"},
    {"id": 6, "name": "Keto Drops Pro", "platform": "Hotmart Global", "type": "Lançamento"},
    # Adicione mais produtos para completar de 20 a 30 itens
]

@app.route('/api/radar', methods=['GET'])
def get_radar_produtos():
    produtos_processados = []
    
    # Ordena ou embaralha para simular tempo real
    random.shuffle(PRODUCTS_DB)
    
    for index, prod in enumerate(PRODUCTS_DB[:30]):
        # Define os Top 10 baseados na posição da lista processada
        is_top_10 = index < 10
        status_icon = "🔥 ALTA" if is_top_10 else "✅ NORMAL"
        
        # Simulação de buscas em tempo real (Pode ser integrado com API do Google Trends/Keywords)
        searches_month = random.randint(15000, 120000) if is_top_10 else random.randint(1500, 12000)
        searches_today = random.randint(300, 2500) if is_top_10 else random.randint(20, 300)
        
        # Lógica de melhor país para anunciar
        paises_sugeridos = ["USA", "UK", "Canada", "Australia", "Germany"]
        melhor_pais = paises_sugeridos[0] if is_top_10 else random.choice(paises_sugeridos)
        
        produtos_processados.append({
            "ranking": index + 1,
            "nome": prod["name"],
            "plataforma": prod["platform"],
            "tipo": prod["type"],
            "status": status_icon,
            "buscas_mes": searches_month,
            "buscas_hoje": searches_today,
            "melhor_pais_anunciar": melhor_pais,
            "motivo_afirmacao": f"Excelente volume no {melhor_pais} com baixa concorrência de CPC hoje."
        })
        
    return jsonify({"produtos": produtos_processados})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

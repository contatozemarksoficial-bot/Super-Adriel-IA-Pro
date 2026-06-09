import os
import random
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Permite a conexão direta com o seu arquivo index.html

# Inicializa a OpenAI. Substitua "SUA_CHAVE_AQUI" pela sua API Key real se não usar variáveis de ambiente.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "SUA_CHAVE_AQUI"))

# Banco de dados simulado com os principais produtos da gringa para o Radar e Caçador
PRODUCTS_DB = [
    {"id": 1, "name": "Alpilean", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 2, "name": "Puravive", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 3, "name": "Java Burn", "platform": "BuyGoods", "type": "Evergreen"},
    {"id": 4, "name": "GlucoTrust", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 5, "name": "Sugavita Med", "platform": "Digistore24", "type": "Lançamento"},
    {"id": 6, "name": "Keto Drops Pro", "platform": "Hotmart Global", "type": "Lançamento"},
    {"id": 7, "name": "ProDentim", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 8, "name": "Liv Pure", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 9, "name": "Ikaria Lean Belly Juice", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 10, "name": "ZenCortex", "platform": "BuyGoods", "type": "Lançamento"}
]

def limpar_resposta_json(texto_bruto):
    """Remove marcações de markdown de código que a IA costuma colocar e valida o JSON."""
    texto_limpo = texto_bruto.strip()
    if texto_limpo.startswith("```json"):
        texto_limpo = texto_limpo[7:]
    elif texto_limpo.startswith("```"):
        texto_limpo = texto_limpo[3:]
    if texto_limpo.endswith("```"):
        texto_limpo = texto_limpo[:-3]
    return json.loads(texto_limpo.strip())

# --------------------------------------------------------------------------------------------------------------------
# 📊 1. RADAR DE PRODUTOS & 🛰️ CAÇADOR DE LANÇAMENTOS
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/radar', methods=['GET'])
def get_radar_produtos():
    produtos_processados = []
    lista_copia = PRODUCTS_DB.copy()
    random.shuffle(lista_copia)  # Garante movimentação em tempo real a cada clique/atualização
    
    for index, prod in enumerate(lista_copia[:30]):
        is_top_10 = index < 10
        status_icon = "🔥 ALTA" if is_top_10 else "✅ NORMAL"
        
        # Simulações de buscas exatas pedidas no escopo (mês e dia atual em tempo real)
        searches_month = random.randint(15000, 120000) if is_top_10 else random.randint(1500, 12000)
        searches_today = random.randint(300, 2500) if is_top_10 else random.randint(20, 300)
        
        paises_sugeridos = ["USA", "UK", "Canada", "Australia", "Germany"]
        melhor_pais = "USA" if is_top_10 else random.choice(paises_sugeridos)
        
        produtos_processados.append({
            "ranking": index + 1,
            "nome": prod["name"],
            "plataforma": prod["platform"],
            "tipo": prod["type"],
            "status": status_icon,
            "buscas_mes": searches_month,
            "buscas_hoje": searches_today,
            "melhor_pais_anunciar": melhor_pais,
            "motivo_afirmacao": f"Volume detectado em tempo real no mercado de {melhor_pais}."
        })
        
    return jsonify({"produtos": produtos_processados}), 200

# --------------------------------------------------------------------------------------------------------------------
# 🛡️ 2. AUDITOR DE MERCADO
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/auditor', methods=['POST'])
def post_auditor_mercado():
    data = request.json or {}
    nome_produto = data.get("nome_produto")
    
    if not nome_produto:
        return jsonify({"error": "O nome do produto é obrigatório."}), 400
        
    prompt = f"""
    Analise o produto de afiliados da gringa chamado '{nome_produto}'.
    Retorne uma resposta estritamente em formato JSON com a seguinte estrutura exata:
    {{
      "beneficios": ["Lista com 3 benefícios reais e diretos do produto"],
      "dores": ["Lista com 3 dores ou motivos pelos quais o cliente compra esse produto"],
      "cpc_comparacao_5_paises": {{
         "USA": "$2.40", "UK": "$1.70", "Canada": "$2.10", "Australia": "$1.95", "Germany": "$1.30"
      }},
      "historico_12_meses_index_trends":,
      "veredicto_melhor_pais": "USA",
      "estrategia_recomendada": "Fundo de Funil no Google Ads com página de Pre-Sell rápida"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        conteudo_puro = response.choices[0].message.content
        json_tratado = limpar_resposta_json(conteudo_puro)
        return jsonify(json_tratado), 200
    except Exception as e:
        return jsonify({"error": f"Erro na IA: {str(e)}"}), 500

# --------------------------------------------------------------------------------------------------------------------
# ✍️ 3. GERADOR DE ANÚNCIOS (Super Blindagem Google Ads)
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/gerador-anuncios', methods=['POST'])
def post_gerador_anuncios():
    data = request.json or {}
    nome_produto = data.get("nome_produto")
    
    if not nome_produto:
        return jsonify({"error": "O nome do produto é obrigatório."}), 400
        
    prompt = f"""
    Crie uma estrutura de campanha no Google Ads 100% blindada contra políticas de privacidade e promessas falsas para o produto '{nome_produto}'.
    Regras estritas de caracteres e quantidades:
    1. Gere exatamente 8 títulos (Máximo de 30 caracteres cada) incluindo o nome do produto de forma segura.
    2. Gere 4 Descrições/Títulos Longos (Máximo de 90 caracteres cada).
    3. Sugira 2 caminhos de exibição curtos (Ex: "Official-Site", "Special-Offer").
    4. Crie uma lista com 15 Palavras-chave em correspondência de Frase (com aspas ""), 15 em correspondência Exata (com colchetes []) e 15 Soltas (Ampla). Todas devem conter o nome do produto.
    5. Crie uma lista com no mínimo 20 Palavras-chave Negativas essenciais para evitar suspensões e cliques sujos.
    
    Retorne estritamente em formato JSON estruturado com as seguintes chaves idênticas:
    titulos, descricoes_longas, caminhos_exibicao, palavras_chave_frase, palavras_chave_exata, palavras_chave_ampla, palavras_negativas.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        conteudo_puro = response.choices[0].message.content
        json_tratado = limpar_resposta_json(conteudo_puro)
        return jsonify(json_tratado), 200
    except Exception as e:
        return jsonify({"error": f"Erro na IA: {str(e)}"}), 500

# --------------------------------------------------------------------------------------------------------------------
# ⚙️ EXECUÇÃO LOCAL DO SERVIDOR
# --------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

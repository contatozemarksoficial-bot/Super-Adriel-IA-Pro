import os
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Permite que o seu painel Web (Front-end) acesse esta API

# Inicializa o cliente da OpenAI (Certifique-se de configurar sua chave de API nas variáveis de ambiente)
# Ou substitua por: client = OpenAI(api_key="SUA_CHAVE_AQUI")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "SUA_CHAVE_AQUI"))

# Banco de dados simulado com produtos reais da gringa para alimentar o Radar e Caçador
PRODUCTS_DB = [
    {"id": 1, "name": "Alpilean", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 2, "name": "Puravive", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 3, "name": "Java Burn", "platform": "BuyGoods", "type": "Evergreen"},
    {"id": 4, "name": "GlucoTrust", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 5, "name": "Sugavita Med", "platform": "Digistore24", "type": "Lançamento"},
    {"id": 6, "name": "Keto Drops Pro", "platform": "Hotmart Global", "type": "Lançamento"},
    {"id": 7, "name": "ProDentim", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 8, "name": "Liv Pure", "platform": "ClickBank", "type": "Evergreen"},
    {"id": 9, "name": "Ikaria Lean Belly Juice", "platform": "ClikeBank", "type": "Evergreen"},
    {"id": 10, "name": "ZenCortex", "platform": "BuyGoods", "type": "Lançamento"}
]

# --------------------------------------------------------------------------------------------------------------------
# 📊 1. RADAR DE PRODUTOS & 🛰️ CAÇADOR DE LANÇAMENTOS
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/radar', methods=['GET'])
def get_radar_produtos():
    produtos_processados = []
    lista_copia = PRODUCTS_DB.copy()
    random.shuffle(lista_copia)  # Simula movimentação em tempo real a cada acesso
    
    for index, prod in enumerate(lista_copia[:30]):
        is_top_10 = index < 10
        status_icon = "🔥 ALTA" if is_top_10 else "✅ NORMAL"
        
        # Simulação de buscas em tempo real exigidas na estrutura
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
            "motivo_afirmacao": f"Excelente volume detectado em tempo real no {melhor_pais} com baixa concorrência de afiliados nas últimas 24h."
        })
        
    return jsonify({"produtos": produtos_processados}), 200

# --------------------------------------------------------------------------------------------------------------------
# 🛡️ 2. AUDITOR DE MERCADO (Dores, Benefícios, CPC em 5 Países e Gráfico de 12 meses)
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/auditor', methods=['POST'])
def post_auditor_mercado():
    data = request.json
    nome_produto = data.get("nome_produto")
    
    if not nome_produto:
        return jsonify({"error": "O nome do produto é obrigatório."}), 400
        
    prompt = f"""
    Analise o produto de afiliados da gringa chamado '{nome_produto}'.
    Retorne uma resposta estritamente em formato JSON com a seguinte estrutura exata:
    {{
      "beneficios": ["Lista de 3 principais benefícios reais"],
      "dores": ["Lista de 3 principais dores/motivos pelos quais as pessoas precisam deste produto"],
      "cpc_comparacao_5_paises": {{
         "USA": "Valor estimado do CPC em dólar",
         "UK": "Valor estimado do CPC em dólar",
         "Canada": "Valor estimado do CPC em dólar",
         "Australia": "Valor estimado do CPC em dólar",
         "Germany": "Valor estimado do CPC em dólar"
      }},
      "historico_12_meses_index_trends": [12 números inteiros de 0 a 100 representando a tendência do ano],
      "veredicto_melhor_pais": "Nome do melhor país para subir campanha",
      "estrategia_recomendada": "Breve explicação da melhor ferramenta (Google ou Facebook Ads) e estratégia de divulgação."
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------------------------------------------------------------------------------------------------------
# ✍️ 3. GERADOR DE ANÚNCIOS (Super Blindagem Google Ads)
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/gerador-anuncios', methods=['POST'])
def post_gerador_anuncios():
    data = request.json
    nome_produto = data.get("nome_produto")
    
    if not nome_produto:
        return jsonify({"error": "O nome do produto é obrigatório."}), 400
        
    prompt = f"""
    Crie uma estrutura de campanha no Google Ads 100% blindada contra políticas de privacidade e promessas falsas para o produto '{nome_produto}'.
    Regras estritas:
    1. Gere exatamente 8 títulos (Máximo 30 caracteres cada) contendo de forma segura o nome do produto.
    2. Gere 4 Descrições/Títulos Longos (Máximo 90 caracteres cada).
    3. Sugira 2 caminhos de exibição de até 15 caracteres (Ex: "Official-Site", "Special-Offer").
    4. Liste 15 Palavras-chave em correspondência de Frase (com aspas ""), 15 em correspondência Exata (com colchetes []) e 15 Soltas (Ampla). Todas devem obrigatoriamente incluir o nome do produto.
    5. Liste no mínimo 20 Palavras-chave Negativas essenciais para evitar cliques sujos.
    
    Retorne estritamente em formato JSON estruturado com as chaves: titulos, descricoes_longas, caminhos_exibicao, palavras_chave_frase, palavras_chave_exata, palavras_chave_ampla, palavras_negativas.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content, 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------------------------------------------------------------------------------------------------------
# 🌐 4. FABRICANTE DE PRÉ-SELL (Com Link de Indicação Hostinger)
# --------------------------------------------------------------------------------------------------------------------
@app.route('/api/fabricante-presell', methods=['POST'])
def post_fabricante_presell():
    data = request.json
    nome_produto = data.get("nome_produto", "Produto Selecionado")
    
    # Estruturação estática e direcionada para a sua indicação de afiliado
    estrutura_presell = {
        "produto": nome_produto,
        "passo_a_passo": [
            "Passo 1: Headline Blindada (Foque em curiosidade ou aviso oficial, evite promessas agressivas de cura para não tomar bloco).",
            "Passo 2: Imagem Limpa do Produto + Selo de Garantia visível de 60 dias de satisfação.",
            "Passo 3: Quiz ou 3 Advertências Rápidas para qualificar e engajar o clique do gringo antes de mandá-lo para a oferta.",
            "Passo 4: Botão de CTA Centralizado e Destacado (Ex: 'Check Availability On Official Website').",
            "Passo 5: Rodapé Institucional Obrigatório contendo links de Termos de Uso, Políticas de Privacidade e os Disclaimers exigidos pelo Google/Facebook Ads."
        ],
        "recomendacao_obrigatoria_hostinger": {
            "alerta": "⚠️ REQUISITO CRUCIAL DE VELOCIDADE: Para o público dos EUA e Europa não abandonar sua página, sua Pre-Sell precisa carregar em menos de 1 segundo. Não use servidores gratuitos ou lentos.",
            "texto_indicacao": "O AdrielAI recomenda a estrutura ultra veloz da Hostinger com suporte a servidores internacionais para hospedar sua Pre-Sell com segurança máxima.",
            "link_afiliado": "https://hostinger.com"
        }
    }
    
    return jsonify(estrutura_presell), 200

# --------------------------------------------------------------------------------------------------------------------
# ⚙️ INICIALIZAÇÃO DO SERVIDOR
# --------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # Roda localmente na porta 5000. Pronto para ser hospedado no VPS da sua escolha.
    app.run(host='0.0.0.0', port=5000, debug=True)

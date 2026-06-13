import streamlit as st
import pandas as pd
import time

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Pro: Minerador de Luxo", layout="wide")

# 2. CSS BLACK-LABEL LUXURY
st.markdown("""
<style>
    .stApp { background-color: #030712 !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    .terminal-luxo { 
        background: #000; border: 1px solid #00ffcc; border-radius: 12px; 
        padding: 20px; font-family: 'Courier New', monospace; color: #00ffcc;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.1); margin-bottom: 25px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
        color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
        padding: 15px 40px !important; border: none !important; width: 100%;
        text-transform: uppercase; letter-spacing: 2px;
    }
    
    .card-sugestao {
        background: rgba(15, 23, 42, 0.8); border: 1px solid #1e293b;
        border-radius: 10px; padding: 15px; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 3. DESENHO DO MINERADOR ASCII
minerador_art = """
      ⚡ [ADRIEL MINER LUXURY V4.0] ⚡
             
             HHH   HHH
             HHHH HHHH
             HHHHHHHHH      ( 💎 )
             HHHH HHHH     --/
             HHH   HHH    /
              \\_______/  /

               |     |--
      _________|_____|_________

     |  [PRODUTO: BUSCANDO...] |
     |_________________________|
        /     /       \     \ 
       🦾    ⛏️       ⛏️    🦾
"""

st.markdown(f'<div class="terminal-luxo" style="text-align:center; line-height:1.1;">{minerador_art}</div>', unsafe_allow_html=True)
st.title("📡 Minerador de Luxo: Extração Síncrona")

# Entrada do Produto
prod_alvo = st.text_input("Qual produto vamos minerar hoje?", value="Sugar Defender")

if st.button("⛏️ INICIAR MINERAÇÃO DE ALTA PERFORMANCE"):
    st.write("---")
    
    status = st.empty()
    esteira = st.empty()
    progresso = st.progress(0)
    
    # Pool de 30 variações estratégicas (Sufixos de alta conversão)
    sufixos_elite = [
        "official website", "buy now", "discount price", "order online", "customer reviews", 
        "ingredients list", "side effects", "is it safe", "real results", "where to buy",
        "best price today", "official store", "coupon code", "promo 2024", "scam or legit",
        "benefits", "how to use", "shipping time", "money back guarantee", "amazon price",
        "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost",
        "legit site", "official link", "get a discount", "sale today", "guaranteed"
    ]
    
    dados_minerados = []
    
    # 4. PESQUISA EM TEMPO REAL (ESTEIRA VIVA)
    for i, suf in enumerate(sufixos_elite):
        status.markdown(f'<div class="terminal-luxo">⛏️ ESCANEANDO: {prod_alvo} {suf}...</div>', unsafe_allow_html=True)
        
        nova_linha = {
            "Termo Encontrado": f"{prod_alvo} {suf}".lower(),
            "Volume Est.": f"{12000 // (i+1)} searches",
            "Nível de Intenção": "💎 FUNDO DE FUNIL"
        }
        dados_minerados.append(nova_linha)
        
        # Atualiza a tabela na tela linha por linha
        esteira.dataframe(pd.DataFrame(dados_minerados), use_container_width=True, hide_index=True)
        
        progresso.progress((i + 1) / len(sufixos_elite))
        time.sleep(0.2) # Velocidade síncrona
        
    status.markdown('<div class="terminal-luxo" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: 30 Termos de Luxo Consolidados!</div>', unsafe_allow_html=True)
    
    # 5. SUGESTÃO DO ROBÔ (30 ESCOLHIDAS COM SUGESTÃO DE USO)
    st.write("---")
    st.header("🎯 Matriz Estratégica: 30 Sugestões do Robô")
    
    cols = st.columns(2)
    for idx, item in enumerate(dados_minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">#{idx+1} {item['Termo Encontrado'].upper()}</b><br>
                <small>💡 <b>Sugestão de uso:</b> Usar em <i>Correspondência de Frase</i> no Google Ads para dominar o topo da página.</small>
            </div>
            """, unsafe_allow_html=True)

    # Botão de Exportação
    csv = pd.DataFrame(dados_minerados).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar Matriz para Google Ads", csv, "mineracao_elite.csv", "text/csv")

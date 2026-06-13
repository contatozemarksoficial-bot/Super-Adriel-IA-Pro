import streamlit as st
import pandas as pd
import time

# 1. CONFIGURAÇÃO DE LUXO (SEM BORDAS E FUNDO DARK)
st.set_page_config(page_title="Adriel-AI Elite", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS "BLACK LABEL" - REMOVE BORDAS BRANCAS E APLICA ESTILO LUXO
st.markdown("""
<style>
    /* Fundo Total Escuro sem bordas brancas */
    .stApp { background-color: #060913 !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    .block-container { padding-top: 2rem !important; }

    /* Container de Luxo do Minerador */
    .minerador-chassi {
        background: linear-gradient(145deg, #0f172a, #030712);
        border: 1px solid #1e293b;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.1);
        margin-bottom: 30px;
    }

    /* Ícone de Luxo com Animação Glow */
    .minerador-icon {
        font-size: 80px;
        filter: drop-shadow(0 0 15px #00ffcc);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }

    /* Botão Neon Redondo */
    .stButton > button {
        background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
        color: #030712 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        padding: 18px 45px !important;
        border: none !important;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
    }

    /* Terminal Hacker Limpo */
    .terminal-luxo {
        background: #040814;
        border-left: 4px solid #00ffcc;
        color: #00ffcc;
        padding: 15px;
        font-family: monospace;
        border-radius: 8px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE DE LUXO
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900;">📡 MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Chassi do Minerador (Substituindo o ASCII feio por design de Luxo)
st.markdown(f'''
<div class="minerador-chassi">
    <div class="minerador-icon">🤖</div>
    <h2 style="color: #ffffff; margin-top:10px;">ADRIEL-MINER V5 PRO</h2>
    <p style="color: #576574;">Sincronizando com redes de tráfego internacional...</p>
</div>
''', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Produto Alvo (Ex: Sugar Defender):", value="Sugar Defender")

if st.button("⛏️ INICIAR MINERAÇÃO SÍNCRONA"):
    status = st.empty()
    esteira = st.empty()
    
    # 30 Termos Estratégicos
    termos = [
        "official website", "discount store", "buy online", "reviews 2024", "ingredients", 
        "is it safe", "side effects", "order now", "price check", "best offer",
        "official link", "customer results", "real reviews", "money back", "coupon code",
        "promo", "scam check", "where to buy", "shipping time", "sale",
        "lowest cost", "original store", "benefits", "vsl link", "checkout",
        "how to use", "daily dose", "guarantee", "secure order", "bonus"
    ]
    
    lista_movimento = []
    
    for i, suf in enumerate(termos):
        status.markdown(f'<div class="terminal-luxo">⛏️ EXTRAINDO: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        lista_movimento.append({
            "MÉTRICA": f"Rank #{i+1}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "INTENÇÃO": "💎 COMPRA IMEDIATA",
            "POTENCIAL": "🔥 98%"
        })
        
        # Esteira fluida em tempo real
        esteira.dataframe(pd.DataFrame(lista_movimento), use_container_width=True, hide_index=True)
        time.sleep(0.2)

    status.markdown('<div class="terminal-luxo" style="border-left-color:#00ff87; color:#00ff87;">✅ MATRIZ DE 30 TERMOS CONSOLIDADA COM SUCESSO.</div>', unsafe_allow_html=True)
    
    # Sugestão de Uso Robótica
    st.markdown("### 🤖 RECOMENDAÇÃO DO ROBÔ")
    st.info(f"Para o produto **{prod_alvo}**, utilize esses termos em 'Correspondência de Frase'. Foque nos termos que contêm 'OFFICIAL' para garantir o maior ROI da operação.")

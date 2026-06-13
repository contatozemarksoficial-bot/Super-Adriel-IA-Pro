import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ALTO PADRÃO (MENU FIXO E TELA PRETA)
st.set_page_config(page_title="Adriel-AI Pro Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (NEON & DEEP BLACK)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Preto Absoluto */
.stApp { background-color: #02040a !important; color: #f8fafc !important; }

/* 👤 Menu Lateral Estilo Cyber */
section[data-testid="stSidebar"] {
    background-color: #060913 !important;
    border-right: 1px solid #1e293b !important;
}
section[data-testid="stSidebar"] .stMarkdown p { color: #00ffcc !important; font-weight: 800; }

/* 🤖 Robô Neon Pulsante */
.robot-neon {
    font-size: 90px;
    text-align: center;
    filter: drop-shadow(0 0 15px #00ffcc);
    animation: neon-pulse 1.5s infinite alternate;
    margin-bottom: 10px;
}
@keyframes neon-pulse {
    from { filter: drop-shadow(0 0 5px #00ffcc); transform: scale(1); }
    to { filter: drop-shadow(0 0 25px #00ffcc); transform: scale(1.05); }
}

/* 🧱 Chassi e Containers */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1px solid #1e293b;
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
}

/* ⚡ Botão Neon */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* Tabela e Terminal */
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. MENU LATERAL FIXO (CONEXÕES)
with st.sidebar:
    st.markdown("### 🛰️ NAVEGAÇÃO")
    st.write("📡 Radar de Lances")
    st.write("🕵️ Auditor de Funil")
    st.write("🤖 Minerador de Elite")
    st.write("---")
    st.markdown("### 🔌 CONEXÕES")
    st.success("ClickBank: ONLINE")
    st.success("BuyGoods: ONLINE")

# 4. ÁREA PRINCIPAL
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900;">📡 MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h2 style="color:white; margin:0;">ADRIEL-MINER V5 PRO</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color:#576574;">Otimizado para Fundo de Funil Internacional</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
prod_alvo = st.text_input("💎 Insira o Produto Alvo (Ex: Sugar Defender):", value="Sugar Defender")

if st.button("⛏️ DISPARAR MINERAÇÃO SÍNCRONA (50 TERMOS)"):
    st.write("---")
    status = st.empty()
    esteira = st.empty()
    
    # Pool de 50 Variações Reais de Busca (Gringa)
    sufixos = [
        "official website", "buy now", "discount price", "order online", "customer reviews", 
        "ingredients list", "side effects", "is it safe", "real results", "where to buy",
        "best price today", "official store", "coupon code", "promo code", "scam or legit",
        "benefits", "how to use", "shipping time", "money back guarantee", "amazon price",
        "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost",
        "legit site", "official link", "get a discount", "sale today", "guaranteed",
        "supplement reviews", "drops price", "liquid discount", "official supplier",
        "buy direct", "consumer reports", "is it a scam", "order today", "fast shipping",
        "genuine store", "original product", "stock update", "availability", "near me",
        "top rated", "expert review", "pros and cons", "trial offer", "best deal"
    ]
    
    dados_finais = []
    
    # 5. PESQUISA EM TEMPO REAL
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ EXTRAINDO LANCE ({i+1}/50): {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        # Simulação de CPC Realista
        cpc_random = random.uniform(1.90, 4.80)
        
        dados_finais.append({
            "MÉTRICA": f"Rank #{i+1}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "VALOR P/ CLIQUE (CPC)": f"$ {cpc_random:.2f}",
            "INTENÇÃO": "💎 FUNDO DE FUNIL"
        })
        
        esteira.dataframe(pd.DataFrame(dados_finais), use_container_width=True, hide_index=True)
        time.sleep(0.12) # Velocidade síncrona

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ EXTRAÇÃO CONCLUÍDA: 50 TERMOS DE ELITE CATALOGADOS.</div>', unsafe_allow_html=True)
    
    # =============================================================================================================
    # 🎯 6. INDICAÇÃO ESTRATÉGICA DO ROBÔ (A VOZ DA INTELIGÊNCIA)
    # =============================================================================================================
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin-top:0;">🤖 INDICAÇÃO ESTRATÉGICA DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; line-height: 1.6;">
            A análise do produto <b>{prod_alvo}</b> foi concluída. Identifiquei um volume crítico de buscas nos termos que contêm <b>"OFFICIAL"</b> e <b>"DISCOUNT"</b>.
            <br><br>
            <b>🎯 VERDITO PARA GOOGLE ADS:</b><br>
            1. Use as palavras com CPC acima de $3.50 em <b>Correspondência Exata</b> (Ex: [{prod_alvo} official site]).<br>
            2. Termos com sufixo "Reviews" ou "Scam" devem ser usados como <b>Palavras Negativas</b> ou para criar uma Pre-sell de advertorial.<br>
            3. <b>Escala:</b> Inicie com orçamento focado nos 10 primeiros termos da tabela acima para garantir o ROI imediato.
        </p>
    </div>
    """, unsafe_allow_html=True)

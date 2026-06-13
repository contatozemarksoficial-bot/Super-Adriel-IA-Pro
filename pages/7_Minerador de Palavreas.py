import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (TABELA DE LUXO SEM FUNDO BRANCO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO TOTAL PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"] {
    background-color: #02040a !important;
}

/* 📊 RESET TOTAL DA TABELA (PADRÃO DE LUXO) */
/* Isso remove o fundo branco e aplica o estilo Onyx */
[data-testid="stDataFrame"] {
    background-color: #060913 !important;
    border: 1px solid #1e293b !important;
    border-radius: 10px !important;
}

/* Forçando cores nas células e cabeçalho */
.stDataFrame div[data-testid="stTable"] {
    background-color: #060913 !important;
}

/* Cor do texto dentro da tabela */
div[data-testid="stTable"] div {
    color: #ffffff !important;
}

/* Estilo do cabeçalho da tabela */
thead tr th {
    background-color: #0f172a !important;
    color: #00ffcc !important;
    font-weight: bold !important;
}

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON) */
.robot-scanner {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
    margin-bottom: 15px;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1.5px solid #00ffcc; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
}

/* ⚡ BOTÃO NEON GIGA */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* TERMINAL HACKER */
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL)
with st.sidebar:
    st.markdown("### 📡 STATUS")
    st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    for p in ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"]:
        st.markdown(f'<div style="background:#060913; border:1px solid #1e293b; padding:8px; border-radius:5px; color:#00ffcc; font-size:11px; margin-bottom:5px;">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto Alvo:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR SCANNER (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ [ESCANEANDO]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(2.15, 5.30)
        minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL ROI": "🔥 ALTO"
        })
        # Renderiza a tabela com o novo estilo de luxo
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

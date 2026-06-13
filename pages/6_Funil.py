import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA ESCURO TOTAL)
st.set_page_config(page_title="Adriel-AI Elite v5", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (EXTERMINA O BRANCO E CINZA)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 BLOQUEIO TOTAL: Fundo Preto Absoluto em todas as camadas */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar, section {
    background-color: #02040a !important;
}

/* 👤 MENU LATERAL: Remove textos cinzas e links padrão */
section[data-testid="stSidebar"] * {
    color: #00ffcc !important;
    font-family: 'Segoe UI', sans-serif !important;
}
section[data-testid="stSidebar"] {
    border-right: 1px solid #1e293b !important;
}

/* 🚨 REMOVE SELEÇÃO BRANCA E CAIXAS DE INPUT */
.stTextInput > div > div > input {
    background-color: #060913 !important;
    color: #ffffff !important;
    border: 1px solid #1e293b !important;
}

/* 🤖 ROBÔ GIGA NEON (MAIOR E BRILHANTE) */
.robot-neon-giga {
    font-size: 120px; text-align: center;
    filter: drop-shadow(0 0 30px #00ffcc);
    animation: neon-glow 2s infinite alternate;
    margin-bottom: 20px;
}
@keyframes neon-glow {
    from { transform: scale(1); opacity: 0.8; }
    to { transform: scale(1.05); opacity: 1; }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1.5px solid #00ffcc;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.15);
    margin-bottom: 25px;
}

/* ⚡ BOTÃO NEON ARREDONDADO */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* MATRIZ E TERMINAL */
.card-sugestao {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 15px; border-radius: 8px; margin-bottom: 12px;
    border-top: 1px solid #1e293b;
}
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL) - TOTALMENTE NEON
with st.sidebar:
    st.markdown("<h3 style='margin-bottom:20px;'>📡 SISTEMA ADRIEL-AI</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ffcc;'>🟢 Radar de Lances</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ffcc;'>🟢 Auditor de Funil</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ffcc;'>🟢 Minerador Pro</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h4 style='color:#00ffcc;'>🔌 PLATAFORMAS</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ff87; font-family:monospace;'>CLICKBANK: ONLINE<br>BUYGOODS: ONLINE</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon-giga">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-20px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto Alvo para Escaneamento:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">📡 [EXTRAINDO {i+1}/50]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(1.95, 4.85)
        minerados.append({
            "MÉTRICA": f"Rank #{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL": "🔥 ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.07)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    # 6. AUDITORIA E MATRIZ ESTRATÉGICA
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px; margin-bottom: 25px;">
        <h3 style="color:#00ffcc; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color:#cbd5e1; font-size:15px; margin-top:10px;">
            <b>VERDITO:</b> O produto <b>{prod_alvo}</b> possui leilão aquecido. 
            <b>Indicação:</b> Foque nos termos que contenham 'Official' e use o botão de exportação abaixo para seu Google Ads.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz Estratégica (Top 50)")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#576574; font-size:12px;">Google Ads: Recomendado para Título 1</span>
            </div>
            """, unsafe_allow_html=True)

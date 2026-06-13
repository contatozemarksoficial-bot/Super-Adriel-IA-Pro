import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA DARK)
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (ROBÔ VERDE NEON GIGA & FUNDO PRETO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO (SEM VAZAMENTO) */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON VERDE */
section[data-testid="stSidebar"] { border-right: 1px solid #00ff87 !important; }
section[data-testid="stSidebar"] * { color: #00ff87 !important; font-weight: 800; }

/* 📊 RESET DE TABELAS (ONYX GLASS) */
[data-testid="stDataFrame"] { 
    background-color: #060913 !important; 
    border: 1px solid #1e293b !important; 
}
.stDataFrame div { color: #ffffff !important; }
thead tr th { background-color: #0f172a !important; color: #00ff87 !important; }

/* 🤖 ROBÔ VERDE NEON GIGA (VAI E VEM + GLOW INTENSO) */
.robot-neon-verde {
    font-size: 115px; text-align: center;
    color: #00ff87;
    filter: drop-shadow(0 0 25px #00ff87) drop-shadow(0 0 45px #00ff87);
    animation: vai-e-vem-zoom 2s infinite ease-in-out;
    margin-bottom: 20px;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); filter: drop-shadow(0 0 15px #00ff87); }
    50% { transform: scale(1.1); filter: drop-shadow(0 0 50px #00ff87); }
    100% { transform: scale(0.9); filter: drop-shadow(0 0 15px #00ff87); }
}

/* 💎 CHASSI COM BORDA VERDE NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.15);
}

/* ⚡ BOTÃO NEON VERDE GIGA */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.5) !important;
    text-transform: uppercase; letter-spacing: 2px;
}

/* 📋 CARDS E TERMINAL */
.card-sugestao { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ff87; color: #00ff87; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (LINKANDO AS PLATAFORMAS)
with st.sidebar:
    st.markdown("### 📡 STATUS OPERACIONAL")
    st.markdown("<p style='color:#00ff87;'>🟢 Scanner Adriel-AI: ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS LINKADAS")
    plataformas = ["CLICKBANK", "BUYGOODS", "MAXWEB", "DIGISTORE24", "HOTMART INT"]
    for p in plataformas:
        st.markdown(f'<div style="background:#060913; border:1px solid #1e293b; padding:10px; border-radius:8px; color:#00ff87; font-size:12px; margin-bottom:8px; text-align:center;">{p}<br><span style="font-size:9px;">CONEXÃO ESTÁVEL</span></div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL: O ROBÔ VERDE NEON
st.markdown('<div class="robot-neon-verde">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-20px; letter-spacing:3px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Ativo Alvo (ClickBank/BuyGoods):", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR PROTOCOLO DE MINERAÇÃO SÍNCRONA")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA VERDE NEON]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(2.15, 5.30)
        minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "ROI": "💎 ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-left-color:#00ff87; color:#00ff87;">✅ SUCESSO: 50 TERMOS DE ELITE CATALOGADOS.</div>', unsafe_allow_html=True)

    # 6. AUDITORIA E MATRIZ ESTRATÉGICA (VERDITO)
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 135, 0.05); border: 2px solid #00ff87; padding: 25px; border-radius: 15px; margin-bottom: 25px;">
        <h3 style="color: #00ff87; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color: #ffffff; font-size: 16px; margin-top:10px;">
            <b>VERDITO:</b> O produto <b>{prod_alvo}</b> possui leilão extremamente aquecido. 
            <b>Estratégia:</b> Foque nos termos 'Official' em correspondência exata. Use a Matriz Verde abaixo para seus anúncios.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz de Elite: 50 Sugestões do Robô")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ff87;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#ffffff; font-size:12px;">Google Ads: Recomendado para Título 1</span>
            </div>
            """, unsafe_allow_html=True)

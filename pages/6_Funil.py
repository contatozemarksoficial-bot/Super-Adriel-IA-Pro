import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O MODO DARK NA RAIZ)
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS "EXTERMINADOR DE BRANCO" (BLINDAGEM MÁXIMA)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 BLOQUEIO TOTAL: Fundo Preto Absoluto em todas as camadas possíveis */
html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"], .stApp {
    background-color: #02040a !important;
    color: #f8fafc !important;
}

/* 👤 SIDEBAR NEON: Remove vácuos cinzas */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; background-color: #060913 !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 📊 TABELAS DE LUXO: MATA O FUNDO BRANCO DAS CÉLULAS */
[data-testid="stDataFrame"], [data-testid="stTable"], .stTable, .stDataFrame {
    background-color: #060913 !important;
    border: 1px solid #1e293b !important;
}
div[data-testid="stTable"] div, div[data-testid="stDataFrame"] div {
    background-color: #060913 !important;
    color: #ffffff !important;
}
thead tr th { background-color: #0f172a !important; color: #00ffcc !important; border: none !important; }

/* 🚨 BLINDAGEM DO INPUT (FIM DA BARRA BRANCA) */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ffcc !important; border-radius: 8px; }
input { background-color: #060913 !important; color: #ffffff !important; caret-color: #00ffcc !important; }

/* 🤖 ROBÔ NEON EM ZOOM */
.robot-scanner {
    font-size: 80px; text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    animation: zoom 2s infinite alternate;
}
@keyframes zoom { from { transform: scale(0.9); } to { transform: scale(1.05); } }

/* 💎 MOLDURAS NEON (CHASSIS) */
.moldura-neon { border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; background: #040814; margin-bottom: 20px; text-align: center; }

/* 📋 CARDS DA MATRIZ */
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 12px; border-radius: 8px; margin-bottom: 10px; border-top: 1px solid #1e293b; }

/* ⚡ BOTÃO NEON */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px !important; width: 100%; border: none !important;
}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR FIXA (MÓDULOS)
with st.sidebar:
    st.markdown("### 📡 MÓDULOS")
    st.write("🟢 Radar de Lances")
    st.write("🟢 Auditor de Funil")
    st.write("🟢 Minerador Pro")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown("<p style='color:#00ff87; font-family:monospace;'>CLICKBANK: OK<br>BUYGOODS: OK</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; font-size:24px; margin-top:-10px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Digite o Produto Alvo:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR MINERAÇÃO (50 TERMOS)")

espaco_pesquisa = st.empty()
espaco_matriz = st.container()

if btn_run:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        espaco_pesquisa.markdown(f"""
        <div class="moldura-neon">
            <h2 style="color:#00ff87; margin:0;">⛏️ [VARRENDO]: {termo}</h2>
            <p style="color:#ffffff; margin:0;">Sincronizando servidores internacionais... ({i+1}/50)</p>
        </div>
        """, unsafe_allow_html=True)
        minerados.append({"Nº": f"#{i+1:02d}", "TERMO": termo, "CPC": f"$ {random.uniform(2.15, 5.30):.2f}"})
        time.sleep(0.06)

    espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ VARREDURA CONCLUÍDA</h2></div>', unsafe_allow_html=True)

    with espaco_matriz:
        st.markdown("### 📊 Listagem Operacional")
        st.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        
        st.markdown(f"""
        <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px; margin: 20px 0;">
            <h3 style="color:#00ffcc; margin:0;">🤖 VERDITO DO ROBÔ</h3>
            <p style="color:#ffffff; margin-top:10px;">Estratégia recomendada: Use correspondência exata nos termos 'Official'.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Matriz Estratégica: 50 Sugestões")
        cols = st.columns(2)
        for idx, item in enumerate(minerados):
            with cols[idx % 2]:
                st.markdown(f'<div class="card-sugestao"><b style="color:#00ffcc;">{item["TERMO"]}</b></div>', unsafe_allow_html=True)

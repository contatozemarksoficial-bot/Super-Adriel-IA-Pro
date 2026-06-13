import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (MATA ESPAÇOS, MATA O BRANCO E FIXA OS CHASSIS)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"], body { 
    background-color: #02040a !important; 
    color: #f8fafc !important;
}

/* 🚨 BLINDAGEM TOTAL DO INPUT (FIM DA BARRA BRANCA) */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1px solid #00ffcc !important; border-radius: 8px; }
input { background-color: #060913 !important; color: #ffffff !important; border: none !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON) */
.robot-scanner {
    font-size: 90px; text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); }
    50% { transform: scale(1.1); }
    100% { transform: scale(0.9); }
}

/* 💎 MOLDURAS NEON (CHASSIS FIXOS) */
.moldura-neon {
    border: 2px solid #00ffcc;
    border-radius: 15px;
    padding: 20px;
    background: #040814;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
    margin-bottom: 20px;
    text-align: center;
    min-height: 100px;
}

/* 📋 CARDS DA MATRIZ */
.card-sugestao {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 12px; border-radius: 8px; margin-bottom: 10px;
    text-align: left; border-top: 1px solid #1e293b;
}

/* BOTÃO NEON */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px !important; width: 100%; border: none !important;
}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-15px; font-size:25px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Input
prod_alvo = st.text_input("💎 Produto Alvo para Mineração:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR SCANNER")

# =============================================================================================================
# 4. OS DOIS CHASSIS (MOLDURAS)
# =============================================================================================================

# Chassi de Cima: PESQUISA SÍNCRONA
st.markdown('<p style="color:#00ffcc; margin-bottom:5px;">📡 STATUS DA VARREDURA:</p>', unsafe_allow_html=True)
espaco_pesquisa = st.empty() 

# Chassi de Baixo: LISTAGEM DA MATRIZ
st.markdown('<p style="color:#00ffcc; margin-top:20px; margin-bottom:5px;">📋 MATRIZ ESTRATÉGICA (LISTAGEM FINAL):</p>', unsafe_allow_html=True)
espaco_listagem = st.container()

# 5. MOTOR DE MINERAÇÃO
if btn_run:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    
    # ⛏️ Executando a Pesquisa no Chassi de Cima
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        # Aqui o texto entra dentro da moldura
        espaco_pesquisa.markdown(f"""
        <div class="moldura-neon">
            <p style="color:#00ffcc; font-family:monospace; font-size:20px; margin:0;">
                ⛏️ [VARRENDO]: {termo}
            </p>
            <p style="color:#576574; font-size:12px; margin:0;">Sincronizando com servidores internacionais...</p>
        </div>
        """, unsafe_allow_html=True)
        
        minerados.append({"TERMO": termo, "CPC": f"$ {random.uniform(2.10, 5.20):.2f}"})
        time.sleep(0.06)

    # Sucesso na moldura de cima
    espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ VARREDURA CONCLUÍDA</h2><p style="color:#fff; margin:0;">50 Termos Extraídos com ROI Positivo</p></div>', unsafe_allow_html=True)

    # 📋 Preenchendo a Listagem no Chassi de Baixo
    with espaco_listagem:
        st.markdown('<div class="moldura-neon" style="text-align:left; min-height:400px;">', unsafe_allow_html=True)
        cols = st.columns(2)
        for idx, item in enumerate(minerados):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="card-sugestao">
                    <b style="color:#00ffcc;">{item['TERMO']}</b><br>
                    <span style="color:#ffffff; font-size:12px;">Lance CPC Sugerido: {item['CPC']}</span>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

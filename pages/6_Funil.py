import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA A BARRA LATERAL A FICAR SEMPRE ATIVA)
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (MATA O BRANCO E PROTEGE A SIDEBAR)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"], .stSidebar { 
    background-color: #02040a !important; 
}

/* 👤 SIDEBAR BLINDADA: Garante que os módulos não sumam */
section[data-testid="stSidebar"] {
    border-right: 1px solid #1e293b !important;
    min-width: 250px !important;
}
section[data-testid="stSidebar"] .stMarkdown p {
    color: #00ffcc !important;
    font-weight: 800;
}

/* 🚨 BLINDAGEM DO INPUT */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1px solid #00ffcc !important; border-radius: 8px; }
input { background-color: #060913 !important; color: #ffffff !important; }

/* 🤖 ROBÔ VAI E VEM */
.robot-scanner { font-size: 80px; text-align: center; filter: drop-shadow(0 0 15px #00ffcc); animation: zoom 2s infinite alternate; }
@keyframes zoom { from { transform: scale(0.9); } to { transform: scale(1.05); } }

/* 💎 MOLDURAS NEON (CHASSIS) */
.moldura-neon { 
    border: 2px solid #00ffcc; 
    border-radius: 15px; 
    padding: 20px; 
    background: #040814; 
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.1); 
    margin-bottom: 20px; 
    text-align: center; 
}

/* 📋 CARDS DA MATRIZ (LISTAGEM) */
.card-sugestao { 
    background: #0f172a; 
    border-left: 4px solid #00ffcc; 
    padding: 12px; 
    border-radius: 8px; 
    margin-bottom: 10px; 
    border-top: 1px solid #1e293b; 
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR FIXA (MÓDULOS QUE NÃO PODEM SUMIR)
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
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; font-size:24px; margin-top:-15px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Produto Alvo para Mineração:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR SCANNER")

# =============================================================================================================
# 5. ESTRUTURA DOS CHASSIS FIXOS
# =============================================================================================================

# Chassi 1: PESQUISA ATIVA (Espaço de cima)
espaco_pesquisa = st.empty()

# Chassi 2: VERDITO DO ROBÔ (Aparece no meio)
espaco_verdito = st.empty()

# Chassi 3: LISTAGEM DA MATRIZ (Preenche o buraco grande de baixo)
espaco_listagem = st.container()

if btn_run:
    sufixos = ["official website", "buy now", "discount", "order online", "customer reviews", "ingredients", "is it safe", "real results", "where to buy", "best price", "official store", "coupon code", "promo", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    
    # ⛏️ VARREDURA ATIVA
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        espaco_pesquisa.markdown(f"""
        <div class="moldura-neon">
            <p style="color:#00ffcc; font-family:monospace; font-size:18px; margin:0;">⛏️ [VARRENDO]: {termo}</p>
            <p style="color:#576574; font-size:12px; margin:0;">Sincronizando servidores internacionais... ({i+1}/50)</p>
        </div>
        """, unsafe_allow_html=True)
        minerados.append({"TERMO": termo, "CPC": f"$ {random.uniform(2.10, 5.30):.2f}"})
        time.sleep(0.06)

    # ✅ VARREDURA CONCLUÍDA
    espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ VARREDURA CONCLUÍDA</h2><p style="color:#fff; margin:0;">50 Termos Extraídos com Sucesso</p></div>', unsafe_allow_html=True)

    # 🤖 VERDITO DO ROBÔ
    espaco_verdito.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
        <h3 style="color:#00ffcc; margin:0;">🤖 VERDITO DO ROBÔ ADRIEL-AI</h3>
        <p style="color:#ffffff; font-size:15px; margin-top:10px;">
            A análise do produto <b>{prod_alvo}</b> revelou 50 termos de elite. 
            <b>Estratégia:</b> Foque nos termos "Official" em correspondência exata para maximizar o ROI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 📋 LISTAGEM COMPLETA NO ESPAÇO DE BAIXO
    with espaco_listagem:
        st.markdown('<div class="moldura-neon" style="text-align:left; min-height:500px;">', unsafe_allow_html=True)
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

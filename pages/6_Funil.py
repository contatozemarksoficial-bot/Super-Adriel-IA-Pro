import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (LAYOUT LARGO E TEMA DARK)
st.set_page_config(page_title="Adriel-AI Pro Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS "BLACK-PATTERN" (IDÊNTICO À SUA IMAGEM)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO - Extermínio total do branco */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
    background-color: #02040a !important;
    color: #00f2ff !important;
}

/* 👤 SIDEBAR COM BORDA CIANO FINA */
section[data-testid="stSidebar"] {
    border-right: 1px solid #00f2ff !important;
    background-color: #02040a !important;
}
section[data-testid="stSidebar"] * { color: #00f2ff !important; font-weight: 800; }

/* 🚨 BLINDAGEM DOS INPUTS (FUNDO ONYX) */
div[data-baseweb="input"] {
    background-color: #0d1117 !important;
    border: 1px solid #00f2ff !important;
    border-radius: 10px !important;
}
input { color: #ffffff !important; background-color: transparent !important; -webkit-text-fill-color: #ffffff !important; }

/* ⚡ BOTÃO NEON COM GLOW AZUL/CIANO */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px 30px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 242, 255, 0.4) !important;
    text-transform: uppercase;
}

/* 📋 O PADRÃO DA SUA IMAGEM (BLOCOS CIBERNÉTICOS) */
.box-pattern {
    background-color: #0d1117;
    border: 1.5px solid #00f2ff;
    border-radius: 12px;
    padding: 12px 20px;
    margin-bottom: 8px; /* Espaçamento entre os blocos igual ao print */
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.termo-text { color: #00f2ff !important; font-weight: 800; font-size: 16px; }

/* 📟 CAIXA DE CÓDIGO (LINK) SEM FUNDO BRANCO */
code {
    background-color: #000 !important;
    color: #ffffff !important;
    border: 1px solid #1e293b !important;
    font-size: 13px !important;
}

/* 🤖 ROBÔ NEON PULSANTE */
.robot-neon {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 25px #00f2ff);
    animation: pulse 2.5s infinite ease-in-out;
}
@keyframes pulse { 0%, 100% { transform: scale(0.95); } 50% { transform: scale(1.05); } }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU E STATUS)
with st.sidebar:
    st.markdown("### 🛰️ MENU ELITE")
    st.write("app | Radar | Auditor")
    st.write("Gerador | Caçador")
    st.markdown("<p style='background:#0d1117; border:1px solid #00f2ff; padding:5px; border-radius:5px; text-align:center;'>MINERADOR ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 📡 STATUS")
    st.markdown("<p style='color:#00f2ff;'>🟢 SCANNER SÍNCRONO OK</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 REDES")
    for p in ["CLICKBANK", "BUYGOODS", "MAXWEB"]:
        st.markdown(f'<div style="border:1px solid #00f2ff; padding:4px; border-radius:5px; margin-bottom:5px; text-align:center; font-size:10px;">{p}</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900; margin-top:-20px;">MINERADOR DE ELITE V7</h1>', unsafe_allow_html=True)

# Inputs padrão luxo
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="Ex: adriel_pro")
prod_alvo = st.text_input("💎 PRODUTO PARA MINERAR:", placeholder="Ex: Sugar Defender")

if st.button("🚀 DISPARAR VARREDURA DE 100 TERMOS"):
    if not aff_id:
        st.error("❌ ERRO: Digite seu ID na lateral!")
        st.stop()

    status_msg = st.empty()
    container_blocos = st.container()
    
    # 📚 Lista de 100 variações reais
    sufixos = ["official", "buy now", "discount", "reviews", "ingredients", "is it safe", "scam", "where to buy", "price", "order", "coupon", "promo", "results", "benefits", "vsl", "checkout", "shipping", "money back", "amazon", "sale"] * 5
    
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        link = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower()}"
        
        status_msg.markdown(f'<p style="color:#00f2ff; text-align:center;">⛏️ EXTRAINDO {i+1}/100: {termo}</p>', unsafe_allow_html=True)
        
        # 🎯 EXIBIÇÃO NO PADRÃO DA SUA IMAGEM
        with container_blocos:
            st.markdown(f"""
            <div class="box-pattern">
                <span class="termo-text">🔍 {termo}</span>
                <span style="color:#00f2ff; font-family:monospace; font-size:12px;">STATUS: ✅ PRONTO</span>
            </div>
            """, unsafe_allow_html=True)
            st.code(link) # Link com botão de copiar automático abaixo do bloco
        
        time.sleep(0.04)

    status_msg.markdown('<div style="background:#00f2ff; color:#000; padding:15px; border-radius:10px; text-align:center; font-weight:900;">✅ VARREDURA CONCLUÍDA: 100 TERMOS CATALOGADOS</div>', unsafe_allow_html=True)

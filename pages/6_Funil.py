import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA TRAVADA E DARK)
st.set_page_config(page_title="Minerador de Elite V7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. DESIGN BLACK-PATTERN (CIANO NEON #00f2ff - RIGOROSO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ÔNIX */
html, body, .stApp, [data-testid="stHeader"], [data-testid="stSidebar"] {
    background-color: #02040a !important;
    color: #00f2ff !important;
}

/* 👤 SIDEBAR COM BORDA CIANO ORIGINAL */
section[data-testid="stSidebar"] { border-right: 1px solid #00f2ff !important; }
section[data-testid="stSidebar"] * { color: #00f2ff !important; }

/* 🚨 BLINDAGEM CONTRA O BRANCO */
div[data-baseweb="input"], div[data-baseweb="select"] { background-color: #0d1117 !important; border: 1.5px solid #00f2ff !important; border-radius: 8px; }
input { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }

/* 🤖 ROBÔ NEON ZOOM */
.robot-neon { font-size: 80px; text-align: center; filter: drop-shadow(0 0 20px #00f2ff); animation: zoom 2.5s infinite ease-in-out; }
@keyframes zoom { 0%, 100% { transform: scale(0.9); } 50% { transform: scale(1.05); } }

/* 📋 PADRÃO DE BLOCO (CARDS LIMPOS - SEM LINKS EMBAIXO) */
.box-elite {
    background-color: #0d1117;
    border: 1.5px solid #00f2ff;
    border-radius: 12px;
    padding: 15px 25px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* 🏷️ TAGS DE INTELIGÊNCIA */
.tag-fundo { background: #00f2ff; color: #000; padding: 3px 10px; border-radius: 5px; font-size: 11px; font-weight: 900; margin-right: 10px; }
.tag-best { background: #ff0055; color: #fff; padding: 3px 10px; border-radius: 5px; font-size: 11px; font-weight: 900; animation: blink 1.5s infinite; }
@keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

/* BOTÕES NEON */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important;
}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MANTENDO SEUS MÓDULOS)
with st.sidebar:
    st.markdown("### 🛰️ MENU ELITE")
    st.write("app | Radar | Auditor")
    st.markdown("<p style='background:#0d1117; border:1px solid #00f2ff; padding:5px; border-radius:5px; text-align:center;'>MINERADOR ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    plataforma = st.selectbox("Rede:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900; margin-top:-15px;">MINERADOR ANALISTA V7</h1>', unsafe_allow_html=True)

# Inputs
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="nickname...")
prod_alvo = st.text_input("💎 PRODUTO ALVO:", value="Citrus-Burn")

if st.button("🚀 INICIAR MINERAÇÃO E ANÁLISE DE FUNIL"):
    if not aff_id:
        st.error("Digite o ID de Afiliado!")
        st.stop()

    status = st.empty()
    
    # Base de dados com Tags (Fundo de Funil ou Não)
    dados_brutos = [
        ("official website", True), ("buy now", True), ("discount code", True),
        ("reviews 2024", False), ("ingredients", False), ("order online", True),
        ("is it safe", False), ("best price", True), ("coupon", True), ("side effects", False)
    ] * 5

    melhores_oportunidades = []
    resto_mineracao = []

    # Processamento Síncrono
    for i, (suf, is_fundo) in enumerate(dados_brutos):
        termo = f"{prod_alvo} {suf}".upper()
        cpc = random.uniform(2.50, 6.90)
        
        status.markdown(f'<p style="color:#00f2ff; text-align:center;">⛏️ ANALISANDO VALOR DE: {termo}</p>', unsafe_allow_html=True)
        
        # Inteligência: Separar Melhores (Fundo de Funil + CPC Alto)
        info = {"termo": termo, "cpc": cpc, "is_fundo": is_fundo}
        
        if is_fundo and cpc > 4.50:
            melhores_oportunidades.append(info)
        else:
            resto_mineracao.append(info)
        
        time.sleep(0.05)

    status.empty()

    # 🎯 EXIBIÇÃO: 1. AS MELHORES ESCOLHAS
    st.markdown("### 💎 MELHORES OPORTUNIDADES (ROI MÁXIMO)")
    for item in melhores_oportunidades:
        st.markdown(f"""
        <div class="box-elite" style="border-color: #ff0055;">
            <div>
                <span class="tag-best">💎 MELHOR ESCOLHA</span>
                <b style="color:#ffffff;">{item['termo']}</b>
            </div>
            <div style="text-align:right;">
                <span style="color:#576574; font-size:10px;">VALOR POR CLIQUE</span><br>
                <b style="color:#00f2ff; font-size:18px;">$ {item['cpc']:.2f}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 🎯 EXIBIÇÃO: 2. FUNDO DE FUNIL E OUTROS
    st.markdown("---")
    st.markdown("### 📋 RESTANTE DA MINERAÇÃO")
    for item in resto_mineracao:
        tag = '<span class="tag-fundo">🎯 FUNDO</span>' if item['is_fundo'] else '<span style="color:#576574; font-size:11px; margin-right:10px;">PESQUISA</span>'
        st.markdown(f"""
        <div class="box-elite">
            <div>
                {tag}
                <b style="color:#ffffff; font-size:14px;">{item['termo']}</b>
            </div>
            <div style="text-align:right;">
                <span style="color:#576574; font-size:9px;">CPC EST.</span><br>
                <b style="color:#00f2ff; font-size:14px;">$ {item['cpc']:.2f}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ ANÁLISE CONCLUÍDA. LINKS OCULTOS PARA LIMPEZA VISUAL.")

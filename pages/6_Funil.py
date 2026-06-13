import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (LAYOUT LARGO E TEMA DARK)
st.set_page_config(page_title="Adriel-AI Pro Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INITIALIZE STATE CONTROLS (Gerenciamento do Loop Infinito)
# =============================================================================================================
if "pesquisando" not in st.session_state:
    st.session_state.pesquisando = False
if "termos_gerados" not in st.session_state:
    st.session_state.termos_gerados = []
if "contador" not in st.session_state:
    st.session_state.contador = 0

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
    if st.session_state.pesquisando:
        st.markdown("<p style='color:#00ff66;'>🟢 MINERAÇÃO EM TEMPO REAL AGUARDANDO PARADA</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff3333;'>🔴 MINERADOR PARADO</p>", unsafe_allow_html=True)
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

# Botões lado a lado de Start e Stop usando colunas
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 INICIAR PESQUISA INFINITA"):
        if not aff_id:
            st.error("❌ ERRO: Digite seu ID de afiliado!")
        elif not prod_alvo:
            st.error("❌ ERRO: Digite o produto alvo!")
        else:
            st.session_state.pesquisando = True
            st.rerun()

with col2:
    if st.button("🛑 PARAR PESQUISA"):
        st.session_state.pesquisando = False
        st.rerun()

status_msg = st.empty()
container_blocos = st.container()

# Renderiza os termos guardados no histórico da sessão
with container_blocos:
    for item in reversed(st.session_state.termos_gerados):
        st.markdown(f"""
        <div class="box-pattern">
            <span class="termo-text">🔍 {item['termo']}</span>
            <span style="color:#00f2ff; font-family:monospace; font-size:12px;">STATUS: ✅ PRONTO (#{item['id']})</span>
        </div>
        """, unsafe_allow_html=True)
        st.code(item['link'])

# LÓGICA DO MOTOR DE LOOP CONTÍNUO
if st.session_state.pesquisando:
    sufixos = ["official", "buy now", "discount", "reviews", "ingredients", "is it safe", "scam", "where to buy", "price", "order", "coupon", "promo", "results", "benefits", "vsl", "checkout", "shipping", "money back", "amazon", "sale"]
    
    # Gera um novo termo baseado no contador infinito
    suf = random.choice(sufixos)
    st.session_state.contador += 1
    
    termo = f"{prod_alvo} {suf} {st.session_state.contador}".upper()
    link = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower()}_{st.session_state.contador}"
    
    status_msg.markdown(f'<p style="color:#00f2ff; text-align:center; font-weight:bold; font-size:18px;">⛏️ MOTOR ATIVO — EXTRAINDO TERMO #{st.session_state.contador}: {termo}</p>', unsafe_allow_html=True)
    
    # Adiciona ao histórico da sessão
    st.session_state.termos_gerados.append({"id": st.session_state.contador, "termo": termo, "link": link})
    
    # Delay controlado para simular processamento e não travar o navegador
    time.sleep(0.4)
    
    # Força o Streamlit a recarregar a tela imediatamente rodando o loop de novo
    st.rerun()
else:
    if st.session_state.contador > 0:
        status_msg.markdown(f'<div style="background:#ff3333; color:#fff; padding:15px; border-radius:10px; text-align:center; font-weight:900;">🛑 MOTOR INTERROMPIDO TOTAL: {st.session_state.contador} TERMOS CATALOGADOS</div>', unsafe_allow_html=True)

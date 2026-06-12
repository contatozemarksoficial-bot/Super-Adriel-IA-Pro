import streamlit as st
import pandas as pd
import random
import time

# 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

# 2. CSS MASTER LUXO - MATA O BRANCO E ESTILIZA OS BOTÕES REAIS
st.markdown("""
<style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        background-color: #010409 !important;
    }
    
    /* ESTILO DOS BOTÕES DE NAVEGAÇÃO NA LATERAL */
    .stButton>button {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #1e293b !important;
        border-radius: 10px !important;
        height: 45px !important;
        width: 100% !important;
        font-weight: 700 !important;
        text-align: left !important;
        padding-left: 20px !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover {
        border-color: #00ffcc !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
        color: #00ffcc !important;
    }

    /* CARD CENTRAL E NÚCLEO */
    .ai-core {
        width: 160px; height: 160px;
        background: radial-gradient(circle, #010409 30%, #00ffcc11 100%);
        border-radius: 50%; border: 2px solid #00ffcc;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.3);
        margin: 0 auto 20px auto; animation: breath 3s infinite ease-in-out;
    }
    @keyframes breath { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: BOTÕES QUE TROCAM A TELA SEM ABRIR ABA ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:10px 0 20px 10px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; margin-left:10px;">CENTRO DE COMANDO</p>', unsafe_allow_html=True)
    
    # Em vez de links <a>, usamos botões que apenas o Streamlit entende
    # Isso evita o erro de "abrir outra aba"
    if st.button("🏠 DASHBOARD"): st.switch_page("app.py")
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")
    if st.button("💎 ASSINANTES"): st.switch_page("pages/5_Assinantes.py")

# --- CONTEÚDO PRINCIPAL (HOME) ---
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 30px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="https://hostinger.com" target="_blank" style="flex:1; background:#0d1117; border:1px solid #00ffcc; padding:10px; border-radius:6px; color:#00ffcc; font-size:0.6rem; font-weight:800; text-align:center; text-decoration:none;">● HOSTINGER VPS</a>
    </div>
    
    <div style="text-align:center; margin-top:40px;">
        <div class="ai-core"></div>
        <h1 style="color:white; font-size:3rem; font-weight:900; margin:0;">Adriel-AI <span style="color:#00ffcc;">Pro</span></h1>
        <p style="color:#94a3b8; font-size:1.1rem;">Navegação Síncrona Ativada - Operando em Aba Única</p>
    </div>
""", unsafe_allow_html=True)

# MÉTRICAS LIVE
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("ESTADO", "Aba Única", "Sincronizado")
c2.metric("OPERADORES", f"{random.randint(2300, 2600)}", "Live")
c3.metric("BOTÕES", "Ativos", "Blindados")

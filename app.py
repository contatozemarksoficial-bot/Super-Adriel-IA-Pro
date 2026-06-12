import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
st.set_page_config(page_title="Adriel-IA Pro", layout="wide", initial_sidebar_state="expanded")

# 2. CSS MASTER LUXO V18 - PROTOCOLO "ROBÔ VIVO" E MATA BRANCO
st.markdown("""
<style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        background-color: #010409 !important;
    }
    
    /* DESIGN DOS BOTÕES DE NAVEGAÇÃO SÍNCRONA */
    .stButton>button {
        background-color: #0d1117 !important; color: #ffffff !important;
        border: 1px solid #1e293b !important; border-radius: 10px !important;
        height: 45px !important; width: 100% !important;
        font-weight: 700 !important; text-align: left !important;
        padding-left: 20px !important; text-transform: uppercase !important;
        font-size: 0.75rem !important; transition: 0.3s !important;
    }
    .stButton>button:hover {
        border-color: #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.3) !important;
        color: #00ffcc !important;
    }

    /* A CARA DO ROBÔ ADRIEL-IA PRO */
    .robot-face {
        width: 180px; height: 160px;
        background: #0d1117;
        border: 3px solid #00ffcc;
        border-radius: 45px 45px 25px 25px;
        margin: 0 auto 30px auto;
        position: relative;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.25);
        animation: float 4s infinite ease-in-out;
    }
    .eye-left, .eye-right {
        width: 38px; height: 38px;
        background: #00ffcc;
        border-radius: 50%;
        position: absolute; top: 45px;
        box-shadow: 0 0 25px #00ffcc;
        animation: blink 5s infinite;
    }
    .eye-left { left: 35px; }
    .eye-right { right: 35px; }
    
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-12px) rotate(1deg); } }
    @keyframes blink { 0%, 92%, 100% { transform: scaleY(1); } 96% { transform: scaleY(0.1); } }

    .brand-text { 
        color: white; font-size: 3.5rem; font-weight: 900; 
        text-align: center; letter-spacing: -2px; margin-top: 10px;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CENTRO DE COMANDO ADRIEL-IA PRO ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:10px 0 20px 10px;">🤖 Adriel-IA <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    
    # Navegação com nomes exatos dos arquivos no seu GitHub
    if st.button("🏠 DASHBOARD"): st.switch_page("app.py")
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")
    if st.button("💎 ASSINANTES"): st.switch_page("pages/5_Assinantes.py")

# --- CONTEÚDO DA HOME ---

# Portais de Conexão com seu link Hostinger
st.markdown(f"""
    <div style="display: flex; gap: 12px; margin-bottom: 45px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.65rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.65rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="https://hostinger.com" target="_blank" style="flex:1; background:#0d1117; border:2px solid #00ffcc; padding:12px; border-radius:8px; color:#00ffcc; font-size:0.65rem; font-weight:800; text-align:center; text-decoration:none; box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);">● HOSTINGER VPS</a>
    </div>
""", unsafe_allow_html=True)

# A CARA DO ROBÔ E O NOME CORRETO
st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <div class="robot-face">
            <div class="eye-left"></div>
            <div class="eye-right"></div>
        </div>
        <div class="brand-text">Adriel-IA <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.2rem; font-weight:600; letter-spacing:1px;">Inteligência Preditiva de Tráfego Global</p>
    </div>
""", unsafe_allow_html=True)

# MÉTRICAS DE VIDA DO SISTEMA
st.markdown("<br><br>", unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
m1.metric("MOTOR IA", "Adriel-IA Pro", "v18.2")
m2.metric("VARREDURAS", f"{random.randint(4500, 5200)}", "Live")
m3.metric("BANCO DE DADOS", "Sincronizado", "Global")

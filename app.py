import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

# 2. CSS MASTER LUXO - PROTOCOLO "CARA DO ROBÔ" E MATA BRANCO
st.markdown("""
<style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        background-color: #010409 !important;
    }
    
    /* DESIGN DOS BOTÕES DE NAVEGAÇÃO */
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
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
        color: #00ffcc !important;
    }

    /* A CARA DO ROBÔ ADRIEL-AI PRO */
    .robot-face {
        width: 180px; height: 160px;
        background: #0d1117;
        border: 3px solid #00ffcc;
        border-radius: 40px 40px 20px 20px;
        margin: 0 auto 30px auto;
        position: relative;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.2);
        animation: float 3s infinite ease-in-out;
    }
    .eye-left, .eye-right {
        width: 35px; height: 35px;
        background: #00ffcc;
        border-radius: 50%;
        position: absolute; top: 45px;
        box-shadow: 0 0 20px #00ffcc;
        animation: blink 4s infinite;
    }
    .eye-left { left: 35px; }
    .eye-right { right: 35px; }
    
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
    @keyframes blink { 0%, 90%, 100% { transform: scaleY(1); } 95% { transform: scaleY(0.1); } }

    .brand-text { 
        color: white; font-size: 3.2rem; font-weight: 900; 
        text-align: center; letter-spacing: -2px; margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: NAVEGAÇÃO INTERNA ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:10px 0 20px 10px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    
    # Navegação usando nomes simples (Ajuste se seus nomes de arquivos forem diferentes)
    if st.button("🏠 DASHBOARD"): st.switch_page("app.py")
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")
    if st.button("💎 ASSINANTES"): st.switch_page("pages/5_Assinantes.py")

# --- CONTEÚDO PRINCIPAL ---

# Botões de Plataforma com seu link da Hostinger
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 40px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="https://hostinger.com" target="_blank" style="flex:1; background:#0d1117; border:2px solid #00ffcc; padding:10px; border-radius:6px; color:#00ffcc; font-size:0.6rem; font-weight:800; text-align:center; text-decoration:none;">● HOSTINGER VPS</a>
    </div>
""", unsafe_allow_html=True)

# A CARA DO ROBÔ NO LUGAR DO CÍRCULO
st.markdown("""
    <div style="text-align:center; margin-top:40px;">
        <div class="robot-face">
            <div class="eye-left"></div>
            <div class="eye-right"></div>
        </div>
        <div class="brand-text">Adriel-AI <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.2rem; font-weight:500;">Inteligência Preditiva de Tráfego Global</p>
    </div>
""", unsafe_allow_html=True)

# MÉTRICAS
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("STATUS", "Online", "Aba Única")
c2.metric("OPERADORES", f"{random.randint(2300, 2600)}", "Live")
c3.metric("BOTÕES", "Ativos", "Sincronizados")

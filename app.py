import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-IA Pro", layout="wide", initial_sidebar_state="expanded")

# --- SUA CHAVE MESTRE ---
CHAVE_MESTRE = "https://hostinger.com"

# 2. CSS MASTER LUXO - PROTOCOLO "NÚCLEO VIVO"
st.markdown(f"""
<style>
    header, [data-testid="stHeader"] {{ visibility: hidden; height: 0px; }}
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{
        background-color: #010409 !important;
    }}
    [data-testid="stSidebar"] {{ border-right: 1px solid #1e293b !important; }}
    
    /* BOTÕES DE NAVEGAÇÃO */
    .stButton>button {{
        background-color: #0d1117 !important; color: #ffffff !important;
        border: 1px solid #1e293b !important; border-radius: 10px !important;
        height: 45px !important; width: 100% !important;
        font-weight: 700 !important; text-align: left !important;
        padding-left: 20px !important; text-transform: uppercase !important;
        transition: 0.3s !important;
    }}
    .stButton>button:hover {{ border-color: #00ffcc !important; color: #00ffcc !important; }}

    /* O CÍRCULO QUE VIROU A CARA DO ROBÔ */
    .robot-circle {{
        width: 200px; height: 200px;
        background: #010409;
        border-radius: 50%;
        border: 3px solid #00ffcc;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.4), inset 0 0 30px rgba(0, 255, 204, 0.2);
        margin: 0 auto 30px auto;
        position: relative;
        animation: breath 4s infinite ease-in-out;
    }
    
    /* OLHOS DENTRO DO CÍRCULO */
    .eye {{
        width: 40px; height: 40px;
        background: #00ffcc;
        border-radius: 50%;
        position: absolute; top: 60px;
        box-shadow: 0 0 20px #00ffcc;
        animation: blink 5s infinite;
    }}
    .eye.left {{ left: 45px; }}
    .eye.right {{ right: 45px; }}

    /* BOCA DENTRO DO CÍRCULO */
    .mouth {{
        width: 60px; height: 4px;
        background: #00ffcc;
        position: absolute; bottom: 50px; left: 50%;
        transform: translateX(-50%);
        border-radius: 10px;
        box-shadow: 0 0 10px #00ffcc;
    }}

    @keyframes breath {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.05); }} }}
    @keyframes blink {{ 0%, 90%, 100% {{ transform: scaleY(1); }} 95% {{ transform: scaleY(0.1); }} }}

    .brand-title {{ color: white; font-size: 3.5rem; font-weight: 900; text-align: center; letter-spacing: -2px; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:15px;">🤖 Adriel-IA <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    if st.button("🏠 DASHBOARD"): st.switch_page("app.py")
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")
    if st.button("💎 5. ASSINANTES"): st.switch_page("pages/5_Assinantes.py")

# --- CONTEÚDO ---
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 40px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="{CHAVE_MESTRE}" target="_blank" style="flex:1; background:#0d1117; border:2px solid #00ffcc; padding:12px; border-radius:8px; color:#00ffcc; font-size:0.6rem; font-weight:800; text-align:center; text-decoration:none;">🔌 CONECTAR HOSTINGER (MESTRE)</a>
    </div>
    <div style="text-align:center; margin-top:40px;">
        <div class="robot-circle">
            <div class="eye left"></div>
            <div class="eye right"></div>
            <div class="mouth"></div>
        </div>
        <div class="brand-title">Adriel-IA <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.2rem; font-weight:600;">Inteligência Preditiva de Tráfego Global</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("STATUS", "Online", "v20.5")
c2.metric("RASTREIOS", f"{random.randint(4500, 5200)}", "LIVE")
c3.metric("CHAVE MESTRE", "Ativa", "SINC")

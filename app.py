import streamlit as st
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-IA Pro", layout="wide", initial_sidebar_state="expanded")

# --- SUA CHAVE MESTRE ---
CHAVE_MESTRE = "https://hostinger.com"

# 2. CSS MASTER LUXO - PROTOCOLO BLACK TOTAL
st.markdown(f"""
<style>
    header, [data-testid="stHeader"] {{ visibility: hidden; height: 0px; }}
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {{
        background-color: #010409 !important;
    }}
    [data-testid="stSidebar"] {{ border-right: 1px solid #1e293b !important; }}
    
    /* BOTÕES DA LATERAL */
    .sidebar-menu {{ display: flex; flex-direction: column; gap: 8px; padding: 15px; }}
    .menu-btn {{
        display: flex; align-items: center; gap: 12px; padding: 12px;
        background: #0d1117; border: 1px solid #1e293b; border-radius: 8px;
        color: #ffffff !important; text-decoration: none !important;
        font-weight: 700; font-size: 0.75rem; text-transform: uppercase; transition: 0.3s;
    }}
    .menu-btn:hover {{ border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); transform: translateX(5px); }}

    /* CARA DO ROBO NO CIRCULO */
    .robot-circle {{
        width: 180px; height: 180px;
        background: radial-gradient(circle, #0d1117 40%, #00ffcc05 100%);
        border-radius: 50%; border: 3px solid #00ffcc;
        box-shadow: 0 0 50px rgba(0, 255, 204, 0.3);
        margin: 40px auto 20px auto; position: relative;
        animation: float 4s infinite ease-in-out;
    }}
    .eye {{
        width: 35px; height: 35px; background: #00ffcc;
        border-radius: 50%; position: absolute; top: 55px;
        box-shadow: 0 0 20px #00ffcc; animation: blink 5s infinite;
    }}
    .eye.left {{ left: 40px; }} .eye.right {{ right: 40px; }}
    .mouth {{
        width: 60px; height: 4px; background: #00ffcc;
        position: absolute; bottom: 50px; left: 50%;
        transform: translateX(-50%); border-radius: 10px;
    }}

    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-10px); }} }}
    @keyframes blink {{ 0%, 92%, 100% {{ transform: scaleY(1); }} 96% {{ transform: scaleY(0.1); }} }}

    .brand-title {{ color: white; font-size: 3rem; font-weight: 900; text-align: center; letter-spacing: -2px; margin: 0; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (NAVEGAÇÃO SEGURA) ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:15px;">🤖 Adriel-IA <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="sidebar-menu">
        <a href="/" target="_self" class="menu-btn">🏠 DASHBOARD</a>
        <a href="Radar" target="_self" class="menu-btn">📡 1. RADAR ELITE</a>
        <a href="Auditor" target="_self" class="menu-btn">🕵️ 2. AUDITOR IA</a>
        <a href="RSA" target="_self" class="menu-btn">✍️ 3. GERADOR RSA</a>
        <a href="Cacador" target="_self" class="menu-btn">🎯 4. CACADOR V10</a>
        <a href="Assinantes" target="_self" class="menu-btn">💎 ASSINANTES</a>
        <a href="Funil" target="_self" class="menu-btn">📐 6. FUNIL</a>
    </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO ---
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 40px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="{CHAVE_MESTRE}" target="_blank" style="flex:1.5; background:#0d1117; border:2px solid #00ffcc; padding:12px; border-radius:8px; color:#00ffcc; font-size:0.65rem; font-weight:900; text-align:center; text-decoration:none;">🔌 CONECTAR HOSTINGER</a>
    </div>
    <div style="text-align:center;">
        <div class="robot-circle"><div class="eye left"></div><div class="eye right"></div><div class="mouth"></div></div>
        <div class="brand-title">Adriel-IA <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.1rem; font-weight:600; margin-top:5px;">Inteligencia Preditiva de Trafego Global</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("STATUS", "Online", "v23.5")
c2.metric("VARREDURAS", "4,840", "LIVE")
c3.metric("CHAVE MESTRE", "Ativa", "✓")

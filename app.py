import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
st.set_page_config(page_title="Adriel-IA Pro", layout="wide", initial_sidebar_state="expanded")

# --- SUA CHAVE MESTRE BLINDADA ---
CHAVE_MESTRE = "https://hostinger.com"

# 2. CSS MASTER LUXO - PROTOCOLO BLACK TOTAL
st.markdown(f"""
<style>
    header, [data-testid="stHeader"] {{ visibility: hidden; height: 0px; }}
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {{
        background-color: #010409 !important;
    }}
    [data-testid="stSidebar"] {{ border-right: 1px solid #1e293b !important; }}
    
    /* BOTÕES DE NAVEGAÇÃO QUE RESPONDEM NA HORA */
    .stButton>button {{
        background-color: #0d1117 !important; color: #ffffff !important;
        border: 1px solid #1e293b !important; border-radius: 10px !important;
        height: 48px !important; width: 100% !important;
        font-weight: 700 !important; text-align: left !important;
        padding-left: 20px !important; text-transform: uppercase !important;
        font-size: 0.75rem !important; transition: 0.3s !important;
    }}
    .stButton>button:hover {{ border-color: #00ffcc !important; box-shadow: 0 0 20px rgba(0, 255, 204, 0.2); }}

    /* O CÍRCULO COM A CARA DO ROBÔ ADRIEL-IA PRO */
    .robot-circle {{
        width: 200px; height: 200px;
        background: radial-gradient(circle, #0d1117 40%, #00ffcc05 100%);
        border-radius: 50%; border: 3px solid #00ffcc;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.3);
        margin: 40px auto 20px auto; position: relative;
        animation: float 4s infinite ease-in-out;
    }}
    .eye {{
        width: 40px; height: 40px; background: #00ffcc;
        border-radius: 50%; position: absolute; top: 60px;
        box-shadow: 0 0 25px #00ffcc; animation: blink 5s infinite;
    }}
    .eye.left {{ left: 45px; }}
    .eye.right {{ right: 45px; }}
    .mouth {{
        width: 70px; height: 4px; background: #00ffcc;
        position: absolute; bottom: 55px; left: 50%;
        transform: translateX(-50%); border-radius: 10px;
        box-shadow: 0 0 10px #00ffcc;
    }}

    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-15px); }} }}
    @keyframes blink {{ 0%, 92%, 100% {{ transform: scaleY(1); }} 96% {{ transform: scaleY(0.1); }} }}

    .brand-title {{ color: white; font-size: 3.5rem; font-weight: 900; text-align: center; letter-spacing: -2px; margin: 0; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CENTRO DE COMANDO ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:15px;">🤖 Adriel-IA <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:15px;">Módulos</p>', unsafe_allow_html=True)
    
    # Navegação usando st.switch_page (O modo que não abre abas)
    # IMPORTANTE: Se os nomes dos arquivos no seu Github forem diferentes, ele não responde.
    if st.button("🏠 DASHBOARD"): st.rerun()
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("💎 5. ASSINANTES"): st.switch_page("pages/5_Assinantes.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")

# --- CONTEÚDO PRINCIPAL ---

# 1. BOTÕES DE PLATAFORMA (TOP)
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 40px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="{CHAVE_MESTRE}" target="_blank" style="flex:1.5; background:#0d1117; border:2px solid #00ffcc; padding:12px; border-radius:8px; color:#00ffcc; font-size:0.65rem; font-weight:900; text-align:center; text-decoration:none; box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);">🔌 CONECTAR CHAVE MESTRE (HOSTINGER)</a>
    </div>
""", unsafe_allow_html=True)

# 2. A CARA DO ROBÔ NO CÍRCULO
st.markdown("""
    <div style="text-align:center;">
        <div class="robot-circle">
            <div class="eye left"></div>
            <div class="eye right"></div>
            <div class="mouth"></div>
        </div>
        <div class="brand-title">Adriel-IA <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.2rem; font-weight:600; letter-spacing:1px; margin-top:5px;">Inteligência Preditiva de Tráfego Global</p>
    </div>
""", unsafe_allow_html=True)

# 3. MÉTRICAS LIVE
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("STATUS", "Online", "Sincronizado")
c2.metric("OPERADORES", f"{random.randint(2300, 2600)}", "Live")
c3.metric("CHAVE MESTRE", "Vinculada", "✓")

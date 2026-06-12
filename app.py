import streamlit as st
import pandas as pd
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

# 2. CSS MASTER - BLACK TOTAL (MATA O BRANCO E CORRIGE TELA)
st.markdown("""
<style>
    /* FUNDO TOTAL PRETO */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {
        background-color: #010409 !important;
    }

    /* ESCONDE MENU PADRÃO */
    [data-testid="stSidebarNav"] { display: none; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* MENU DE BOTÕES DA LATERAL */
    .sidebar-menu { display: flex; flex-direction: column; gap: 8px; padding: 15px; }
    .menu-btn {
        display: flex; align-items: center; gap: 12px; padding: 12px;
        background: #0d1117; border: 1px solid #1e293b; border-radius: 8px;
        color: #ffffff !important; text-decoration: none !important;
        font-weight: 700; font-size: 0.75rem; text-transform: uppercase; transition: 0.3s;
    }
    .menu-btn:hover { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
    .icon-n { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; font-size: 1.1rem; }

    /* BADGES SUPERIORES */
    .plat-bar { display: flex; gap: 10px; margin-bottom: 20px; }
    .plat-item { flex: 1; background: #0d1117; border: 1px solid #1e293b; padding: 10px; border-radius: 6px; text-align: center; color: #f9fafb; font-size: 0.6rem; font-weight: 800; text-decoration: none !important; }
    .plat-item:hover { border-color: #00ffcc; }

    /* CARD CENTRAL */
    .welcome-box {
        border: 1px solid #1e293b; padding: 40px; border-radius: 25px;
        background: linear-gradient(145deg, #0d1117 0%, #010409 100%);
        text-align: center; margin-top: 20px; border-top: 5px solid #00ffcc;
        box-shadow: 0 25px 50px rgba(0,0,0,0.7);
    }
</style>
""", unsafe_allow_html=True)

# --- CONSTRUÇÃO DA SIDEBAR (NAVEGAÇÃO NA MESMA ABA) ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.8rem; font-weight:900; padding:20px; letter-spacing:-1px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:20px;">Comandos</p>', unsafe_allow_html=True)
    
    # ATENÇÃO: Verifique se o nome após href= é o nome real da sua página no Streamlit
    st.markdown("""
    <div class="sidebar-menu">
        <a href="/" target="_self" class="menu-btn"><span class="icon-n">🏠</span> DASHBOARD</a>
        <a href="Radar" target="_self" class="menu-btn"><span class="icon-n">📡</span> 1. RADAR</a>
        <a href="Auditor" target="_self" class="menu-btn"><span class="icon-n">🕵️</span> 2. AUDITOR</a>
        <a href="RSA" target="_self" class="menu-btn"><span class="icon-n">✍️</span> 3. GERADOR RSA</a>
        <a href="Cacador" target="_self" class="menu-btn"><span class="icon-n">🎯</span> 4. CAÇADOR</a>
        <a href="Presell" target="_self" class="menu-btn"><span class="icon-n">📄</span> 5. PRE-SELL</a>
        <a href="Funil" target="_self" class="menu-btn"><span class="icon-n">📐</span> 6. FUNIL</a>
        <a href="Assinantes" target="_self" class="menu-btn"><span class="icon-n">💎</span> ASSINANTES</a>
    </div>
    """, unsafe_allow_html=True)

# --- HEADER E PLATAFORMAS (SEU LINK DA HOSTINGER GARANTIDO) ---
st.markdown(f"""
    <div class="plat-bar">
        <a href="https://clickbank.com" target="_blank" class="plat-item">● CLICKBANK</a>
        <a href="https://buygoods.com" target="_blank" class="plat-item">● BUYGOODS</a>
        <a href="https://stripe.com" target="_blank" class="plat-item">● STRIPE</a>
        <a href="https://hostinger.com" target="_blank" class="plat-item" style="border-color:#00ffcc; color:#00ffcc;">● HOSTINGER VPS</a>
    </div>
""", unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
st.markdown(f"""
    <div class="welcome-box">
        <h1 style="color:white; font-size:2.8rem; font-weight:900; margin:0;">Adriel-AI <span style="color:#00ffcc;">Pro</span></h1>
        <p style="color:#94a3b8; font-size:1.1rem; margin-top:10px;">Sistema operacional de inteligência preditiva e faturamento.</p>
        <hr style="border-color:#1e293b; margin:30px 0; opacity:0.3;">
        <p style="color:#00ffcc; font-weight:800; letter-spacing:2px; text-transform:uppercase;">Selecione um comando na barra lateral para navegar</p>
    </div>
""", unsafe_allow_html=True)

# MÉTRICAS LIVE
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("STATUS", "Online", "Sincronizado")
c2.metric("OPERADORES", f"{random.randint(2200, 2500)}", "Live")
c3.metric("BANCO DE DADOS", "Global", "Ativo")

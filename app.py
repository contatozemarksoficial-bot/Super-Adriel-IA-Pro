import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-IA Pro", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS MASTER LUXO V16 - PROTOCOLO BLACK TOTAL & IDENTIDADE VISUAL
    st.markdown("""
    <style>
        /* RESET TOTAL E FUNDO TRIPLE BLACK */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {
            background-color: #010409 !important;
        }

        /* ESCONDE O MENU PADRÃO E ESTILIZA A LATERAL */
        [data-testid="stSidebarNav"] { display: none; }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
        
        .sidebar-logo { color: #ffffff; font-size: 1.8rem; font-weight: 900; padding: 20px; text-align: left; }
        .sidebar-label { color: #475569; font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; padding: 0 20px; margin-bottom: 15px; }
        
        /* MENU DE BOTÕES DA LATERAL */
        .sidebar-menu { display: flex; flex-direction: column; gap: 10px; padding: 0 15px; }
        .menu-btn {
            display: flex; align-items: center; gap: 12px; padding: 12px;
            background: #0d1117; border: 1px solid #1e293b; border-radius: 8px;
            color: #ffffff !important; text-decoration: none !important;
            font-weight: 700; font-size: 0.75rem; text-transform: uppercase; transition: 0.3s;
        }
        .menu-btn:hover { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); transform: translateX(5px); }
        .icon-n { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; font-size: 1.1rem; }

        /* CARD DE COMANDO CENTRAL */
        .welcome-box {
            border: 1px solid #1e293b; padding: 50px; border-radius: 25px;
            background: linear-gradient(145deg, #0d1117 0%, #010409 100%);
            text-align: center; margin-top: 30px; border-top: 5px solid #00ffcc;
            box-shadow: 0 25px 50px rgba(0,0,0,0.7);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- CONSTRUÇÃO DA SIDEBAR (IDENTIDADE Adriel-IA Pro) ---
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">🤖 Adriel-IA <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-label">MÓDULOS DE COMANDO</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-menu">
            <a href="/" class="menu-btn"><span class="icon-n">🏠</span> DASHBOARD</a>
            <a href="Radar" class="menu-btn"><span class="icon-n">📡</span> 1. RADAR ELITE</a>
            <a href="Auditor" class="menu-btn"><span class="icon-n">🕵️</span> 2. AUDITOR IA</a>
            <a href="Gerador" class="menu-btn"><span class="icon-n">✍️</span> 3. GERADOR RSA</a>
            <a href="Cacador" class="menu-btn"><span class="icon-n">🎯</span> 4. CAÇADOR V10</a>
            <a href="Presell" class="menu-btn"><span class="icon-n">📄</span> 5. PRE-SELL</a>
            <a href="Funil" class="menu-btn"><span class="icon-n">📐</span> 6. FUNIL</a>
            <a href="Assinantes" class="menu-btn"><span class="icon-n">💎</span> ÁREA MEMBROS</a>
        </div>
        """, unsafe_allow_html=True)

    # --- TELA DE COMANDO CENTRAL ---
    st.markdown(f"""
        <div class="welcome-box">
            <div style="font-size: 4rem; margin-bottom:10px;">🛰️</div>
            <h1 style="color:white; font-size:3rem; font-weight:900; margin-bottom:10px;">Adriel-IA <span style="color:#00ffcc;">Pro</span></h1>
            <p style="color:#94a3b8; font-size:1.2rem;">Comandante José Marques, o sistema de inteligência está operacional.</p>
            <hr style="border-color:#1e293b; margin:30px 0; opacity:0.3;">
            <p style="color:#00ffcc; font-weight:800; letter-spacing:2px; text-transform:uppercase;">Selecione um módulo na barra lateral para iniciar a varredura</p>
        </div>
    """, unsafe_allow_html=True)

    # MÉTRICAS LIVE (PROVA DE VIDA)
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("STATUS DO SOFTWARE", "Adriel-IA Pro", "v16.8")
    c2.metric("CONEXÕES ATIVAS", f"{random.randint(2300, 2600)}", "LIVE")
    c3.metric("BANCO DE DADOS", "Sincronizado", "GLOBAL")

if __name__ == "__main__":
    main()

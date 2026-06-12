import streamlit as st
import pandas as pd
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS DE BLINDAGEM TOTAL - PROTOCOLO TRIPLE BLACK
    st.markdown("""
    <style>
        /* REMOVE CABEÇALHO E FORÇA FUNDO PRETO EM TUDO */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {
            background-color: #010409 !important;
        }

        /* ESCONDE O MENU PADRÃO DO STREAMLIT */
        [data-testid="stSidebarNav"] { display: none; }
        
        /* BORDA DE SEPARAÇÃO DA LATERAL */
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

        /* MENU DE BOTÕES DA LATERAL (ADRIEL-AI PRO) */
        .sidebar-menu { display: flex; flex-direction: column; gap: 10px; padding: 15px; }
        .menu-btn {
            display: flex; align-items: center; gap: 12px; padding: 12px;
            background: #0d1117; border: 1px solid #1e293b; border-radius: 8px;
            color: #ffffff !important; text-decoration: none !important;
            font-weight: 700; font-size: 0.75rem; text-transform: uppercase;
            transition: 0.3s all;
        }
        .menu-btn:hover {
            border-color: #00ffcc;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
            transform: translateX(5px);
        }
        .icon-n { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; font-size: 1.1rem; }

        /* CARD DE BOAS-VINDAS */
        .welcome-box {
            border: 1px solid #1e293b; padding: 40px; border-radius: 25px;
            background: linear-gradient(145deg, #0d1117 0%, #010409 100%);
            text-align: center; margin-top: 30px; border-top: 5px solid #00ffcc;
            box-shadow: 0 25px 50px rgba(0,0,0,0.7);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- CONSTRUÇÃO DA SIDEBAR (IDENTIDADE ADRIEL-AI PRO) ---
    with st.sidebar:
        st.markdown('<div style="text-align:center; padding:20px 0;"><span style="color:white; font-size:1.6rem; font-weight:900;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></span></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:15px;">Módulos Ativos</p>', unsafe_allow_html=True)
        
        # Estrutura de links síncronos
        st.markdown("""
        <div class="sidebar-menu">
            <a href="/" class="menu-btn"><span class="icon-n">🏠</span> DASHBOARD</a>
            <a href="Radar" class="menu-btn"><span class="icon-n">📡</span> 1. RADAR ELITE</a>
            <a href="Auditor" class="menu-btn"><span class="icon-n">🕵️</span> 2. AUDITOR IA</a>
            <a href="RSA" class="menu-btn"><span class="icon-n">✍️</span> 3. GERADOR RSA</a>
            <a href="Cacador" class="menu-btn"><span class="icon-n">🎯</span> 4. CAÇADOR V10</a>
            <a href="Presell" class="menu-btn"><span class="icon-n">📄</span> 5. PRE-SELL</a>
            <a href="Funil" class="menu-btn"><span class="icon-n">📐</span> 6. FUNIL</a>
            <a href="Assinantes" class="menu-btn"><span class="icon-n">💎</span> ÁREA MEMBROS</a>
        </div>
        """, unsafe_allow_html=True)

    # --- TELA DE COMANDO CENTRAL ---
    st.markdown("""
        <div class="welcome-box">
            <h1 style="color:white; font-size:2.5rem; font-weight:900; margin-bottom:10px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></h1>
            <p style="color:#94a3b8; font-size:1.1rem;">Bem-vindo ao centro de inteligência preditiva, Comandante José Marques.</p>
            <hr style="border-color:#1e293b; margin:25px 0;">
            <p style="color:#00ffcc; font-weight:800; letter-spacing:2px;">OPERACIONAL: SELECIONE UM MÓDULO NA SIDEBAR</p>
        </div>
    """, unsafe_allow_html=True)

    # MÉTRICAS LIVE
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("SOFTWARE", "Adriel-AI Pro", "v16.5")
    c2.metric("CONEXÕES", f"{random.randint(2100, 2500)}", "Live")
    c3.metric("BANCO DE DADOS", "Sincronizado", "Global")

if __name__ == "__main__":
    main()

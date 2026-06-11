import streamlit as st
import pandas as pd
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE
    st.set_page_config(page_title="Adriel-AI Pro | Dashboard", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS DE BLINDAGEM (Corrige o sumiço e mantém o luxo)
    st.markdown("""
    <style>
        /* Garante que o corpo da página esteja visível */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp { background-color: #010409 !important; }
        
        /* Sidebar Personalizada */
        [data-testid="stSidebarNav"] { display: none; }
        [data-testid="stSidebar"] { background-color: #010409 !important; border-right: 1px solid #1e293b !important; }
        
        .sidebar-menu { display: flex; flex-direction: column; gap: 10px; padding: 10px; }
        .menu-item {
            display: flex; align-items: center; gap: 12px; padding: 12px;
            background: #0d1117; border: 1px solid #1e293b; border-radius: 10px;
            color: #ffffff !important; text-decoration: none !important;
            font-weight: 700; font-size: 0.8rem; text-transform: uppercase;
            transition: 0.3s;
        }
        .menu-item:hover { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); transform: translateX(5px); }
        .icon-n { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; }

        /* Card de Boas-Vindas */
        .welcome-card {
            border: 1px solid #1e293b; padding: 50px; border-radius: 30px;
            background: linear-gradient(145deg, #0d1117 0%, #010409 100%);
            text-align: center; margin-top: 50px; border-top: 5px solid #00ffcc;
            box-shadow: 0 30px 60px rgba(0,0,0,0.8);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- SIDEBAR COM BOTÕES (RESTAURADA) ---
    with st.sidebar:
        st.markdown('<div style="text-align:center; padding-bottom:20px;"><span style="color:white; font-size:1.5rem; font-weight:900;">🤖 ADRIEL-AI <span style="color:#00ffcc;">PRO</span></span></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-menu">
            <a href="/" class="menu-item"><span class="icon-n">🏠</span> DASHBOARD</a>
            <a href="Radar" class="menu-item"><span class="icon-n">📡</span> 1. RADAR</a>
            <a href="Auditor" class="menu-item"><span class="icon-n">🕵️</span> 2. AUDITOR</a>
            <a href="RSA" class="menu-item"><span class="icon-n">✍️</span> 3. GERADOR RSA</a>
            <a href="Cacador" class="menu-item"><span class="icon-n">🛰️</span> 4. CAÇADOR V10</a>
            <a href="Presell" class="menu-item"><span class="icon-n">📄</span> 5. PRE-SELL</a>
            <a href="Funil" class="menu-item"><span class="icon-n">📐</span> 6. FUNIL</a>
            <a href="Assinantes" class="menu-item"><span class="icon-n">💎</span> ÁREA MEMBROS</a>
        </div>
        """, unsafe_allow_html=True)

    # --- CONTEÚDO PRINCIPAL (PARA NÃO FICAR TUDO PRETO) ---
    st.markdown(f"""
        <div class="welcome-card">
            <div style="font-size: 4rem;">🛰️</div>
            <h1 style="color:white; font-size:3rem; font-weight:900; margin-bottom:10px;">SISTEMA OPERACIONAL <span style="color:#00ffcc;">ATIVO</span></h1>
            <p style="color:#94a3b8; font-size:1.2rem;">Comandante José Marques, o Adriel-AI Pro está pronto para a caçada.</p>
            <p style="color:#00ffcc; font-weight:bold; letter-spacing:2px; margin-top:20px;">SELECIONE UM MÓDULO NA BARRA LATERAL PARA INICIAR</p>
        </div>
    """, unsafe_allow_html=True)

    # DASHBOARD FINANCEIRO RÁPIDO (PROVA DE VIDA)
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("FATURAMENTO HOJE", "R$ 14.580", "+5%")
    c2.metric("OPERADORES ONLINE", "2.326", "LIVE")
    c3.metric("ROI MÉDIO", "285%", "HIGH")

if __name__ == "__main__":
    main()

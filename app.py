import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Gestão Suprema", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS MASTER LUXO - PROTOCOLO TRIPLE BLACK TOTAL
    st.markdown("""
    <style>
        /* RESET TOTAL E FUNDO PRETO ABSOLUTO */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {
            background-color: #010409 !important;
        }

        /* ESCONDE O MENU PADRÃO E ESTILIZA A LATERAL EM BOTÕES */
        [data-testid="stSidebarNav"] { display: none; }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
        
        .sidebar-logo { color: #ffffff; font-size: 1.8rem; font-weight: 900; padding: 20px; text-align: left; }
        .sidebar-label { color: #475569; font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; padding: 0 20px; margin-bottom: 15px; }
        
        .sidebar-menu { display: flex; flex-direction: column; gap: 8px; padding: 0 15px; }
        .menu-btn {
            display: flex; align-items: center; gap: 12px; padding: 12px;
            background: #0d1117; border: 1px solid #1e293b; border-radius: 8px;
            color: #ffffff !important; text-decoration: none !important;
            font-weight: 700; font-size: 0.75rem; text-transform: uppercase; transition: 0.3s;
        }
        .menu-btn:hover { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); transform: translateX(5px); }
        .icon-n { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; font-size: 1.1rem; }

        /* HEADER E LIVE STATUS */
        .header-top { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #1e293b; margin-bottom: 25px; }
        .live-status { color: #00ffcc; font-size: 0.75rem; font-weight: 800; display: flex; align-items: center; gap: 8px; }
        .blink { height: 8px; width: 8px; background-color: #00ffcc; border-radius: 50%; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

        /* PLATAFORMAS (BADGES CLICÁVEIS) */
        .plat-bar { display: flex; gap: 10px; margin-bottom: 30px; overflow-x: auto; }
        .plat-item { flex: 1; background: #0d1117; border: 1px solid #1e293b; padding: 12px; border-radius: 8px; text-align: center; color: #f9fafb; font-size: 0.65rem; font-weight: 800; text-decoration: none !important; transition: 0.3s; min-width: 120px; }
        .plat-item:hover { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }

        /* MÉTRICAS DE FATURAMENTO */
        .metric-card {
            background: #0d1117; border: 1px solid #1e293b; padding: 25px; border-radius: 15px;
            text-align: center; border-bottom: 4px solid #00ffcc;
        }
        .m-label { color: #94a3b8; font-size: 0.65rem; font-weight: 800; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 1px; }
        .m-value { color: #ffffff; font-size: 1.8rem; font-weight: 900; }

        /* CARDS DE LICENÇA ACESSÍVEIS */
        .plan-card {
            background: #0d1117; border: 1px solid #1e293b; padding: 35px; border-radius: 20px;
            text-align: left; transition: 0.4s; height: 100%; display: flex; flex-direction: column; justify-content: space-between;
        }
        .plan-card:hover { border-color: #00ffcc; transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.6); }
        .p-price { color: #ffffff; font-size: 2.5rem; font-weight: 900; margin: 15px 0; }
        
        .btn-checkout {
            display: block; width: 100%; padding: 16px; background: #00ffcc; color: #010409 !important;
            border-radius: 10px; text-align: center; font-weight: 900; font-size: 0.9rem;
            text-transform: uppercase; text-decoration: none !important; transition: 0.3s;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
        }
        .btn-checkout:hover { background: #ffffff; box-shadow: 0 0 40px #00ffcc; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

    # --- SIDEBAR (CONFORME O PRINT) ---
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-label">MÓDULOS DE COMANDO</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="sidebar-menu">
            <a href="/" class="menu-btn"><span class="icon-n">🏠</span> DASHBOARD</a>
            <a href="Radar" class="menu-btn"><span class="icon-n">📡</span> 1. RADAR ELITE</a>
            <a href="Auditor" class="menu-btn"><span class="icon-n">🕵️</span> 2. AUDITOR IA</a>
            <a href="RSA" class="menu-btn"><span class="icon-n">✍️</span> 3. GERADOR RSA</a>
            <a href="Cacador" class="menu-btn"><span class="icon-n">🎯</span> 4. CAÇADOR V10</a>
            <a href="Presell" class="menu-btn"><span class="icon-n">📄</span> 5. PRE-SELL</a>
            <a href="Funil" class="menu-btn"><span class="icon-n">📐</span> 6. FUNIL</a>
            <a href="Assinantes" class="menu-btn" style="border-left: 4px solid #00ffcc; background: #1e293b;"><span class="icon-n">💎</span> ASSINANTES</a>
        </div>
        """, unsafe_allow_html=True)

    # --- HEADER E PLATAFORMAS ---
    st.markdown(f"""
        <div class="header-top">
            <div style="font-size:2rem; font-weight:900; color:white;">🛰️ Central de <span style="color:#00ffcc;">Assinantes</span></div>
            <div class="live-status"><span class="blink"></span> {random.randint(2300, 2600):,} OPERADORES CONECTADOS AGORA</div>
        </div>
        <div class="plat-bar">
            <a href="https://clickbank.com" target="_blank" class="plat-item">● CLICKBANK</a>
            <a href="https://buygoods.com" target="_blank" class="plat-item">● BUYGOODS</a>
            <a href="https://digistore24.com" target="_blank" class="plat-item">● DIGISTORE24</a>
            <a href="https://stripe.com" target="_blank" class="plat-item">● STRIPE DASH</a>
            <a href="https://hostinger.com" target="_blank" class="plat-item">● HOSTINGER VPS</a>
        </div>
    """, unsafe_allow_html=True)

    # --- MÉTRICAS DE FATURAMENTO ---
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-card"><div class="m-label">FATURAMENTO GERAL</div><div class="m-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-card"><div class="m-label">LICENÇAS ATIVAS</div><div class="m-value">2.105</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-card"><div class="m-label">RECORRÊNCIA (MRR)</div><div class="m-value">R$ 104.200</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-card" style="border-bottom-color:#ff0055;"><div class="m-label">TAXA DE CHURN</div><div class="m-value">0.8%</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h2 style="color:white; font-size:1.8rem; font-weight:900; letter-spacing:-1px;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h2>', unsafe_allow_html=True)

    # --- CARDS DE VENDAS ---
    p1, p2, p3 = st.columns(3)
    
    licencas = [
        {"n": "PLANO MENSAL START", "v": "R$ 47", "d": "Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata do robô.", "l": "#"},
        {"n": "PLANO MENSAL PRO", "v": "R$ 97", "d": "Start + Módulo RSA (45 Keywords) + Arquiteto de Funil. Foco em escala semanal acelerada.", "l": "#"},
        {"n": "PLANO ELITE MASTER", "v": "R$ 197", "d": "ACESSO TOTAL ILIMITADO + Construtor Pre-Sell Hostinger. O poder máximo da Adriel-AI Pro.", "l": "#"}
    ]

    cols = [p1, p2, p3]
    for i, lic in enumerate(licencas):
        with cols[i]:
            st.markdown(f"""
            <div class="plan-card">
                <div>
                    <p style="color:#94a3b8; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:1px;">{lic['n']}</p>
                    <div class="p-price">{lic['v']}</div>
                    <p style="color:#94a3b8; font-size:0.85rem; line-height:1.6; margin-bottom:25px;">{lic['d']}</p>
                </div>
                <a href="{lic['l']}" target="_blank" class="btn-checkout">💳 PAGAR COM CARTÃO / PIX</a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='color:#475569; font-size:0.6rem; text-align:center;'>ESTRUTURA BLINDADA - PROTOCOLO ADRIEL-AI PRO V16.8</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


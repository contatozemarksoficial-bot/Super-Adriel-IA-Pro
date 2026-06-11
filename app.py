import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Gestão", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS DE ALTA PERFORMANCE - PROTOCOLO BLACK TOTAL (MATA O BRANCO NA LATERAL)
    st.markdown("""
    <style>
        /* Remove cabeçalho */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        
        /* FUNDO TOTAL PRETO (Corpo e Lateral) */
        .stApp, [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #010409 !important;
        }

        /* TEXTO DA LATERAL EM BRANCO NÍTIDO */
        [data-testid="stSidebarNav"] span { 
            color: #ffffff !important; 
            font-weight: 700 !important;
            font-size: 0.9rem !important;
        }
        
        /* Borda fina para separar a lateral do corpo */
        [data-testid="stSidebar"] {
            border-right: 1px solid #1e293b !important;
        }

        /* Logo e Badges */
        .main-logo {
            color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;
            display: flex; align-items: center; gap: 15px;
            text-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
        }
        .badge-pro {
            background: linear-gradient(90deg, #00ffcc, #0088ff);
            color: #010409; padding: 4px 15px; border-radius: 6px;
            font-size: 0.9rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88;
        }

        /* PLATAFORMAS LINCADAS */
        .plat-link { text-decoration: none !important; color: inherit !important; }
        .plat-badge {
            padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b;
            background: #0d1117; color: #f9fafb; font-size: 0.7rem; font-weight: 800;
            display: flex; align-items: center; gap: 8px; transition: 0.3s;
            cursor: pointer; justify-content: center;
        }
        .plat-badge:hover { border-color: #00ffcc; background: #010409; box-shadow: 0 0 15px #00ffcc33; }
        .online-dot { height: 7px; width: 7px; background: #00ffcc; border-radius: 50%; box-shadow: 0 0 10px #00ffcc; }

        /* Widgets de Faturamento */
        .metric-container {
            background: rgba(13, 17, 23, 0.9); border: 1px solid #1e293b;
            padding: 20px; border-radius: 15px; border-bottom: 4px solid #00ffcc;
            text-align: center;
        }
        .m-label { color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; font-weight: 700; }
        .m-value { color: #ffffff; font-size: 1.6rem; font-weight: 900; }

        /* CARDS DE LICENÇA (CHECKOUT REAL) */
        .plan-card {
            border: 1px solid #1e293b; padding: 30px; border-radius: 20px;
            background: linear-gradient(145deg, #0d1117, #010409);
            margin-bottom: 20px; transition: 0.4s; position: relative; overflow: hidden;
        }
        .plan-card:hover { border-color: #00ffcc; transform: translateY(-5px); }
        .plan-price { font-size: 2.5rem; color: #ffffff; font-weight: 900; margin: 10px 0; }
        
        .btn-checkout-real {
            display: block; width: 100%; padding: 15px; margin-top: 20px;
            background: #00ffcc; color: #010409 !important;
            border-radius: 10px; text-align: center; text-decoration: none !important;
            font-weight: 900; font-size: 0.9rem; text-transform: uppercase;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.4); transition: 0.3s;
        }
        .btn-checkout-real:hover { background: #ffffff; box-shadow: 0 0 40px #00ffcc; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
    with c_live:
        st.markdown(f'<div style="text-align:right; padding-top:15px;"><div style="color:#00ffcc; font-weight:800; font-size:0.8rem;"><span style="display:inline-block; width:8px; height:8px; background:#00ffcc; border-radius:50%; margin-right:5px; animation:pulse 1.5s infinite;"></span> {random.randint(1840, 2350):,} OPERADORES ATIVOS NA ÁREA</div></div>', unsafe_allow_html=True)

    # --- PLATAFORMAS LINCADAS (CONECTADAS) ---
    st.markdown("<br>", unsafe_allow_html=True)
    lp1, lp2, lp3, lp4, lp5 = st.columns(5)
    platas = [
        ("CLICKBANK", "https://clickbank.com", lp1),
        ("BUYGOODS", "https://buygoods.com", lp2),
        ("DIGISTORE24", "https://digistore24.com", lp3),
        ("STRIPE DASH", "https://stripe.com", lp4),
        ("HOSTINGER VPS", "https://hostinger.com", lp5)
    ]
    for name, link, col in platas:
        with col:
            st.markdown(f'<a href="{link}" target="_blank" class="plat-link"><div class="plat-badge"><div class="online-dot"></div> {name}</div></a>', unsafe_allow_html=True)

    # --- DASHBOARD FINANCEIRO ---
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-container"><div class="m-label">Faturamento Geral</div><div class="m-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-container"><div class="m-label">Licenças Ativas</div><div class="m-value">2.105</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-container"><div class="m-label">Recorrência (MRR)</div><div class="m-value">R$ 104.200</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-container" style="border-bottom-color:#ff0055;"><div class="m-label">Taxa de Churn</div><div class="m-value">0.8%</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- NOVAS LICENÇAS ACESSÍVEIS ---
    st.markdown('<h3 style="color:white; margin-bottom:25px; letter-spacing:1px;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h3>', unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    licencas = [
        {"n": "PLANO MENSAL START", "v": "R$ 47", "desc": "Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata.", "link": "#"},
        {"n": "PLANO MENSAL PRO", "v": "R$ 97", "desc": "Start + Módulo RSA (45 Keywords) + Arquiteto de Funil. Foco em quem já escala.", "link": "#"},
        {"n": "PLANO ELITE MASTER", "v": "R$ 197", "desc": "ACESSO TOTAL ILIMITADO + Construtor Pre-Sell Hostinger. O poder máximo do robô.", "link": "#"}
    ]

    cols = [p1, p2, p3]
    for i, lic in enumerate(licencas):
        with cols[i]:
            st.markdown(f"""
            <div class="plan-card">
                <div class="m-label">{lic['n']}</div>
                <div class="plan-price">{lic['v']}</div>
                <p style="color:#94a3b8; font-size:0.8rem; height:50px;">{lic['desc']}</p>
                <a href="{lic['link']}" target="_blank" class="btn-checkout-real">💳 PAGAR COM CARTÃO / PIX</a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br><p style='color:#475569; font-size:0.6rem; text-align:center;'>SISTEMA BLINDADO - REBOOT DE CACHE RECOMENDADO APÓS ATUALIZAÇÃO</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

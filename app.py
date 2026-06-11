import streamlit as st
import pandas as pd
import random

def main():
    st.set_page_config(page_title="Adriel-AI Pro | Gestão", layout="wide", initial_sidebar_state="expanded")

    # CSS MATA BRANCO NA LATERAL E DESIGN CINEMA
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #010409 !important;
        }
        [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
        
        .main-logo { color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; display: flex; align-items: center; gap: 15px; }
        .badge-pro { background: linear-gradient(90deg, #00ffcc, #0088ff); color: #010409; padding: 4px 15px; border-radius: 6px; font-size: 0.9rem; font-weight: 900; }
        
        .plat-link { text-decoration: none !important; color: inherit !important; }
        .plat-badge { padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b; background: #0d1117; color: #f9fafb; font-size: 0.7rem; font-weight: 800; display: flex; align-items: center; gap: 8px; transition: 0.3s; cursor: pointer; justify-content: center; }
        .plat-badge:hover { border-color: #00ffcc; background: #010409; box-shadow: 0 0 15px #00ffcc33; }
        .online-dot { height: 7px; width: 7px; background: #00ffcc; border-radius: 50%; box-shadow: 0 0 10px #00ffcc; }

        .metric-container { background: rgba(13, 17, 23, 0.9); border: 1px solid #1e293b; padding: 20px; border-radius: 15px; border-bottom: 4px solid #00ffcc; text-align: center; }
        .m-value { color: #ffffff; font-size: 1.6rem; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)

    # --- PLATAFORMAS LINCADAS (ADICIONE SEU LINK AQUI) ---
    st.markdown("<br>", unsafe_allow_html=True)
    lp1, lp2, lp3, lp4, lp5 = st.columns(5)
    
    # COLE SEU LINK DA HOSTINGER ENTRE AS ASPAS ABAIXO:
    seu_link_hostinger = "COLE_SEU_LINK_AQUI" 
    
    platas = [
        ("CLICKBANK", "https://clickbank.com", lp1),
        ("BUYGOODS", "https://buygoods.com", lp2),
        ("DIGISTORE24", "https://digistore24.com", lp3),
        ("STRIPE DASH", "https://stripe.com", lp4),
        ("HOSTINGER VPS", seu_link_hostinger, lp5) # Seu link agora está aqui!
    ]
    
    for name, link, col in platas:
        with col:
            st.markdown(f'<a href="{link}" target="_blank" class="plat-link"><div class="plat-badge"><div class="online-dot"></div> {name}</div></a>', unsafe_allow_html=True)

    # --- DASHBOARD FINANCEIRO ---
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-container"><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">FATURAMENTO GERAL</div><div class="m-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-container"><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">LICENÇAS ATIVAS</div><div class="m-value">2.105</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-container"><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">RECORRÊNCIA (MRR)</div><div class="m-value">R$ 104.200</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-container" style="border-bottom-color:#ff0055;"><div style="color:#94a3b8; font-size:0.7rem; font-weight:700;">CHURN RATE</div><div class="m-value">0.8%</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)
    st.info("Terminal Adriel-AI configurado com sucesso. Clique nos badges superiores para acessar as plataformas.")

if __name__ == "__main__":
    main()

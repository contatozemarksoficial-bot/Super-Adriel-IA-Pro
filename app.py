import streamlit as st
import pandas as pd
import altair as alt
import time
import random
from datetime import datetime, timedelta

def main():
    # 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
    st.set_page_config(page_title="Adriel-AI Pro | Área de Membros", layout="wide", initial_sidebar_state="expanded")

    if "sessao_ativa" not in st.session_state: st.session_state.sessao_ativa = False

    # 2. CSS DE LUXO (Protocolo Triple Black + Neon)
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp { background-color: #010409 !important; }
    
    /* Logo e Header Top */
    .main-logo {
        color: #ffffff; font-size: 3rem; font-weight: 900; letter-spacing: -2px;
        display: flex; align-items: center; gap: 15px;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
    }
    .badge-pro {
        background: linear-gradient(90deg, #00ffcc, #00ccaa);
        color: #010409; padding: 4px 15px; border-radius: 6px;
        font-size: 1rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88;
    }
    
    /* Contador de Acessos */
    .live-counter {
        background: rgba(0, 255, 204, 0.1);
        border: 1px solid #00ffcc33;
        padding: 10px 20px; border-radius: 50px;
        color: #00ffcc; font-weight: 700; font-size: 0.9rem;
        display: inline-flex; align-items: center; gap: 8px;
    }
    .dot { height: 8px; width: 8px; background-color: #00ffcc; border-radius: 50%; display: inline-block; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    /* Botões de Afiliado Luxo */
    .btn-afiliado {
        display: inline-block; padding: 12px 20px;
        border: 1px solid #00ffcc; border-radius: 8px;
        color: #00ffcc !important; text-decoration: none;
        font-weight: 800; font-size: 0.8rem; text-transform: uppercase;
        transition: 0.4s; text-align: center; width: 100%;
        background: transparent; margin-top: 10px;
    }
    .btn-afiliado:hover { background: #00ffcc; color: #010409 !important; box-shadow: 0 0 20px #00ffcc; }

    /* Cards de Membro */
    .member-card {
        border: 1px solid #1e293b; padding: 35px; border-radius: 24px;
        background: linear-gradient(160deg, #0d1117 0%, #010409 100%);
        margin-bottom: 30px; border-top: 4px solid #00ffcc;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }
    
    .status-badge { color: #00ffcc; font-size: 0.7rem; font-weight: 800; letter-spacing: 2px; }
    .product-title { color: #ffffff; font-size: 2.2rem; font-weight: 900; margin: 5px 0; }
    .metric-hero { color: #ffffff; font-size: 2.5rem; font-weight: 900; letter-spacing: -1px; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #010409 !important; border-right: 1px solid #1e293b !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ÁREA DE MEMBROS ---
    c_logo, c_live = st.columns([2, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8; margin-top:-10px; margin-left:65px;">Dashboard Exclusivo de Inteligência Preditiva</p>', unsafe_allow_html=True)
    with c_live:
        # Simula contagem de pessoas acessando agora
        acessos = random.randint(1240, 1580)
        st.markdown(f'<div style="text-align:right;"><div class="live-counter"><span class="dot"></span> {acessos:,} USUÁRIOS ONLINE AGORA</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- COMANDO DE VARREDURA ---
    col_v1, col_btn, col_v2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 INICIAR VARREDURA EM TEMPO REAL"):
            st.session_state.sessao_ativa = True

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- LISTA DE PRODUTOS ELITE ---
    if st.session_state.sessao_ativa:
        with st.status("🤖 Robô Adriel-AI acessando Big Data Gringo...", expanded=False):
            time.sleep(1)

        hoje = datetime.now()
        meses = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
        
        produtos = [
            {"n": "Nagano Tonic", "v24": "4.812", "st": "ESCALA AGRESSIVA", "p": "USA/AUSTRALIA", "plat": "BuyGoods", "com": "$127", "peso": 1.6},
            {"n": "FitSpresso", "v24": "7.329", "st": "DOMÍNIO TOTAL", "p": "CANADA/USA", "plat": "ClickBank", "com": "$145", "peso": 2.3},
            {"n": "Sugar Defender", "v24": "5.610", "st": "ESCALA ESTÁVEL", "p": "UK/USA", "plat": "Digistore24", "com": "$132", "peso": 1.9}
        ]

        for p in produtos:
            st.markdown(f'<div class="member-card">', unsafe_allow_html=True)
            c_txt, c_chart = st.columns([1, 1.3], gap="large")
            
            with c_txt:
                st.markdown(f"""
                    <span class="status-badge">● {p['st']}</span>
                    <div class="product-title">🔥 {p['n']}</div>
                    <div style="margin: 20px 0;">
                        <span style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Volume de Buscas (24h)</span><br>
                        <span class="metric-hero">{p['v24']}</span> <span style="color:#00ffcc; font-weight:700;">LIVE</span>
                    </div>
                    <p style="color:#94a3b8; margin-bottom:5px;">Plataforma: <b style="color:white;">{p['plat']}</b></p>
                    <p style="color:#94a3b8;">Comissão Média: <b style="color:#00ffcc;">{p['com']}</b></p>
                    
                    <a href="#" class="btn-afiliado">🔑 SOLICITAR AFILIAÇÃO {p['plat'].upper()}</a>
                """, unsafe_allow_html=True)
            
            with c_chart:
                st.markdown("<p style='color:white; font-weight:bold; font-size:0.8rem; letter-spacing:1px;'>📈 TENDÊNCIA ESTATÍSTICA (12 MESES)</p>", unsafe_allow_html=True)
                vol_mensal = [int((35 + (i * 4)) * p['peso'] * 1000) for i in range(12)]
                df = pd.DataFrame({"Mês": meses, "Volume": vol_mensal})
                
                chart = alt.Chart(df).mark_bar(
                    color='#00ffcc', cornerRadiusTopLeft=5, cornerRadiusTopRight=5
                ).encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0)),
                    y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title=None, grid=False))
                ).properties(width='container', height=250, background='transparent').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

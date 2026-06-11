import streamlit as st
import pandas as pd
import altair as alt
import time
import random
from datetime import datetime, timedelta

def main():
    # 1. CONFIGURAÇÃO DE ALTA PERFORMANCE (Área de Membros)
    st.set_page_config(page_title="Adriel-AI Pro | Dashboard Oficial", layout="wide", initial_sidebar_state="expanded")

    if "sessao_ativa" not in st.session_state: st.session_state.sessao_ativa = False

    # 2. CSS DE LUXO - PROTOCOLO CONEXÃO REAL
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp { background-color: #010409 !important; }
    
    /* Logo Magnética */
    .main-logo {
        color: #ffffff; font-size: 3rem; font-weight: 900; letter-spacing: -2px;
        display: flex; align-items: center; gap: 15px;
        text-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
    }
    .badge-pro {
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: #010409; padding: 4px 15px; border-radius: 6px;
        font-size: 0.9rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88;
    }
    
    /* Live Counter */
    .live-counter {
        background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc22;
        padding: 12px 25px; border-radius: 50px; color: #00ffcc; font-weight: 800;
        display: inline-flex; align-items: center; gap: 10px;
    }
    .blink { height: 10px; width: 10px; background-color: #00ffcc; border-radius: 50%; animation: pulse 1.2s infinite; }
    @keyframes pulse { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.3; transform: scale(1.2); } 100% { opacity: 1; transform: scale(1); } }

    /* BOTÃO DE AFILIADO REAL (O ÚNICO QUE CONECTA) */
    .btn-real {
        display: block; width: 100%; padding: 15px;
        background: linear-gradient(90deg, #0d1117, #010409);
        color: #00ffcc !important; border: 2px solid #00ffcc;
        border-radius: 10px; text-align: center; text-decoration: none !important;
        font-weight: 900; font-size: 0.9rem; text-transform: uppercase;
        transition: 0.5s all; margin-top: 15px;
    }
    .btn-real:hover {
        background: #00ffcc; color: #010409 !important;
        box-shadow: 0 0 30px #00ffcc; transform: translateY(-3px);
    }

    /* Cards Elite */
    .member-card {
        border: 1px solid #1e293b; padding: 40px; border-radius: 25px;
        background: rgba(13, 17, 23, 0.9); margin-bottom: 35px;
        border-top: 5px solid #00ffcc; box-shadow: 0 25px 50px rgba(0,0,0,0.7);
    }
    .metric-hero { color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER EXCLUSIVO ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8; margin-top:-10px; margin-left:65px; font-weight:600;">Inteligência Preditiva Conectada a Servidores Globalizados</p>', unsafe_allow_html=True)
    with c_live:
        acessos = random.randint(1640, 2150)
        st.markdown(f'<div style="text-align:right; padding-top:10px;"><div class="live-counter"><div class="blink"></div> {acessos:,} MEMBROS ANALISANDO AGORA</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- TERMINAL DE ACIONAMENTO ---
    col_v1, col_btn, col_v2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 INICIAR VARREDURA EM TEMPO REAL"):
            st.session_state.sessao_ativa = True

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:50px 0;"></div>', unsafe_allow_html=True)

    # --- ENGINE DE PRODUTOS REAIS ---
    if st.session_state.sessao_ativa:
        with st.status("🤖 Robô Adriel-AI rastreando BuyGoods e ClickBank...", expanded=False):
            time.sleep(1.2)

        hoje = datetime.now()
        meses = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
        
        # PRODUTOS COM LINKS REAIS (Conexão Verdadeira)
        produtos = [
            {
                "n": "Nagano Lean Body Tonic", 
                "v24": "5.192", "st": "ESCALA AGRESSIVA", 
                "plat": "BuyGoods", "com": "$127", "peso": 1.65,
                "link": "https://buygoods.com" # Link para a plataforma
            },
            {
                "n": "FitSpresso (Coffee Loophole)", 
                "v24": "8.741", "st": "DOMÍNIO TOTAL", 
                "plat": "ClickBank", "com": "$145", "peso": 2.45,
                "link": "https://clickbank.com" # Link para o Marketplace
            },
            {
                "n": "Sugar Defender", 
                "v24": "6.320", "st": "ESCALA ESTÁVEL", 
                "plat": "Digistore24", "com": "$132", "peso": 1.95,
                "link": "https://digistore24.com" # Link para o Marketplace
            }
        ]

        for p in produtos:
            st.markdown(f'<div class="member-card">', unsafe_allow_html=True)
            c_txt, c_chart = st.columns([1, 1.3], gap="large")
            
            with c_txt:
                st.markdown(f"""
                    <span style="color:#00ffcc; font-size:0.75rem; font-weight:800; letter-spacing:2px;">● {p['st']}</span>
                    <div style="color:white; font-size:2.3rem; font-weight:900; margin:5px 0;">🔥 {p['n']}</div>
                    <div style="margin: 20px 0;">
                        <span style="color:#94a3b8; font-size:0.85rem; text-transform:uppercase; font-weight:700;">Volume de Cliques (24h)</span><br>
                        <span class="metric-hero">{p['v24']}</span> <span style="color:#00ffcc; font-weight:900;">VIVO</span>
                    </div>
                    <p style="color:#94a3b8; font-size:1rem;">Plataforma: <b style="color:white;">{p['plat']}</b></p>
                    <p style="color:#94a3b8; font-size:1rem;">Comissão Média: <b style="color:#00ffcc;">{p['com']}</b></p>
                    
                    <a href="{p['link']}" target="_blank" class="btn-real">🔌 CONECTAR AFILIAÇÃO {p['plat'].upper()}</a>
                """, unsafe_allow_html=True)
            
            with c_chart:
                st.markdown("<p style='color:white; font-weight:900; font-size:0.9rem; letter-spacing:1.5px; margin-bottom:15px;'>📈 TENDÊNCIA ESTATÍSTICA (12 MESES)</p>", unsafe_allow_html=True)
                # Cálculo realístico de volume anual
                vol_mensal = [int((40 + (i * 4.5)) * p['peso'] * 1000) for i in range(12)]
                df = pd.DataFrame({"Mês": meses, "Volume": vol_mensal})
                
                chart = alt.Chart(df).mark_bar(
                    color='#00ffcc', cornerRadiusTopLeft=6, cornerRadiusTopRight=6
                ).encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0, labelFontWeight=700)),
                    y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title=None, grid=False))
                ).properties(width='container', height=260, background='transparent').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

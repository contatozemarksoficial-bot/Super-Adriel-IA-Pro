import streamlit as st
import pandas as pd
import altair as alt
import time
from datetime import datetime, timedelta

def main():
    # 1. CONFIGURAÇÃO DE ELITE
    st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

    if "caça_ativa" not in st.session_state: st.session_state.caça_ativa = False

    # 2. CSS DE ALTA PERFORMANCE (Design com Divisões Neon)
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp { background-color: #010409 !important; }
    
    /* Menu Lateral Premium */
    [data-testid="stSidebar"] { background-color: #010409 !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }

    /* Divisória Neon Pulsante */
    .divider-neon {
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ffcc, transparent);
        margin: 40px 0;
        opacity: 0.6;
    }

    /* Cabeçalho de Luxo */
    .header-box {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 0;
    }
    .brand-text { color: #ffffff; font-size: 2.5rem; font-weight: 900; letter-spacing: -1.5px; }
    .pro-badge { 
        background: #00ffcc; color: #010409; padding: 3px 12px; 
        border-radius: 4px; font-size: 0.9rem; font-weight: 800;
        box-shadow: 0 0 15px #00ffcc; margin-left: 10px;
    }

    /* Botão de Ativação */
    .stButton>button {
        background: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 8px;
        font-weight: 800; height: 50px; text-transform: uppercase;
        letter-spacing: 1.5px; transition: 0.4s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.4);
        transform: scale(1.02);
    }

    /* Cards de Produtos com Divisão Interna */
    .product-card {
        border: 1px solid #1e293b;
        padding: 30px;
        border-radius: 20px;
        background: rgba(13, 17, 23, 0.8);
        margin-bottom: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    }
    .status-tag { color: #00ffcc; font-size: 0.75rem; font-weight: bold; letter-spacing: 2px; }
    .product-name { color: #ffffff; font-size: 2rem; font-weight: 800; margin: 10px 0; }
    .metric-value { color: #ffffff; font-size: 2.2rem; font-weight: 900; }
    .metric-label { color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

    # --- TOP BAR ---
    st.markdown("""
        <div class="header-box">
            <div class="brand-text">🤖 Adriel-AI <span class="pro-badge">PRO</span></div>
            <div style="color: #94a3b8; font-weight: 500;">Inteligência Preditiva de Tráfego</div>
        </div>
    """, unsafe_allow_html=True)

    # --- ÁREA DE COMANDO (DIVISÃO 1) ---
    col_v1, col_btn, col_v2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 ATIVAR VARREDURA DO ROBÔ"):
            st.session_state.caça_ativa = True

    # LINHA DIVISÓRIA NEON
    st.markdown('<div class="divider-neon"></div>', unsafe_allow_html=True)

    # --- ÁREA DE RESULTADOS (DIVISÃO 2) ---
    if st.session_state.caça_ativa:
        with st.status("🤖 Robô processando Big Data gringo...", expanded=False):
            time.sleep(1)

        hoje = datetime.now()
        meses_eixo = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
        
        produtos = [
            {"n": "Nagano Tonic", "e": "YouTube Ads", "v24": "4.812", "st": "ESCALA AGRESSIVA", "p": "USA/Austrália", "peso": 1.6},
            {"n": "FitSpresso", "e": "Facebook Ads", "v24": "7.329", "st": "DOMÍNIO TOTAL", "p": "Canadá/USA", "peso": 2.3},
            {"n": "Sugar Defender", "e": "Google Review", "v24": "5.610", "st": "ESCALA ESTÁVEL", "p": "UK/USA", "peso": 1.9}
        ]

        for p in produtos:
            # Estrutura de Card com Divisão de Colunas
            st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
            c_txt, c_chart = st.columns([1, 1.2], gap="large")
            
            with c_txt:
                st.markdown(f"""
                    <span class="status-tag">● STATUS: {p['st']}</span>
                    <div class="product-name">🔥 {p['n']}</div>
                    <p style="color: #94a3b8; font-weight: 500;">
                        <span style="color:#00ffcc;">⚖️ Veredito:</span> Oferta validada para escala agressiva no canal <b>{p['e']}</b>.
                    </p>
                    <div style="margin-top:25px;">
                        <span class="metric-label">Volume de Buscas (24h)</span><br>
                        <span class="metric-value">{p['v24']}</span> <span style="color:#94a3b8;">pesquisas</span>
                    </div>
                    <div style="margin-top:15px;">
                        <span class="metric-label">Foco Geográfico</span><br>
                        <b style="color:white; font-size:1.1rem;">{p['p']}</b>
                    </div>
                """, unsafe_allow_html=True)
            
            with c_chart:
                st.markdown("<p style='color:white; font-weight:bold; font-size:0.9rem;'>📊 TENDÊNCIA ESTATÍSTICA (12 MESES)</p>", unsafe_allow_html=True)
                vol_mensal = [int((35 + (i * 4)) * p['peso'] * 1000) for i in range(12)]
                df_graf = pd.DataFrame({"Mês": meses_eixo, "Volume": vol_mensal})
                
                chart = alt.Chart(df_graf).mark_bar(
                    color='#00ffcc', cornerRadiusTopLeft=5, cornerRadiusTopRight=5
                ).encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0)),
                    y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title=None, grid=False))
                ).properties(width='container', height=250, background='transparent').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

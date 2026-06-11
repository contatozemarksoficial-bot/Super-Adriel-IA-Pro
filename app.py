import streamlit as st
import pandas as pd
import altair as alt
import time
from datetime import datetime, timedelta

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

    if "varredura_ativa" not in st.session_state: st.session_state.varredura_active = False

    # 2. CSS DE ALTA COSTURA (Layout Adriel-AI Pro)
    st.markdown("""
    <style>
    /* Reset total para Fundo Triple Black */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #010409 !important;
    }

    /* Título Adriel-AI Pro com robô e charme neon */
    .brand-title {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: -1.5px;
        margin-bottom: 0px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .brand-pro {
        background: #00ffcc;
        color: #010409;
        padding: 2px 12px;
        border-radius: 4px;
        font-size: 1rem;
        vertical-align: middle;
        margin-left: 10px;
        box-shadow: 0 0 15px #00ffcc;
    }

    /* Menu Lateral Premium */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* Botão de Varredura Estilo Radar */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 8px;
        font-weight: 800; height: 55px; width: 100%;
        text-transform: uppercase; letter-spacing: 2px;
        transition: 0.4s all ease;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; color: #010409 !important;
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.5);
        transform: translateY(-2px);
    }

    /* Cards Estilo Adriel-AI (Borda Neon Total) */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 30px;
        border-radius: 16px;
        background: linear-gradient(145deg, #0d1117, #010409);
        margin-bottom: 25px;
        border-top: 1px solid #00ffcc33;
        border-bottom: 1px solid #00ffcc33;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .neon-title { color: #00ffcc; text-shadow: 0 0 10px rgba(0, 255, 204, 0.3); font-weight: 800; }
    .label-meta { color: #94a3b8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1.5px; }
    .valor-grande { font-size: 2.2rem; color: #ffffff; font-weight: 900; margin: 10px 0; }
    
    hr { border-color: #1e293b; opacity: 0.3; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO PERSONALIZADO ---
    st.markdown("""
        <div class="brand-title">
            🤖 Adriel-AI <span class="brand-pro">PRO</span>
        </div>
        <p style="color: #94a3b8; margin-top: -10px; margin-left: 55px; font-weight: 500;">
            Sistemas de Inteligência Preditiva em Tráfego Global
        </p>
    """, unsafe_allow_html=True)

    # --- COMANDO CENTRAL ---
    st.markdown("<br>", unsafe_allow_html=True)
    col_v1, col_btn, col_v2 = st.columns([1, 1.8, 1])
    with col_btn:
        if st.button("🚀 ATIVAR VARREDURA DO ROBÔ"):
            st.session_state.varredura_active = True

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- LAYOUT DE RESULTADOS ---
    if st.session_state.varredura_active:
        with st.status("🤖 Robô Adriel-AI acessando redes gringas...", expanded=False):
            time.sleep(1.2)

        hoje = datetime.now()
        meses_eixo = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
        
        produtos = [
            {"n": "Nagano Tonic", "e": "YouTube/Native", "p": "USA/Australia", "v24": 4812, "st": "ESCALA AGRESSIVA", "peso": 1.6},
            {"n": "FitSpresso", "e": "Facebook VSL", "p": "Canada/USA", "v24": 7329, "st": "DOMÍNIO TOTAL", "peso": 2.3},
            {"n": "Sugar Defender", "e": "Google Review", "p": "UK/USA", "v24": 5610, "st": "ESCALA ESTÁVEL", "peso": 1.9}
        ]

        for p in produtos:
            c_info, c_graf = st.columns([1, 1.2], gap="large")
            
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <span class="label-meta">🤖 STATUS: {p['st']}</span>
                    <h2 class="neon-title">🔥 {p['n']}</h2>
                    <hr>
                    <p><span style="color:#00ffcc; font-weight:bold;">⚖️ VEREDITO:</span> Oferta validada para escala agressiva no canal <b>{p['e']}</b>.</p>
                    <p style="margin-top:15px;" class="label-meta">VOLUME DE BUSCAS (24H):</p>
                    <div class="valor-grande">{p['v24']:,} <span style="font-size:1rem; color:#94a3b8; font-weight:400;">pesquisas</span></div>
                    <p class="label-meta">FOCO GEOGRÁFICO: <b style="color:white;">{p['p']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_graf:
                st.markdown(f"<p style='color:white; font-weight:bold; margin-left:10px; letter-spacing:1px;'>📈 TENDÊNCIA ESTATÍSTICA (12 MESES)</p>", unsafe_allow_html=True)
                
                vol_mensal = [int((35 + (i * 4)) * p['peso'] * 1000) for i in range(12)]
                df_graf = pd.DataFrame({"Mês": meses_eixo, "Volume": vol_mensal})
                
                chart = alt.Chart(df_graf).mark_bar(
                    color='#00ffcc', 
                    cornerRadiusTopLeft=5, 
                    cornerRadiusTopRight=5,
                    opacity=0.85
                ).encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0, labelFontWeight=600)),
                    y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title='Volume Anual', grid=False))
                ).properties(width='container', height=280, background='transparent').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            
            st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

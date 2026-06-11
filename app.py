import streamlit as st
import pandas as pd
import altair as alt
import time
from datetime import datetime, timedelta

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Radar Pro - Luxo V12", layout="wide", initial_sidebar_state="expanded")

    if "varredura_ativa" not in st.session_state: st.session_state.varredura_active = False

    # 2. CSS DE ALTA COSTURA (Layout de Luxo)
    st.markdown("""
    <style>
    /* Reset total para Fundo Triple Black */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #010409 !important;
    }

    /* Menu Lateral Premium */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700; letter-spacing: 0.5px; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* Botão de Varredura Estilo Radar */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 6px;
        font-weight: bold; height: 50px; width: 100%;
        text-transform: uppercase; letter-spacing: 2px;
        transition: 0.4s all ease;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; color: #010409 !important;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.4);
    }

    /* Cards de Vidro (Glassmorphism) */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 30px;
        border-radius: 16px;
        background: linear-gradient(145deg, #0d1117, #010409);
        margin-bottom: 20px;
        border-left: 6px solid #00ffcc;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.3);
    }
    
    .neon-title { color: #00ffcc; text-shadow: 0 0 10px rgba(0, 255, 204, 0.3); font-weight: 800; }
    .label-meta { color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }
    .valor-grande { font-size: 2rem; color: #ffffff; font-weight: 800; margin: 10px 0; }
    
    /* Linha divisória fina */
    hr { border-color: #1e293b; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO ---
    st.markdown('<h1 style="color: #ffffff; font-size: 2.5rem; font-weight: 900; letter-spacing: -2px;">RADAR <span style="color: #00ffcc;">ELITE</span></h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; margin-bottom: 30px;">Sincronização direta com servidores de tráfego gringo.</p>', unsafe_allow_html=True)

    # --- COMANDO CENTRAL ---
    col_v1, col_btn, col_v2 = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("🚀 INICIAR VARREDURA SINCRONIZADA"):
            st.session_state.varredura_active = True

    st.markdown("---")

    # --- LAYOUT DE RESULTADOS ---
    if st.session_state.varredura_active:
        with st.status("📡 Conectando à rede de satélites Ads...", expanded=False):
            time.sleep(1)

        # Base de dados blindada
        hoje = datetime.now()
        meses_eixo = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
        
        produtos = [
            {"n": "Nagano Tonic", "e": "YouTube/Native", "p": "USA/Australia", "v24": 4291, "st": "ESCALA AGRESSIVA", "peso": 1.5},
            {"n": "FitSpresso", "e": "Facebook VSL", "p": "Canada/USA", "v24": 7120, "st": "DOMÍNIO TOTAL", "peso": 2.2},
            {"n": "Sugar Defender", "e": "Google Review", "p": "UK/USA", "v24": 5290, "st": "ESCALA ESTÁVEL", "peso": 1.8}
        ]

        for p in produtos:
            # Dividindo em duas colunas: Info e Gráfico
            c_info, c_graf = st.columns([1, 1.2], gap="large")
            
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <span class="label-meta">{p['st']}</span>
                    <h2 class="neon-title">🔥 {p['n']}</h2>
                    <hr>
                    <p><span style="color:#00ffcc; font-weight:bold;">⚖️ VEREDITO:</span> Oferta validada para escala no canal <b>{p['e']}</b>.</p>
                    <p style="margin-top:15px;" class="label-meta">Volume Real (24h):</p>
                    <div class="valor-grande">{p['v24']:,} <span style="font-size:1rem; color:#94a3b8;">buscas</span></div>
                    <p class="label-meta">País Alvo: <b style="color:white;">{p['p']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_graf:
                st.markdown(f"<p style='color:white; font-weight:bold; margin-left:10px;'>📈 Tendência Histórica (12 Meses)</p>", unsafe_allow_html=True)
                
                # Gerador de dados determinístico (Escala em Milhares)
                vol_mensal = [int((35 + (i * 4)) * p['peso'] * 1000) for i in range(12)]
                df_graf = pd.DataFrame({"Mês": meses_eixo, "Volume": vol_mensal})
                
                chart = alt.Chart(df_graf).mark_bar(
                    color='#00ffcc', 
                    cornerRadiusTopLeft=4, 
                    cornerRadiusTopRight=4,
                    opacity=0.9
                ).encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0)),
                    y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title='Volume Anual', grid=False))
                ).properties(width='container', height=280, background='transparent').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            
            st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

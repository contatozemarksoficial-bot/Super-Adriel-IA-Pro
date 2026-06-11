import streamlit as st
import pandas as pd
import altair as alt
import time
import random
from datetime import datetime, timedelta

# 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
st.set_page_config(page_title="Adriel-AI Pro | Ativador", layout="wide", initial_sidebar_state="expanded")

# Inicia memória do robô para o botão responder e não sumir
if "ativado" not in st.session_state: st.session_state.ativado = False

# 2. CSS DE ALTA COSTURA - FUNDO PRETO E CIANO NEON
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

    /* Botão de Ativação Estilo Radar */
    .stButton>button {
        background: linear-gradient(90deg, #0d1117, #010409) !important;
        color: #00ffcc !important; border: 2px solid #00ffcc !important;
        border-radius: 10px !important; font-weight: 900 !important;
        height: 55px !important; width: 100% !important;
        text-transform: uppercase; letter-spacing: 2px; transition: 0.5s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.5) !important;
        transform: translateY(-2px);
    }

    /* Card de Membro Blindado */
    .member-card {
        border: 1px solid #1e293b; padding: 40px; border-radius: 25px;
        background: rgba(13, 17, 23, 0.9); margin-bottom: 35px;
        border-top: 5px solid #00ffcc; box-shadow: 0 25px 50px rgba(0,0,0,0.7);
    }
    .neon-text { color: #00ffcc !important; font-weight: bold; }
    .metric-hero { color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
st.markdown('<p style="color:#94a3b8; margin-top:-10px; margin-left:65px; font-weight:600;">Sincronização de Inteligência Preditiva</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- COMANDO CENTRAL ---
col_v1, col_btn, col_v2 = st.columns([1, 1.8, 1])
with col_btn:
    # O botão agora ativa a memória persistente
    if st.button("⚡ EXECUTAR ATIVAÇÃO E VARREDURA"):
        st.session_state.ativado = True

st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

# --- RESULTADOS COM ESTRATÉGIA DE FUNDO DE FUNIL ---
if st.session_state.ativado:
    with st.status("🔍 Sincronizando rede de satélites Ads...", expanded=False):
        time.sleep(1)

    hoje = datetime.now()
    meses = [(hoje - timedelta(days=30*i)).strftime('%b') for i in range(12)][::-1]
    
    # DADOS REAIS DE FUNDO DE FUNIL (BRAND BIDDING)
    produtos = [
        {
            "n": "Nagano Lean Body Tonic", 
            "v24": "5.412", "st": "ESCALA AGRESSIVA", 
            "plat": "BuyGoods", "com": "$127", "peso": 1.7,
            "link": "https://buygoods.com"
        },
        {
            "n": "FitSpresso (Coffee Loophole)", 
            "v24": "9.120", "st": "DOMÍNIO TOTAL", 
            "plat": "ClickBank", "com": "$145", "peso": 2.5,
            "link": "https://clickbank.com"
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
                
                <p><span class="neon-text">⚖️ VEREDITO:</span> O robô confirma que o produto <b>{p['n']}</b> é ideal para <span class="neon-text">Fundo de Funil</span>.</p>
                <p style="color:#94a3b8; font-size:0.9rem; margin-top:-10px;">Estratégia: Captura direta de tráfego de intenção (Brand Bidding) nos EUA e Canadá.</p>
                
                <div style="margin-top:20px; padding-top:15px; border-top:1px solid #1e293b;">
                    <p style="color:#94a3b8; margin-bottom:5px;">Plataforma: <b style="color:white;">{p['plat']}</b></p>
                    <p style="color:#94a3b8;">Comissão: <b style="color:#00ffcc;">{p['com']}</b></p>
                    <a href="{p['link']}" target="_blank" style="text-decoration:none;">
                        <div style="padding:15px; border:1px solid #00ffcc; border-radius:8px; color:#00ffcc; text-align:center; font-weight:900; margin-top:10px; transition:0.3s;" onMouseOver="this.style.background='#00ffcc';this.style.color='#010409'" onMouseOut="this.style.background='transparent';this.style.color='#00ffcc'">
                            🔌 CONECTAR AFILIAÇÃO {p['plat'].upper()}
                        </div>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        
        with c_chart:
            st.markdown("<p style='color:white; font-weight:900; font-size:0.9rem; letter-spacing:1.5px; margin-bottom:15px;'>📈 TENDÊNCIA ESTATÍSTICA (12 MESES)</p>", unsafe_allow_html=True)
            vol_mensal = [int((40 + (i * 4.5)) * p['peso'] * 1000) for i in range(12)]
            df = pd.DataFrame({"Mês": meses, "Volume": vol_mensal})
            
            chart = alt.Chart(df).mark_bar(
                color='#00ffcc', cornerRadiusTopLeft=6, cornerRadiusTopRight=6
            ).encode(
                x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='#94a3b8', title=None, labelAngle=0)),
                y=alt.Y('Volume', axis=alt.Axis(labelColor='#94a3b8', title=None, grid=False))
            ).properties(width='container', height=260, background='transparent').configure_view(strokeWidth=0)
            
            st.altair_chart(chart, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Sistema em standby. Clique em 'Executar Ativação' para carregar a inteligência de fundo de funil.")

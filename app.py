import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE (GRUDADO NO TETO DO MONITOR)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL (TRAVA O DESIGN DO MONITOR E OCULTA BARRAS NATIVAS)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Exato do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }

/* 🚨 DELEÇÃO CIRÚRGICA DA BARRA BRANCA SUPERIOR E MENU LATERAL CINZA NATIVO */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; height: 0px !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* Indicador de Operadores Ativos (Canto Superior Direito) */
.operadores-ativos { text-align: right; color: #00ffcc !important; font-weight: 800; font-size: 14px; margin-top: -10px; }

/* Molduras de Conexões de Plataformas (Fila Superior) */
.box-plataforma {
    background-color: #0f1526 !important; border: 1px solid #1e293b !important; border-radius: 8px !important;
    padding: 10px !important; text-align: center; font-size: 10px !important; font-weight: 900 !important; color: #cbd5e1 !important; letter-spacing: 1px;
}

/* Customização dos Containers de Métricas em Gradiente Escuro do seu Chassi */
[data-testid="stMetricContainer"] {
    background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important;
    border-bottom: 3px solid #00ffcc !important; padding: 20px !important; border-radius: 12px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
}
div[data-testid="stMetricContainer"]:nth-of-type(4) { border-bottom: 3px solid #ff0055 !important; }

/* Forçador de cor branca nas métricas para sumir com o apagado */
[data-testid="stMetricLabel"], [data-testid="stMetricValue"] { color: #ffffff !important; }
[data-testid="stMetricValue"] { font-size: 1.8rem !important; font-weight: 800 !important; }

/* 🧱 CARDS DOS PLANOS E SEÇÕES INTERNAS */
.card-plano-luxo { background-color: #080f1d !important; border: 1px solid #1e293b !important; border-radius: 14px !important; padding: 25px !important; min-height: 200px; }
.caixa-holografica-master { background-color: #080f1d !important; border: 2px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; width: 100% !important; }

/* Seletor Executivo de Módulos (Menu de Abas do Tema) */
.stSelectbox > div { background-color: #0f172a !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; }
.stSelectbox div[role="button"] { color: #00ffcc !important; font-weight: 800 !important; }

/* 🚨 REPROGRAMAÇÃO DO BOTÃO DE CHECKOUT CIANO DO PRINT EM FORMATO CÁPSULA ARREDONDADA */
div.stLinkButton > a, .stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
    padding: 12px 20px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
    display: block !important; text-align: center !important; text-decoration: none !important;
}
div.stLinkButton > a:hover, .stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important; transform: scale(1.01) !important; }
div.stLinkButton > a p, .stButton > button p { color: #030712 !important; font-weight: 900 !important; }

/* Caixas de texto e tabelas */
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 12px !important; }
.stCodeBlock, pre { background-color: #0b111e !important; border: 1px solid #1e293b !important; border-radius: 8px !important; }
.stCodeBlock code, pre code { color: #33ffdd !important; font-size: 13.5px !important; }
.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; }
</style>
""", unsafe_allow_html=True)

# Inicialização segura do painel na memória RAM
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "Área de Membros (Faturamento)"

# =============================================================================================================
# 🏢 ESTRUTURA VISUAL CORPORATIVA (IDÊNTICA AO PRINT DO SEU MONITOR)
# =============================================================================================================
col_tit, col_ope = st.columns([2.0, 1.0])
with col_tit:
    st.markdown('<h2 style="font-size: 2.5rem; font-weight: 900; color: #ffffff; margin:0; font-family: sans-serif;">🤖 Adriel-AI <span style="background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px;">PRO</span></h2>', unsafe_allow_html=True)
with col_ope:
    st.markdown('<p class="operadores-ativos">🟢 1.895 OPERADORES ATIVOS NA ÁREA</p>', unsafe_allow_html=True)

st.write("")

# Fila Superior de Conexões Ativas das Plataformas
col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
col_p1.markdown('<div class="box-plataforma">🟢 • CLICKBANK</div>', unsafe_allow_html=True)
col_p2.markdown('<div class="box-plataforma">🟢 • BUYGOODS</div>', unsafe_allow_html=True)
col_p3.markdown('<div class="box-plataforma">🟢 • DIGISTORE24</div>', unsafe_allow_html=True)
col_p4.markdown('<div class="box-plataforma">🟢 • STRIPE DASH</div>', unsafe_allow_html=True)
col_p5.markdown('<div class="box-plataforma">🟢 • HOSTINGER VPS</div>', unsafe_allow_html=True)

st.write("")

# Monitoramento de Métricas Reais do Painel Superior
col_met1, col_met2, col_met3, col_met4 = st.columns(4)
with col_met1: st.metric(label="FATURAMENTO GERAL", value="R$ 142.580")
with col_met2: st.metric(label="LICENÇAS ATIVAS", value="2.105")
with col_met3: st.metric(label="RECORRÊNCIA (MRR)", value="R$ 104.200")
with col_met4: st.metric(label="TAXA DE CHURN", value="0.8%")

st.write("---")

# Seletor de Módulos integrado ao tema para navegar no teto sem a barra cinza feia da esquerda
st.session_state.modulo_ativo = st.selectbox(
    "Navegação Master de Módulos (Selecione a ferramenta de trabalho):",
    ["Área de Membros (Faturamento)", "Módulo 7: Minerador de Palavras Vivas"]
)

st.write("")
url_hostinger = "https://hostinger.com"

# =============================================================================================================
# ROTEADOR DE TELAS DO TESTE
# =============================================================================================================

# 💳 TELA 1: EXIBIÇÃO ORIGINAL DO SEU PRINT (OS 3 CARDS DE VALORES FUNCIONAIS)
if st.session_state.modulo_ativo == "Área de Membros (Faturamento)":
    st.markdown('<h3 style="font-size: 1.6rem; font-weight: 800; color: #ffffff;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h3>', unsafe_allow_html=True)
    st.write("")
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1:
        st.markdown('<div class="card-plano-luxo"><span style="color:#94a3b8; font-weight:bold; font-size:11px;">PLANO MENSAL START</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#fff !important;">R$ 47</h2><p style="font-size:13px; color:#94a3b8;">Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata.</p></div>', unsafe_allow_html=True)
        st.link_button("💳 PAGAR COM CARTÃO / PIX", url_hostinger, use_container_width=True, key="btn_st_t1")
    with col_v2:
        st.markdown('<div class="card-plano-luxo"><span style="color:#94a3b8; font-weight:bold; font-size:11px;">PLANO MENSAL PRO</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#fff !important;">R$ 97</h2><p style="font-size:13px; color:#94a3b8;">Start + Módulo RSA (45 Keywords) + Arquiteto de Funil. Foco em quem já escala.</p></div>', unsafe_allow_html=True)
        st.link_button("💳 PAGAR COM CARTÃO / PIX ", url_hostinger, use_container_width=True, key="btn_st_t2")
    with col_v3:
        st.markdown('<div class="card-plano-luxo"><span style="color:#94a3b8; font-weight:bold; font-size:11px;">PLANO ELITE MASTER</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#fff !important;">R$ 197</h2><p style="font-size:13px; color:#94a3b8;">ACESSO TOTAL ILIMITADO + Construtor Pre-Sell Hostinger. O poder máximo do robô.</p></div>', unsafe_allow_html=True)
        st.link_button("💳 PAGAR COM CARTÃO / PIX  ", url_hostinger, use_container_width=True, key="btn_st_t3")

# 📡 TELA 2: MINERADOR VIVO DESCARREGANDO UMA POR UMA (O SHOW VISUAL)
elif st.session_state.modulo_ativo == "Módulo 7: Minerador de Palavras Vivas":

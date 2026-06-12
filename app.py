import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE (GRUDADO NO TETO DO MONITOR)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL (DESTRÓI O CINZA DA ESQUERDA E FIXA O NEON DO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Exato do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }

/* 🚨 DELEÇÃO CIRÚRGICA DE TODA E QUALQUER BARRA LATERAL CINZA OU CABEÇALHO NATIVO */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; height: 0px !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { display: none !important; width: 0px !important; visibility: hidden !important; }

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

/* 🧱 CARDS DOS PLANOS DA ADESÃO COM ARREMATES DE LUXO DE ACORDO COM SEU PRINT */
.container-card-luxo {
    background-color: #080f1d; border: 1px solid #1e293b; border-radius: 14px; padding: 25px;
    min-height: 250px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;
}
.caixa-holografica-master { background-color: #080f1d !important; border: 2px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; width: 100% !important; }

/* 🚨 REPROGRAMAÇÃO COMPILADA DOS BOTÕES NATIVOS LINK DO STREAMLIT EM CÁPSULA CIANO NEON VIBRANTE */
div.stLinkButton > a, .stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important; /* Formato cápsula arredondada Apple */
    padding: 12px 24px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
    display: block !important; text-align: center !important; text-decoration: none !important;
}
div.stLinkButton > a:hover, .stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.8) !important; transform: scale(1.02) !important; color: #030712 !important; }
div.stLinkButton > a p, .stButton > button p { color: #030712 !important; font-weight: 900 !important; }

/* Caixa do seletor e inputs */
.stSelectbox > div { background-color: #0f172a !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
.stSelectbox div[role="button"] { color: #00ffcc !important; font-weight: 800 !important; }
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 14px !important; font-size: 15px !important; }

/* Tabelas e Terminais */
h1, h2, h3, h4, .stMarkdown p { color: #ffffff !important; }
.stCodeBlock, pre { background-color: #0b111e !important; border: 1px solid #1e293b !important; border-radius: 8px !important; }
.stCodeBlock code, pre code { color: #33ffdd !important; font-size: 13.5px !important; }
.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; }
</style>
""", unsafe_allow_html=True)

# URL de comissão parceira da Hostinger
url_hostinger = "https://hostinger.com"

# =============================================================================================================
# 🔒 3. INTERFACE DA TRAVA DE SEGURANÇA: ENTRADA COM CHAVE MESTRE VIP NO CÓDIGO
# =============================================================================================================
st.markdown('<p class="operadores-ativos">🛡️ SECURITY PROTOCOL ACTIVE</p>', unsafe_allow_html=True)
st.write("")

# Campo de Texto para Validação de Acesso
chave_digitada = st.text_input("🛡️ CHAVE MESTRE REQUERIDA — Insira seu Token de Ativação SaaS para destravar:", type="password", placeholder="Digite a chave secreta aqui...")
st.write("")

# 🚨 VERIFICAÇÃO DIRETA: SE O TEXTO DIGITADO FOR A CHAVE MESTRE, ABRE TODO O IMPÉRIO!
if chave_digitada.strip() == "ADRIEL-VIP-2026":
    
    # 🏢 SEÇÃO INTERNA DESTRANCADA TOTALMENTE ACESA (A FERRARI DO SEU PRINT)
    col_tit, col_ope = st.columns([2.0, 1.0])
    with col_tit:
        st.markdown('<h2 style="font-size: 2.5rem; font-weight: 900; color: #ffffff; margin:0; font-family: sans-serif;">🤖 Adriel-AI <span style="background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px;">PRO</span></h2>', unsafe_allow_html=True)
    with col_ope:
        st.markdown('<p class="operadores-ativos" style="color: #00ffcc !important;">🟢 COMANDANTE CONECTADO</p>', unsafe_allow_html=True)

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

    # Seletor de Módulos integrado ao tema para navegar no teto
    modulo_selecionado = st.selectbox(
        "Navegação Master de Módulos (Selecione a ferramenta de trabalho):",
        ["Área de Membros (Faturamento Recorrente)", "Módulo 7: Minerador de Palavras Vivas"]
    )

    st.write("")

    # ROTEADOR DE TELAS INTERNAS DESTRANCADAS
    if modulo_selecionado == "Área de Membros (Faturamento Recorrente)":
        st.markdown('<h3 style="font-size: 1.6rem; font-weight: 800; color: #ffffff;">💳 ADESÃO ÀS LICENÇAS DISPONÍVEIS</h3>', unsafe_allow_html=True)
        st.write("Seu painel corporativo está respondendo de forma totalmente íntegra na nuvem.")
        st.write("")
        
        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            st.markdown('<div class="container-card-luxo"><div><span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL START</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 47</h2><p style="font-size:13px; color:#94a3b8; line-height:1.5;">Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata de ofertas na gringa.</p></div></div>', unsafe_allow_html=True)
            st.link_button("💳 PAGAR COM CARTÃO / PIX", url_hostinger, use_container_width=True, key="lnk_start_real")
        with col_v2:
            st.markdown('<div class="container-card-luxo"><div><span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL PRO</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 97</h2><p style="font-size:13px; color:#94a3b8; line-height:1.5;">Start + Módulo RSA (45 Keywords) + Arquiteto de Funil. Foco total em quem já escala campanhas pesadas.</p></div></div>', unsafe_allow_html=True)
            st.link_button("💳 PAGAR COM CARTÃO / PIX ", url_hostinger, use_container_width=True, key="lnk_pro_real")
        with col_v3:

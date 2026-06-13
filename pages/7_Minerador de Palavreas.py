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
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
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
.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; font-size: 11px !important; line-height: 1.2 !important; }
</style>
""", unsafe_allow_html=True)

url_hostinger = "https://hostinger.com"

# Inicialização segura das variáveis de controle de privilégio do plano
if "plano_usuario" not in st.session_state: 
    st.session_state.plano_usuario = None

# =============================================================================================================
# 🔒 3. VERIFICAÇÃO INTELIGENTE DE CRIPTOGRAFIA DE PLANOS (TELA DE BLOQUEIO DO CLIENTE)
# =============================================================================================================
if st.session_state.plano_usuario is None:
    col_t, col_o = st.columns([2.0, 1.0])
    with col_t: st.markdown('<h2 style="font-size: 2.5rem; font-weight: 900; color: #ffffff; margin:0;">🤖 Adriel-AI <span style="background:#ff0055; color:#fff; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px; font-weight:900;">TRANCADO</span></h2>', unsafe_allow_html=True)
    with col_o: st.markdown('<p class="operadores-ativos" style="color:#ff0055 !important;">🔴 AGUARDANDO CRIPTOGRAFIA DE PLANO</p>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("""
    <div style="background-color: rgba(255, 0, 85, 0.04); border: 2px solid #ff0055; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(255,0,85,0.1);">
        <h3 style="color: #ff4d88; margin-top:0; font-weight:900; font-size:18px;">🔒 TERMINAL DE ACESSO SAAS INTEGRADO</h3>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom:0; line-height:1.6;">
            A inteligência robótica Adriel-AI Pro está bloqueada. Insira o token de licença específico enviado ao seu e-mail pós-faturamento. O sistema identificará automaticamente a sua assinatura e liberará as ferramentas correspondentes ao seu nível de plano contratado.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    chave_comprada = st.text_input("Insira o Token de Licença do Plano Adquirido:", type="password", placeholder="Digite a chave do seu plano para testar (START-47, PRO-97 ou ELITE-197)...")
    st.write("")
    
    if st.button("🔑 RETER LICENÇA E ACESSAR SOFTWARE"):
        token_limpo = chave_comprada.strip()
        if token_limpo == "START-47":
            st.session_state.plano_usuario = "START"
            st.rerun()
        elif token_limpo == "PRO-97":
            st.session_state.plano_usuario = "PRO"
            st.rerun()
        elif token_limpo == "ELITE-197":
            st.session_state.plano_usuario = "ELITE"
            st.rerun()
        else:
            st.markdown('<div style="background-color: rgba(255,0,85,0.1); border: 1px solid #ff0055; color: #ff4d88; padding: 12px; border-radius: 8px; font-weight: bold; font-size: 14px; text-align: center; margin-bottom: 20px;">❌ Token Inválido. Teste as chaves oficiais: START-47, PRO-97 ou ELITE-197.</div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<h3 style="font-size: 1.6rem; font-weight: 800; color: #ffffff; text-align:center;">💳 SELECIONE UM PLANO PUBLICITÁRIO PARA ADESÃO IMEDIATA</h3>', unsafe_allow_html=True)
    st.write("")
    
    col_v1, col_v2, col_v3 = st.columns(3)
    with col_v1:
        st.markdown("""<div class="container-card-luxo"><div><span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL START</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 47</h2><p style="font-size:13px; color:#94a3b8; line-height:1.5; margin-bottom:20px;"><b>Chave de Teste: START-47</b><br>Liberação exclusiva do Módulo 1 (Radar de Produtos). Acesso básico para validação imediata.</p></div></div>""", unsafe_allow_html=True)
        st.link_button("💳 CONTRATAR START", url_hostinger, use_container_width=True, key="btn_p1_buy")
    with col_v2:
        st.markdown("""<div class="container-card-luxo"><div><span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL PRO</span><h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 97</h2><p style="font-size:13px; color:#94a3b8; line-height:1.5; margin-bottom:20px;"><b>Chave de Teste: PRO-97</b><br>Radar + Módulo RSA (Keywords) + Arquiteto de Funil. Foco em quem já escala campanhas.</p></div></div>""", unsafe_allow_html=True)
        st.link_button("💳 CONTRATAR PRO", url_hostinger, use_container_width=True, key="btn_p2_buy")
    with col_v3:

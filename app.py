import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

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

/* Customização dos Containers de Métricas em Gradiente Escuro */
[data-testid="stMetricContainer"] {
    background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important;
    border-bottom: 3px solid #00ffcc !important; padding: 20px !important; border-radius: 12px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
}
div[data-testid="stMetricContainer"]:nth-of-type(4) { border-bottom: 3px solid #ff0055 !important; }

[data-testid="stMetricLabel"], [data-testid="stMetricValue"] { color: #ffffff !important; }
[data-testid="stMetricValue"] { font-size: 1.8rem !important; font-weight: 800 !important; }

/* 🧱 DESIGN DOS CARDS DE VALORES E CENTRAL HOLOGRÁFICA EM HTML PURO BLINDADO */
.container-card-luxo {
    background-color: #080f1d; border: 1px solid #1e293b; border-radius: 14px; padding: 25px;
    min-height: 250px; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box;
}

.caixa-holografica-master { background-color: #080f1d !important; border: 2px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; width: 100% !important; }

/* 🚨 BOTÕES NATIVOS EM CÁPSULAS PERFEITAS DA APPLE CIANO NEON DO SEU PRINT */
div.stLinkButton > a, .stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important; /* Formato Pílula */
    padding: 12px 24px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
    display: block !important; text-align: center !important; text-decoration: none !important;
}
div.stLinkButton > a:hover, .stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important; transform: scale(1.01) !important; }
div.stLinkButton > a p, .stButton > button p { color: #030712 !important; font-weight: 900 !important; }

/* 🚨 BOTÃO DE RESET ESPECÍFICO VERMELHO ATIVO */
.btn-reset-guerra div.stButton > button {
    background: linear-gradient(135deg, #ff0055 0%, #ff4d88 100%) !important;
    color: #ffffff !important; box-shadow: 0 0 15px rgba(255, 0, 85, 0.4) !important;
}
.btn-reset-guerra div.stButton > button p { color: #ffffff !important; }

/* Customização da Caixa do Seletor e Inputs */
.stSelectbox > div { background-color: #0f172a !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
.stSelectbox div[role="button"] { color: #00ffcc !important; font-weight: 800 !important; }
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 14px !important; font-size: 15px !important; }

/* Tabelas e Terminais */
.stCodeBlock, pre { background-color: #0b111e !important; border: 1px solid #1e293b !important; border-radius: 8px !important; }
.stCodeBlock code, pre code { color: #33ffdd !important; font-size: 13.5px !important; }
.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; }
</style>
""", unsafe_allow_html=True)

# 🚨 FORÇADOR DE MEMÓRIA CRÍTICO (Ao dar Deploy, inicia obrigatoriamente Deslogado para testar)
if "cliente_autenticado" not in st.session_state: 
    st.session_state.cliente_autenticado = False

if "modulo_ativo" not in st.session_state: 
    st.session_state.modulo_ativo = "Área de Membros (Faturamento)"

url_hostinger = "https://hostinger.com"

# =============================================================================================================
# 🔒 TELA DE CADASTRO E BLOQUEIO DE CLIENTE (TEMA DE LUXO REMODELADO - ZERO REBORDAS BRANCAS)
# =============================================================================================================
if not st.session_state.cliente_autenticado:
    col_t, col_o = st.columns([2.0, 1.0])
    with col_t: st.markdown('<h2 style="font-size: 2.6rem; font-weight: 900; color: #ffffff; margin:0;">🤖 Adriel-AI <span style="background:#ff0055; color:#fff; padding:3px 10px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px; font-weight:900; text-shadow:none;">TRANCADO</span></h2>', unsafe_allow_html=True)
    with col_o: st.markdown('<p class="operadores-ativos" style="color:#ff0055 !important;">🔴 SISTEMA AGUARDANDO LICENÇA VÁLIDA</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    st.markdown("""
    <div style="background-color: rgba(255, 0, 85, 0.04); border: 2px solid #ff0055; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(255,0,85,0.1);">
        <h3 style="color: #ff4d88; margin-top:0; font-weight:900; font-size:18px;">⚠️ CHAVE DE LICENÇA MANDATÓRIA REQUERIDA</h3>
        <p style="color: #cbd5e1; font-size: 13.5px; margin-bottom:0; line-height:1.6;">
            Este ecossistema militar de inteligência gringa está restrito a assinantes ativos. Insira a sua chave digital recebida por e-mail no terminal abaixo para validar o login e liberar os robôs de mineração. Se você ainda não possui acesso ativo, realize a adesão imediata a um dos planos na base do painel.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    chave_digitada = st.text_input("Digite a sua Chave de Acesso SaaS abaixo:", placeholder="Insira o Token de Ativação (Dica do Teste: ADRIEL-VIP-2026)...", key="input_pass_mestre")
    st.write("")
    
    if st.button("🔑 EFETUAR LOGIN NO SISTEMA", key="btn_login_mestre"):
        if chave_digitada.strip() == "ADRIEL-VIP-2026":
            st.session_state.cliente_autenticado = True
            st.rerun()
        else:
            st.markdown('<div style="background-color: rgba(255,0,85,0.1); border: 1px solid #ff0055; color: #ff4d88; padding: 12px; border-radius: 8px; font-weight: bold; font-size: 14px; text-align: center; margin-bottom: 20px;">❌ Chave de Acesso Inválida ou Expirada no Banco de Dados.</div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<h3 style="font-size: 1.6rem; font-weight: 800; color: #ffffff; text-align:center; letter-spacing:0.5px;">💳 CONTRATAR ASSINATURA RECORRENTE DO ROBÔ</h3>', unsafe_allow_html=True)
    st.write("")
    
    col_v1, col_v2, col_v3 = st.columns(3)
    
    with col_v1:
        st.markdown(f"""
        <div class="container-card-luxo">
            <div>
                <span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL START</span>
                <h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 47</h2>
                <p style="font-size:13px; color:#94a3b8; line-height:1.5; margin-bottom:20px;">
                    Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata de ofertas na gringa.
                </p>
            </div>
            <a href="{url_hostinger}" target="_blank" class="botao-capsula-neon">💳 ASSINAR PREMIUM</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col_v2:
        st.markdown(f"""
        <div class="container-card-luxo">
            <div>
                <span style="color:#94a3b8; font-weight:bold; font-size:11px; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL PRO</span>
                <h2 style="font-size:2.4rem; font-weight:900; margin:10px 0; color:#ffffff !important;">R$ 97</h2>
                <p style="font-size:13px; color:#94a3b8; line-height:1.5; margin-bottom:20px;">

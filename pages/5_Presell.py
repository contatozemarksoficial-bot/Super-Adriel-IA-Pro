import streamlit as st
import pandas as pd
import requests
import json
import time
import re

# 1. CONFIGURAÇÃO OFICIAL DE ALTO LUXO DE CINEMA
st.set_page_config(page_title="Adriel-AI Pro", page_icon="🤖", layout="wide")

CHAVE_MESTRA = "ONYX_MASTER_2026"

# Inicialização de estados de sessão blindados contra deslogues
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "DASHBOARD"
if "status_usuario" not in st.session_state: st.session_state.status_usuario = "ADMIN"  # Abre ativo para testes
if "api_key_global" not in st.session_state: st.session_state.api_key_global = ""

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL LUXO SUPREMO CYBER-PULSE
# =============================================================================================================
st.markdown("""
<style>
/* Reset de fundo escuro profundo de cinema */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #0c111d !important; }

/* Ocultação total e absoluta da navegação nativa redundante do Streamlit */
[data-testid="stSidebarNav"], ul[data-testid="stSidebarNavItems"], .stSidebarNavItems { 
    display: none !important; visibility: hidden !important; height: 0px !important; opacity: 0 !important;
}
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2rem; padding-right: 2rem; }

/* BOTÕES DO MENU LATERAL ESCUROS (IGUAL AO SEU PRINT) */
.stButton > button {
    background-color: #111827 !important; color: #ffffff !important;
    border: 1px solid #1f293b !important; border-radius: 8px !important;
    padding: 14px 20px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.5px !important;
    text-transform: uppercase !important; transition: all 0.2s ease-in-out !important;
}
.stButton > button:hover {
    border-color: #00ffcc !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; }

/* 🧠 PAINEL HUD HOLOGRÁFICO: A CARA DO ROBÔ INTELIGENTE */
.hud-robot {
    background: radial-gradient(circle at 50% 50%, #0d1e3d 0%, #040814 100%) !important;
    border: 2px dashed #00ffcc !important; border-radius: 20px !important; padding: 30px !important; text-align: center !important;
    box-shadow: 0 0 35px rgba(0, 255, 204, 0.15) !important; margin-bottom: 25px !important;
}

/* CARDS DE MONITORAMENTO DE CONSULTAS DA CONTA */
.grid-metricas { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
.card-metric {
    background-color: #0f172a !important; border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important;
    padding: 22px !important; text-align: center !important; box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
}
.card-metric-title { font-size: 11px; font-weight: 800; color: #64748b; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }
.card-metric-value { font-size: 28px; font-weight: 900; color: #ffffff; }

/* CARDS DE PREÇO DO SEU PRINT COM BORDAS ARREDONDADAS */
.card-plano {
    background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 16px !important;
    padding: 35px !important; box-shadow: 0 12px 40px rgba(0,0,0,0.6) !important; text-align: left;
}
.plano-title { font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }
.plano-price { font-size: 40px; font-weight: 900; color: #ffffff; margin: 15px 0; font-family: monospace; }
.plano-desc { font-size: 13.5px; color: #94a3b8; line-height: 1.6; margin-bottom: 30px; min-height: 60px; }

/* Botão de Pagamento Verde Fluorescente Arredondado */
.btn-compra {
    display: block; background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%);
    color: #030712 !important; text-decoration: none !important; text-align: center;
    font-weight: 900; font-size: 13px; padding: 15px; border-radius: 30px;
    text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
}
.terminal-cyber { background-color: #02040a !important; border: 2px solid #1e293b !important; border-left: 4px solid #00ffcc !important; border-radius: 8px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; font-size: 13px !important; }
.stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. INTERFACE LATERAL: LINKS DE COMANDO SUPER LUXO ESTÁVEIS
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 3px;">👑 Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #475569; font-weight: bold; margin-bottom: 25px; letter-spacing:1px;">MÓDULOS DE COMANDO</p>', unsafe_allow_html=True)
    
    if st.button("📊 DASHBOARD", key="m_dash"): st.session_state.modulo_ativo = "DASHBOARD"
    if st.button("🔥 1. RADAR ELITE", key="m_rad"): st.session_state.modulo_ativo = "RADAR"
    if st.button("🛰️ 2. AUDITOR IA", key="m_aud"): st.session_state.modulo_ativo = "AUDITOR"
    if st.button("✍️ 3. GERADOR RSA", key="m_gen"): st.session_state.modulo_ativo = "GERADOR"
    if st.button("🎯 4. CAÇADOR V10", key="m_cac"): st.session_state.modulo_ativo = "CACADOR"
    if st.button("📄 5. PRE-SELL AUTOMÁTICA", key="m_pre"): st.session_state.modulo_ativo = "PRESELL"
    st.write("---")
    if st.button("👥 ASSINANTES", key="m_ass"): st.session_state.modulo_ativo = "ASSINANTES"

# =============================================================================================================
# 4. ENGENHARIA DE TELAS SUPREMA UNIFICADA REAL (MÓDULO POR MÓDULO LUXUOSO)
# =============================================================================================================

# 📊 DASHBOARD PRINCIPAL (TELA DO ROBÔ)
if st.session_state.modulo_ativo == "DASHBOARD":
    st.markdown('<h1 style="font-size: 2.3rem; font-weight: 900; color: #ffffff;">🤖 ADRIEL-AI PRO CENTER</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
    <div class="hud-robot">
        <div style="color: #00ffcc; font-size: 20px; font-weight: 900; letter-spacing: 3px;">🌀 ENGINE HARDWARE ONLINE</div>
        <p style="color: #94a3b8; font-size: 14.5px; max-width: 680px; margin: 10px auto 0 auto; line-height:1.6;">
            A inteligência central está operando em velocidade máxima. Selecione qualquer um dos robôs de tráfego gringo na barra lateral esquerda para iniciar pesquisas reais.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="grid-metricas"><div class="card-metric"><div class="card-metric-title">Faturamento Geral</div><div class="card-metric-value">R$ 142.580</div></div><div class="card-metric"><div class="card-metric-title">Licenças Ativas</div><div class="card-metric-value">2.105</div></div><div class="card-metric"><div class="card-metric-title">Recorrência (MRR)</div><div class="card-metric-value">R$ 104.200</div></div><div class="card-metric"><div class="card-metric-title">Taxa de Churn</div><div class="card-metric-value">0.8%</div></div></div>', unsafe_allow_html=True)

# 👥 CENTRAL DE ASSINANTES (EXATO DO SEU PRINT)
elif st.session_state.modulo_ativo == "ASSINANTES":
    st.markdown('<h1 style="font-size: 2.2rem; font-weight: 900; color: #ffffff;">&nbsp;💳 Central de Assinantes</h1>', unsafe_allow_html=True)
    st.markdown('<div class="grid-metricas"><div class="card-metric"><div class="card-metric-title">Faturamento Geral</div><div class="card-metric-value">R$ 142.580</div></div><div class="card-metric"><div class="card-metric-title">Licenças Ativas</div><div class="card-metric-value">2.105</div></div><div class="card-metric"><div class="card-metric-title">Recorrência (MRR)</div><div class="card-metric-value">R$ 104.200</div></div><div class="card-metric"><div class="card-metric-title">Taxa de Churn</div><div class="card-metric-value">0.8%</div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<h2 style="font-size: 1.5rem; font-weight: 800; color: #ffffff; margin-bottom:15px;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h2>', unsafe_allow_html=True)
    col_p1, col_p2, col_p3 = st.columns(3)
    col_p1.markdown('<div class="card-plano"><div class="plano-title">Plano Mensal Start</div><div class="plano-price">R$ 47</div><div class="plano-desc">Acesso básico aos módulos iniciais para validação imediata do robô gringo.</div><br><a href="https://hostinger.com" target="_blank" class="btn-compra">= PAGAR COM CARTÃO / PIX</a></div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown('<div class="card-plano" style="border: 2px solid #00ffcc;"><div class="plano-title" style="color:#00ffcc;">Plano Mensal Pro</div><div class="plano-price" style="color:#00ffcc;">R$ 97</div><div class="plano-desc">Módulo RSA completo + Arquitetura avançada de funil com alta velocidade e escala.</div><br><a href="#" class="btn-compra">= PAGAR COM CARTÃO / PIX</a></div>', unsafe_allow_html=True)

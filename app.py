import streamlit as st
import pandas as pd
import requests
import json
import time
from datetime import datetime

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE DE ELITE 2026
st.set_page_config(page_title="Adriel-AI Pro - Control Center", page_icon="👑", layout="wide")

# CHAVE MESTRA DO ADMINISTRADOR
CHAVE_MESTRA = "ONYX_MASTER_2026"

# Inicialização de estados globais de navegação e segurança
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "DASHBOARD"
if "status_usuario" not in st.session_state:
    st.session_state.status_usuario = "ADMIN"  # Opções: ADMIN, ATIVO, BLOQUEADO
if "api_key_global" not in st.session_state:
    st.session_state.api_key_global = ""

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL LUXO SUPREMO (COPIA FIEL DO PRINT DE TELA)
# =============================================================================================================
st.markdown("""
<style>
/* Reset de fundo escuro profundo */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #0c111d !important; }

/* Ocultação total da barra nativa superior branca */
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
    transform: scale(1.01);
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; }

/* CARDS DE FATURAMENTO DA BARRA SUPERIOR */
.grid-metricas { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
.card-metric {
    background-color: #0d121f !important; border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important;
    padding: 20px !important; text-align: center !important; box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
}
.card-metric-title { font-size: 11px; font-weight: 800; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }
.card-metric-value { font-size: 28px; font-weight: 900; color: #ffffff; }

/* CARDS DE PREÇO DOS PLANOS */
.card-plano {
    background-color: #0d121f !important; border: 1px solid #1e293b !important; border-radius: 16px !important;
    padding: 30px !important; box-shadow: 0 12px 35px rgba(0,0,0,0.5) !important; min-height: 280px;
}
.plano-title { font-size: 11px; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
.plano-price { font-size: 36px; font-weight: 900; color: #ffffff; margin: 15px 0; }
.plano-desc { font-size: 13px; color: #cbd5e1; line-height: 1.5; margin-bottom: 25px; min-height: 50px; }

/* Botão de Compra e Ação Verde Água Neon */
.btn-compra {
    display: block; background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%);
    color: #030712 !important; text-decoration: none !important; text-align: center;
    font-weight: 900; font-size: 13px; padding: 14px; border-radius: 30px;
    text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
}
.stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
.top-badge-container { display: flex; gap: 15px; margin-bottom: 25px; }
.top-badge { background-color: #0f172a; border: 1px solid #1e293b; padding: 6px 16px; border-radius: 6px; font-size: 11px; font-family: monospace; font-weight: bold; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. CONSTRUÇÃO DO MENU LATERAL FLUIDO DE ELITE (EXATO DO PRINT)
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 5px;">⚙️ Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #64748b; font-weight: bold; margin-bottom: 20px;">MÓDULOS DE COMANDO</p>', unsafe_allow_html=True)
    
    if st.button("📊 DASHBOARD", use_container_width=True): st.session_state.modulo_ativo = "DASHBOARD"
    if st.button("🔥 1. RADAR ELITE", use_container_width=True): st.session_state.modulo_ativo = "RADAR"
    if st.button("🛰️ 2. AUDITOR IA", use_container_width=True): st.session_state.modulo_ativo = "AUDITOR"
    if st.button("✍️ 3. GERADOR RSA", use_container_width=True): st.session_state.modulo_ativo = "GERADOR"
    if st.button("🎯 4. CAÇADOR V10", use_container_width=True): st.session_state.modulo_ativo = "CACADOR"
    if st.button("📄 5. PRE-SELL", use_container_width=True): st.session_state.modulo_ativo = "PRESELL"
    st.write("---")
    if st.button("👥 ASSINANTES", use_container_width=True): st.session_state.modulo_ativo = "ASSINANTES"

# =============================================================================================================
# 4. GESTOR EXCLUSIVO DE ASSINATURA E TRAVA DE INADIMPLÊNCIA
# =============================================================================================================
if st.session_state.status_usuario == "BLOQUEADO" and st.session_state.modulo_ativo != "ASSINANTES":
    st.markdown("<div class='card-saas' style='text-align:center; padding:40px; margin-top:50px; border: 2px solid #ff0055;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#ff0055;'>🚨 ACESSO SUSPENSO: FATURAMENTO PENDENTE</h1>", unsafe_allow_html=True)
    st.write("Sua assinatura mensal recorrente expirou. Efetue a regularização do plano para liberar as chaves de API.")
    if st.button("💳 IR PARA CENTRAL DE ASSINANTES"):
        st.session_state.modulo_ativo = "ASSINANTES"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =============================================================================================================
# 5. EXECUÇÃO PARALELA DAS TELAS (NÚCLEO DO ECOSSISTEMA DO ROBÔ)
# =============================================================================================================

if st.session_state.status_usuario == "ADMIN" or st.session_state.api_key_global == CHAVE_MESTRA:
    st.markdown("<div style='background:rgba(255,255,255,0.02); border:2px dashed #cc66ff; border-radius:12px; padding:15px; margin-bottom:20px;'>", unsafe_allow_html=True)
    st.markdown("<h6 style='color:#cc66ff; margin:0;'>⚙️ INTERRUPTOR DE SEGURANÇA (MODO GESTOR MASTER)</h6>", unsafe_allow_html=True)
    c_adm1, c_adm2 = st.columns(2)
    if c_adm1.button("Simular Perfil: Cliente Ativo PRO"):
        st.session_state.status_usuario = "ATIVO"
        st.rerun()
    if c_adm2.button("Simular Perfil: Bloquear por Falta de Pagamento"):
        st.session_state.status_usuario = "BLOQUEADO"
        st.session_state.modulo_ativo = "ASSINANTES"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 📊 MONITOR 1: DASHBOARD / ASSINANTES (EXATO DO SEU PRINT)
if st.session_state.modulo_ativo in ["DASHBOARD", "ASSINANTES"]:
    col_tit, col_online = st.columns(2)
    with col_tit: st.markdown('<h1 style="font-size: 2.2rem; font-weight: 900; color: #ffffff;">💳 Central de Assinantes</h1>', unsafe_allow_html=True)
    with col_online: st.markdown('<p style="text-align: right; color: #00ffcc; font-size: 12px; font-weight: bold; margin-top: 15px;">● 2,387 OPERADORES CONECTADOS AGORA</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="top-badge-container"><div class="top-badge">🔹 CLICKBANK</div><div class="top-badge">🔹 BUYGOODS</div><div class="top-badge">🔹 DIGISTORE24</div><div class="top-badge">🔹 STRIPE DASH</div><div class="top-badge">🔹 HOSTINGER VPS</div></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="grid-metricas"><div class="card-metric"><div class="card-metric-title">Faturamento Geral</div><div class="card-metric-value">R$ 142.580</div></div><div class="card-metric"><div class="card-metric-title">Licenças Ativas</div><div class="card-metric-value">2.105</div></div><div class="card-metric"><div class="card-metric-title">Recorrência (MRR)</div><div class="card-metric-value">R$ 104.200</div></div><div class="card-metric"><div class="card-metric-title">Taxa de Churn</div><div class="card-metric-value">0.8%</div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<h2 style="font-size: 1.5rem; font-weight: 800; color: #ffffff;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h2>', unsafe_allow_html=True)
    
    col_p1, col_p2, col_p3 = st.columns(3)
    
    # 🟢 CORREÇÃO DA INDENTAÇÃO: Removidos os blocos 'with col' vazios e renderizados diretamente por markdowns injetados de forma plana e segura

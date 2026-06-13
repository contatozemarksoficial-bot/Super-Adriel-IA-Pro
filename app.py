import streamlit as st
import pandas as pd
import requests
import json
import time
from datetime import datetime

# 1. CONFIGURAÇÃO OFICIAL DE ALTO LUXO DE CINEMA
st.set_page_config(page_title="Adriel-AI Pro", page_icon="🤖", layout="wide")

CHAVE_MESTRA = "ONYX_MASTER_2026"

# Inicialização de estados de sessão de segurança e navegação
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "DASHBOARD"
if "status_usuario" not in st.session_state: st.session_state.status_usuario = "DESLOGADO"
if "api_key_global" not in st.session_state: st.session_state.api_key_global = ""

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL DESIGN DE SUCESSO (CÓPIA CIRÚRGICA DO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* Reset de fundo escuro profundo uniforme */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #0c111d !important; }

/* Oculta completamente os links e botões nativos do Streamlit na barra lateral */
[data-testid="stSidebarNav"], ul[data-testid="stSidebarNavItems"], .stSidebar button { display: none !important; height: 0px !important; }
[data-testid="stHeader"] { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2.5rem; padding-right: 2.5rem; }

/* 💎 MENU LATERAL PREMIUM EM HTML/CSS (IGUAL AO SEU PRINT) */
.sidebar-premium {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px 0;
}
.menu-item-luxo {
    display: block;
    background-color: #111827 !important;
    color: #ffffff !important;
    border: 1px solid #1f293b !important;
    border-radius: 8px !important;
    padding: 14px 20px !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    text-decoration: none !important;
    transition: all 0.2s ease-in-out !important;
    font-family: 'Segoe UI', sans-serif;
}
.menu-item-luxo:hover {
    border-color: #00ffcc !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    color: #00ffcc !important;
}
.menu-active {
    border-color: #00ffcc !important;
    background-color: #161f33 !important;
    color: #00ffcc !important;
}

/* CARDS DE FATURAMENTO PRETOS COM BORDA CIANO */
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
# 3. BARRA LATERAL FIXA DE COMANDO COM LINKS CUSTOMIZADOS EM HTML (RESOLVE O LAYOUT)
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 5px;">👑 Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #64748b; font-weight: bold; margin-bottom: 20px;">MÓDULOS DE COMANDO</p>', unsafe_allow_html=True)
    
    # Captura a mudança de página através de parâmetros na URL nativa (Query Params)
    query_params = st.query_params
    if "p" in query_params:
        st.session_state.modulo_ativo = query_params["p"]

    m = st.session_state.modulo_ativo

    # Renderiza o menu de botões escuros idêntico ao seu print usando HTML limpo
    st.markdown(f"""
    <div class="sidebar-premium">
        <a href="?p=DASHBOARD" target="_self" class="menu-item-luxo {'menu-active' if m=='DASHBOARD' else ''}">📊 Dashboard</a>
        <a href="?p=RADAR" target="_self" class="menu-item-luxo {'menu-active' if m=='RADAR' else ''}">🔥 1. Radar Elite</a>
        <a href="?p=AUDITOR" target="_self" class="menu-item-luxo {'menu-active' if m=='AUDITOR' else ''}">🛰️ 2. Auditor IA</a>
        <a href="?p=GERADOR" target="_self" class="menu-item-luxo {'menu-active' if m=='GERADOR' else ''}">✍️ 3. Gerador RSA</a>
        <a href="?p=CACADOR" target="_self" class="menu-item-luxo {'menu-active' if m=='CACADOR' else ''}">🎯 4. Caçador V10</a>
        <a href="?p=PRESELL" target="_self" class="menu-item-luxo {'menu-active' if m=='PRESELL' else ''}">📄 5. Pre-Sell</a>
        <hr style="border-color:#1f293b; margin: 10px 0;">
        <a href="?p=ASSINANTES" target="_self" class="menu-item-luxo {'menu-active' if m=='ASSINANTES' else ''}">👥 Assinantes</a>
        <a href="?p=LOGOUT" target="_self" class="menu-item-luxo" style="border-color:#ff0055 !important; color:#ff0055;">🚪 Desconectar</a>
    </div>
    """, unsafe_allow_html=True)

# Gerencia o botão de Desconectar
if st.session_state.modulo_ativo == "LOGOUT":
    st.session_state.status_usuario = "DESLOGADO"
    st.session_state.modulo_ativo = "DASHBOARD"
    st.query_params.clear()
    st.rerun()

# =============================================================================================================
# 4. TRAVA DE SEGURANÇA CONTRA INADIMPLÊNCIA MENSAL
# =============================================================================================================
if st.session_state.status_usuario == "BLOQUEADO" and st.session_state.modulo_ativo != "ASSINANTES":
    st.markdown("<div class='card-saas' style='text-align:center; padding:40px; margin-top:50px; border: 2px solid #ff0055;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#ff0055;'>🚨 ACESSO CONGELADO: MENSALIDADE EM ATRASO</h1>", unsafe_allow_html=True)
    st.write("A sua assinatura Pro expirou na integradora de pagamentos do cartão.")
    st.markdown("<a href='?p=ASSINANTES' target='_self' class='btn-compra' style='max-width:300px; margin: 20px auto;'>💳 ACESSAR PLANOS PARA REGULARIZAR</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =============================================================================================================
# 5. RENDERIZAÇÃO DAS TELAS INTEGRADAS (PAINEL DO DONO + DASHBOARD CORRIGIDO)
# =============================================================================================================

# 🔑 TELA DE LOGIN / CENTRAL DE ACESSO
if st.session_state.status_usuario == "DESLOGADO":
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='card-saas' style='margin-top:50px; border-color:#00ffcc;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#00ffcc;'>🔑 INTEL ENTRADA SAAS</h2>", unsafe_allow_html=True)
        st.write("Digite sua chave secreta de acesso mestre:")
        
        # Injeção temporária para o botão de login funcionar via formulário Streamlit nativo na tela de login
        chave_input = st.text_input("Chave de Licença ou Código Secreto:", type="password", value="")
        if st.button("🔓 VERIFICAR CREDENCIAIS NO SERVIDOR"):
            if chave_input.strip() == CHAVE_MESTRA:
                st.session_state.status_usuario = "ADMIN"
                st.session_state.modulo_ativo = "DASHBOARD"
                st.success("👑 Chave Mestra Válida! Modo Gestor Liberado.")
                time.sleep(0.5)
                st.rerun()
            else: st.error("❌ Token inválido ou assinatura pendente.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# 👑 PAINEL EXCLUSIVO DO DONO DO ROBÔ (Aparece no topo após logar)
if st.session_state.status_usuario == "ADMIN":
    st.markdown("<div style='background:rgba(255,255,255,0.02); border:2px dashed #cc66ff; border-radius:12px; padding:15px; margin-bottom:20px;'>", unsafe_allow_html=True)
    st.markdown("<h6 style='color:#cc66ff; margin:0;'>⚙️ INTERRUPTOR DA CHAVE MESTRA (SIMULADOR DE ACESSO)</h6>", unsafe_allow_html=True)
    

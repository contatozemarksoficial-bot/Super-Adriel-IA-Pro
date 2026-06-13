import streamlit as st
import pandas as pd
import requests
import json
import time

# 1. CONFIGURAÇÃO PREMIUM DESIGN DE CINEMA 2026
st.set_page_config(page_title="Adriel-AI Pro", page_icon="🤖", layout="wide")

CHAVE_MESTRA = "ONYX_MASTER_2026"

# Inicialização de estados de sessão blindados contra recarregamento
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "DASHBOARD"
if "status_usuario" not in st.session_state: st.session_state.status_usuario = "DESLOGADO"
if "api_key_global" not in st.session_state: st.session_state.api_key_global = ""

# =============================================================================================================
# 2. DESIGN CYBERPUNK LUXO SUPREMO INJETADO (CÓPIA REAL E FIEL DE PROJETO BLACK-LABEL)
# =============================================================================================================
st.markdown("""
<style>
/* Fundo preto espacial de cinema */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #030712 !important; 
    color: #f3f4f6 !important; 
}
[data-testid="stSidebar"] section { background-color: #090d16 !important; border-right: 1px solid #1e293b !important; }

/* Aniquilação de menus nativos e barras brancas redundantes do Streamlit */
[data-testid="stSidebarNav"], ul[data-testid="stSidebarNavItems"] { display: none !important; height: 0px !important; }
[data-testid="stHeader"] { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2.5rem; padding-right: 2.5rem; }

/* 🚨 ENGENHARIA DE BOTÕES DO MENU LATERAL (MOLDADOS COMO BLOCOS ESCUROS SAAS) */
.stButton > button {
    background-color: #0f172a !important; 
    color: #94a3b8 !important;
    border: 1px solid #1e293b !important; 
    border-radius: 8px !important;
    padding: 14px 20px !important; 
    width: 100% !important; 
    text-align: left !important;
    font-weight: 700 !important; 
    font-size: 13px !important; 
    text-transform: uppercase !important; 
    letter-spacing: 0.5px !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
/* Efeito de iluminação Neon ao passar o mouse */
.stButton > button:hover {
    border-color: #00ffcc !important;
    color: #00ffcc !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    transform: translateY(-1px);
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; }

/* 🧠 HUD CENTRAL DO ROBÔ INTELIGENTE (A CARA DO PROJETO) */
.hud-robot {
    background: radial-gradient(circle at 50% 50%, #0d1e3d 0%, #030712 100%) !important;
    border: 2px dashed #00ffcc !important; border-radius: 20px !important; padding: 30px !important; text-align: center !important;
    box-shadow: 0 0 35px rgba(0, 255, 204, 0.15) !important; margin-bottom: 25px !important;
}
.hud-robot-title { color: #00ffcc !important; font-size: 20px !important; font-weight: 900 !important; letter-spacing: 3px !important; text-transform: uppercase !important; margin-bottom: 5px !important; }

/* CARDS DE MONITORAMENTO DE CONSULTAS DA CONTA */
.grid-metricas { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
.card-metric {
    background-color: #0f172a !important; border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important;
    padding: 22px !important; text-align: center !important; box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
}
.card-metric-title { font-size: 11px; font-weight: 800; color: #64748b; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }
.card-metric-value { font-size: 28px; font-weight: 900; color: #ffffff; font-family: 'Segoe UI', sans-serif; }

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
    text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4); transition: 0.2s;
}
.btn-compra:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7); transform: translateY(-1px); }

.top-badge-container { display: flex; gap: 15px; margin-bottom: 25px; }
.top-badge { background-color: #0f172a; border: 1px solid #1e293b; padding: 6px 16px; border-radius: 6px; font-size: 11px; font-family: monospace; font-weight: bold; color: #38bdf8; }
.terminal-cyber { background-color: #02040a !important; border: 2px solid #1e293b !important; border-left: 4px solid #00ffcc !important; border-radius: 8px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; font-size: 13px !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. INTERFACE LATERAL: LINKS DE COMANDO SUPER LUXO ESTÁVEIS
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 3px;">👑 Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #475569; font-weight: bold; margin-bottom: 25px; letter-spacing:1px;">MÓDULOS DE COMANDO</p>', unsafe_allow_html=True)
    
    # Sistema de gatilhos em memória pura: Não usa URL, logo nunca desloga o administrador!
    if st.session_state.status_usuario in ["ATIVO", "ADMIN"]:
        if st.button("📊 DASHBOARD", key="menu_dash"): st.session_state.modulo_ativo = "DASHBOARD"
        if st.button("🔥 1. RADAR ELITE", key="menu_rad"): st.session_state.modulo_ativo = "RADAR"
        if st.button("🛰️ 2. AUDITOR IA", key="menu_aud"): st.session_state.modulo_ativo = "AUDITOR"
        if st.button("✍️ 3. GERADOR RSA", key="menu_gen"): st.session_state.modulo_ativo = "GERADOR"
        if st.button("🎯 4. CAÇADOR V10", key="menu_cac"): st.session_state.modulo_ativo = "CACADOR"
        if st.button("📄 5. PRE-SELL", key="menu_pre"): st.session_state.modulo_ativo = "PRESELL"
        st.write("---")
        if st.button("👥 ASSINANTES", key="menu_ass"): st.session_state.modulo_ativo = "ASSINANTES"
    else:
        if st.button("🔒 CENTRAL DE LOGIN", key="menu_lock_login"): st.session_state.modulo_ativo = "DASHBOARD"
        if st.button("💳 VER PLANOS SUPREMOS", key="menu_lock_plan"): st.session_state.modulo_ativo = "ASSINANTES"

    if st.session_state.status_usuario != "DESLOGADO":
        st.write("---")
        if st.button("🚪 DESCONECTAR SISTEMA", key="menu_logout"):
            st.session_state.status_usuario = "DESLOGADO"
            st.session_state.modulo_ativo = "DASHBOARD"
            st.rerun()

# =============================================================================================================
# 4. GESTOR DE TRAVA FINANCEIRA ATIVA
# =============================================================================================================
if st.session_state.status_usuario == "BLOQUEADO" and st.session_state.modulo_ativo != "ASSINANTES":
    st.markdown("<div class='card-saas' style='text-align:center; padding:40px; margin-top:50px; border: 2px solid #ff0055;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#ff0055;'>🚨 ACESSO SUSPENSO: FATURAMENTO EXPIRADO</h1>", unsafe_allow_html=True)
    st.write("A sua mensalidade recorrente falhou. Efetue a regularização para destravar as consultas e os robôs.")
    if st.button("💳 ENTRAR NA CENTRAL DE ASSINANTES"):
        st.session_state.modulo_ativo = "ASSINANTES"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =============================================================================================================
# 5. ENGENHARIA DE TELAS SUPREMA UNIFICADA
# =============================================================================================================

# 🔒 TELA DE ACESSO CRIPTOGRAFADA
if st.session_state.status_usuario == "DESLOGADO" and st.session_state.modulo_ativo == "DASHBOARD":
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        st.markdown("<div class='card-saas' style='margin-top:60px; border: 2px solid #00ffcc; box-shadow: 0 0 25px rgba(0,255,204,0.15);'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#00ffcc;'>🔑 SECURITY AUTH CONTROL</h2>", unsafe_allow_html=True)
        st.write("Insira sua chave de licença ativa ou use o código master:")
        
        chave_digitada = st.text_input("Chave Secreta Operacional:", type="password", value="")
        st.write("")
        
        if st.button("🔓 LIBERAR ACESSO AO CLUSTER NUVEM"):
            if chave_digitada.strip() == CHAVE_MESTRA:
                st.session_state.status_usuario = "ADMIN"
                st.session_state.modulo_ativo = "DASHBOARD"
                st.success("👑 Chave Mestra Ativada! Modo Gestor Liberado.")
                time.sleep(0.4)
                st.rerun()
            elif chave_digitada.strip() == "cliente":
                st.session_state.status_usuario = "ATIVO"

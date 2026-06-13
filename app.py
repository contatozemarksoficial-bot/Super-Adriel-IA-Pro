import streamlit as st
import pandas as pd
import requests
import json
import time

# 1. CONFIGURAÇÃO OFICIAL DE ALTO LUXO DE CINEMA
st.set_page_config(page_title="Adriel-AI Pro", page_icon="🤖", layout="wide")

# Inicialização de estados de sessão de segurança e navegação
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "DASHBOARD"
if "status_usuario" not in st.session_state: st.session_state.status_usuario = "DESLOGADO"
if "api_key_global" not in st.session_state: st.session_state.api_key_global = ""

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL DESIGN DE SUCESSO (CÓPIA CIRÚRGICA DO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* Fundo preto azulado profundo uniforme */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #0c111d !important; }

/* Oculta completamente os links nativos e feios do Streamlit */
[data-testid="stSidebarNav"], ul[data-testid="stSidebarNavItems"] { display: none !important; height: 0px !important; }
[data-testid="stHeader"] { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2.5rem; padding-right: 2.5rem; }

/* BOTÕES ESCUROS QUADRADOS DO MENU LATERAL (IDENTICOS AO SEU PRINT) */
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

/* CARDS DE FATURAMENTO PRETOS COM BORDA CIANO */
.grid-metricas { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
.card-metric {
    background-color: #0d121f !important; border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important;
    padding: 20px !important; text-align: center !important; box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
}
.card-metric-title { font-size: 11px; font-weight: 800; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }
.card-metric-value { font-size: 28px; font-weight: 900; color: #ffffff; }

/* CARDS DE PREÇO DOS PLANOS MENSAL R$ 47, R$ 97, R$ 197 */
.grid-planos { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-top: 15px; }
.card-plano {
    background-color: #0d121f !important; border: 1px solid #1e293b !important; border-radius: 16px !important;
    padding: 30px !important; box-shadow: 0 12px 35px rgba(0,0,0,0.5) !important;
}
.plano-title { font-size: 11px; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
.plano-price { font-size: 36px; font-weight: 900; color: #ffffff; margin: 15px 0; }
.plano-desc { font-size: 13px; color: #cbd5e1; line-height: 1.5; margin-bottom: 25px; min-height: 50px; }

.btn-compra {
    display: block; background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%);
    color: #030712 !important; text-decoration: none !important; text-align: center;
    font-weight: 900; font-size: 13px; padding: 14px; border-radius: 30px;
    text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
}
.stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
.top-badge-container { display: flex; gap: 15px; margin-bottom: 25px; }
.top-badge { background-color: #0f172a; border: 1px solid #1e293b; padding: 6px 16px; border-radius: 6px; font-size: 11px; font-family: monospace; font-weight: bold; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. BARRA LATERAL FIXA DE COMANDO (MENU PROFISSIONAL DO SEU ROBÔ)
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 5px;">👑 Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #64748b; font-weight: bold; margin-bottom: 20px;">MÓDULOS DE COMANDO</p>', unsafe_allow_html=True)
    
    # Renderização Condicional dos Botões do Menu Lateral
    if st.session_state.status_usuario in ["ATIVO", "ADMIN"]:
        if st.button("📊 DASHBOARD", use_container_width=True): st.session_state.modulo_ativo = "DASHBOARD"
        if st.button("🔥 1. RADAR ELITE", use_container_width=True): st.session_state.modulo_ativo = "RADAR"
        if st.button("🛰️ 2. AUDITOR IA", use_container_width=True): st.session_state.modulo_ativo = "AUDITOR"
        if st.button("✍️ 3. GERADOR RSA", use_container_width=True): st.session_state.modulo_ativo = "GERADOR"
        if st.button("🎯 4. CAÇADOR V10", use_container_width=True): st.session_state.modulo_ativo = "CACADOR"
        if st.button("📄 5. PRE-SELL", use_container_width=True): st.session_state.modulo_ativo = "PRESELL"
        st.write("---")
        if st.button("👥 ASSINANTES", use_container_width=True): st.session_state.modulo_ativo = "ASSINANTES"
    else:
        if st.button("🔒 CENTRAL DE LOGIN", use_container_width=True): st.session_state.modulo_ativo = "DASHBOARD"
        if st.button("💳 VER PLANOS DISPONÍVEIS", use_container_width=True): st.session_state.modulo_ativo = "ASSINANTES"

    if st.session_state.status_usuario != "DESLOGADO":
        st.write("---")
        if st.button("🚪 DESCONECTAR SISTEMA", use_container_width=True):
            st.session_state.status_usuario = "DESLOGADO"
            st.session_state.modulo_ativo = "DASHBOARD"
            st.rerun()

# =============================================================================================================
# 4. TRAVA DE SEGURANÇA CONTRA INADIMPLÊNCIA MENSAL
# =============================================================================================================
if st.session_state.status_usuario == "BLOQUEADO" and st.session_state.modulo_ativo != "ASSINANTES":
    st.markdown("<div class='card-saas' style='text-align:center; padding:40px; margin-top:50px; border: 2px solid #ff0055;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color:#ff0055;'>🚨 ACESSO CONGELADO: MENSALIDADE EM ATRASO</h1>", unsafe_allow_html=True)
    st.write("A sua assinatura Pro expirou na integradora de pagamentos do cartão.")
    if st.button("💳 ACESSAR PLANOS PARA REGULARIZAR"):
        st.session_state.modulo_ativo = "ASSINANTES"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =============================================================================================================
# 6. RENDERIZAÇÃO DAS TELAS E INTEGRAÇÃO DA CHAVE MESTRA
# =============================================================================================================

# 🔑 TELA DE LOGIN / CENTRAL DE ACESSO
if st.session_state.status_usuario == "DESLOGADO" and st.session_state.modulo_ativo == "DASHBOARD":
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div class='card-saas' style='margin-top:50px; border-color:#00ffcc;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#00ffcc;'>🔑 INTEL ENTRADA SAAS</h2>", unsafe_allow_html=True)
        st.write("Digite sua chave de licença ou utilize a Chave Mestra:")
        
        chave_input = st.text_input("Chave de Licença ou Código Secreto:", value="")
        st.write("")
        
        if st.button("🔓 VERIFICAR CREDENCIAIS NO SERVIDOR"):
            # CHAVE MESTRA QUE DESTRAVA TUDO E ATIVA O MENU DO DONO
            if chave_input.strip() == "ONYX_MASTER_2026":
                st.session_state.status_usuario = "ADMIN"
                st.session_state.modulo_ativo = "DASHBOARD"
                st.success("👑 Chave Mestra Válida! Modo Administrador Liberado.")
                time.sleep(0.5)
                st.rerun()
            elif chave_input.strip() == "cliente":
                st.session_state.status_usuario = "ATIVO"
                st.session_state.modulo_ativo = "DASHBOARD"
                st.rerun()
            elif chave_input.strip() == "bloqueado":
                st.session_state.status_usuario = "BLOQUEADO"
                st.session_state.modulo_ativo = "ASSINANTES"
                st.rerun()
            else:
                st.error("❌ Token inválido ou assinatura cancelada no gateway.")
        st.markdown("</div>", unsafe_allow_html=True)

# 👑 PAINEL EXCLUSIVO DO DONO DO ROBÔ (Para você simular e ver como fica a tela do cliente)
if st.session_state.status_usuario == "ADMIN":
    st.markdown("<div style='background:rgba(255,255,255,0.02); border:2px dashed #cc66ff; border-radius:12px; padding:15px; margin-bottom:20px;'>", unsafe_allow_html=True)
    st.markdown("<h6 style='color:#cc66ff; margin:0;'>⚙️ INTERRUPTOR DA CHAVE MESTRA CONTROLE DE CLIENTES</h6>", unsafe_allow_html=True)
    c_adm1, c_adm2 = st.columns(2)
    if c_adm1.button("🟢 Ver como Cliente Ativo Pro"):
        st.session_state.status_usuario = "ATIVO"
        st.rerun()

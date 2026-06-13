
import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE DE LUXO DE CINEMA
st.set_page_config(page_title="Adriel-AI Pro - Control Center", page_icon="👑", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL LUXO SUPREMO CYBER-GLOW (VISUAL PREMIUM PROFISSIONAL)
# =============================================================================================================
st.markdown("""
<style>
/* Reset de fundo preto azulado profundo */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #02040a !important; 
    color: #f1f5f9 !important; 
}
[data-testid="stSidebar"] section { background-color: #060b16 !important; }

/* Menu lateral iluminado e visível */
[data-testid="stSidebar"] *, [data-testid="stSidebarNav"] a, [data-testid="stSidebarNav"] span {
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    font-family: 'Segoe UI', sans-serif !important;
}

/* Ocultação cirúrgica da barra nativa superior */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }

/* Botões em Cápsula Arredondada Ciano Neon de Luxo */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #010409 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
    padding: 14px 28px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; 
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important; transition: all 0.3s ease !important;
}
.stButton > button:hover { box-shadow: 0 0 30px rgba(0, 255, 135, 0.8) !important; transform: scale(1.01) !important; }

/* Painel HUD Holográfico Holograma */
.hud-luxo {
    background: radial-gradient(circle at 50% 50%, #0c1a30 0%, #030712 100%) !important;
    border: 2px solid #00ffcc !important;
    border-radius: 20px !important;
    padding: 30px !important;
    text-align: center !important;
    box-shadow: 0 0 35px rgba(0, 255, 204, 0.2) !important;
    margin-bottom: 25px !important;
}

/* Cards de Preço e Módulos */
.card-saas {
    background: linear-gradient(145deg, #0b1329, #040814) !important;
    border: 1px solid #1e293b !important;
    border-radius: 16px !important;
    padding: 25px !important;
    margin-bottom: 20px !important;
    box-shadow: 0 12px 40px rgba(0,0,0,0.7) !important;
}
.card-destaque {
    border: 2px solid #00ffcc !important;
    box-shadow: 0 0 30px rgba(0, 255, 204, 0.25) !important;
}
.card-bloqueado {
    border: 2px solid #ff0055 !important;
    box-shadow: 0 0 30px rgba(255, 0, 85, 0.25) !important;
}
.neon-text { color: #00ffcc !important; font-weight: bold; }
.danger-text { color: #ff0055 !important; font-weight: bold; }
.price-tag { font-size: 34px; font-weight: 900; color: #ffffff; margin: 15px 0; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. MOTOR DE CONTROLE DE ACESSO E SESSÃO (MIND-BLOWING)
# =============================================================================================================
if "user_status" not in st.session_state:
    st.session_state.user_status = "DESLOGADO" # Opções: DESLOGADO, ATIVO, BLOQUEADO_INADIMPLENTE, ADMIN
if "painel_view" not in st.session_state:
    st.session_state.painel_view = "🏠 Início"

# CHAVE MESTRA SECRETA DO ADRIEL
CHAVE_MESTRA_ONYX = "ONYX_MASTER_2026"

# =============================================================================================================
# 4. BARRA LATERAL ULTRA-MÓDULO (MENU INTEGRADO)
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; text-align:center; margin-bottom:10px;">⚡ ADRIEL-AI PRO</h2>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:11px; color:#64748b;'>PLATAFORMA SAAS DE ARBITRAGEM</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Exibição de Status de Acordo com a Conta
    if st.session_state.user_status == "DESLOGADO":
        st.warning("🔒 Aguardando Autenticação...")
    elif st.session_state.user_status == "ATIVO":
        st.success("🟢 CONTA: ATIVA (PRO)")
    elif st.session_state.user_status == "BLOQUEADO_INADIMPLENTE":
        st.error("🔴 CONTA: SUSPENSA / INADIMPLENTE")
    elif st.session_state.user_status == "ADMIN":
        st.info("👑 MODO GESTOR: CHAVE MESTRA")
        
    st.write("---")
    
    # Links de Navegação do Painel
    if st.session_state.user_status in ["ATIVO", "ADMIN"]:
        if st.button("🏠 Dashboard Operacional"): st.session_state.painel_view = "🏠 Dashboard Operacional"
        if st.button("🤝 Menu de Afiliados"): st.session_state.painel_view = "🤝 Menu de Afiliados"
        if st.button("💳 Planos de Assinatura"): st.session_state.painel_view = "💳 Planos de Assinatura"
    elif st.session_state.user_status == "BLOQUEADO_INADIMPLENTE":
        if st.button("🚨 Tela de Bloqueio"): st.session_state.painel_view = "🚨 Tela de Bloqueio"
        if st.button("💳 Regularizar Mensalidade"): st.session_state.painel_view = "💳 Planos de Assinatura"
    else:
        if st.button("🏠 Central de Acesso"): st.session_state.painel_view = "🏠 Início"
        if st.button("💳 Conhecer Planos"): st.session_state.painel_view = "💳 Planos de Assinatura"
        
    if st.session_state.user_status != "DESLOGADO":
        st.write("---")
        if st.button("🚪 Encerrar Sessão"):
            st.session_state.user_status = "DESLOGADO"
            st.session_state.painel_view = "🏠 Início"
            st.rerun()

# =============================================================================================================
# 5. RENDERIZAÇÃO DE TELA DE ACORDO COM SELEÇÃO DO MENU
# =============================================================================================================

# 🔓 TELA DE INÍCIO / LOGIN
if st.session_state.painel_view == "🏠 Início" and st.session_state.user_status == "DESLOGADO":
    col1, col2, col3 = st.columns([1, 1.6, 1])
    with col2:
        st.markdown("<div class='card-saas' style='margin-top:40px; border-color:#00ffcc;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center; color:#00ffcc;'>🔑 SECURITY LOGIN INTERNACIONAL</h2>", unsafe_allow_html=True)
        st.write("Insira suas credenciais ou utilize sua chave secreta de administrador:")
        
        login_user = st.text_input("Usuário, E-mail ou Chave Mestra:", value="adriel")
        login_pass = st.text_input("Senha de Acesso (Deixe em branco se usar Chave Mestra):", type="password", value="1234")
        
        if st.button("🔓 AUTENTICAR VIA PROTOCOLO TLS"):
            # 👑 FILTRO 1: Verificação da Chave Mestra do Dono do Robô
            if login_user.strip() == CHAVE_MESTRA_ONYX:
                st.session_state.user_status = "ADMIN"
                st.session_state.painel_view = "🏠 Dashboard Operacional"
                st.success("👑 Chave Mestra detectada! Modo Administrador Ativado.")
                time.sleep(0.5)
                st.rerun()
            # 🟢 FILTRO 2: Simulação de Cliente Ativo Adimplente
            elif login_user.strip() == "adriel" and login_pass == "1234":
                st.session_state.user_status = "ATIVO"
                st.session_state.painel_view = "🏠 Dashboard Operacional"
                st.success("Acesso Pro Autorizado com Sucesso!")
                time.sleep(0.4)
                st.rerun()
            # 🔴 FILTRO 3: Simulação de Cliente Bloqueado (Não pagou a mensalidade)
            elif login_user.strip() == "inadimplente" and login_pass == "9999":
                st.session_state.user_status = "BLOQUEADO_INADIMPLENTE"
                st.session_state.painel_view = "🚨 Tela de Bloqueio"
                st.error("Aviso de Pendência Financeira Localizado.")
                time.sleep(0.4)
                st.rerun()
            else:
                st.error("❌ Acesso negado! Credenciais inválidas ou licença expirada.")
        st.markdown("</div>", unsafe_allow_html=True)

# 🔴 TELA DE BLOQUEIO POR FALTA DE PAGAMENTO (ASSINATURA EXPIRADA)
elif st.session_state.painel_view == "🚨 Tela de Bloqueio" or st.session_state.user_status == "BLOQUEADO_INADIMPLENTE":
    if st.session_state.user_status == "BLOQUEADO_INADIMPLENTE":
        st.markdown("<div class='hud-luxo' style='border-color:#ff0055; box-shadow: 0 0 35px rgba(255,0,85,0.25);'>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:#ff0055; font-size:3rem;'>🚨 SISTEMA BLOQUEADO POR INADIPLÊNCIA</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Aviso de Renovação Recorrente Pendente</h3>", unsafe_allow_html=True)
        st.write("Detectamos que a sua assinatura mensal do **Adriel-AI Pro** venceu e o pagamento automático falhou na integradora do cartão.")
        st.write("Para evitar o cancelamento definitivo do seu banco de dados e a perda dos seus tokens de Proxy Serper, efetue a regularização abaixo.")
        st.markdown("<p class='danger-text'>Dias de atraso: 4 dias | Módulos paralisados: Minerador, Auditor e Fabricante HTML</p>", unsafe_allow_html=True)
        
        if st.button("💳 REGULARIZAR ASSINATURA AGORA (REATIVAR ROBÔ)"):
            st.session_state.painel_view = "💳 Planos de Assinatura"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# 🏠 DASHBOARD PRINCIPAL DA ÁREA DE MEMBROS (CLIENTE REAL ATIVO)

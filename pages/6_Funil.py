import streamlit as st
import time

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA PRIVADA)
st.set_page_config(page_title="Acesso Restrito - Adriel AI", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (LOGIN DE LUXO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"] { background-color: #02040a !important; }

/* 🤖 ROBÔ GUARDIÃO (NEON VERDE) */
.robot-guard {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00ff87);
    animation: pulse-glow 2s infinite alternate;
}
@keyframes pulse-glow {
    from { opacity: 0.7; transform: scale(1); }
    to { opacity: 1; transform: scale(1.05); }
}

/* 💎 CHASSI DE LOGIN PARTICULAR */
.chassi-login {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 0 40px rgba(0, 255, 135, 0.15);
    max-width: 500px;
    margin: 0 auto;
    text-align: center;
}

/* ⚡ INPUTS DE ELITE */
div[data-baseweb="input"] { 
    background-color: #060913 !important; 
    border: 1.5px solid #00ff87 !important; 
    border-radius: 50px !important; /* Arredondado de luxo */
    padding: 5px 15px !important;
}
input { background-color: #060913 !important; color: #ffffff !important; }

/* BOTÃO DE ACESSO */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.4) !important;
    letter-spacing: 2px;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE DE LOGIN
st.markdown('<div class="robot-guard">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; letter-spacing:3px;">CONEXÃO PARTICULAR</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#576574; margin-top:-15px;">Autenticação síncrona Adriel-AI Elite v7</p>', unsafe_allow_html=True)

# Centralização do Chassi
col_center = st.columns([1, 2, 1])[1]

with col_center:
    st.markdown('<div class="chassi-login">', unsafe_allow_html=True)
    
    # Campos de Credenciais
    email = st.text_input("E-mail de Operador:", placeholder="seu@email.com")
    senha = st.text_input("Senha Criptografada:", type="password", placeholder="••••••••")
    
    st.write("")
    
    # Botão de Login
    if st.button("🔓 ACESSAR TERMINAL"):
        if email == "admin" and senha == "admin": # Defina aqui seu login real
            with st.spinner("Validando criptografia..."):
                time.sleep(1.5)
                st.success("✅ ACESSO LIBERADO!")
                time.sleep(1)
                st.session_state['login_concluido'] = True
                st.rerun()
        elif email == "" or senha == "":
            st.warning("⚠️ Insira suas credenciais.")
        else:
            st.error("❌ Credenciais Inválidas. Acesso Negado.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 4. RODAPÉ
st.write("")
st.markdown('<p style="text-align:center; color:#1e293b; font-size:11px;">🔒 Protocolo de segurança ativa. IP rastreado para fins de auditoria.</p>', unsafe_allow_html=True)

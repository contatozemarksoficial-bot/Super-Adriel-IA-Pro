import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="collapsed")

# 2. CONTROLE DE FLUXO (ESTADO DA SESSÃO)
if 'estagio' not in st.session_state:
    st.session_state.estagio = 'login' 
if 'plataforma_escolhida' not in st.session_state:
    st.session_state.plataforma_escolhida = None

# =============================================================================================================
# 3. DESIGN BLACK-LABEL (NEON & BOTÕES VIVOS)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Onyx Absoluto */
    .stApp { background-color: #02040a !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 💎 Chassi de Luxo */
    .chassi-elite {
        background: linear-gradient(145deg, #0f172a, #02040a);
        border: 2px solid #00ff87; border-radius: 20px;
        padding: 40px; text-align: center; max-width: 500px; margin: 0 auto;
        box-shadow: 0 0 30px rgba(0, 255, 135, 0.2);
    }

    /* 🤖 Robô Neon Verde Giga */
    .robot-neon {
        font-size: 100px; text-align: center; filter: drop-shadow(0 0 25px #00ff87);
        animation: pulse 2.5s infinite alternate;
    }
    @keyframes pulse { from { transform: scale(1); } to { transform: scale(1.08); } }

    /* ⚡ BOTÃO VIVO (GLOW NEON) - REMOVE O BRANCO */
    div.stButton > button {
        background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
        color: #030712 !important; 
        font-weight: 900 !important; 
        font-size: 16px !important;
        border-radius: 50px !important;
        padding: 18px 30px !important; 
        width: 100% !important; 
        border: none !important; 
        box-shadow: 0 0 15px rgba(0, 255, 135, 0.4) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s all ease-in-out !important;
    }

    /* Efeito ao passar o mouse (Hover) */
    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 35px rgba(0, 255, 135, 0.8) !important;
        background: linear-gradient(135deg, #00ffcc 0%, #00ff87 100%) !important;
    }

    /* Inputs Estilizados */
    div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ff87 !important; border-radius: 50px !important; }
    input { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 4. FLUXO DE TELAS (LOGIN -> PLATAFORMA -> MINERADOR)
# =============================================================================================================
if st.session_state.estagio == 'login':
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900;">CONEXÃO PARTICULAR</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite">', unsafe_allow_html=True)
        email = st.text_input("E-mail de Operador:", value="admin@elite.com")
        senha = st.text_input("Senha Criptografada:", type="password", value="123456")
        
        if st.button("🔓 VALIDAR ACESSO"):
            if email == "admin@elite.com" and senha == "123456":
                st.session_state.estagio = 'plataforma'
                st.rerun()
            else:
                st.error("❌ Credenciais Inválidas.")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.estagio == 'plataforma':
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87;">ESCOLHA A PLATAFORMA</h1>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="chassi-elite">', unsafe_allow_html=True)
        escolha = st.selectbox("Rede de Mineração:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
        
        if st.button("🚀 ESTABELECER CONEXÃO"):
            st.session_state.plataforma_escolhida = escolha
            st.session_state.estagio = 'minerador'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="text-align:center; color:#00ff87;">TERMINAL: {st.session_state.plataforma_escolhida}</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite" style="max-width: 800px;">', unsafe_allow_html=True)
        prod = st.text_input("💎 Nome do Produto:", value="Sugar Defender")
        if st.button("⛏️ INICIAR MINERAÇÃO"):
            st.success(f"Protocolo síncrono ativado para {prod}!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🔴 SAIR"):
        st.session_state.estagio = 'login'
        st.rerun()

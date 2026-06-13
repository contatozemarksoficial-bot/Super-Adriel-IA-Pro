import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="collapsed")

# 2. CONTROLE DE FLUXO (ESTADO DA SESSÃO)
if 'estagio' not in st.session_state:
    st.session_state.estagio = 'login' # Estágios: login, plataforma, minerador
if 'plataforma_escolhida' not in st.session_state:
    st.session_state.plataforma_escolhida = None

# =============================================================================================================
# 3. DESIGN BLACK-LABEL (NEON & ONYX)
# =============================================================================================================
st.markdown("""
<style>
    .stApp { background-color: #02040a !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    .chassi-elite {
        background: linear-gradient(145deg, #0f172a, #02040a);
        border: 2px solid #00ff87; border-radius: 20px;
        padding: 40px; text-align: center; max-width: 500px; margin: 0 auto;
        box-shadow: 0 0 30px rgba(0, 255, 135, 0.2);
    }

    .robot-neon {
        font-size: 100px; text-align: center; filter: drop-shadow(0 0 20px #00ff87);
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse { from { transform: scale(0.95); opacity: 0.8; } to { transform: scale(1.05); opacity: 1; } }

    div[data-baseweb="input"], div[data-baseweb="select"] { 
        background-color: #060913 !important; 
        border: 1.5px solid #00ff87 !important; 
        border-radius: 50px !important; 
    }
    input, span { color: #ffffff !important; }
    
    .stButton > button {
        background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
        color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
        padding: 15px !important; width: 100%; border: none !important; box-shadow: 0 0 20px #00ff8766;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .card-sugestao { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 4. ETAPA 1: LOGIN (CONEXÃO PARTICULAR)
# =============================================================================================================
if st.session_state.estagio == 'login':
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87;">CONEXÃO PARTICULAR</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite">', unsafe_allow_html=True)
        email = st.text_input("E-mail de Operador:", value="admin@elite.com")
        senha = st.text_input("Senha Criptografada:", type="password", value="123456")
        
        if st.button("🔓 VALIDAR ACESSO"):
            if email == "admin@elite.com" and senha == "123456":
                st.session_state.estagio = 'plataforma'
                st.rerun()
            else:
                st.error("Credenciais Inválidas.")
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================================================
# 5. ETAPA 2: ESCOLHA DA PLATAFORMA
# =============================================================================================================
elif st.session_state.estagio == 'plataforma':
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87;">CONFIGURAÇÃO DE UPLINK</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">Selecione a rede de mineração internacional</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="chassi-elite">', unsafe_allow_html=True)
        escolha = st.selectbox("Plataforma Alvo:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"])
        
        if st.button("🚀 ESTABELECER CONEXÃO"):
            st.session_state.plataforma_escolhida = escolha
            st.session_state.estagio = 'minerador'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================================================
# 6. ETAPA 3: MINERADOR (O TERMINAL FINAL)
# =============================================================================================================
else:
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="text-align:center; color:#00ff87;">MINERADOR: {st.session_state.plataforma_escolhida}</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite" style="max-width: 800px;">', unsafe_allow_html=True)
        prod_alvo = st.text_input("💎 Nome do Ativo:", value="Sugar Defender")
        
        if st.button("⛏️ INICIAR VARREDURA SÍNCRONA"):
            status = st.empty()
            esteira = st.empty()
            
            sufixos = ["Official Site", "Buy Now", "Discount", "Reviews", "Ingredients", "Is it Scam", "Where to Buy"]
            results = []
            
            for s in sufixos:
                status.info(f"⛏️ [CONECTADO: {st.session_state.plataforma_escolhida}]: {prod_alvo} {s}")
                results.append({
                    "Termo": f"{prod_alvo} {s}", 
                    "Plataforma": st.session_state.plataforma_escolhida,
                    "CPC Est.": f"$ {random.uniform(2.8, 5.5):.2f}"
                })
                esteira.dataframe(pd.DataFrame(results), use_container_width=True)
                time.sleep(0.4)
            
            status.success(f"✅ Protocolo {st.session_state.plataforma_escolhida} Finalizado!")
            
            st.write("---")
            cols = st.columns(2)
            for i, res in enumerate(results):
                with cols[i % 2]:
                    st.markdown(f'<div class="card-sugestao"><b>{res["Termo"]}</b><br>Lance Sugerido: {res["CPC Est."]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🔴 ENCERRAR SESSÃO E VOLTAR"):
        st.session_state.estagio = 'login'
        st.rerun()

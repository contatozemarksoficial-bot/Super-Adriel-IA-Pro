import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# 2. CONTROLE DE SESSÃO (Login + Pesquisa)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'executando' not in st.session_state:
    st.session_state.executando = False
if 'resultados' not in st.session_state:
    st.session_state.resultados = []

# =============================================================================================================
# 3. DESIGN BLACK-LABEL (CORES ORIGINAIS CIANO #00f2ff)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ÔNIX */
html, body, .stApp, [data-testid="stHeader"], [data-testid="stSidebar"] {
    background-color: #02040a !important; color: #00f2ff !important;
}

/* 👤 SIDEBAR BLINDADA */
section[data-testid="stSidebar"] { border-right: 1px solid #00f2ff !important; background-color: #02040a !important; }
section[data-testid="stSidebar"] * { color: #00f2ff !important; font-weight: 800; }

/* 🚨 INPUTS SEM BRANCO */
div[data-baseweb="input"] { background-color: #0d1117 !important; border: 1px solid #00f2ff !important; border-radius: 8px; }
input { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }

/* 📋 BLOCOS DE RESULTADO */
.box-elite {
    background-color: #0d1117; border: 1.5px solid #00f2ff; border-radius: 12px;
    padding: 15px 25px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;
}

/* ⚡ BOTÕES ORIGINAIS */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important; width: 100%;
}
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 4. TELA DE LOGIN (PAINEL DE ASSINANTE)
# =============================================================================================================
if not st.session_state.autenticado:
    st.markdown("<h1 style='text-align:center;'>🔐 CONEXÃO PARTICULAR</h1>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div style='max-width:400px; margin:0 auto;'>", unsafe_allow_html=True)
        email = st.text_input("E-mail do Assinante:")
        senha = st.text_input("Senha de Acesso:", type="password")
        if st.button("🔓 ENTRAR NO SISTEMA"):
            # DEFINA SEU LOGIN AQUI
            if email == "admin@elite.com" and senha == "123456":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("❌ Acesso Negado.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =============================================================================================================
# 5. ÁREA LOGADA (MINERADOR ELITE)
# =============================================================================================================

# Menu Lateral (Só aparece logado)
with st.sidebar:
    st.markdown("### 🛰️ MENU ELITE")
    st.write("app | Radar | Gerador | Funil")
    st.markdown("<p style='background:#0d1117; border:1px solid #00f2ff; padding:5px; border-radius:5px; text-align:center;'>MINERADOR ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    if st.button("🛑 ENCERRAR SESSÃO"):
        st.session_state.autenticado = False
        st.session_state.executando = False
        st.rerun()

st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Interface de Comando
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", value="adriel_pro")
prod_alvo = st.text_input("💎 PRODUTO ALVO:", value="Sugar Defender")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 INICIAR PESQUISA"):
        st.session_state.executando = True
with c2:
    if st.button("🛑 PARAR PESQUISA"):
        st.session_state.executando = False

# Containers de Exibição
status_info = st.empty()
area_elite = st.container()
area_outros = st.container()

# 6. MOTOR DE PESQUISA (Obedecendo o Login)
sufixos_elite = ["official", "buy now", "discount", "order", "coupon", "price"]
sufixos_outros = ["reviews", "ingredients", "is it safe", "scam", "side effects", "results"]

if st.session_state.executando:
    while st.session_state.executando:
        cat = random.choice(["elite", "outros"])
        suf = random.choice(sufixos_elite if cat == "elite" else sufixos_outros)
        termo = f"{prod_alvo} {suf}".upper()
        cpc = random.uniform(2.80, 8.50)
        
        # Salva resultado
        st.session_state.resultados.insert(0, {"termo": termo, "cpc": f"$ {cpc:.2f}", "cat": cat})
        status_info.markdown(f"<p style='text-align:center;'>⛏️ ANALISANDO: {termo}</p>", unsafe_allow_html=True)
        
        # Mostra resultados
        with area_elite:
            st.markdown("### 💎 PALAVRAS DE ELITE (FUNDO DE FUNIL)")
            for r in [x for x in st.session_state.resultados if x['cat'] == "elite"][:8]:
                st.markdown(f'<div class="box-elite"><b>🔍 {r["termo"]}</b><b>{r["cpc"]}</b></div>', unsafe_allow_html=True)
        
        with area_outros:
            st.markdown("### 📊 RESTANTE DA MINERAÇÃO")
            for r in [x for x in st.session_state.resultados if x['cat'] == "outros"][:4]:
                st.markdown(f'<div class="box-elite" style="opacity:0.6;"><span>{r["termo"]}</span><span>{r["cpc"]}</span></div>', unsafe_allow_html=True)
        
        time.sleep(1)
        st.rerun()

# Se não estiver executando mas houver resultados, mostra eles estáticos
elif len(st.session_state.resultados) > 0:
    st.info("Sessão Ativa - Pesquisa em Pausa")

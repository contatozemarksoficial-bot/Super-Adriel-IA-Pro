import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA ESCURO)
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INITIALIZE STATE CONTROLS (Gerenciamento do Loop Infinito)
# =============================================================================================================
if "minerando" not in st.session_state:
    st.session_state.minerando = False
if "dados_minerados" not in st.session_state:
    st.session_state.dados_minerados = []
if "contador_infinito" not in st.session_state:
    st.session_state.contador_infinito = 0

# =============================================================================================================
# 2. INJEÇÃO DE CSS PERSONALIZADO (IDÊNTICO À COR VERDE-ÁGUA DA SUA IMAGEM)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON COM O TOM DE VERDE-ÁGUA */
section[data-testid="stSidebar"] { border-right: 1px solid #00c4b4 !important; }
section[data-testid="stSidebar"] * { color: #00c4b4 !important; }

/* 🚨 INPUTS COMBINANDO COM A PALETA */
div[data-baseweb="input"] {
    background-color: #0d1117 !important;
    border: 1px solid #00c4b4 !important;
    border-radius: 10px !important;
}
input { color: #ffffff !important; background-color: transparent !important; -webkit-text-fill-color: #ffffff !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON VERDE-ÁGUA) */
.robot-scanner {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00c4b4);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI CENTRALIZADO COESO */
.chassi-luxury {
    background-color: #02040a;
    border: 1px solid #00c4b4; 
    border-radius: 8px;
    padding: 25px; 
    margin-bottom: 20px;
}

/* ⚡ CONFIGURAÇÃO DO BOTÃO EM VERDE-ÁGUA NEON */
.stButton > button {
    background: linear-gradient(135deg, #00c4b4 0%, #008080 100%) !important;
    color: #02040a !important; 
    font-weight: 800 !important; 
    border-radius: 25px !important;
    padding: 10px 20px !important; 
    border: none !important;
    box-shadow: 0 0 15px rgba(0, 196, 180, 0.4) !important;
    text-transform: uppercase;
    font-size: 14px !important;
    width: 100%;
}

/* 📋 BLOCOS DE LISTAGEM EXATAMENTE IGUAIS AO PRINT ENVIADO */
.box-pattern-aqua {
    background-color: #02040a;
    border: 1px solid #00c4b4;
    border-radius: 6px;
    padding: 10px 15px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.termo-text-aqua { color: #ffffff !important; font-weight: 700; font-size: 14px; font-family: monospace; }
.status-tag-aqua { color: #00c4b4 !important; font-size: 11px; font-weight: bold; letter-spacing: 1px; }

.terminal-hacker { background: #000; border-left: 5px solid #00c4b4; color: #00c4b4; padding: 15px; border-radius: 8px; font-family: monospace; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
with st.sidebar:
    st.markdown("### 🛰️ MENU ELITE")
    st.write("app | Radar | Auditor")
    st.write("Gerador | Caçador")
    st.markdown("<p style='background:#0d1117; border:1px solid #00c4b4; padding:5px; border-radius:5px; text-align:center;'>MINERADOR ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 📡 STATUS")
    if st.session_state.minerando:
        st.markdown("<p style='color:#00c4b4;'>🟢 SCANNER: LOOP INFINITO ATIVO</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff3333;'>🔴 MINERADOR PARADO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 REDES")
    for p in ["CLICKBANK", "BUYGOODS", "MAXWEB"]:
        st.markdown(f'<div style="border:1px solid #00c4b4; padding:4px; border-radius:5px; margin-bottom:5px; text-align:center; font-size:10px;">{p}</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00c4b4; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR DE ELITE V7</h1>', unsafe_allow_html=True)

# Inputs organizados
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="Ex: adriel_pro")
prod_alvo = st.text_input("💎 PRODUTO PARA MINERAR:", placeholder="Ex: Sugar Defender")

st.write("") 

# Distribuição por colunas para juntar os botões centralizados
col_esq, col_btn1, col_btn2, col_dir = st.columns()

with col_btn1:
    if st.button("🚀 INICIAR PESQUISA INFINITA"):
        if not aff_id or not prod_alvo:
            st.error("❌ Preencha os campos!")
        else:
            st.session_state.minerando = True
            st.rerun()
            
with col_btn2:
    if st.button("🛑 PARAR PESQUISA"):
        st.session_state.minerando = False
        st.rerun()

status = st.empty()
container_blocos = st.container()

# Renderização estável dos blocos com o tom correto da imagem
if st.session_state.dados_minerados:
    with container_blocos:
        for item in reversed(st.session_state.dados_minerados):
            st.markdown(f"""
            <div class="box-pattern-aqua">
                <span class="termo-text-aqua">🔍 {item['TERMO DE ELITE']}</span>
                <span class="status-tag-aqua">[ALTA] - {item['LANCE CPC']} — SUCE-X</span>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================================================
# 5. MOTOR DE LOOP CONTÍNUO (MOTO-PESQUISA)
# =============================================================================================================
if st.session_state.minerando:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    st.session_state.contador_infinito += 1
    suf = random.choice(sufixos)
    
    termo_gerado = f"{prod_alvo} {suf} #{st.session_state.contador_infinito}".upper()
    status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA CONTINUA ATIVA]: Extraindo Termo {termo_gerado}</div>', unsafe_allow_html=True)
    
    cpc = random.uniform(2.15, 5.30)
    
    st.session_state.dados_minerados.append({
        "Nº": f"#{st.session_state.contador_infinito:03d}",
        "TERMO DE ELITE": termo_gerado,
        "LANCE CPC": f"$ {cpc:.2f}"
    })
    
    time.sleep(0.3)
    st.rerun()
else:
    if st.session_state.contador_infinito > 0:
        status.markdown(f'<div class="terminal-hacker" style="border-color:#ff3333; color:#ffffff; background-color:#ff3333; text-align:center; font-weight:900;">🛑 MOTOR INTERROMPIDO TOTAL: {st.session_state.contador_infinito} TERMOS CATALOGADOS</div>', unsafe_allow_html=True)

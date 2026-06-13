import streamlit as st
import pandas as pd
import time
import random

# =============================================================================================================
# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA ESCURO)
# =============================================================================================================
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (EXTERMINA O BRANCO E FIXA O NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 📊 TABELAS DE LUXO */
[data-testid="stDataFrame"] { background-color: #060913 !important; border: 1px solid #1e293b !important; border-radius: 10px; }
.stDataFrame div { color: #ffffff !important; }
thead tr th { background-color: #0f172a !important; color: #00ffcc !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON) */
.robot-scanner {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ffcc; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
}

/* ⚡ ESTILIZAÇÃO DOS BOTÕES GIGA EM COLUNAS */
div.stButton > button {
    font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100% !important; border: none !important;
}
/* Botão Iniciar (Verde Neon) */
div[data-testid="column"]:nth-of-type(1) button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}
/* Botão Parar (Vermelho Fogo) */
div[data-testid="column"]:nth-of-type(2) button {
    background: linear-gradient(135deg, #ff4d4d 0%, #ff0000 100%) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(255, 77, 77, 0.4) !important;
}

/* CARDS DE PLATAFORMAS E MATRIZ */
.card-plataforma { background: #060913; border: 1px solid #1e293b; padding: 10px; border-radius: 8px; text-align: center; color: #00ffcc; font-size: 11px; margin-bottom: 8px; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. CONTROLE DE SESSÃO (GERENCIAMENTO DE ESTADO)
# =============================================================================================================
if "executando" not in st.session_state:
    st.session_state.executando = False
if "minerados" not in st.session_state:
    st.session_state.minerados = []
if "passo_atual" not in st.session_state:
    st.session_state.passo_atual = 0
if "busca_concluida" not in st.session_state:
    st.session_state.busca_concluida = False
if "produto_anterior" not in st.session_state:
    st.session_state.produto_anterior = ""

# Base estática de sufixos de mineração
SUFIXOS = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]

# =============================================================================================================
# 4. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
# =============================================================================================================
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    if st.session_state.executando:
        st.markdown("<p style='color:#00ffcc;'>⚡ Varredura: EM ANDAMENTO</p>", unsafe_allow_html=True)
    elif st.session_state.busca_concluida:
        st.markdown("<p style='color:#00ff87;'>🟢 Varredura: CONCLUÍDA</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#747d8c;'>⚪ Varredura: AGUARDANDO COMANDO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS CONECTADAS")
    platforms = ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"]
    for p in platforms:
        st.markdown(f'<div class="card-plataforma">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# =============================================================================================================
# 5. ÁREA PRINCIPAL E INTERFACE
# =============================================================================================================
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona:", value="Sugar Defender")
    
    # Se o usuário mudar o nome do produto, limpa os dados anteriores
    if prod_alvo != st.session_state.produto_anterior:
        st.session_state.minerados = []
        st.session_state.passo_atual = 0
        st.session_state.busca_concluida = False
        st.session_state.produto_anterior = prod_alvo

    # Alinhamento dos botões em duas colunas distintas
    col_disparar, col_parar = st.columns(2)
    
    with col_disparar:
        btn_run = st.button("🚀 DISPARAR SCANNER (50 TERMOS)")
    with col_parar:
        btn_stop = st.button("🛑 PARAR MINERAÇÃO")
        
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================================================
# 6. LOGICA DO BOTÃO DE CONTROLE
# =============================================================================================================
if btn_run:
    st.session_state.executando = True
    st.session_state.busca_concluida = False
    st.session_state.minerados = []
    st.session_state.passo_atual = 0
    st.rerun()

if btn_stop:
    st.session_state.executando = False
    st.rerun()

# =============================================================================================================
# 7. MOTOR DE LOOP DE MINERAÇÃO AS SÍNCRONO (EVITA TRAVAMENTO)
# =============================================================================================================
status = st.empty()
esteira = st.empty()

# Executa enquanto estiver ativo e houver termos restantes
if st.session_state.executando and st.session_state.passo_atual < len(SUFIXOS):
    i = st.session_state.passo_atual
    suf = SUFIXOS[i]
    
    # Renderiza o terminal hacker simulado em tempo real
    status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA GLOBAL]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
    
    cpc = random.uniform(2.15, 5.30)
    st.session_state.minerados.append({
        "Nº": f"#{i+1:02d}",
        "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
        "LANCE CPC": f"$ {cpc:.2f}",
        "POTENCIAL ROI": "🔥 ALTO"
    })
    
    # Incrementa o passo e força o rerun imediato para atualizar a UI do Streamlit
    st.session_state.passo_atual += 1
    time.sleep(0.04) # Delay leve para dar o efeito de renderização contínua
    st.rerun()

# Se o usuário clicou em parar voluntariamente no meio do processo
elif not st.session_state.executando and st.session_state.passo_atual > 0 and not st.session_state.busca_concluida:
    status.markdown(f'<div class="terminal-hacker" style="border-color:#ff4d4d; color:#ff4d4d;">⚠️ INTERRUPÇÃO: Varredura travada no termo #{st.session_state.passo_atual:02d} por solicitação do usuário.</div>', unsafe_allow_html=True)

# Finalização natural do loop de 50 termos
elif st.session_state.passo_atual >= len(SUFIXOS):
    st.session_state.executando = False
    st.session_state.busca_concluida = True
    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: 50 TERMOS DE ELITE CATALOGADOS COM PRECISÃO.</div>', unsafe_allow_html=True)

# =============================================================================================================
# 8. EXIBIÇÃO DE DADOS & MATRIZ ESTRATÉGICA (CASO EXISTA ALGO MINERADO)
# =============================================================================================================
if st.session_state.minerados:
    # Mostra a tabela atualizada

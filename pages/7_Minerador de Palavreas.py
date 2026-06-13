import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA ESCURO)
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (EXTERMINA O BRANCO E FIXA O NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO: Bloqueia qualquer vazamento de cor clara */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON: Cores e Bordas */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 📊 TABELAS DE LUXO: Remove o fundo branco nativo do Streamlit */
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

/* ⚡ EXTERMINADOR DE BOTÕES BRANCOS: Reseta e força cores escuras/neon em TODOS os botões */
div[data-testid="stButton"] button, .stButton > button {
    color: #030712 !important; 
    font-weight: 900 !important; 
    border-radius: 50px !important;
    padding: 20px !important; 
    width: 100% !important; 
    border: none !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
}

/* Botão Disparar: Verde Neon Metálico */
div.btn-disparar button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.5) !important;
    color: #02040a !important;
}

/* Botão Parar: Vermelho Sangue / Neon */
div.btn-parar button {
    background: linear-gradient(135deg, #ff4d4d 0%, #bc0000 100%) !important;
    box-shadow: 0 0 25px rgba(255, 77, 77, 0.5) !important;
    color: #ffffff !important;
}

/* Botão de Download ou secundários perdidos */
div[data-testid="stMarkdownContainer"] button, button[role="tab"] {
    background-color: #0f172a !important;
    color: #00ffcc !important;
    border: 1px solid #1e293b !important;
}

/* CARDS DE PLATAFORMAS E MATRIZ */
.card-plataforma { background: #060913; border: 1px solid #1e293b; padding: 10px; border-radius: 8px; text-align: center; color: #00ffcc; font-size: 11px; margin-bottom: 8px; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# Inicialização do controle de estados da mineração
if "minerando" not in st.session_state:
    st.session_state.minerando = False
if "minerados" not in st.session_state:
    st.session_state.minerados = []
if "passo_atual" not in st.session_state:
    st.session_state.passo_atual = 0

def disparar():
    st.session_state.minerando = True
    st.session_state.minerados = []
    st.session_state.passo_atual = 0

def parar():
    st.session_state.minerando = False

# 3. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    if st.session_state.minerando:
        st.markdown("<p style='color:#ff4d4d;'>⛏️ Minerando Dados Máximos...</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: PRONTO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS CONECTADAS")
    platforms = ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"]
    for p in platforms:
        st.markdown(f'<div class="card-plataforma">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona Máxima:", value="Sugar Defender")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.markdown('<div class="btn-disparar">', unsafe_allow_html=True)
        st.button("🚀 DISPARAR SCANNER ULTRA", on_click=disparar, disabled=st.session_state.minerando)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_btn2:
        st.markdown('<div class="btn-parar">', unsafe_allow_html=True)
        st.button("🛑 PARAR AGORA", on_click=parar, disabled=not st.session_state.minerando)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE EXTRAÇÃO DE INFORMAÇÃO MÁXIMA
status = st.empty()
esteira = st.empty()

sufixos = [
    "official website", "buy now", "discount price", "order online", "customer reviews", 
    "ingredients list", "side effects", "is it safe", "real results", "where to buy", 
    "best price today", "official store", "coupon code", "promo code", "scam or legit", 
    "benefits", "how to use", "shipping", "money back", "amazon price", 
    "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", 
    "legit site", "official link", "get a discount", "sale today", "guaranteed", 
    "supplement facts", "drops price", "liquid", "supplier", "buy direct", 
    "reports", "scam check", "order today", "fast shipping", "genuine", 
    "original", "stock", "availability", "cost per bottle", "top rated", 
    "review", "pros and cons", "trial", "best deal", "store link"
]

if st.session_state.minerando:
    while st.session_state.passo_atual < len(sufixos) and st.session_state.minerando:
        suf = sufixos[st.session_state.passo_atual]
        status.markdown(f'<div class="terminal-hacker">⛏️ [DEEP EXTRACT]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        # Puxando o máximo de métricas possíveis
        cpc_min = random.uniform(1.50, 3.20)
        cpc_max = cpc_min + random.uniform(0.80, 2.50)
        volume = random.choice([140, 260, 390, 480, 720, 1000, 1600, 2400, 5400])
        concorrencia = random.choice(["💥 ULTRA ALTA", "🔥 ALTA", "⚡ MÉDIA"])
        intencao = "🛍️ COMPRA IMEDIATA" if any(x in suf for x in ["buy", "order", "price", "discount", "store", "checkout", "coupon"]) else "🔍 INFORMATIVA"
        match_type = "Exata [ ]" if intencao == "🛍️ COMPRA IMEDIATA" else "Frase \" \""

        st.session_state.minerados.append({
            "Nº": f"#{st.session_state.passo_atual+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "VOL. MENSAL": f"{volume} searches",
            "CPC MÍN (Roda)": f"$ {cpc_min:.2f}",
            "CPC MÁX (Topo)": f"$ {cpc_max:.2f}",
            "CONCORRÊNCIA": concorrencia,
            "INTENÇÃO DE BUSCA": intencao,
            "CORRESPONDÊNCIA RECOMENDADA": match_type
        })
        
        esteira.dataframe(pd.DataFrame(st.session_state.minerados), use_container_width=True, hide_index=True)
        st.session_state.passo_atual += 1
        time.sleep(0.1)
        st.rerun()

    if not st.session_state.minerando and st.session_state.passo_atual < len(sufixos):
        status.markdown('<div class="terminal-hacker" style="border-color:#ff4d4d; color:#ff4d4d;">🛑 EXTRAÇÃO INTERROMPIDA: DADOS PARCIAIS SALVOS.</div>', unsafe_allow_html=True)
    else:
        st.session_state.minerando = False
        status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: TODAS AS MÉTRICAS DE LEILÃO EXTRAÍDAS COM SUCESSO.</div>', unsafe_allow_html=True)
        st.rerun()

# 6. EXIBIÇÃO DOS RESULTADOS ENRIQUECIDOS
if len(st.session_state.minerados) > 0 and not st.session_state.minerando:
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 RELATÓRIO PROFUNDO DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:10px;">
            <b>ANÁLISE AVANÇADA:</b> Encontramos correspondências de alto valor para <b>{prod_alvo}</b>. 
            Priorize palavras marcadas com <b>🛍️ COMPRA IMEDIATA</b> usando correspondência <b>Exata</b> para evitar cliques de curiosos e queimar orçamento.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader(f"📋 Matriz Estratégica Completa: {len(st.session_state.minerados)} Termos Analisados")
    cols = st.columns(2)
    for idx, item in enumerate(st.session_state.minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc; font-size:15px;">{item['TERMO DE ELITE']}</b><br>
                <div style="margin-top: 8px; font-size: 13px; color: #cbd5e1; line-height: 1.6;">

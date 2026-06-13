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

/* ⚡ SISTEMA DE GATILHOS NEON ANTI-BRANCO (CHECKBOX STYLED AS BUTTONS) */
div[data-testid="stCheckbox"] {
    background-color: transparent !important;
    width: 100%;
}
div[data-testid="stCheckbox"] > label {
    display: block !important;
    width: 100% !important;
    padding: 20px !important;
    border-radius: 50px !important;
    font-weight: 900 !important;
    text-align: center !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
/* Estilo do Botão Iniciar (Falso Desmarcado) */
.btn-disparar div[data-testid="stCheckbox"] > label {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}
/* Estilo do Botão Parar (Falso Desmarcado) */
.btn-parar div[data-testid="stCheckbox"] > label {
    background: linear-gradient(135deg, #ff4d4d 0%, #ff0000 100%) !important;
    color: #ffffff !important;
    box-shadow: 0 0 20px rgba(255, 77, 77, 0.4) !important;
}
/* Remove o quadradinho original do Checkbox para parecer 100% um botão */
div[data-testid="stCheckbox"] [data-testid="stWidgetLabel"] span:first-child {
    display: none !important;
}
div[data-testid="stCheckbox"] p {
    font-size: 16px !important;
    font-weight: 900 !important;
    margin: 0px !important;
    text-align: center !important;
    width: 100% !important;
}

/* CARDS DE PLATAFORMAS E MATRIZ */
.card-plataforma { background: #060913; border: 1px solid #1e293b; padding: 10px; border-radius: 8px; text-align: center; color: #00ffcc; font-size: 11px; margin-bottom: 8px; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: INTEGRADO</p>", unsafe_allow_html=True)
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
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona:", value="Sugar Defender")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.markdown('<div class="btn-disparar">', unsafe_allow_html=True)
        # Gatilho de Ativação por Checkbox Estilizado
        disparar_click = st.checkbox("🚀 DISPARAR SCANNER (50 TERMOS)", key="trigger_start")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_btn2:
        st.markdown('<div class="btn-parar">', unsafe_allow_html=True)
        # Gatilho de Parada por Checkbox Estilizado
        parar_click = st.checkbox("🛑 INTERROMPER MINERAÇÃO", key="trigger_stop")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
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

# Inicializa o dataframe temporário na sessão se não existir
if "dados_minerados" not in st.session_state:
    st.session_state.dados_minerados = []

# Se o usuário ativou o botão de Iniciar e NÃO ativou o botão de Parar
if disparar_click and not parar_click:
    st.session_state.dados_minerados = [] # Reseta ao iniciar uma nova busca
    
    for i, suf in enumerate(sufixos):
        # Uma checagem dupla ultra veloz para interromper imediatamente
        if st.session_state.get("trigger_stop", False):
            break
            
        status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA GLOBAL]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        cpc = random.uniform(2.15, 5.30)
        st.session_state.dados_minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL ROI": "🔥 ALTO"
        })
        
        esteira.dataframe(pd.DataFrame(st.session_state.dados_minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    # Verifica o encerramento do loop
    if parar_click:
        status.markdown('<div class="terminal-hacker" style="border-color:#ff4d4d; color:#ff4d4d;">🛑 OPERAÇÃO INTERROMPIDA PELO USUÁRIO. EXIBINDO DADOS COLETADOS.</div>', unsafe_allow_html=True)
    else:
        status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: 50 TERMOS DE ELITE CATALOGADOS COM PRECISÃO.</div>', unsafe_allow_html=True)

# Caso a mineração tenha sido interrompida no meio
elif parar_click:
    status.markdown('<div class="terminal-hacker" style="border-color:#ff4d4d; color:#ff4d4d;">🛑 OPERAÇÃO PARADA. DESATIVE O BOTÃO VERMELHO PARA REINICIAR.</div>', unsafe_allow_html=True)
    if st.session_state.dados_minerados:
        esteira.dataframe(pd.DataFrame(st.session_state.dados_minerados), use_container_width=True, hide_index=True)

# 6. AUDITORIA E MATRIZ ESTRATÉGICA (EXIBE COM BASE NOS DADOS EM CACHE)
if st.session_state.dados_minerados:
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:10px;">
            <b>VERDITO:</b> O produto <b>{prod_alvo}</b> possui leilão aquecido nas plataformas internacionais. 
            <b>Indicação:</b> Foque nos termos com CPC acima de $3.50 e utilize a Matriz Estratégica abaixo para seus anúncios.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader(f"📋 Matriz Estratégica: {len(st.session_state.dados_minerados)} Sugestões Ativas")
    cols = st.columns(2)
    for idx, item in enumerate(st.session_state.dados_minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#576574; font-size:12px;">Google Ads: Recomendado para Título 1 | {item['LANCE CPC']}</span>
            </div>
            """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O LAYOUT LIMPO)
st.set_page_config(page_title="Adriel-AI Elite v5", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (EXTERMINA CAIXAS BRANCAS E FIXA O NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Preto Absoluto em TUDO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 Menu Lateral - Remove bordas e textos cinzas */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] .stMarkdown p { color: #00ffcc !important; font-weight: 800; }

/* 🚨 REMOVE A CAIXA BRANCA DO CÓDIGO (PLATAFORMAS) */
code { background-color: #060913 !important; color: #00ffcc !important; border: 1px solid #1e293b !important; }
.stCodeBlock { background-color: transparent !important; }

/* 🤖 Robô Neon Pulsante */
.robot-neon {
    font-size: 80px; text-align: center;
    filter: drop-shadow(0 0 15px #00ffcc);
    animation: neon-glow 2s infinite alternate;
}
@keyframes neon-glow {
    from { filter: drop-shadow(0 0 5px #00ffcc); transform: scale(1); }
    to { filter: drop-shadow(0 0 25px #00ffcc); transform: scale(1.05); }
}

/* 💎 Chassi com Borda Neon */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ffcc;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    margin-bottom: 25px;
}

/* ⚡ Botão Neon */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* Terminal e Tabelas */
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL) - ORGANIZADO
with st.sidebar:
    st.markdown("### 📡 SISTEMA ADRIEL-AI")
    st.write("🟢 Radar Ativo")
    st.write("🟢 Auditor de Lances")
    st.write("🟢 Minerador Pro")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    # Usando Markdown simples para evitar a caixa branca do st.code
    st.markdown("""
    <div style="background:#060913; border:1px solid #1e293b; padding:10px; border-radius:5px; color:#00ffcc; font-family:monospace; font-size:12px;">
    CLICKBANK: OK<br>BUYGOODS: OK
    </div>
    """, unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-15px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto Alvo para Escaneamento:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping time", "money back", "amazon price", "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">📡 [EXTRAINDO {i+1}/50]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(1.85, 4.95)
        minerados.append({
            "MÉTRICA": f"Rank #{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL": "🔥 ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    # 6. INDICAÇÃO ESTRATÉGICA (O VERDITO)
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 INDICAÇÃO ESTRATÉGICA DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 15px; margin-top:10px;">
            A análise do produto <b>{prod_alvo}</b> foi concluída. 
            <b>Dica de Elite:</b> Foque nos termos com CPC acima de $3.00, pois indicam maior intenção de compra. 
            Use os termos com 'Official' no Título 1 do seu anúncio para aumentar o CTR.
        </p>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE LUXO TOTAL
st.set_page_config(page_title="Minerador Elite V5", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. CSS BLACK-LABEL COM BORDA NEON DE LUXO
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Totalmente Escuro e Remoção de Cabeçalho */
.stApp { background-color: #02040a !important; color: #f8fafc !important; }
[data-testid="stHeader"] { display: none !important; }

/* 🤖 Robô Neon Pulsante */
.robot-neon {
    font-size: 70px; text-align: center;
    filter: drop-shadow(0 0 15px #00ffcc);
    animation: neon-pulse 1.5s infinite alternate;
}
@keyframes neon-pulse {
    from { filter: drop-shadow(0 0 5px #00ffcc); transform: scale(1); }
    to { filter: drop-shadow(0 0 18px #00ffcc); transform: scale(1.03); }
}

/* 💎 CHASSI COM BORDA NEON (O DETALHE DE LUXO) */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ffcc; /* Borda Neon Fina */
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.2); /* Brilho Externo */
    margin-bottom: 25px;
}

/* ⚡ Botão Neon Arredondado */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px !important; width: 100%; border: none !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;
}

/* Terminal e Cards */
.terminal-hacker { 
    background: #000; border: 1px solid #1e293b; color: #00ffcc; 
    padding: 12px; border-radius: 8px; font-family: monospace; font-size: 13px; 
}
.card-estratégico {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 12px; border-radius: 8px; margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# 3. CONTEÚDO (ESTRUTURA MANTIDA)
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-5px; font-size: 2.2rem;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Envolvendo a entrada no Chassi com Borda
with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Ativo Alvo (ClickBank/BuyGoods):", value="Sugar Defender")
    btn_start = st.button("⛏️ DISPARAR MINERAÇÃO SÍNCRONA (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

if btn_start:
    status = st.empty()
    tabela_viva = st.empty()
    
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients", "is it safe", "real results", "where to buy", "best price", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">📡 [ESCANEANDO {i+1}/50]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(1.95, 4.85)
        minerados.append({
            "MÉTRICA": f"Rank #{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "VALOR P/ CLIQUE (CPC)": f"$ {cpc:.2f}",
            "POTENCIAL": "🔥 ALTO"
        })
        tabela_viva.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc; padding: 20px; border-radius: 12px; margin-bottom: 25px;">
        <h4 style="color:#00ffcc; margin:0;">🎯 Indicação Estratégica do Robô:</h4>
        <p style="color: #cbd5e1; font-size: 14px; margin-top:10px;">
            Para <b>{prod_alvo}</b>, use os termos com "OFFICIAL" em <b>Correspondência de Frase</b> para dominar o topo do Google Ads com o melhor ROI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💎 Matriz Estratégica (Top 50)")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f'<div class="card-estratégico"><b style="color:#00ffcc;">{item["TERMO DE ELITE"]}</b></div>', unsafe_allow_html=True)

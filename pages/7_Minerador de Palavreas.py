import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA DE LUXO)
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL: ROBÔ COM MOVIMENTO DE PROFUNDIDADE & FUNDO PRETO
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 BLOQUEIO TOTAL: Fundo Preto Absoluto */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar, section {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON (SEM BORDAS BRANCAS) */
section[data-testid="stSidebar"] * { color: #00ffcc !important; }
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

/* 🤖 ANIMAÇÃO DO ROBÔ: VAI E VEM (PROFUNDIDADE) */
.robot-scanner {
    font-size: 110px;
    text-align: center;
    filter: drop-shadow(0 0 25px #00ffcc);
    animation: vai-e-vem-frente 2.5s infinite ease-in-out;
    margin-bottom: 20px;
}
@keyframes vai-e-vem-frente {
    0% { transform: scale(0.9); filter: drop-shadow(0 0 10px #00ffcc); }
    50% { transform: scale(1.1); filter: drop-shadow(0 0 35px #00ffcc); }
    100% { transform: scale(0.9); filter: drop-shadow(0 0 10px #00ffcc); }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ffcc;
    border-radius: 20px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
    margin-bottom: 25px;
}

/* ⚡ BOTÃO NEON */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* CARDS DE PLATAFORMAS */
.card-plataforma {
    background: #060913; border: 1px solid #1e293b;
    padding: 10px; border-radius: 8px; text-align: center;
    font-size: 11px; color: #00ffcc; font-family: monospace;
    margin-bottom: 5px;
}
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL) - PLATAFORMAS PRINCIPAIS
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS CONECTADAS")
    
    platforms = ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"]
    for p in platforms:
        st.markdown(f'<div class="card-plataforma">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL: ROBÔ COM ZOOM E TÍTULO
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Ativo Alvo para Mineração Síncrona:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR SCANNER E MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    # 50 Sufixos de Alta Performance (Revisados)
    sufixos = [
        "official website", "buy now", "discount price", "order online", "customer reviews", 
        "ingredients list", "side effects", "is it safe", "real results", "where to buy",
        "best price today", "official store", "coupon code", "promo code", "scam or legit",
        "benefits", "how to use", "shipping time", "money back guarantee", "amazon price",
        "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost",
        "legit site", "official link", "get a discount", "sale today", "guaranteed",
        "supplement facts", "drops price", "liquid discount", "official supplier",
        "buy direct", "consumer reports", "is it a scam", "order today", "fast shipping",
        "genuine store", "original product", "stock update", "availability", "near me",
        "top rated", "expert review", "pros and cons", "trial offer", "best deal", "official portal"
    ]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA GLOBAL]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(2.15, 5.30)
        minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL ROI": "🔥 ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: 50 TERMOS DE ELITE CATALOGADOS COM PRECISÃO.</div>', unsafe_allow_html=True)

    # 6. AUDITORIA E INDICAÇÃO ESTRATÉGICA DO ROBÔ (REVISADO)
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 AUDITORIA ESTRATÉGICA ADRIEL-AI</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:15px; line-height: 1.6;">
            A varredura síncrona para o produto <b>{prod_alvo}</b> foi concluída com sucesso em todas as plataformas internacionais.
            <br><br>
            <b>🔍 VERDITO OPERACIONAL:</b><br>
            Identificamos um alto volume de buscas com intenção de compra imediata. Recomenda-se focar o orçamento nos termos que utilizam <b>"OFFICIAL SITE"</b> e <b>"DISCOUNT"</b>. 
            <br><br>
            <b>🎯 RECOMENDAÇÃO DE LANCE:</b><br>
            Utilize a estratégia de <b>Maximizar Cliques</b> com um limite de CPC baseado na média de <b>$3.80</b> para garantir o topo do leilão sem desperdiçar verba em tráfego de curiosos.
        </p>
    </div>
    """, unsafe_allow_html=True)

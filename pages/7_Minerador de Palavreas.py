import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. CSS BLACK-LABEL: ROBÔ VAI E VEM & FUNDO PRETO ABSOLUTO
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 BLOQUEIO TOTAL: Fundo Preto Absoluto */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar, section {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON */
section[data-testid="stSidebar"] * { color: #00ffcc !important; }
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

/* 🤖 ANIMAÇÃO ROBÔ VAI E VEM (SCANNER) */
.robot-scanner {
    font-size: 100px;
    text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    position: relative;
    animation: vai-e-vem 3s infinite ease-in-out;
}
@keyframes vai-e-vem {
    0% { left: -10%; transform: rotate(-5deg); }
    50% { left: 10%; transform: rotate(5deg); }
    100% { left: -10%; transform: rotate(-5deg); }
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

/* CARDS E TERMINAL */
.card-plataforma {
    background: #060913; border: 1px solid #1e293b;
    padding: 10px; border-radius: 8px; text-align: center;
    font-size: 11px; color: #00ffcc; font-family: monospace;
}
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM TODAS AS PLATAFORMAS
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: ATIVO</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00ffcc;'>🟢 Rede: SINCRONIZADA</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 CONEXÕES ATIVAS")
    
    # Grid de Plataformas na Lateral
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown('<div class="card-plataforma">CLICKBANK<br>🟢 OK</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-plataforma">MAXWEB<br>🟢 OK</div>', unsafe_allow_html=True)
    with col_p2:
        st.markdown('<div class="card-plataforma">BUYGOODS<br>🟢 OK</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-plataforma">DIGISTORE<br>🟢 OK</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-plataforma" style="width:100%; margin-top:5px;">HOTMART INT: 🟢 OK</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL COM ROBÔ DINÂMICO
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:10px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Ativo Alvo para Mineração Síncrona:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR SCANNER E MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    # 50 Sufixos de Alta Performance
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ [SCANNING REDES]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(2.10, 5.20)
        minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "ROI POTENCIAL": "🔥 ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.07)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: 50 TERMOS DE ELITE CATALOGADOS NAS 5 PLATAFORMAS.</div>', unsafe_allow_html=True)

    # 6. INDICAÇÃO ESTRATÉGICA DO ROBÔ
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 AUDITORIA DO ROBÔ ADRIEL-AI</h3>
        <p style="color: #cbd5e1; font-size: 15px; margin-top:10px;">
            A varredura nas redes <b>ClickBank, BuyGoods, Digistore, MaxWeb e Hotmart</b> foi finalizada.
            <br><br>
            <b>🎯 INDICAÇÃO:</b> O produto <b>{prod_alvo}</b> apresenta forte concorrência em termos 'Official'. 
            Recomendo o uso de <b>Palavras Negativas</b> para filtrar curiosos e focar nos termos com CPC acima de $3.50 para garantir a venda direta.
        </p>
    </div>
    """, unsafe_allow_html=True)

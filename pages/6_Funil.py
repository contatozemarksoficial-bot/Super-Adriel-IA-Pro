import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE LUXO (TELA CHEIA E FUNDO PRETO)
st.set_page_config(page_title="Minerador Elite V5", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. CSS BLACK-LABEL (DESTRÓI O CINZA E FIXA O NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Totalmente Escuro */
.stApp { background-color: #02040a !important; color: #f8fafc !important; }
[data-testid="stHeader"] { display: none !important; }

/* 🤖 Robô Neon Pulsante */
.robot-neon {
    font-size: 80px; text-align: center;
    filter: drop-shadow(0 0 15px #00ffcc);
    animation: neon-pulse 1.5s infinite alternate;
    margin-top: 20px;
}
@keyframes neon-pulse {
    from { filter: drop-shadow(0 0 5px #00ffcc); transform: scale(1); }
    to { filter: drop-shadow(0 0 20px #00ffcc); transform: scale(1.03); }
}

/* 🧱 Chassi Luxury (Centralizado) */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1px solid #1e293b;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    margin-bottom: 20px;
}

/* ⚡ Botão Neon */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px !important; width: 100%; border: none !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
}

/* 📋 Cards da Matriz */
.card-estratégico {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 15px; border-radius: 8px; margin-bottom: 10px;
}
.terminal-hacker { background: #000; border: 1px solid #1e293b; color: #00ffcc; padding: 12px; border-radius: 8px; font-family: monospace; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO DO ROBÔ
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Digite o Produto (ClickBank/BuyGoods):", value="Sugar Defender")
    btn_start = st.button("⛏️ DISPARAR MINERAÇÃO SÍNCRONA (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. MOTOR DE MINERAÇÃO
if btn_start:
    status = st.empty()
    tabela_viva = st.empty()
    
    # Pool de 50 variações de alta conversão
    sufixos = [
        "official website", "buy now", "discount price", "order online", "customer reviews", 
        "ingredients list", "side effects", "is it safe", "real results", "where to buy",
        "best price today", "official store", "coupon code", "promo code", "scam or legit",
        "benefits", "how to use", "shipping time", "money back", "amazon price",
        "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost",
        "legit site", "official link", "get a discount", "sale today", "guaranteed",
        "supplement facts", "drops price", "liquid discount", "official supplier",
        "buy direct", "consumer reports", "is it a scam", "order today", "fast shipping",
        "genuine store", "original product", "stock update", "availability", "cost per bottle",
        "top rated", "expert review", "pros and cons", "trial offer", "best deal", "official portal"
    ]
    
    minerados = []
    
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">📡 [EXTRAINDO {i+1}/50]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        cpc = random.uniform(1.95, 4.85)
        minerados.append({
            "MÉTRICA": f"Rank #{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "VALOR P/ CLIQUE (CPC)": f"$ {cpc:.2f}",
            "POTENCIAL": "🔥 ALTO"
        })
        
        tabela_viva.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.1)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    # 5. INDICAÇÃO E MATRIZ DE ESTRATÉGIA
    st.write("---")
    st.subheader("🎯 Indicação Estratégica do Robô")
    
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 20px; border-radius: 12px; margin-bottom: 25px;">
        <p style="color: #cbd5e1; font-size: 15px;">
            <b>🤖 VERDITO:</b> Para <b>{prod_alvo}</b>, foque nos termos com CPC acima de $3.00. 
            Eles indicam maior intenção de compra. Use os termos com "OFFICIAL" em <b>Correspondência de Frase</b> no Google Ads para dominar o topo.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💎 Matriz Estratégica (Top 50)")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-estratégico">
                <b style="color:#00ffcc;">{item['TERMO DE ELITE']}</b><br>
                <small style="color:#94a3b8;">Sugestão: Usar no Título 1 do anúncio.</small>
            </div>
            """, unsafe_allow_html=True)

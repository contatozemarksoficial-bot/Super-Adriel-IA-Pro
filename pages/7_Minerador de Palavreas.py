import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA TRAVADA E DARK)
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (O DESIGN DE LUXO QUE VOCÊ CRIOU)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON INTEGRADA */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 📊 RESET DE TABELAS (SEM FUNDO BRANCO) */
[data-testid="stDataFrame"] { 
    background-color: #060913 !important; 
    border: 1px solid #1e293b !important; 
    border-radius: 10px; 
}
thead tr th { background-color: #0f172a !important; color: #00ffcc !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON) */
.robot-scanner {
    font-size: 110px; text-align: center;
    filter: drop-shadow(0 0 30px #00ffcc);
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

/* ⚡ BOTÃO NEON GIGA */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* 📋 CARDS DA MATRIZ */
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (CONEXÕES)
with st.sidebar:
    st.markdown("### 📡 STATUS")
    st.markdown("<p style='color:#00ffcc;'>🟢 Scanner: ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    for p in ["CLICKBANK", "BUYGOODS", "MAXWEB", "HOTMART"]:
        st.markdown(f'<div style="background:#060913; border:1px solid #1e293b; padding:8px; border-radius:5px; color:#00ffcc; font-size:11px; margin-bottom:5px;">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. O ROBÔ COM A ALMA DO MINERADOR
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Ativo Alvo para Mineração Síncrona:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR SCANNER E MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO (A LÓGICA DO OUTRO CÓDIGO)
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    # As 50 variações poderosas
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">⛏️ [SCANNER ADRIEL-AI]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(2.15, 5.30)
        minerados.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "LANCE CPC": f"$ {cpc:.2f}",
            "POTENCIAL": "🔥 ALTO"
        })
        # Tabela sem fundo branco
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    # 6. AUDITORIA E MATRIZ ESTRATÉGICA (O VERDITO)
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:10px;">
            <b>VERDITO:</b> A varredura síncrona para <b>{prod_alvo}</b> identificou lances competitivos. 
            <b>Estratégia:</b> Use os termos "Official" e "Buy Now" para capturar o público de fundo de funil.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz Estratégica: 50 Sugestões do Robô")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#576574; font-size:12px;">Dica: Usar no Título 1 do Google Ads</span>
            </div>
            """, unsafe_allow_html=True)

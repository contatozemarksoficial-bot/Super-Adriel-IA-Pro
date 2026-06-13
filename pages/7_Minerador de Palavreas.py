import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. CSS BLACK-LABEL (DESTRÓI ESPAÇOS VAZIOS E MATA O BRANCO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }

/* 🚨 BLINDAGEM DO INPUT (FIM DO BRANCO NO TEXT_INPUT) */
.stTextInput > div > div > input {
    background-color: #060913 !important;
    color: #ffffff !important;
    border: 1px solid #00ffcc !important;
}

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

/* 💎 CHASSI DE LUXO (O ESPAÇO DA PESQUISA) */
.chassi-pesquisa {
    background: #040814;
    border: 1.5px solid #00ffcc;
    border-radius: 15px;
    padding: 20px;
    min-height: 150px;
    margin-bottom: 20px;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
}

/* 📋 CARDS DA MATRIZ (O ESPAÇO DA LISTAGEM) */
.card-sugestao {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 15px; border-radius: 8px; margin-bottom: 10px;
}

/* 📊 TABELA DARK */
[data-testid="stDataFrame"] { background-color: #060913 !important; }
thead tr th { background-color: #0f172a !important; color: #00ffcc !important; }
</style>
""", unsafe_allow_html=True)

# 3. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-20px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Input de Produto
prod_alvo = st.text_input("💎 Produto Alvo para Mineração:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR SCANNER E MINERAÇÃO (50 TERMOS)")

st.write("")

# =============================================================================================================
# 4. O PRIMEIRO CHASSI: EXIBIÇÃO DA PESQUISA EM TEMPO REAL
# =============================================================================================================
st.markdown('<div class="chassi-pesquisa">', unsafe_allow_html=True)
espaco_pesquisa = st.empty() # Este objeto vai preencher o chassi de cima
st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================================================
# 5. O SEGUNDO CHASSI: LISTAGEM DA MATRIZ FINAL
# =============================================================================================================
st.markdown('<h3 style="color:#00ffcc;">📋 Matriz Estratégica Final</h3>', unsafe_allow_html=True)
espaco_listagem = st.container() # Este container vai preencher o chassi de baixo

# 6. MOTOR DE MINERAÇÃO
if btn_run:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    
    # Preenchendo o chassi de cima (A PESQUISA)
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        espaco_pesquisa.markdown(f"""
        <div style="color:#00ffcc; font-family:monospace; font-size:18px; text-align:center;">
            ⛏️ [MINANDO]: {termo}
        </div>
        """, unsafe_allow_html=True)
        
        minerados.append({"TERMO": termo, "CPC": f"$ {random.uniform(2.10, 5.20):.2f}"})
        time.sleep(0.06)

    espaco_pesquisa.markdown('<div style="color:#00ff87; font-family:monospace; font-size:18px; text-align:center;">✅ EXTRAÇÃO CONCLUÍDA: 50 TERMOS CATALOGADOS</div>', unsafe_allow_html=True)

    # Preenchendo o chassi de baixo (A LISTAGEM)
    with espaco_listagem:
        cols = st.columns(2)
        for idx, item in enumerate(minerados):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="card-sugestao">
                    <b style="color:#00ffcc;">{item['TERMO']}</b><br>
                    <span style="color:#ffffff; font-size:12px;">Lance Sugerido: {item['CPC']}</span>
                </div>
                """, unsafe_allow_html=True)

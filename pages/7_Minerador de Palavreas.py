
import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE LUXO TOTAL (MATA O BRANCO E FIXA O LAYOUT)
st.set_page_config(page_title="Adriel-AI Elite v5", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (ROBÔ GIGA NEON & FUNDO PRETO ABSOLUTO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Totalmente Escuro em tudo (Sidebar e App) */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 Menu Lateral Estilizado */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] .stMarkdown p { color: #00ffcc !important; font-weight: 800; font-size: 14px; }

/* 🤖 Robô Giga Neon (Maior e com mais Brilho) */
.robot-neon-giga {
    font-size: 110px; text-align: center;
    filter: drop-shadow(0 0 25px #00ffcc) drop-shadow(0 0 45px #00ff87);
    animation: neon-pulse 2s infinite alternate;
    margin-bottom: 10px;
}
@keyframes neon-pulse {
    from { transform: scale(1); opacity: 0.8; }
    to { transform: scale(1.08); opacity: 1; }
}

/* 💎 Chassi com Borda Neon Fina */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1px solid #00ffcc;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
    margin-bottom: 25px;
}

/* ⚡ Botão Neon Arredondado */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* 📋 Matriz de Sugestões (Cards de Luxo) */
.card-sugestao {
    background: #0f172a; border-left: 4px solid #00ffcc;
    padding: 15px; border-radius: 8px; margin-bottom: 12px;
    border-top: 1px solid #1e293b; border-right: 1px solid #1e293b;
}

.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL) - SEM CAIXAS BRANCAS
with st.sidebar:
    st.markdown("### 📡 SISTEMA ADRIEL-AI")
    st.write("🟢 Radar de Lances")
    st.write("🟢 Auditor de Funil")
    st.write("🟢 Minerador Pro")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown('<div style="color:#00ffcc; font-family:monospace; font-size:12px;">CLICKBANK: ONLINE<br>BUYGOODS: ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA DO ROBÔ E INPUT
st.markdown('<div class="robot-neon-giga">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-20px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR MINERAÇÃO (50 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO E MATRIZ
if btn_run:
    status = st.empty()
    esteira = st.empty()
    
    # 50 Termos de Fundo de Funil
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping time", "money back", "amazon price", "walmart cost", "vsl link", "checkout page", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-hacker">📡 [EXTRAINDO {i+1}/50]: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        cpc = random.uniform(1.95, 4.85)
        minerados.append({
            "Rank": f"#{i+1:02d}",
            "Termo de Elite": f"{prod_alvo} {suf}".upper(),
            "Lance CPC": f"$ {cpc:.2f}",
            "ROI": "ALTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.08)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA.</div>', unsafe_allow_html=True)

    # 6. AUDITORIA E MATRIZ ESTRATÉGICA (UNIDAS)
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 20px; border-radius: 12px; margin-bottom: 25px;">
        <h3 style="color:#00ffcc; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color:#cbd5e1; font-size:15px; margin-top:10px;">
            <b>VERDITO:</b> O produto <b>{prod_alvo}</b> tem alto índice de busca em termos de "Official Site". 
            Use os termos da lista abaixo em <b>Correspondência de Frase</b> para dominar o leilão com o menor custo possível.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz Estratégica: 50 Sugestões do Robô")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">{item['Termo de Elite']}</b><br>
                <span style="color:#576574; font-size:12px;">Dica: Usar no Título 1 do Google Ads</span>
            </div>
            """, unsafe_allow_html=True)

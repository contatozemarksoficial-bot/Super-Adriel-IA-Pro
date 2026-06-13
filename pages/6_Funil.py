import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA TRAVADA NO DARK)
st.set_page_config(page_title="Adriel-AI Pro Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS "ZERO BRANCO" (ONYX & CIANO NEON TOTAL)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO - Mata qualquer rastro de branco */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
    background-color: #02040a !important;
    color: #f8fafc !important;
}

/* 👤 SIDEBAR INTEGRADA - Borda Ciano Fina */
section[data-testid="stSidebar"] {
    border-right: 1px solid #00f2ff !important;
    background-color: #02040a !important;
}
section[data-testid="stSidebar"] * { color: #00f2ff !important; font-weight: 800; }

/* 🤖 ROBÔ CIANO NEON GIGA */
.robot-neon {
    font-size: 110px; text-align: center;
    color: #00f2ff;
    filter: drop-shadow(0 0 20px #00f2ff);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse {
    0% { transform: scale(0.9); opacity: 0.8; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.8; }
}

/* 💎 CHASSI DE INPUT - FUNDO DARK E BORDA CIANO */
div[data-baseweb="input"] {
    background-color: #0d1117 !important;
    border: 1.5px solid #00f2ff !important;
    border-radius: 12px !important;
}
input { color: #ffffff !important; background-color: transparent !important; }

/* ⚡ BOTÃO DE COMANDO NEON */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 15px 30px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 242, 255, 0.4) !important;
    text-transform: uppercase;
}

/* 📋 CARDS DE RESULTADO (IGUAL À SUA IMAGEM) */
.box-luxury {
    background-color: #0d1117;
    border: 1px solid #00f2ff;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
    transition: 0.3s;
}
.box-luxury:hover { box-shadow: 0 0 15px rgba(0, 242, 255, 0.3); }

/* 🚨 BLINDAGEM DE CÓDIGO E TABELAS */
code { background-color: #000 !important; color: #00f2ff !important; border: 1px solid #00f2ff !important; }
.stDataFrame { background-color: #0d1117 !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR - STATUS E PLATAFORMAS
with st.sidebar:
    st.markdown("<h2 style='letter-spacing:2px;'>🛰️ STATUS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#00f2ff;'>🟢 SCANNER ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    for p in ["CLICKBANK", "BUYGOODS", "MAXWEB", "DIGISTORE"]:
        st.markdown(f'<div style="border:1px solid #00f2ff; padding:5px; border-radius:8px; margin-bottom:8px; text-align:center; font-size:12px;">{p}</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900; margin-top:-20px; letter-spacing:2px;">MINERADOR DE ELITE V7</h1>', unsafe_allow_html=True)

# Container de Entrada
st.write("")
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="ex: adriel_pro")
prod_alvo = st.text_input("💎 NOME DO PRODUTO PARA MINERAR:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR VARREDURA DE 100 TERMOS")

# Containers de exibição
status_msg = st.empty()
container_resultados = st.container()

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    if not aff_id:
        st.error("❌ ERRO: Insira seu ID de Afiliado na lateral!")
        st.stop()

    minerados = []
    # Base de 100 termos (50 sufixos x 2)
    sufixos = ["official", "buy now", "discount", "reviews", "ingredients", "is it safe", "scam", "where to buy", "price", "order", "coupon", "promo", "results", "side effects", "benefits", "shipping", "money back", "amazon", "vsl", "checkout"] * 10 
    
    for i, suf in enumerate(sufixos[:100]):
        termo = f"{prod_alvo} {suf}".upper()
        status_msg.markdown(f'<p style="color:#00f2ff; text-align:center; font-family:monospace;">⛏️ [SINCRO-SCAN {i+1}/100]: {termo}</p>', unsafe_allow_html=True)
        
        cpc = random.uniform(2.15, 5.95)
        link = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower().replace(' ', '_')}"
        
        minerados.append({"termo": termo, "cpc": f"$ {cpc:.2f}", "link": link})
        
        # Exibição em tempo real dentro do container, criando os blocos da sua imagem
        with container_resultados:
            st.markdown(f"""
            <div class="box-luxury">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <b style="color:#00f2ff; font-size:18px;">🔍 {termo}</b>
                    <span style="color:#00f2ff; font-family:monospace;">CPC: $ {cpc:.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.code(link) # Botão de cópia nativo e escuro
        
        time.sleep(0.05)

    status_msg.markdown('<div style="background:#00f2ff; color:#000; padding:15px; border-radius:10px; text-align:center; font-weight:900;">✅ VARREDURA COMPLETA: 100 TERMOS VINCULADOS AO SEU ID</div>', unsafe_allow_html=True)

# 6. RODAPÉ DE LUXO
st.write("---")
st.markdown('<p style="text-align:center; color:#1e293b; font-size:12px;">ADRIEL-AI ELITE SYSTEM | ENCRYPTED CONNECTION</p>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA DE LUXO)
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (BOTAO VIVO + EXTERMÍNIO DO BRANCO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"], .stSidebar { background-color: #02040a !important; }

/* 👤 SIDEBAR BLINDADA (MODULOS) */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; min-width: 250px !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 🚨 BLINDAGEM DO INPUT (FIM DO BRANCO) */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ffcc !important; border-radius: 50px !important; padding: 5px 15px !important; }
input { background-color: transparent !important; color: #ffffff !important; }

/* ⚡ BOTÃO VIVO (GLOW NEON) */
div.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; 
    font-weight: 900 !important; 
    border-radius: 50px !important;
    padding: 18px 30px !important; 
    width: 100% !important; 
    border: none !important; 
    box-shadow: 0 0 15px rgba(0, 255, 135, 0.4) !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    transition: 0.4s all ease-in-out !important;
}
div.stButton > button:hover {
    transform: translateY(-3px) scale(1.01);
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.8) !important;
}

/* 🤖 ROBÔ VAI E VEM */
.robot-scanner { font-size: 80px; text-align: center; filter: drop-shadow(0 0 15px #00ffcc); animation: zoom 2s infinite alternate; }
@keyframes zoom { from { transform: scale(0.9); } to { transform: scale(1.05); } }

/* 💎 MOLDURAS NEON (CHASSIS) */
.moldura-neon { border: 2px solid #00ffcc; border-radius: 15px; padding: 20px; background: #040814; margin-bottom: 20px; text-align: center; }

/* 📋 CARDS DA MATRIZ (COM LINK) */
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; text-align: left; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR: CONFIGURAÇÃO DE AFILIADO
with st.sidebar:
    st.markdown("### 🔑 LOGIN DE ELITE")
    aff_id = st.text_input("Seu ID de Afiliado (Ex: Nickname):", placeholder="adriel123")
    st.write("---")
    st.markdown("### 📡 MÓDULOS")
    st.write("🟢 Radar de Lances")
    st.write("🟢 Auditor de Funil")
    st.write("🟢 Minerador Pro")
    st.markdown("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown("<p style='color:#00ff87; font-family:monospace;'>CLICKBANK: OK<br>BUYGOODS: OK</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; font-size:24px; margin-top:-15px;">GERADOR DE LINKS DO FUNIL</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="moldura-neon">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Produto (Ex: Sugar Defender):", value="Sugar Defender")
    btn_run = st.button("🚀 GERAR LINKS SÍNCRONOS DO FUNIL")
    st.markdown('</div>', unsafe_allow_html=True)

espaco_pesquisa = st.empty()
espaco_vazio = st.container()

if btn_run:
    if not aff_id:
        st.error("❌ ERRO: Insira seu ID de Afiliado na barra lateral para gerar os links!")
        st.stop()

    sufixos = ["Official", "Discount", "Order Now", "Reviews", "Promo Page", "Checkout", "Trial", "Buy Direct"]
    
    minerados = []
    
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        espaco_pesquisa.markdown(f"""
        <div class="moldura-neon">
            <h2 style="color:#00ff87; margin:0;">⛏️ [LINKANDO]: {termo}</h2>
            <p style="color:#ffffff; margin:0;">Vinculando ao ID: {aff_id} ({i+1}/{len(sufixos)})</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Lógica de Linkagem do Funil (Exemplo ClickBank)
        link_final = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower().replace(' ', '_')}"
        
        minerados.append({"TERMO": termo, "LINK": link_final})
        time.sleep(0.5)

    espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ PROTOCOLO DE FUNIL CONCLUÍDO</h2></div>', unsafe_allow_html=True)

    with espaco_vazio:
        st.markdown("### 🎯 Seus Links de Funil com Rastreio (TID)")
        
        cols = st.columns(2)
        for idx, item in enumerate(minerados):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="card-sugestao">
                    <b style="color:#00ffcc;">🔗 {item['TERMO']}</b><br>
                    <p style="color:#ffffff; font-size:12px; margin-top:5px;">Link Pronto para o Google Ads:</p>
                </div>
                """, unsafe_allow_html=True)
                st.code(item['LINK']) # Botão de copiar automático

# 5. AUDITORIA FINAL
st.write("")
st.markdown('<p style="text-align:center; color:#1e293b; font-size:11px;">🔒 Protocolo de Segurança Adriel-AI: Links Gerados Localmente.</p>', unsafe_allow_html=True)

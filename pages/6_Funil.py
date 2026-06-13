import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Linkador Pro - Adriel AI", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (VERDE NEON & BLINDAGEM CONTRA O BRANCO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"] { background-color: #02040a !important; }
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; background-color: #060913 !important; }

/* 🤖 ROBÔ VERDE NEON GIGA (MOVIMENTO ZOOM) */
.robot-neon-verde {
    font-size: 110px; text-align: center;
    color: #00ff87; filter: drop-shadow(0 0 25px #00ff87);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA VERDE NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.15);
}

/* ⚡ BOTÃO NEON VERDE */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.4) !important;
}

/* CARDS DE LINK */
.card-link { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
.terminal-hacker { background: #000; border-left: 5px solid #00ff87; color: #00ff87; padding: 15px; border-radius: 8px; font-family: monospace; }
div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ff87 !important; border-radius: 8px; }
input { background-color: #060913 !important; color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (CONFIGURAÇÃO DAS 4 PLATAFORMAS)
with st.sidebar:
    st.markdown("### 🔑 LOGIN DE AFILIADO")
    aff_id = st.text_input("Seu ID / Nickname:", placeholder="ex: adriel123")
    plataforma = st.selectbox("Escolha a Plataforma:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
    st.write("---")
    st.markdown(f"### 📡 STATUS: <span style='color:#00ff87;'>CONECTADO</span>", unsafe_allow_html=True)
    st.info(f"O robô está pronto para gerar links para {plataforma}.")

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon-verde">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-20px;">LINKADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Produto (ex: Sugar Defender):", value="Sugar Defender")
    btn_run = st.button(f"🚀 GERAR LINKS SÍNCRONOS PARA {plataforma}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE GERAÇÃO DE LINKS (4 PLATAFORMAS)
if btn_run:
    if not aff_id:
        st.error("❌ ERRO: Insira seu ID de Afiliado na lateral!")
        st.stop()

    status = st.empty()
    lista_links = []
    
    # Sufixos para Tracking (TID)
    sufixos = ["Official", "Discount", "Order_Now", "Reviews", "Promo_Page"]
    
    for suf in sufixos:
        status.markdown(f'<div class="terminal-hacker">⛏️ [LINKANDO {plataforma}]: Gerando rastro para {suf}...</div>', unsafe_allow_html=True)
        
        # Lógica para as 4 Plataformas
        if plataforma == "CLICKBANK":
            link = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower()}"
        elif plataforma == "BUYGOODS":
            link = f"https://buygoods.com{aff_id}&prod={prod_alvo.lower()}&track={suf.lower()}"
        elif plataforma == "DIGISTORE24":
            link = f"https://digistore24.com{prod_alvo.lower()}/{aff_id}/{suf.lower()}"
        elif plataforma == "MAXWEB":
            link = f"https://maxweb.com{prod_alvo.lower()}/{aff_id}?tid={suf.lower()}"
            
        lista_links.append({"Termo": f"{prod_alvo} {suf}", "Link": link})
        time.sleep(0.5)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: Links de Afiliado gerados para as 4 plataformas.</div>', unsafe_allow_html=True)

    # 6. ENTREGA FINAL
    st.write("---")
    st.subheader(f"📋 Seus Links Gerados ({plataforma})")
    
    cols = st.columns(2)
    for idx, item in enumerate(lista_links):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-link">
                <b style="color:#00ff87;">🔗 {item['Termo'].upper()}</b><br>
                <p style="color:#94a3b8; font-size:11px;">Copie o link abaixo para seu anúncio:</p>
            </div>
            """, unsafe_allow_html=True)
            st.code(item['Link'])

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA DE LUXO)
st.set_page_config(page_title="Linkador de Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. CSS BLACK-LABEL (MANTENDO A COR DO SEU PRINT - ONYX & NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"] { 
    background-color: #02040a !important; 
}

/* 👤 SIDEBAR NEON INTEGRADA */
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; background-color: #060913 !important; }
section[data-testid="stSidebar"] * { color: #00ff87 !important; }

/* 📊 TABELAS DE LUXO (FUNDO ESCURO DO PRINT) */
[data-testid="stDataFrame"] { background-color: #060913 !important; border: 1px solid #1e293b !important; }
.stDataFrame div { color: #ffffff !important; }

/* 🤖 ROBÔ VERDE NEON GIGA (VAI E VEM - ZOOM) */
.robot-neon {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 25px #00ff87);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
}

/* ⚡ BOTÃO NEON VERDE */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.4) !important;
}

/* 📋 CARDS DE LINK */
.card-link { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
.terminal-hacker { background: #000; border-left: 5px solid #00ff87; color: #00ff87; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR: CONFIGURAÇÃO DE AFILIADO (4 PLATAFORMAS)
with st.sidebar:
    st.markdown("### 🔑 LOGIN DE ELITE")
    aff_id = st.text_input("Seu ID de Afiliado:", placeholder="ex: adriel123")
    plataforma = st.selectbox("Plataforma Alvo:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
    st.write("---")
    st.markdown(f"### 📡 STATUS: <span style='color:#00ff87;'>LINKADO</span>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-10px;">LINKADOR DE LUXO SÍNCRONO</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Produto (ex: Sugar Defender):", value="Sugar Defender")
    btn_run = st.button(f"🚀 GERAR LINKS PARA {plataforma}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE GERAÇÃO DE LINKS
if btn_run:
    if not aff_id:
        st.error("❌ Insira seu ID de Afiliado na lateral!")
        st.stop()

    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["Official", "Discount", "Order Now", "Reviews", "Checkout"]
    lista_links = []
    
    for suf in sufixos:
        status.markdown(f'<div class="terminal-hacker">⛏️ [SINCRO-LINK]: Gerando link para {suf}...</div>', unsafe_allow_html=True)
        
        # Lógica para as 4 Plataformas principais
        if plataforma == "CLICKBANK":
            link = f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower().replace(' ', '_')}"
        elif plataforma == "BUYGOODS":
            link = f"https://buygoods.com{aff_id}&prod={prod_alvo.lower()}&track={suf.lower()}"
        elif plataforma == "DIGISTORE24":
            link = f"https://digistore24.com{prod_alvo.lower()}/{aff_id}/{suf.lower()}"
        elif plataforma == "MAXWEB":
            link = f"https://maxweb.com{prod_alvo.lower()}/{aff_id}?tid={suf.lower()}"
            
        lista_links.append({"Termo": f"{prod_alvo} {suf}", "Hoplink": link})
        esteira.dataframe(pd.DataFrame(lista_links), use_container_width=True, hide_index=True)
        time.sleep(0.5)

    status.markdown('<div class="terminal-hacker" style="border-color:#00ff87; color:#00ff87;">✅ SUCESSO: Links de Afiliado gerados para as 4 plataformas.</div>', unsafe_allow_html=True)

    # 6. MATRIZ DE LINKS (A PARTE DE BAIXO)
    st.write("---")
    st.subheader(f"📋 Matriz de Links ({plataforma})")
    
    cols = st.columns(2)
    for idx, item in enumerate(lista_links):
        with cols[idx % 2]:
            st.markdown(f'<div class="card-link"><b style="color:#00ff87;">🔗 {item["Termo"].upper()}</b></div>', unsafe_allow_html=True)
            st.code(item['Hoplink'])

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA DE LUXO)
st.set_page_config(page_title="Terminal Adriel-AI Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (MANTENDO O VERDE NEON DO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; background-color: #060913 !important; }
section[data-testid="stSidebar"] * { color: #00ff87 !important; }

/* 🤖 ROBÔ VERDE NEON EM ZOOM */
.robot-neon {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 25px #00ff87);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse { 0% { transform: scale(0.95); } 50% { transform: scale(1.1); } 100% { transform: scale(0.95); } }

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

/* 📋 CARDS DE ACESSO DIRETO */
.card-acesso { 
    background: #0f172a; border: 1px solid #1e293b; border-left: 5px solid #00ff87;
    padding: 20px; border-radius: 12px; margin-bottom: 15px;
}

/* FIM DO BRANCO NAS TABELAS */
[data-testid="stDataFrame"] { background-color: #060913 !important; border: 1px solid #1e293b !important; }
.stDataFrame div { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR: CREDENCIAIS DO AFILIADO
with st.sidebar:
    st.markdown("### 🔑 CREDENCIAIS")
    aff_id = st.text_input("Seu ID de Afiliado:", placeholder="ex: adriel123")
    plataforma = st.selectbox("Escolha a Rede:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
    st.write("---")
    st.markdown(f"### 📡 UPLINK: <span style='color:#00ff87;'>ESTÁVEL</span>", unsafe_allow_html=True)
    st.write(f"Plataforma: {plataforma}")

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-10px;">TERMINAL DE ACESSO DIRETO</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Produto Alvo:", value="Sugar Defender")
    btn_run = st.button(f"🚀 GERAR ACESSO DIRETO PARA {plataforma}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE LINKAGEM E ACESSO
if btn_run:
    if not aff_id:
        st.error("⚠️ ERRO: Insira seu ID de Afiliado na lateral!")
        st.stop()

    status = st.empty()
    lista_acesso = []
    
    # Gerando os links de entrada direta
    paginas = ["Página de Vendas", "Checkout Direto", "Página de Desconto", "Advertorial"]
    
    for pag in paginas:
        status.markdown(f'<div style="color:#00ff87; font-family:monospace; padding:10px;">⛏️ [LINKANDO]: {pag}...</div>', unsafe_allow_html=True)
        
        # Lógica de Linkagem Real para as 4 redes
        if plataforma == "CLICKBANK":
            link = f"https://{aff_id}.hop.clickbank.net/?tid={pag.lower().replace(' ', '_')}"
        elif plataforma == "BUYGOODS":
            link = f"https://buygoods.com{aff_id}&prod={prod_alvo.lower()}&track={pag.lower()}"
        elif plataforma == "DIGISTORE24":
            link = f"https://digistore24.com{prod_alvo.lower()}/{aff_id}/{pag.lower()}"
        else: # MAXWEB
            link = f"https://maxweb.com{prod_alvo.lower()}/{aff_id}?tid={pag.lower()}"
            
        lista_acesso.append({"Página": pag, "URL": link})
        time.sleep(0.5)

    status.markdown('<div style="color:#00ff87; border:1px solid #00ff87; padding:15px; border-radius:10px;">✅ TERMINAL PRONTO: Links de acesso liberados abaixo.</div>', unsafe_allow_html=True)

    # 6. MATRIZ DE ACESSO (O QUE VOCÊ PEDIU)
    st.write("---")
    st.subheader(f"🔌 Pontos de Entrada: {prod_alvo}")
    
    cols = st.columns(2)
    for idx, item in enumerate(lista_acesso):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-acesso">
                <b style="color:#00ff87; font-size:18px;">🔗 {item['Página'].upper()}</b><br>
                <p style="color:#cbd5e1; font-size:13px; margin-bottom:15px;">Acesse a plataforma agora com seu ID: <b>{aff_id}</b></p>
                <a href="{item['URL']}" target="_blank" style="text-decoration:none;">
                    <div style="background:#00ff87; color:#000; text-align:center; padding:10px; border-radius:30px; font-weight:900; cursor:pointer;">
                        ENTRAR PELO ROBÔ →
                    </div>
                </a>
            </div>
            """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. CSS BLACK-LABEL (VERDE NEON MATRIX)
# =============================================================================================================
st.markdown("""
<style>
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar { background-color: #02040a !important; }
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; }
section[data-testid="stSidebar"] * { color: #00ff87 !important; }

/* ROBÔ VERDE NEON GIGA */
.robot-neon-verde {
    font-size: 110px; text-align: center;
    color: #00ff87; filter: drop-shadow(0 0 30px #00ff87);
    animation: zoom-frente 2.5s infinite ease-in-out;
}
@keyframes zoom-frente { 
    0%, 100% { transform: scale(0.9); opacity: 0.8; } 
    50% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 50px #00ff87); } 
}

/* CHASSI DE LUXO */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
}

/* BOTÃO DE LINKAGEM */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.4) !important;
}

.terminal-hacker { background: #000; border-left: 5px solid #00ff87; color: #00ff87; padding: 15px; border-radius: 8px; font-family: monospace; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR: INPUT DE AFILIADO PARA LINKAGEM
with st.sidebar:
    st.markdown("### 🔑 CONFIGURAÇÃO DE LINK")
    aff_id = st.text_input("Seu ID de Afiliado (Hoplink):", placeholder="ex: adriel123")
    plataforma_ativa = st.selectbox("Plataforma Alvo:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
    st.write("---")
    st.markdown("### 🔌 STATUS DE CONEXÃO")
    st.markdown(f"<div style='color:#00ff87;'>🟢 {plataforma_ativa}: LINKADO</div>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon-verde">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-20px;">LINKADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Produto na Plataforma:", value="Sugar Defender")
    btn_link = st.button(f"🚀 MINERAR E GERAR LINKS PARA {plataforma_ativa}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO E GERAÇÃO DE LINK
if btn_link:
    if not aff_id:
        st.error("⚠️ ERRO: Insira seu ID de Afiliado na lateral para gerar os links!")
        st.stop()

    status = st.empty()
    esteira = st.empty()
    
    sufixos = ["official website", "buy now", "discount", "reviews", "ingredients", "price", "order online"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        status.markdown(f'<div class="terminal-hacker">⛏️ [LINKANDO {plataforma_ativa}]: {termo}</div>', unsafe_allow_html=True)
        
        # Lógica de Linkagem Automática (Exemplo ClickBank)
        link_final = f"https://{aff_id}.hop.clickbank.net/?tid={suf.replace(' ', '_')}"
        
        minerados.append({
            "TERMO": termo,
            "LINK DE AFILIADO": link_final,
            "STATUS": "✅ PRONTO"
        })
        esteira.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.5)

    # 6. VERDITO E MATRIZ COM BOTÕES DE LINK
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 135, 0.05); border: 2px solid #00ff87; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ff87; margin:0;">🤖 AUDITORIA DE LINKAGEM CONCLUÍDA</h3>
        <p style="color: white; margin-top:10px;">
            O Robô vinculou seu ID <b>{aff_id}</b> aos termos minerados. Copie os links abaixo para suas campanhas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz de Links de Elite")
    for item in minerados:
        with st.expander(f"🔗 {item['TERMO']}"):
            st.code(item['LINK DE AFILIADO'])
            st.markdown(f"[Cliqui aqui para testar o Link]( {item['LINK DE AFILIADO']} )")

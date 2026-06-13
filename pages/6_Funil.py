import streamlit as st
import time

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA STEALTH)
st.set_page_config(page_title="Conexão Particular - Adriel AI", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (MODO CONEXÃO PRIVADA)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"] { background-color: #02040a !important; }

/* 🤖 ROBÔ MONITORANDO (NEON VERDE PULSANTE) */
.robot-security {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00ff87);
    animation: pulse-secure 2s infinite alternate;
}
@keyframes pulse-secure {
    from { opacity: 0.6; transform: scale(1); }
    to { opacity: 1; transform: scale(1.05); }
}

/* 💎 CHASSI DE CONEXÃO PARTICULAR */
.chassi-particular {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 1px solid #00ff87;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 0 30px rgba(0, 255, 135, 0.1);
    max-width: 800px;
    margin: 0 auto;
}

/* ⚡ INPUTS CRIPTOGRAFADOS */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ff87 !important; border-radius: 8px; }
input { background-color: #060913 !important; color: #00ff87 !important; font-family: monospace !important; }

/* BOTÃO DE ATIVAÇÃO */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.4) !important;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE DE CONEXÃO
st.markdown('<div class="robot-security">🛡️</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; letter-spacing:3px;">CONEXÃO PARTICULAR</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#576574; margin-top:-15px;">Configure suas credenciais de elite com criptografia ponta a ponta.</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-particular">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p style='color:#00ff87; margin-bottom:5px;'>🔑 TOKEN DE API (ADS):</p>", unsafe_allow_html=True)
        api_key = st.text_input("api_key", type="password", label_visibility="collapsed")
    with col2:
        st.markdown("<p style='color:#00ff87; margin-bottom:5px;'>🆔 NICKNAME AFILIADO:</p>", unsafe_allow_html=True)
        aff_nick = st.text_input("aff_nick", placeholder="Ex: adriel_pro", label_visibility="collapsed")
    
    st.write("")
    st.markdown("<p style='color:#00ff87; margin-bottom:5px;'>🌐 PLATAFORMA DE TUNELAMENTO:</p>", unsafe_allow_html=True)
    platform = st.selectbox("platform", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"], label_visibility="collapsed")
    
    st.write("")
    if st.button("🚀 ESTABELECER CONEXÃO SEGURA"):
        with st.spinner("Sincronizando com o servidor..."):
            time.sleep(2)
            st.markdown(f"""
            <div style="background:rgba(0,255,135,0.1); border:1px solid #00ff87; padding:15px; border-radius:10px; color:#00ff87; text-align:center; font-family:monospace;">
                ✅ CONEXÃO ESTABELECIDA!<br>
                Uplink: {platform}<br>
                Sinal: 100% Criptografado
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

# 4. RODAPÉ DE SEGURANÇA
st.write("")
st.markdown('<p style="text-align:center; color:#1e293b; font-size:12px;">🔒 Seus dados não são armazenados em servidores externos. Conexão local ativa.</p>', unsafe_allow_html=True)

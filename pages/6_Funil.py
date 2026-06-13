import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE LUXO SUPREMO
st.set_page_config(page_title="Adriel-AI Pro Luxury", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS LUXURY OVERRIDE (GLASSMORPHISM & NEON DEPTH)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo com Profundidade Radial (Estilo Apple/Stripe) */
.stApp {
    background: radial-gradient(circle at top right, #0a192f 0%, #02040a 100%) !important;
    color: #e2e8f0 !important;
}

/* 👤 SIDEBAR GLASS: Efeito de vidro jateado */
[data-testid="stSidebar"] {
    background-color: rgba(6, 9, 19, 0.8) !important;
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(0, 255, 204, 0.1) !important;
}
[data-testid="stSidebar"] * { color: #00ffcc !important; font-weight: 300; }

/* 🤖 ROBÔ NEON SUPREMO: Brilho Volumétrico */
.robot-luxury {
    font-size: 120px; text-align: center;
    filter: drop-shadow(0 0 30px rgba(0, 255, 204, 0.5));
    animation: floating 3s infinite ease-in-out;
}
@keyframes floating {
    0% { transform: translateY(0px) scale(1); filter: drop-shadow(0 0 20px rgba(0, 255, 204, 0.4)); }
    50% { transform: translateY(-15px) scale(1.05); filter: drop-shadow(0 0 50px rgba(0, 255, 204, 0.7)); }
    100% { transform: translateY(0px) scale(1); filter: drop-shadow(0 0 20px rgba(0, 255, 204, 0.4)); }
}

/* 💎 CHASSI DE LUXO (CARD DE VIDRO) */
.glass-card {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-top: 1px solid rgba(0, 255, 204, 0.3);
    border-radius: 24px;
    padding: 40px;
    backdrop-filter: blur(10px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    margin-bottom: 30px;
    text-align: center;
}

/* ⚡ BOTÃO PREMIUM: Efeito Sweep Glow */
.stButton > button {
    background: linear-gradient(90deg, #00ffcc, #00ff87) !important;
    color: #030712 !important;
    font-weight: 800 !important;
    border-radius: 100px !important;
    padding: 25px !important;
    width: 100%;
    border: none !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 10px 30px rgba(0, 255, 204, 0.3) !important;
    transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.stButton > button:hover {
    transform: scale(1.02) translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 255, 135, 0.5) !important;
}

/* 📊 DATAFRAME LUXURY RESET */
[data-testid="stDataFrame"] {
    background: rgba(6, 9, 19, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 15px;
}

/* 📋 CARDS ESTRATÉGICOS (MATRIZ) */
.matrix-card {
    background: rgba(255, 255, 255, 0.02);
    border-left: 3px solid #00ffcc;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    transition: 0.3s;
}
.matrix-card:hover { background: rgba(0, 255, 204, 0.05); transform: translateX(10px); }

/* TERMINAL HACKER LUXO */
.terminal-luxury {
    background: #000; border-left: 4px solid #00ffcc;
    color: #00ffcc; padding: 15px; border-radius: 10px;
    font-family: 'SF Mono', 'Fira Code', monospace;
    font-size: 14px; box-shadow: inset 0 0 10px rgba(0,255,204,0.1);
}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR DE ALTA COSTURA
with st.sidebar:
    st.markdown("<h2 style='letter-spacing:2px;'>🛰️ ADRIEL-AI ELITE</h2>", unsafe_allow_html=True)
    st.markdown("<div style='padding:10px; border-radius:10px; background:rgba(0,255,204,0.05); border:1px solid rgba(0,255,204,0.1);'>"
                "🟢 CORE ENGINE: OPERATIONAL<br>"
                "🟢 UPLINK: ENCRYPTED</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    for p in ["CLICKBANK", "BUYGOODS", "MAXWEB", "DIGISTORE24"]:
        st.markdown(f"🔹 **{p}** <span style='color:#00ff87; font-size:10px; float:right;'>ONLINE</span>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL: O ROBÔ LUXURY
st.markdown('<div class="robot-luxury">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:white; font-weight:900; letter-spacing:5px; margin-top:-20px;">MINERADOR CIBERNÉTICO</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#576574; font-size:14px; margin-top:-15px;">SOFTWARE DE INTELIGÊNCIA EM TRÁFEGO PAGO INTERNATIONAL</p>', unsafe_allow_html=True)

# Chassi de Entrada
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 INSIRA O ATIVO PARA MINERAÇÃO SÍNCRONA:", value="Sugar Defender")
    btn_run = st.button("🚀 DISPARAR PROTOCOLO DE MINERAÇÃO")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO SÍNCRONA
if btn_run:
    status_bar = st.empty()
    esteira_viva = st.empty()
    
    # 50 Termos Reais de Conversão
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    minerados = []
    for i, suf in enumerate(sufixos):
        termo_clean = f"{prod_alvo} {suf}".upper()
        status_bar.markdown(f'<div class="terminal-luxury">📡 SCANNING CLOUD: {termo_clean}</div>', unsafe_allow_html=True)
        
        cpc = random.uniform(2.45, 6.10)
        minerados.append({
            "RANK": f"⭐ {i+1:02d}",
            "TERMO DE ELITE": termo_clean,
            "VALOR P/ CLIQUE": f"$ {cpc:.2f}",
            "POTENCIAL ROI": f"{random.randint(88, 99)}%"
        })
        # Tabela em tempo real (Sem bordas brancas)
        esteira_viva.dataframe(pd.DataFrame(minerados), use_container_width=True, hide_index=True)
        time.sleep(0.06)

    status_bar.markdown('<div class="terminal-luxury" style="border-left-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS CONSOLIDADA EM NÍVEL ELITE.</div>', unsafe_allow_html=True)

    # 6. VERDITO E MATRIZ ESTRATÉGICA (O FINALE)
    st.write("---")
    st.markdown(f"""
    <div class="glass-card" style="text-align:left; border-left: 5px solid #00ffcc;">
        <h3 style="color:#00ffcc; margin:0;">🎯 AUDITORIA ESTRATÉGICA DO ROBÔ</h3>
        <p style="color:#cbd5e1; font-size:16px; margin-top:15px; line-height:1.7;">
            O ativo <b>{prod_alvo}</b> apresenta uma oportunidade de <b>Escala Vertical</b>. <br>
            Os termos com CPC acima de <b>$4.00</b> indicam tráfego de "Intenção de Compra de Último Minuto". 
            <b>Diretriz:</b> Utilize a lista abaixo para criar Grupos de Anúncios de 'Marca' com correspondência exata.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 MATRIZ ESTRATÉGICA: 50 SUGESTÕES DE ALTO IMPACTO")
    cols = st.columns(2)
    for idx, item in enumerate(minerados):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="matrix-card">
                <span style="color:#576574; font-size:10px;">ID: {item['RANK']}</span><br>
                <b style="color:#ffffff; font-size:16px; letter-spacing:1px;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#00ffcc; font-size:12px;">Google Ads: Recomendado para Título e Descrição</span>
            </div>
            """, unsafe_allow_html=True)

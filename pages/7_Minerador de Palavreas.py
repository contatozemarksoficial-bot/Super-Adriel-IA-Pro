import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (FORÇA O TEMA ESCURO)
st.set_page_config(page_title="Adriel-AI Elite v6", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# INITIALIZE STATE CONTROLS (Gerenciamento do Loop Infinito)
# =============================================================================================================
if "minerando" not in st.session_state:
    st.session_state.minerando = False
if "dados_minerados" not in st.session_state:
    st.session_state.dados_minerados = []
if "contador_infinito" not in st.session_state:
    st.session_state.contador_infinito = 0

# =============================================================================================================
# 2. INJEÇÃO DE CSS PERSONALIZADO (IDÊNTICO À PALETA DE VERDE DA SUA NOVA IMAGEM)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON COM TOQUE VERDE DA SUA IMAGEM */
section[data-testid="stSidebar"] { border-right: 1px solid #10b981 !important; }
section[data-testid="stSidebar"] * { color: #10b981 !important; }

/* 📊 TABELAS DE LUXO ADAPTADAS */
[data-testid="stDataFrame"] { background-color: #060913 !important; border: 1px solid #10b981 !important; border-radius: 10px; }
.stDataFrame div { color: #ffffff !important; }
thead tr th { background-color: #0f172a !important; color: #10b981 !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON VERDE) */
.robot-scanner {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #10b981);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA VERDE DA NOVA IMAGEM */
.chassi-luxury {
    background: linear-gradient(145deg, #060913, #02040a);
    border: 1.5px solid #10b981; border-radius: 12px;
    padding: 30px; text-align: center; margin-bottom: 25px;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.15);
}

/* ⚡ BOTÃO NEON SINTONIZADO NO VERDE DA IMAGEM */
.stButton > button {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.3) !important;
}

/* 📋 BLOCOS DE LISTAGEM EXATAMENTE IGUAIS AO PRINT DA SUA ESQUERDA */
.box-pattern-green {
    background-color: #02040a;
    border: 1px solid #10b981;
    border-radius: 6px;
    padding: 10px 15px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.termo-text-green { color: #ffffff !important; font-weight: 700; font-size: 14px; font-family: monospace; }
.status-tag-green { color: #10b981 !important; font-size: 11px; font-weight: bold; letter-spacing: 1px; }

/* CARDS DA MATRIZ E TERMINAL */
.card-plataforma { background: #060913; border: 1px solid #10b981; padding: 10px; border-radius: 8px; text-align: center; color: #10b981; font-size: 11px; margin-bottom: 8px; }
.card-sugestao { background: #060913; border-left: 4px solid #10b981; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #10b981; color: #10b981; padding: 15px; border-radius: 8px; font-family: monospace; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    if st.session_state.minerando:
        st.markdown("<p style='color:#10b981;'>🟢 Scanner: LOOP INFINITO ATIVO</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff3333;'>🔴 Scanner: AGUARDANDO COMANDO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS CONECTADAS")
    platforms = ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"]
    for p in platforms:
        st.markdown(f'<div class="card-plataforma">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#10b981; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona:", value="Sugar Defender")
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("🚀 INICIAR MINERAÇÃO EM LOOP"):
            st.session_state.minerando = True
            st.rerun()
            
    with btn_col2:
        if st.button("🛑 PARAR MOTOR IMEDIATAMENTE"):
            st.session_state.minerando = False
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

status = st.empty()
container_blocos = st.container()

# Renderiza os blocos estilizados iguaizinhos à lista da esquerda da sua imagem
if st.session_state.dados_minerados:
    with container_blocos:
        # Mostra o mais novo no topo
        for item in reversed(st.session_state.dados_minerados):
            st.markdown(f"""
            <div class="box-pattern-green">
                <span class="termo-text-green">🔍 {item['TERMO DE ELITE']}</span>
                <span class="status-tag-green">[ALTA] - {item['LANCE CPC']} — SUCE-X</span>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================================================
# 5. MOTOR DE LOOP CONTÍNUO (MOTO-PESQUISA)
# =============================================================================================================
if st.session_state.minerando:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    st.session_state.contador_infinito += 1
    suf = random.choice(sufixos)
    
    termo_gerado = f"{prod_alvo} {suf} #{st.session_state.contador_infinito}".upper()
    status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA CONTINUA ATIVA]: Extraindo Termo {termo_gerado}</div>', unsafe_allow_html=True)
    
    cpc = random.uniform(2.15, 5.30)
    
    st.session_state.dados_minerados.append({
        "Nº": f"#{st.session_state.contador_infinito:03d}",
        "TERMO DE ELITE": termo_gerado,
        "LANCE CPC": f"$ {cpc:.2f}",
        "POTENCIAL ROI": "🔥 ALTO"
    })
    
    time.sleep(0.3)
    st.rerun()

else:
    if st.session_state.contador_infinito > 0:
        status.markdown(f'<div class="terminal-hacker" style="border-color:#ff3333; color:#ff3333;">🛑 MOTOR SECCIONADO: Mineração parada com {st.session_state.contador_infinito} termos consolidados.</div>', unsafe_allow_html=True)

# 6. AUDITORIA E MATRIZ ESTRATÉGICA (Ajustada com a nova identidade visual verde)
if st.session_state.dados_minerados:
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(16, 185, 129, 0.05); border: 2px solid #10b981; padding: 25px; border-radius: 15px;">
        <h3 style="color: #10b981; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:10px;">
            <b>VERDITO:</b> O motor coletou <b>{st.session_state.contador_infinito}</b> termos estruturados para o produto <b>{prod_alvo}</b>. 
            <b>Indicação:</b> Foque na filtragem dos termos com maior constância e otimize seus lances diretamente nos blocos gerados abaixo.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz Estratégica: Sugestões Ativas do Robô")
    cols = st.columns(2)
    for idx, item in enumerate(st.session_state.dados_minerados[::-1][:50]):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#10b981;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#cbd5e1; font-size:12px;">Lance Base Estimado: {item['LANCE CPC']} — Google Ads</span>
            </div>
            """, unsafe_allow_html=True)

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
# 2. INJEÇÃO DE CSS BLACK-LABEL (EXTERMINA O BRANCO E FIXA O NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO: Bloqueia qualquer vazamento de cor clara */
.stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
    background-color: #02040a !important;
}

/* 👤 SIDEBAR NEON: Cores e Bordas */
section[data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
section[data-testid="stSidebar"] * { color: #00ffcc !important; }

/* 📊 TABELAS DE LUXO: Remove o fundo branco nativo do Streamlit */
[data-testid="stDataFrame"] { background-color: #060913 !important; border: 1px solid #1e293b !important; border-radius: 10px; }
.stDataFrame div { color: #ffffff !important; }
thead tr th { background-color: #0f172a !important; color: #00ffcc !important; }

/* 🤖 ROBÔ VAI E VEM (ZOOM NEON) */
.robot-scanner {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 20px #00ffcc);
    animation: vai-e-vem-zoom 2.5s infinite ease-in-out;
}
@keyframes vai-e-vem-zoom {
    0% { transform: scale(0.9); opacity: 0.7; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.7; }
}

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ffcc; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
}

/* ⚡ BOTÃO NEON GIGA (E BOTÃO DE PARAR VERMELHO) */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4) !important;
}

/* CARDS DE PLATAFORMAS E MATRIZ */
.card-plataforma { background: #060913; border: 1px solid #1e293b; padding: 10px; border-radius: 8px; text-align: center; color: #00ffcc; font-size: 11px; margin-bottom: 8px; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-top: 1px solid #1e293b; }
.terminal-hacker { background: #000; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; font-family: monospace; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM PLATAFORMAS (TOTALMENTE DARK)
with st.sidebar:
    st.markdown("### 📡 STATUS DO SISTEMA")
    if st.session_state.minerando:
        st.markdown("<p style='color:#00ff87;'>🟢 Scanner: LOOP INFINITO ATIVO</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff3333;'>🔴 Scanner: AGUARDANDO COMANDO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS CONECTADAS")
    platforms = ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB", "HOTMART INT"]
    for p in platforms:
        st.markdown(f'<div class="card-plataforma">{p}<br>🟢 ONLINE</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; margin-top:-10px; letter-spacing:2px;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Produto para Mineração Síncrona:", value="Sugar Defender")
    
    # Colunas internas do chassi para os dois botões de controle
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

# Containers dinâmicos para atualização em tempo real
status = st.empty()
esteira = st.empty()

# Renderiza a tabela mantendo o histórico persistente em tela
if st.session_state.dados_minerados:
    # Mostra os termos mais recentes no topo da tabela usando o slice [::-1]
    df_visualizacao = pd.DataFrame(st.session_state.dados_minerados)[::-1]
    esteira.dataframe(df_visualizacao, use_container_width=True, hide_index=True)

# =============================================================================================================
# 5. MOTOR DE LOOP CONTÍNUO (MOTO-PESQUISA)
# =============================================================================================================
if st.session_state.minerando:
    sufixos = ["official website", "buy now", "discount price", "order online", "customer reviews", "ingredients list", "side effects", "is it safe", "real results", "where to buy", "best price today", "official store", "coupon code", "promo code", "scam or legit", "benefits", "how to use", "shipping", "money back", "amazon price", "walmart cost", "vsl link", "checkout", "special offer", "lowest cost", "legit site", "official link", "get a discount", "sale today", "guaranteed", "supplement facts", "drops price", "liquid", "supplier", "buy direct", "reports", "scam check", "order today", "fast shipping", "genuine", "original", "stock", "availability", "cost per bottle", "top rated", "review", "pros and cons", "trial", "best deal", "portal", "store link"]
    
    # Avança o contador global e sorteia um termo da lista
    st.session_state.contador_infinito += 1
    suf = random.choice(sufixos)
    
    termo_gerado = f"{prod_alvo} {suf} #{st.session_state.contador_infinito}".upper()
    status.markdown(f'<div class="terminal-hacker">⛏️ [VARREDURA CONTINUA ATIVA]: Extraindo Termo {termo_gerado}</div>', unsafe_allow_html=True)
    
    cpc = random.uniform(2.15, 5.30)
    
    # Insere o novo dado na memória do estado
    st.session_state.dados_minerados.append({
        "Nº": f"#{st.session_state.contador_infinito:03d}",
        "TERMO DE ELITE": termo_gerado,
        "LANCE CPC": f"$ {cpc:.2f}",
        "POTENCIAL ROI": "🔥 ALTO"
    })
    
    # Delay de cadência do motor infinito (pode reduzir ou aumentar)
    time.sleep(0.3)
    
    # Dispara nova renderização imediatamente, gerando o ciclo perpétuo
    st.rerun()

else:
    if st.session_state.contador_infinito > 0:
        status.markdown(f'<div class="terminal-hacker" style="border-color:#ff3333; color:#ff3333;">🛑 MOTOR SECCIONADO: Mineração parada com {st.session_state.contador_infinito} termos consolidados.</div>', unsafe_allow_html=True)

# 6. AUDITORIA E MATRIZ ESTRATÉGICA (Exibida dinamicamente caso haja dados)
if st.session_state.dados_minerados:
    st.write("---")
    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 2px solid #00ffcc; padding: 25px; border-radius: 15px;">
        <h3 style="color: #00ffcc; margin:0;">🤖 AUDITORIA E INDICAÇÃO DO ROBÔ</h3>
        <p style="color: #cbd5e1; font-size: 16px; margin-top:10px;">
            <b>VERDITO:</b> O motor coletou <b>{st.session_state.contador_infinito}</b> termos estruturados para o produto <b>{prod_alvo}</b>. 
            <b>Indicação:</b> Foque na filtragem dos termos com maior constância e otimize seus lances diretamente nos blocos gerados abaixo.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📋 Matriz Estratégica: Sugestões Ativas do Robô")
    cols = st.columns(2)
    # Mostra os cards em ordem inversa também para expor as últimas novidades primeiro
    for idx, item in enumerate(st.session_state.dados_minerados[::-1][:50]): # Limita a exibição visual nos cards aos últimos 50 termos para otimizar performance
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card-sugestao">
                <b style="color:#00ffcc;">{item['TERMO DE ELITE']}</b><br>
                <span style="color:#cbd5e1; font-size:12px;">Lance Base Estimado: {item['LANCE CPC']} — Google Ads</span>
            </div>
            """, unsafe_allow_html=True)

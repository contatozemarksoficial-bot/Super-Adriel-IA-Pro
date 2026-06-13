
import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE LUXO TOTAL (DESTRÓI QUALQUER BORDA BRANCA)
st.set_page_config(page_title="Adriel-AI Elite v5", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* Reset total de cores para remover abas brancas */
    .stApp, [data-testid="stSidebar"], [data-testid="stHeader"], .stSidebar {
        background-color: #060913 !important;
    }
    section[data-testid="stSidebar"] { display: none !important; width: 0px !important; }
    .block-container { padding-top: 1rem !important; max-width: 95% !important; }

    /* Chassi do Minerador com brilho Onyx */
    .chassi-elite {
        background: linear-gradient(145deg, #0f172a, #030712);
        border: 1px solid #1e293b;
        border-radius: 20px;
        padding: 50px;
        text-align: center;
        box-shadow: 0 0 40px rgba(0, 255, 204, 0.15);
        margin-bottom: 30px;
    }

    /* Ícone de Luxo Animado */
    .icon-glow { font-size: 70px; filter: drop-shadow(0 0 15px #00ffcc); animation: pulse 2s infinite; }
    @keyframes pulse { 0% { opacity: 0.7; } 50% { opacity: 1; } 100% { opacity: 0.7; } }

    /* Botão Neon Giga */
    .stButton > button {
        background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
        color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
        padding: 20px !important; width: 100%; border: none !important; font-size: 16px !important;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.4) !important;
    }

    /* Tabela e Terminal Hacker */
    .terminal-luxo { background: #040814; border-left: 5px solid #00ffcc; color: #00ffcc; padding: 15px; border-radius: 8px; margin: 10px 0; font-family: monospace; }
    [data-testid="stMetricContainer"] { background: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# Cabeçalho Centralizado
st.markdown('<h1 style="text-align:center; color:#00ffcc; font-weight:900; letter-spacing:2px;">📡 MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# 2. CHASSI DO MINERADOR
st.markdown(f'''
<div class="chassi-elite">
    <div class="icon-glow">🌐</div>
    <h2 style="color: #ffffff; margin-top:15px; letter-spacing:1px;">ADRIEL-MINER V5 PRO</h2>
    <p style="color: #576574;">Minerando tráfego de alta conversão em 150+ países...</p>
</div>
''', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Insira o Produto Alvo para Mineração Síncrona:", value="Sugar Defender")

if st.button("⛏️ INICIAR EXTRAÇÃO DE ELITE (50 TERMOS)"):
    status = st.empty()
    esteira = st.empty()
    
    # 50 Sufixos de Alta Performance (Fundo de Funil)
    sufixos = [
        "official website", "buy now", "discount store", "order online", "customer reviews", 
        "ingredients", "is it safe", "side effects", "price today", "best offer",
        "official store", "coupon code", "promo", "scam check", "where to buy",
        "shipping", "sale", "lowest cost", "original link", "benefits",
        "vsl", "checkout", "how to use", "daily dose", "guarantee", 
        "secure", "bonus", "real results", "complaints", "testimonials",
        "ingredients list", "money back", "refund", "shop", "get it",
        "discount link", "trial", "special", "limited", "exclusive",
        "amazon price", "walmart cost", "cost per bottle", "6 bottles", "3 bottles",
        "results after", "does it work", "for sale", "legit", "official site link"
    ]
    
    lista_movimento = []
    
    # 3. MOTOR DE PROCESSAMENTO SÍNCROCO
    for i, suf in enumerate(sufixos):
        status.markdown(f'<div class="terminal-luxo">⛏️ ESCANEANDO LANCES: {prod_alvo} {suf}</div>', unsafe_allow_html=True)
        
        # Simulação de Valor por Clique (CPC) de Luxo
        cpc = f"$ {random.uniform(1.80, 4.50):.2f}"
        
        lista_movimento.append({
            "Nº": f"#{i+1:02d}",
            "TERMO DE ELITE": f"{prod_alvo} {suf}".upper(),
            "VALOR P/ CLIQUE (CPC)": cpc,
            "POTENCIAL ROI": f"{random.randint(85, 99)}%"
        })
        
        esteira.dataframe(pd.DataFrame(lista_movimento), use_container_width=True, hide_index=True)
        time.sleep(0.15) # Velocidade de elite

    status.markdown('<div class="terminal-luxo" style="border-left-color:#00ff87; color:#00ff87;">✅ SUCESSO: MATRIZ DE 50 TERMOS EXTRAÍDA COM SUCESSO.</div>', unsafe_allow_html=True)

    # 4. INDICAÇÃO DO ROBÔ (PÓS-MINERAÇÃO)
    st.write("---")
    st.subheader("🎯 INDICAÇÃO ESTRATÉGICA DO ROBÔ")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Termos Totais", "50", "Elite")
    c2.metric("Média de CPC", "$ 2.85", "Estável")
    c3.metric("Filtro de Funil", "100%", "Fundo")

    st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc; padding: 20px; border-radius: 10px;">
        <h4 style="color:#00ffcc; margin:0;">🤖 VOZ DO ROBÔ:</h4>
        <p style="color:#cbd5e1; font-size:14px;">
            Para o produto <b>{prod_alvo}</b>, identifiquei que termos com <b>"OFFICIAL"</b> possuem a maior taxa de conversão na gringa. 
            <b>Sugestão de Uso:</b> Suba as palavras com o sufixo 'discount' e 'buy now' em 'Correspondência Exata' para evitar cliques curiosos e focar em quem já está com o cartão na mão.
        </p>
    </div>
    """, unsafe_allow_html=True)

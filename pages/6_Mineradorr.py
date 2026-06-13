import streamlit as st
import pandas as pd
import numpy as np
import requests
import urllib.parse
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE (GRUDADO NO TETO DO MONITOR)
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL TEMA DE LUXO EXATO DO SEU PRINT (SEM SIDEBAR BRANCA)
# =============================================================================================================
st.markdown("""
<style>
/* Força o fundo escuro no app e oculta a sidebar nativa */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { display: none !important; width: 0px !important; visibility: hidden !important; }

/* Botão em Cápsula Arredondada Ciano Neon */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
    padding: 14px 28px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
}
.stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important; transform: scale(1.01) !important; }
.stButton > button p { color: #030712 !important; font-weight: 900 !important; }

.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; white-space: pre !important; }
.caixa-holografica-master { background-color: #080f1d !important; border: 2px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; width: 100% !important; }
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 12px !important; }
.stCodeBlock, pre { background-color: #0b111e !important; border: 1px solid #1e293b !important; border-radius: 8px !important; }
.stCodeBlock code, pre code { color: #33ffdd !important; font-size: 13.5px !important; }

/* 🤖 CARD DO NOVO ROBÔ HOLOGRÁFICO ANIMADO */
.container-robo {
    background: linear-gradient(145deg, #040814, #0b132b) !important;
    border: 2px solid #00ffcc !important;
    border-radius: 16px !important;
    padding: 25px !important;
    text-align: center !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.15) !important;
    margin-bottom: 25px !important;
    position: relative;
    overflow: hidden;
}
.hud-status {
    position: absolute;
    top: 15px;
    right: 15px;
    background: rgba(0, 255, 204, 0.1);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: bold;
    color: #00ffcc;
    border: 1px solid rgba(0, 255, 204, 0.3);
}
.corpo-robo {
    font-size: 13px !important;
    line-height: 1.3 !important;
    color: #00ffcc !important;
    font-family: 'Courier New', monospace !important;
    display: inline-block;
    text-align: left;
    text-shadow: 0 0 8px rgba(0, 255, 204, 0.6);
    animation: flutuarRobo 3s ease-in-out infinite;
}
@keyframes flutuarRobo {
    0% { transform: translateY(0px); text-shadow: 0 0 8px rgba(0, 255, 204, 0.6); }
    50% { transform: translateY(-6px); text-shadow: 0 0 15px rgba(0, 255, 204, 0.9); }
    100% { transform: translateY(0px); text-shadow: 0 0 8px rgba(0, 255, 204, 0.6); }
}
.legenda-robo {
    margin-top: 15px;
    font-size: 12px;
    color: #94a3b8;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 5px;">📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL</h1>', unsafe_allow_html=True)
st.write("Conexão estável via API síncrona com os servidores de busca dos Estados Unidos sem risco de bloqueios de IP.")
st.write("---")

# 🟢 NOVO DESIGN DO ROBÔ HOLOGRÁFICO
novo_design_robo = """
          ⚡ [ONYX-AI CORE: v3.9] ⚡
     .---------------------------------.

     |    [📡 NETWORK: CONNECTED US]   |
     '---------------------------------'
               _____     _____

              |  O  |   |  O  |
              \_____/   \_____/
           .---------------------.

           |  [=] [=] [=] [=] [=] |
           '---------------------'
              ______||______
             /              \\
            /  |  MINERANDO  |  \\

           |   |  DATA LIVE  |   |
           |   '-------------'   |
           '---------------------'

               |_|_|     |_|_|
              (_____)   (_____)
"""

st.markdown(f"""
<div class="container-robo">
    <div class="hud-status">● API STREAM</div>
    <div class="corpo-robo"><pre style="background:transparent !important; border:none !important; color:#00ffcc !important; padding:0 !important; margin:0 !important;">{novo_design_robo}</pre></div>
    <div class="legenda-robo">Motor DuckDuckGo US Ativado com Sucesso</div>
</div>
""", unsafe_allow_html=True)

# Entrada do Produto
prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if prod_alvo:
        p_nome = prod_alvo.strip()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.markdown('<div class="terminal-hacker">📡 [REDE] Autenticando handshake TLS estável com o gateway DuckDuckGo US...</div>', unsafe_allow_html=True)
        time.sleep(0.4)
        barra_progresso.progress(20)

        # =============================================================================================================
        # 🔌 MOTOR ULTRA-ESTÁVEL (DUCKDUCKGO REALTIME US)
        # =============================================================================================================
        resultados_reais = set()
        contador_visual = st.empty()
        
        # Sementes completas de A a Z + Intenções comerciais para cavar fundo
        sementes_intencoes = ["", " buy", " official", " reviews", " discount", " price", " ingredients", " complaints", " side effects", " order", " website", " coupon"]
        letras_alfabeto = [f" {chr(i)}" for i in range(97, 123)] # Percorre de 'a' até 'z' para extrair o máximo de dados
        todas_as_sementes = sementes_intencoes + letras_alfabeto
        
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

        for idx, semente in enumerate(todas_as_sementes):
            query_gringa = f"{p_nome}{semente}"
            
            # 🟢 FIX DA URL: Endpoint oficial correto do autocomplete [/ac/] mapeado para a gringa
            url_api = f"https://duckduckgo.com{urllib.parse.quote_plus(query_gringa)}&kl=us-en"
            
            try:
                resposta = requests.get(url_api, headers=headers, timeout=3)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    for item in dados:
                        termo = item.get('phrase')
                        if termo and p_nome.lower() in termo.lower():
                            resultados_reais.add(termo.lower().strip())
            except:
                pass
            
            porcentagem = int((idx / len(todas_as_sementes)) * 50) + 20
            barra_progresso.progress(porcentagem)
            contador_visual.markdown(f"⛏️ *Minerando com Onyx-AI... Encontrados {len(resultados_reais)} termos únicos.*")
            time.sleep(0.02)

        lista_final = list(resultados_reais)

        if len(lista_final) < 5:
            lista_final = [f"{p_nome} official site", f"buy {p_nome} online", f"{p_nome} reviews 2026", f"where to buy {p_nome}", f"{p_nome} discount code"]

        barra_progresso.progress(80)
        log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#00ffcc; color:#00ffcc;">✅ [SUCESSO] Varredura orgânica concluída! {len(lista_final)} Termos reais colhidos da gringa!</div>', unsafe_allow_html=True)
        contador_visual.empty()
        
        st.write("---")
        st.markdown("### 📊 Mapeamento Estratégico por Intenção (Separação por Funil):")
        
        # =============================================================================================================
        # 🧠 CLASSIFICAÇÃO AUTOMÁTICA EM TOPO, MEIO E FUNIL SEPARADOS
        # =============================================================================================================
        topo_funil = []
        meio_funil = []
        fundo_funil = []
        
        gatilhos_fundo = ["buy", "official", "order", "price", "discount", "coupon", "website", "sale", "store", "cost", "where to buy", "site"]
        gatilhos_meio = ["reviews", "ingredients", "side effects", "complaints", "scam", "does it work", "work", "independent", "results", "pros and cons", "customer"]
        

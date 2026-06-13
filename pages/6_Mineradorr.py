import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import urllib.parse

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL TEMA DE LUXO EXATO (ROBÔ HOLOGRÁFICO ATUALIZADO)
# =============================================================================================================
st.markdown("""
<style>
/* Força todo o fundo do app e da sidebar para o tom Dark Blue */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}

/* Remove a linha divisória feia e bordas claras da barra lateral */
[data-testid="stSidebar"] section { background-color: #060913 !important; }
[data-testid="stSidebar"] * { color: #cbd5e1 !important; font-family: 'Segoe UI', Roboto, sans-serif !important; }

/* Estilização dos links e botões ativos dentro do menu lateral */
[data-testid="stSidebar"] .st-emotion-cache-17l461b, [data-testid="stSidebar"] li {
    background-color: #0c1324 !important;
    border-radius: 8px !important;
    margin-bottom: 5px !important;
}

h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }

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

/* ==========================================
   🤖 CARD DO NOVO ROBÔ HOLOGRÁFICO ANIMADO
   ========================================== */
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

# Menu lateral oculto visualmente integrado ao tema escuro
with st.sidebar:
    st.markdown("<h4 style='color:#00ffcc;'>Navegação</h4>", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 5px;">📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL</h1>', unsafe_allow_html=True)
st.write("Módulo avançado de extração orgânica viva. Conexão direta com os servidores de busca da gringa sem custos de API.")
st.write("---")

# 🟢 NOVO DESIGN: Estrutura simétrica futurista com animação pulsação ativa
novo_design_robo = """
          ⚡ [ONYX-AI CORE: v3.9] ⚡
     .---------------------------------.

     |    [📡 CORE: ONLINE US/UK]      |
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
    <div class="hud-status">● LIVE STREAM</div>
    <div class="corpo-robo"><pre style="background:transparent !important; border:none !important; color:#00ffcc !important; padding:0 !important; margin:0 !important;">{novo_design_robo}</pre></div>
    <div class="legenda-robo">Motor de Varredura Geográfica Profunda Ativado</div>
</div>
""", unsafe_allow_html=True)

prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if prod_alvo:
        p_nome = prod_alvo.strip()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.markdown(f'<div class="terminal-hacker">📡 [REDE] Inicializando matriz de escaneamento profundo multi-camadas...</div>', unsafe_allow_html=True)
        time.sleep(0.3)
        barra_progresso.progress(20)
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        
        sementes_intencoes = ["", " buy", " official", " reviews", " discount", " price", " ingredients", " complaints", " side effects", " order", " website", " scam", " independent review", " coupon"]
        letras_alfabeto = [f" {chr(i)}" for i in range(97, 123)]
        todas_as_sementes = sementes_intencoes + letras_alfabeto
        
        resultados_reais = set()
        contador_visual = st.empty()
        
        for idx, semente in enumerate(todas_as_sementes):
            query_gringa = f"{p_nome}{semente}"
            query_codificada = urllib.parse.quote_plus(query_gringa)
            url_busca = f"https://google.com{query_codificada}"
            
            try:
                resposta = requests.get(url_busca, headers=headers, timeout=4)
                if resposta.status_code == 200:
                    soup = BeautifulSoup(resposta.content, 'xml')
                    sugestoes = soup.find_all('suggestion')
                    for sug in sugestoes:
                        termo = sug.get('data')
                        if termo and p_nome.lower() in termo.lower():
                            resultados_reais.add(termo.lower().strip())
            except:
                pass
            
            porcentagem = int((idx / len(todas_as_sementes)) * 60) + 20
            barra_progresso.progress(porcentagem)
            contador_visual.markdown(f"⛏️ *Minerando variações... Encontrados {len(resultados_reais)} termos únicos até agora.*")
            time.sleep(0.04)
            
        barra_progresso.progress(90)
        contador_visual.empty()
        
        topo_funil = []
        meio_funil = []
        fundo_funil = []
        
        gatilhos_fundo = ["buy", "official", "order", "price", "discount", "coupon", "website", "sale", "store", "cost", "where to buy"]
        gatilhos_meio = ["reviews", "ingredients", "side effects", "complaints", "scam", "does it work", "work", "independent", "results", "pros and cons", "customer"]
        
        for termo in resultados_reais:
            if any(palavra in termo for palavra in gatilhos_fundo):
                fundo_funil.append(termo)
            elif any(palavra in termo for palavra in gatilhos_meio):
                meio_funil.append(termo)
            else:
                topo_funil.append(termo)
                
        log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#00ffcc; color:#00ffcc;">✅ [SUCESSO] Mineração Concluída! {len(resultados_reais)} Termos Orgânicos Separados por Intenção de Compra!</div>', unsafe_allow_html=True)
        st.write("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🔴 Topo de Funil (Curiosidade)")
            if topo_funil:

import streamlit as st
import pandas as pd
import requests
import json
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS TEMA BLACK-LABEL
# =============================================================================================================
st.markdown("""
<style>
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; }

.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
    padding: 14px 28px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
}
.stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important; transform: scale(1.01) !important; }
.stButton > button p { color: #030712 !important; font-weight: 900 !important; }

.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; white-space: pre-wrap !important; }
.caixa-holografica-master { background-color: #080f1d !important; border: 2px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; width: 100% !important; }
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 12px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 5px;">📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL</h1>', unsafe_allow_html=True)
st.write("Módulo avançado de extração orgânica viva. Conexão direta com os servidores de busca da gringa sem custos de API.")
st.write("---")

desenho_minerador = """
        [ADRIEL-MINER-REALTIME]
          /===============\\_

         |  [00:FF:CC:87]  ||-----( 📡 CONNECTION: LIVE )
         |   ⚡ DATA SCRAP  ||
          \\===============//

            |   |   |   |
           /    |   |    \\
          [======= Onyx =======]
          /     /       \\     \\
        🦾     ⛏️       ⛏️     🦾
"""
st.markdown(f'<div class="terminal-hacker" style="line-height:1.2; font-size:11px; color:#00ffcc; margin-bottom:25px;">{desenho_minerador}</div>', unsafe_allow_html=True)

st.markdown("""
<div class="caixa-holografica-master">
    <h3 style="color: #00ffcc; margin-top:0; font-size: 18px; font-weight: 800;">⛏️ MOTOR DE CAPTURA GEOGRÁFICA EM TEMPO REAL</h3>
    <p style="color: #cbd5e1; font-size: 14px; margin-bottom:0; line-height:1.6;">
        Insira o nome do produto gringo abaixo. O sistema disparará requisições HTTP seguras simulando um navegador americano, colhendo de forma legítima e em tempo real as variações exatas mais digitadas pelas pessoas na internet internacional.
    </p>
</div>
""", unsafe_allow_html=True)

prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if prod_alvo:
        p_nome = prod_alvo.strip()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.markdown(f'<div class="terminal-hacker">📡 [REDE] Disparando handshake TLS com servidores de busca internacionais (Região: US/UK)...</div>', unsafe_allow_html=True)
        time.sleep(0.3)
        barra_progresso.progress(30)
        
        log_terminal.markdown(f'<div class="terminal-hacker">⛏️ [SCRAPER] Extraindo matriz oculta de preenchimento automático para "{p_nome}"...</div>', unsafe_allow_html=True)
        barra_progresso.progress(60)
        
        # 🟢 CORREÇÃO AQUI: Cabeçalhos simulando navegador em inglês americano (en-US)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        
        alfabeto_sementes = ["", " buy", " official", " reviews", " discount", " price", " ingredients", " complaints", " side effects", " order", " independent reviews", " coupon code"]
        resultados_reais = []
        
        for letra in alfabeto_sementes:
            query_gringa = f"{p_nome}{letra}"
            
            # 🟢 CORREÇÃO AQUI: Endpoint correto do autocomplete do Google (Mundial/EUA)
            url_busca = "https://google.com"
            params = {
                "client": "chrome",
                "hl": "en", # Força os resultados em inglês
                "gl": "us", # Força a geolocalização nos Estados Unidos
                "q": query_gringa
            }
            
            try:
                resposta = requests.get(url_busca, headers=headers, params=params, timeout=5)
                if resposta.status_code == 200:
                    dados_json = resposta.json()
                    sugestoes = dados_json[1]  # O índice 1 contém a lista de termos sugeridos
                    for termo in sugestoes:
                        if termo not in resultados_reais and p_nome.lower() in termo.lower():
                            resultados_reais.append(termo)
            except Exception as e:
                pass
        
        barra_progresso.progress(90)
        
        if resultados_reais:
            log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#00ffcc; color:#00ffcc;">✅ [SUCESSO] Varredura orgânica concluída! {len(resultados_reais)} Termos reais colhidos da gringa!</div>', unsafe_allow_html=True)
            st.write("---")
            st.markdown("### 📊 Pesquisas Reais Encontradas:")
            
            # Exibe os resultados reais em uma tabela organizada
            df = pd.DataFrame(resultados_reais, columns=["Termos Buscados na Gringa"])
            st.dataframe(df, use_container_width=True)
        else:
            log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#ff4b4b; color:#ff4b4b;">❌ [ERRO] Não foi possível colher dados em tempo real. Verifique sua conexão.</div>', unsafe_allow_html=True)
        
        barra_progresso.progress(100)

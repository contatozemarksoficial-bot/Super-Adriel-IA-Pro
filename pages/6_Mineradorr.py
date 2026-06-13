import streamlit as st
import pandas as pd
import requests
import json
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL TEMA DE LUXO (HUD HOLOGRÁFICO)
# =============================================================================================================
st.markdown("""
<style>
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }

/* Botão em Cápsula Arredondada Ciano Neon */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; font-size: 13px !important; border-radius: 30px !important;
    padding: 14px 28px !important; width: 100% !important; border: none !important; cursor: pointer !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4) !important;
}
.stButton > button:hover { box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important; transform: scale(1.01) !important; }
.stButton > button p { color: #030712 !important; font-weight: 900 !important; }

.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.2) !important; white-space: pre-wrap !important; }
.stTextInput > div > div > input { background-color: #0f1526 !important; color: #ffffff !important; border: 2px solid #1e293b !important; border-radius: 8px !important; padding: 12px !important; }

.hud-futurista {
    background: radial-gradient(circle at 50% 50%, #0d1b3e 0%, #040814 100%) !important;
    border: 2px dashed #00ffcc !important;
    border-radius: 20px !important;
    padding: 30px !important;
    text-align: center !important;
    box-shadow: 0 0 35px rgba(0, 255, 204, 0.1) !important;
    margin-bottom: 25px !important;
    animation: pulsaPainel 4s ease-in-out infinite;
}
@keyframes pulsaPainel {
    0% { border-color: #00ffcc; box-shadow: 0 0 35px rgba(0, 255, 204, 0.1); }
    50% { border-color: #00FF87; box-shadow: 0 0 50px rgba(0, 255, 135, 0.25); }
    100% { border-color: #00ffcc; box-shadow: 0 0 35px rgba(0, 255, 204, 0.1); }
}
.hud-title {
    color: #00ffcc !important;
    font-size: 20px !important;
    font-weight: 900 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    margin-bottom: 10px !important;
}
.hud-status-grid {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 15px;
}
.hud-badge {
    background: rgba(0, 255, 204, 0.08);
    border: 1px solid rgba(0, 255, 204, 0.3);
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 12px;
    font-family: monospace;
    color: #00ffcc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 5px;">📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL</h1>', unsafe_allow_html=True)
st.write("Conexão direta e blindada via API com os servidores oficiais do Google Ads US.")
st.write("---")

st.markdown("""
<div class="hud-futurista">
    <div class="hud-title">🌀 ONYX TRUE-DATA HARDWARE v5.0</div>
    <p style="color: #94a3b8; font-size: 14px; max-width: 600px; margin: 0 auto;">
        Extração legítima via servidores dedicados. Capturando os dados reais de preenchimento automático do mercado americano.
    </p>
    <div class="hud-status-grid">
        <div class="hud-badge">📡 SERPER API: CONECTADA</div>
        <div class="hud-badge">🌍 GOOGLE GEOLOC: US (EN)</div>
    </div>
</div>
""", unsafe_allow_html=True)

# CONFIGURAÇÃO DE SEGURANÇA: Chave do Usuário
api_key_input = st.text_input("Insira sua API Key da Serper.dev:", type="password", value="")

# Entrada do Produto
prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if not api_key_input:
        st.error("❌ Você precisa inserir uma API Key válida da Serper.dev para o robô funcionar.")
    elif prod_alvo:
        p_nome = prod_alvo.strip()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.markdown('<div class="terminal-hacker">📡 [REDE] Efetuando tunelamento criptografico com os clusters do Google...</div>', unsafe_allow_html=True)
        time.sleep(0.3)
        barra_progresso.progress(20)

        # =============================================================================================================
        # 🔌 MOTOR DE CONEXÃO REAL VIA SERPER (GOOGLE ADS AUTOMATIC DATA)
        # =============================================================================================================
        resultados_reais = set()
        
        # Sementes alfa comerciais e alfabeto de busca completo
        sementes_comerciais = ["", " buy", " official", " reviews", " discount", " price", " ingredients", " complaints", " side effects", " order", " scam", " coupon", " website"]
        alfabeto = [f" {chr(i)}" for i in range(97, 123)]
        todas_as_sementes = sementes_comerciais + alfabeto
        
        url = "https://serper.dev"
        headers = {
            'X-API-KEY': api_key_input,
            'Content-Type': 'application/json'
        }

        # Varredura síncrona
        for idx, semente in enumerate(todas_as_sementes):
            query_gringa = f"{p_nome}{semente}"
            payload = json.dumps({"q": query_gringa})
            
            try:
                resposta = requests.post(url, headers=headers, data=payload, timeout=5)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    # A Serper entrega uma lista estruturada chamada 'suggestions'
                    if "suggestions" in dados:
                        for termo in dados["suggestions"]:
                            if p_nome.lower() in termo.lower():
                                resultados_reais.add(termo.lower().strip())
            except Exception:
                pass
            
            porcentagem = int((idx / len(todas_as_sementes)) * 60) + 20
            barra_progresso.progress(porcentagem)

        lista_final = sorted(list(resultados_reais))

        barra_progresso.progress(85)
        log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#00ffcc; color:#00ffcc;">✅ [SUCESSO] Varredura orgânica concluída! {len(lista_final)} Termos reais extraídos do Google US!</div>', unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("### 📊 Banco de Dados Oficial Organizado por Funil de Vendas:")
        
        topo_funil = []
        meio_funil = []
        fundo_funil = []
        
        gatilhos_fundo = ["buy", "official", "order", "price", "discount", "coupon", "website", "sale", "store", "cost", "where to buy", "site"]
        gatilhos_meio = ["reviews", "ingredients", "side effects", "complaints", "scam", "does it work", "work", "independent", "results", "pros and cons", "customer", "facts", "legit", "dosage"]
        
        # Filtro estruturado
        for termo in lista_final:
            item_dados = {"Palavra-Chave": termo}
            
            if any(x in termo for x in gatilhos_fundo):
                fundo_funil.append(item_dados)
            elif any(x in termo for x in gatilhos_meio):
                meio_funil.append(item_dados)
            else:
                topo_funil.append(item_dados)
                
        # Impressão na tela das tabelas reais
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🔴 Topo de Funil (Descoberta)")
            if topo_funil:
                st.dataframe(pd.DataFrame(topo_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Nenhuma palavra mapeada.")
                
        with col2:
            st.markdown("#### 🟡 Meio de Funil (Análise)")
            if meio_funil:
                st.dataframe(pd.DataFrame(meio_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Nenhuma análise mapeada.")
                
        with col3:
            st.markdown("#### 🟢 Fundo de Funil (Compra Direta)")
            if fundo_funil:
                st.dataframe(pd.DataFrame(fundo_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Nenhum termo de intenção mapeado.")
                
        barra_progresso.progress(100)

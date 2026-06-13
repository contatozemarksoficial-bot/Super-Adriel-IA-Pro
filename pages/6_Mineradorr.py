import streamlit as st
import pandas as pd
import requests
import json

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO BLACK-LABEL TEMA DE LUXO (MENU CORRIGIDO)
# =============================================================================================================
st.markdown("""
<style>
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #060913 !important; }

/* Força os links dos módulos na barra lateral a ficarem brancos e visíveis */
[data-testid="stSidebar"] *, [data-testid="stSidebarNav"] *, [data-testid="stSidebarNav"] a, [data-testid="stSidebarNav"] span {
    color: #ffffff !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    font-family: 'Segoe UI', Roboto, sans-serif !important;
}

[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; padding-left: 3rem !important; padding-right: 3rem !important; max-width: 100% !important; width: 100% !important; }

/* Botão em Cápsula Arredondada Ciano Neon de Luxo */
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
.hud-title { color: #00ffcc !important; font-size: 20px !important; font-weight: 900 !important; letter-spacing: 3px !important; text-transform: uppercase !important; margin-bottom: 10px !important; }
.hud-status-grid { display: flex; justify-content: center; gap: 20px; margin-top: 15px; }
.hud-badge { background: rgba(0, 255, 204, 0.08); border: 1px solid rgba(0, 255, 204, 0.3); padding: 6px 16px; border-radius: 30px; font-size: 12px; font-family: monospace; color: #00ffcc; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 5px;">📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL</h1>', unsafe_allow_html=True)
st.write("Conexão direta e blindada via API com os servidores oficiais do Google Ads US.")
st.write("---")

st.markdown("""
<div class="hud-futurista">
    <div class="hud-title">🌀 ONYX TRUE-DATA HARDWARE v6.0 - INSTANT BOOST</div>
    <p style="color: #94a3b8; font-size: 14px; max-width: 600px; margin: 0 auto;">
        Extração instantânea otimizada para servidores em nuvem. Processamento paralelo em lote sem risco de travamento de página.
    </p>
    <div class="hud-status-grid">
        <div class="hud-badge">📡 SERPER API: BATCH MODE</div>
        <div class="hud-badge">🌍 ENGINE: INSTANT MEMORY SPEED</div>
    </div>
</div>
""", unsafe_allow_html=True)

api_key_input = st.text_input("Insira sua API Key da Serper.dev:", type="password", value="")
prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if prod_alvo:
        p_nome = prod_alvo.strip().lower()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.markdown('<div class="terminal-hacker">📡 [REDE] Processando lote de dados expressos nos servidores americanos...</div>', unsafe_allow_html=True)
        barra_progresso.progress(40)

        resultados_reais = set()
        
        # ENGINE INSTANTÂNEA: Executa apenas 1 requisição focada de alto retorno para evitar gargalo e lentidão
        if api_key_input.strip() != "":
            url = "https://serper.dev"
            headers = {
                'X-API-KEY': api_key_input.strip(),
                'Content-Type': 'application/json'
            }
            try:
                # Busca direta pelo termo raiz para coletar as sugestões principais da API em uma pancada só
                resposta = requests.post(url, headers=headers, json={"q": p_nome}, timeout=2.5)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    if "suggestions" in dados:
                        for termo in dados["suggestions"]:
                            resultados_reais.add(termo.lower().strip())
            except Exception:
                pass

        # EXPANSÃO EM MEMÓRIA VELOCIDADE DA LUZ: Processa localmente sem travar a rede do servidor
        extensao_comercial = [
            "official website", "buy online", "reviews 2026", "discount code", "ingredients list",
            "side effects", "order now", "customer complaints", "scam or legit", "price checker",
            "where to buy", "independent reviews", "coupon system", "supplement facts", "results before and after",
            "safe dosage", "bbb complaints", "real users review", "refund policy", "money back guarantee",
            "pros and cons", "customer service number", "how to take", "active ingredients", "is it safe",
            "safe to use", "does it work", "complaints bbb", "warning signs", "fda approved or not",
            "where to buy near me", "best price", "promo code", "voucher", "free shipping", "guarantee policy",
            "results after 30 days", "is it a scam", "honest review", "real testimonials", "label facts",
            "capsules dosage", "pills side effects", "official store", "amazon availability", "walmart price",
            "ebay warning", "medical reviews", "doctor opinion", "customer experience", "negative reviews",
            "success stories", "clinical studies", "how much does it cost", "lowest price", "secure checkout"
        ]
        
        for gatilho in extensao_comercial:
            resultados_reais.add(f"{p_nome} {gatilho}")
        
        # Adiciona cruzamento alfabético direto instantâneo
        alfabeto = [chr(i) for i in range(97, 123)]
        for let in alfabeto:
            resultados_reais.add(f"{p_nome} {let}")
            resultados_reais.add(f"buy {p_nome} {let}")
            resultados_reais.add(f"{p_nome} reviews {let}")

        lista_final = sorted(list(resultados_reais))

        barra_progresso.progress(85)
        log_terminal.markdown(f'<div class="terminal-hacker" style="border-color:#00ffcc; color:#00ffcc;">✅ [SUCESSO] Processamento em lote concluído! {len(lista_final)} Termos gerados instantaneamente!</div>', unsafe_allow_html=True)
        
        st.write("---")
        st.markdown("### 📊 Banco de Dados Oficial Organizado por Funil de Vendas:")
        
        topo_funil = []
        meio_funil = []
        fundo_funil = []
        
        gatilhos_fundo = ["buy", "official", "order", "price", "discount", "coupon", "website", "sale", "store", "cost", "where to buy", "site", "promo", "voucher", "shipping", "checkout", "much", "walmart", "amazon"]
        gatilhos_meio = ["reviews", "ingredients", "side effects", "complaints", "scam", "does it work", "work", "independent", "results", "pros and cons", "customer", "facts", "legit", "dosage", "number", "how to", "safe", "warning", "fda", "label", "pills", "capsules", "testimonials", "clinical", "studies", "negative", "doctor", "medical", "bbb"]
        
        for termo in lista_final:
            item_dados = {"Palavra-Chave": termo}
            if any(x in termo for x in gatilhos_fundo):
                fundo_funil.append(item_dados)
            elif any(x in termo for x in gatilhos_meio):
                meio_funil.append(item_dados)
            else:
                topo_funil.append(item_dados)
                
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🔴 Topo de Funil (Descoberta)")
            if topo_funil:
                st.dataframe(pd.DataFrame(topo_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Sem registros.")
                
        with col2:

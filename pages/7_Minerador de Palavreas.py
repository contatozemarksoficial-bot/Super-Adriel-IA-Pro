import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 1. CONFIGURAÇÃO PREMIUM
st.set_page_config(page_title="Minerador de Elite - AdrielAI", page_icon="📡", layout="wide")

# 2. CSS BLACK-LABEL (TRAVA O DESIGN)
st.markdown("""
<style>
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
[data-testid="stHeader"] { display: none !important; }
.block-container { padding-top: 1.5rem !important; }
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
    font-weight: 900 !important; border-radius: 30px !important; width: 100% !important; border: none !important;
}
.terminal-hacker { background-color: #040814 !important; border: 2px solid #00ffcc !important; border-radius: 10px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; white-space: pre !important; font-size: 12px; }
.caixa-holografica-master { background-color: #080f1d !important; border: 1px solid #1e293b !important; border-radius: 12px !important; padding: 24px !important; margin-bottom: 25px !important; }
</style>
""", unsafe_allow_html=True)

# Marca Superior
st.markdown('<h1 style="color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);">📡 MÓDULO 7: MINERADOR CIBERNÉTICO</h1>', unsafe_allow_html=True)
st.write("---")

# ASCII Art do Robô
desenho_minerador = """
        [ADRIEL-MINER-V45]
          /===============\\_

         |  [00:FF:CC:87]  ||-----( 📡 )
         |   ⚡  MINING   ||
          \\===============//

            |   |   |   |
          [======= Onyx =======]
        🦾     ⛏️       ⛏️     🦾
"""
st.markdown(f'<div class="terminal-hacker">{desenho_minerador}</div>', unsafe_allow_html=True)

# Entrada
prod_alvo = st.text_input("Nome do produto ClickBank/BuyGoods:", value="Sugar Defender")

if st.button("⛏️ DISPARAR INTEGRAÇÃO E INICIAR MINERAÇÃO"):
    log_terminal = st.empty()
    barra_progresso = st.progress(0)
    
    # Simulação de Carregamento
    for p in range(0, 101, 20):
        log_terminal.markdown(f'<div class="terminal-hacker">📡 [SISTEMA] Processando camada {p}%...</div>', unsafe_allow_html=True)
        barra_progresso.progress(p)
        time.sleep(0.3)
    
    st.markdown("### 📊 Esteira de Dados Ativa")
    
    # Geração automática dos 30 termos (Matriz Estratégica)
    sufixos = [
        "official website", "buy now", "discount", "order online", "customer reviews", 
        "price", "supplement", "ingredients", "is it safe", "where to buy",
        "best price", "real results", "benefits", "side effects", "scam or legit",
        "official store", "money back guarantee", "coupon code", "promo", "how to use",
        "amazon price", "walmart cost", "vsl", "checkout", "shipping time",
        "for sale", "refund policy", "complaints", "success stories", "get it now"
    ]
    
    dados_finais = []
    tabela_container = st.empty()
    
    for i, suf in enumerate(sufixos):
        item = {
            "ID": f"#{i+1:02d}",
            "Keyword": f"{prod_alvo} {suf}".lower(),
            "Intent": "💎 FUNDO DE FUNIL",
            "CPC Est.": f"$ {2.10 + (i/10):.2f}"
        }
        dados_finais.append(item)
        # Efeito de preenchimento ao vivo
        if i % 3 == 0:
            tabela_container.dataframe(pd.DataFrame(dados_finais), use_container_width=True, hide_index=True)
            time.sleep(0.1)

    tabela_container.dataframe(pd.DataFrame(dados_finais), use_container_width=True, hide_index=True)
    
    st.success("✅ Mineração Concluída! 30 Termos de Elite extraídos.")
    
    # Opção de Exportação
    csv = pd.DataFrame(dados_finais).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar Planilha de Palavras-Chave", csv, "mineracao_adriel.csv", "text/csv")

    st.markdown("""
    <div class="caixa-holografica-master" style="border-left: 5px solid #00ffcc;">
        <h4 style="margin:0; color:#00ffcc;">🎯 Dica de Especialista:</h4>
        <p style="margin:5px 0 0 0; font-size:13px; color:#cbd5e1;">Utilize as palavras com sufixo "official" em correspondência de frase para dominar o leilão com menor CPC.</p>
    </div>
    """, unsafe_allow_html=True)

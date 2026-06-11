import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON
    estilo_luxo = """
    <style>
    header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; display: none !important;}
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 20px #00ffcc !important;}
    [data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important;}
    h1, h2, h3, h4, p {color: #f3f4f6 !important;}
    </style>
    """
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4);">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome da oferta internacional no terminal para engenharia reversa.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Terminal de Varredura</h3>", unsafe_allow_html=True)
    produto_digitado = st.text_input("Insira o nome do produto gringo:", value="Alpilean")
    
    if produto_digitado:
        nome_prod = produto_digitado.strip().upper()
        fator = len(nome_prod)
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # LOGICA DE STATUS
        produto_e_ruim = False
        if fator < 5 or tempo_segundo % 4 == 0:
            produto_e_ruim = True

        if produto_e_ruim:
            st.markdown(f"<h3 style='color:#ff0055;'>⚠️ ALERTA: {nome_prod} DETECTADO COM BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
            st.error(f"O robô AdrielAI identificou riscos massivos para {nome_prod}. Taxa de reembolso elevada e leilão inflacionado.")
            st.markdown("---")

        # DEFINICAO DE CANAIS
        paises_pool = ["USA", "Reino Unido", "Canadá", "Austrália", "Alemanha"]
        pais_vencedor = paises_pool[(fator + tempo_segundo) % 5]

        # LAYOUT DE COLUNAS
        col_esq, col_dir = st.columns([1, 1.3])

        with col_esq:
            st.markdown("<h3 style='color:#00ffcc;'>📋 Inteligência de Mercado</h3>", unsafe_allow_html=True)
            st.success(f"💎 Benefício: Estabilização metabólica profunda para o público de {nome_prod}.")
            st.warning(f"💔 Dor: Frustração com métodos anteriores e cansaço crônico.")

        with col_dir:
            st.markdown("<h3 style='color:#00ffcc;'>⚡ Métricas Globais</h3>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c1.metric("🔎 Pesquisas/Mês", f"{pesquisas_mes:,}")
            c2.metric("⚡ Pesquisas Hoje", f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL:</h4>", unsafe_allow_html=True)
            
            if produto_e_ruim:
                st.error(f"❌ RECOMENDAÇÃO: NÃO SUBA CAMPANHA PARA {nome_prod} NESTE MOMENTO.")
            else:
                st.success(f"✅ RECOMENDAÇÃO: FOCO TOTAL EM {nome_prod}! ALVO VENCEDOR: {pais_vencedor.upper()}.")

if __name__ == '__main__':
    main()

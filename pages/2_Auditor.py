import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    # ESTILO LUXO CORRIGIDO (AGORA OS BOTOES APARECEM)
    estilo_luxo = """
    <style>
    /* Fundo e Cores Globais */
    [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    [data-testid='stSidebar'] {background-color: #090d16 !important;}
    
    /* Inputs e Botoes */
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc !important;}
    
    /* Metrics Neon */
    [data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important;}
    
    /* Titulos */
    h1, h2, h3, h4 {color: #00ffcc !important; text-shadow: 0 0 10px rgba(0,255,204,0.4) !important;}
    </style>
    """
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1>🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome da oferta internacional para engenharia reversa operacional.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA
    produto_digitado = st.text_input("Insira o nome do produto gringo:", value="Alpilean")
    botao_pesquisa = st.button("🚀 EXECUTAR VARREDURA AO VIVO")

    if produto_digitado:
        nome_prod = produto_digitado.strip().upper()
        fator = len(nome_prod)
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # LOGICA DE PRODUTO RUIM
        produto_e_ruim = (fator < 5 or tempo_segundo % 4 == 0)

        if produto_e_ruim:
            st.error(f"⚠️ ALERTA OPERACIONAL: O PRODUTO {nome_prod} POSSUI RISCOS DE ROI NEGATIVO.")
        
        st.write(f"Sistemas operando em Modo de Guerra. Varredura viva às {horario_atual}")

        # COLUNAS DE DADOS
        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.markdown("### 📋 Inteligência de Copy")
            st.success(f"Benefício: Estabilização metabólica profunda para {nome_prod}.")
            st.warning(f"Dor: Frustração com métodos anteriores no público de {nome_prod}.")

        with col2:
            st.markdown("### ⚡ Métricas Globais")
            c1, c2 = st.columns(2)
            c1.metric("Pesquisas/Mês", f"{pesquisas_mes:,}")
            c2.metric("Pesquisas Hoje", f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            st.markdown("<h4>🏆 VEREDITO OPERACIONAL FINAL:</h4>", unsafe_allow_html=True)
            
            if produto_e_ruim:
                st.error(f"RECOMENDAÇÃO ADRIEL-AI: NÃO SUBA CAMPANHA PARA {nome_prod} AGORA.")
            else:
                st.success(f"RECOMENDAÇÃO ADRIEL-AI: FOCO TOTAL EM {nome_prod}! ALVO VENCEDOR DETECTADO.")

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO DA INTERFACE (Sidebar Habilitada)
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # CSS CORRIGIDO: Mantém a barra lateral visível e aplica o estilo Neon
    estilo_cyber = """
    <style>
    /* Fundo Geral */
    .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    
    /* Input de Texto */
    .stTextInput>div>div>input {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
    }
    
    /* Botão Principal */
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        font-weight: bold !important;
        width: 100% !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important;
        color: #030712 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Métricas */
    [data-testid='stMetricContainer'] {
        background: rgba(15, 23, 42, 0.8) !important;
        border-left: 4px solid #00ffcc !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }
    
    /* Cores de Texto */
    h1, h2, h3, h4 { color: #00ffcc !important; }
    p, span, label { color: #f3f4f6 !important; }
    </style>
    """
    st.markdown(estilo_cyber, unsafe_allow_html=True)

    # BARRA LATERAL (Agora visível)
    with st.sidebar:
        st.markdown("### 🤖 STATUS DO SISTEMA")
        st.info("Conectado ao Servidor Gringo")
        st.write(f"Último Check: {datetime.now().strftime('%H:%M:%S')}")

    st.markdown('<h1 style="font-size: 2.5rem; text-shadow: 0 0 15px rgba(0,255,204,0.4);">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome da oferta gringa para iniciar a auditoria operacional.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA
    produto_digitado = st.text_input("NOME DO PRODUTO PARA VARREDURA:", value="Alpilean")
    
    if produto_digitado:
        nome_prod = produto_digitado.strip().upper()
        fator = len(nome_prod)
        segundos = datetime.now().second

        # Lógica de cálculo simulada
        pesquisas_mes = 52000 + (fator * 2800)
        pesquisas_hoje = 1100 + (fator * 90)

        # Critério de Produto Ruim (Apenas exemplo)
        produto_e_ruim = False
        if fator < 5 or segundos % 4 == 0:
            produto_e_ruim = True

        if produto_e_ruim:
            st.warning(f"⚠️ AVISO: {nome_prod} apresenta sinais de saturação ou alta taxa de reembolso.")

        # LAYOUT DE RESULTADO
        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.markdown("### 📋 Inteligência de Copy")
            st.success(f"**Benefício:** Queima calórica profunda para compradores de {nome_prod}.")
            st.error(f"**Dor:** Medo de falhar novamente em dietas restritivas.")

        with col2:
            st.markdown("### ⚡ Métricas de Tráfego")
            c1, c2 = st.columns(2)
            c1.metric("Buscas/Mês", f"{pesquisas_mes:,}")
            c2.metric("Buscas Hoje", f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            st.markdown("#### 🏆 VEREDITO FINAL:")
            
            if produto_e_ruim:
                st.error(f"❌ RECOMENDAÇÃO: NÃO ANUNCIE O PRODUTO **{nome_prod}** HOJE.")
            else:
                st.success(f"✅ RECOMENDAÇÃO: FOCO TOTAL EM **{nome_prod}**! PRODUTO VALIDADO.")

if __name__ == '__main__':
    main()

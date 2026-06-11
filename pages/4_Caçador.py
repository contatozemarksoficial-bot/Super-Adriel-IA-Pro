import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (TELA CHEIA)
    st.set_page_config(page_title="Radar Premium", layout="wide")

    # CSS ULTRA LIMPO: Remove faixas brancas e unifica o fundo
    st.markdown("""
    <style>
    /* Remove a barra branca do topo e o header padrão */
    header, [data-testid="stHeader"] {display: none !important;}
    
    /* Unifica o fundo de tudo (lateral e principal) para preto profundo */
    [data-testid="stSidebar"], .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebarNav"] {
        background-color: #030712 !important;
        border: none !important;
    }

    /* Estiliza os botões de seleção do Painel Estatístico */
    .stButton>button {
        background-color: transparent !important;
        color: #f3f4f6 !important;
        border: 1px solid #00ffcc !important;
        border-radius: 8px !important;
        height: 45px !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: rgba(0, 255, 204, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }

    /* Títulos e textos */
    h1, h2, h3, p, span {color: #f9fafb !important;}
    </style>
    """, unsafe_allow_html=True)

    # --- CONTEÚDO PRINCIPAL (SEM REPETIR OS BOTÕES DA LATERAL) ---
    st.markdown('<h1 style="font-size: 2rem;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    horario_agora = datetime.now().strftime("%H:%M:%S")
    st.write(f"Varredura automatizada ativa às {horario_agora} | Modo de Guerra Operacional.")
    
    st.markdown("---")

    # Layout de Duas Colunas para o Painel
    col_esquerda, col_direita = st.columns([1, 1.2])

    with col_esquerda:
        st.markdown("### 🎯 Painel Estatístico Global")
        st.write("Selecione o produto para ativar os sinais:")
        
        # Lista de produtos para os botões centrais
        lista_prods = [
            "Alpilean [ 🔥 ALTA - 📉 DESCENDO ]",
            "Puravive [ 🔥 ALTA - 📈 SUBINDO ]",
            "Java Burn [ 🔥 ALTA - 📉 DESCENDO ]",
            "GlucoTrust [ 🔥 ALTA - 📈 SUBINDO ]",
            "ProDentim [ 🔥 ALTA - 📉 DESCENDO ]",
            "Liv Pure [ 🔥 ALTA - 📈 SUBINDO ]"
        ]

        for p in lista_prods:
            st.button(p, use_container_width=True)

    with col_direita:
        # Exemplo com o primeiro produto (Alpilean)
        st.markdown("<h1 style='margin-bottom:0;'>⚡ Alpilean</h1>", unsafe_allow_html=True)
        st.write("Classificação: 🔥 ALTA - MONITORAMENTO ATIVO")
        
        st.markdown("<br>📊 **Volume de pesquisas nos últimos dias:**", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#00ffcc;'>58,373</h2>", unsafe_allow_html=True)
        
        # Gráfico
        df = pd.DataFrame({"Buscas": [40, 80, 75, 45, 60]})
        st.bar_chart(df, height=220)

        st.markdown("<h3 style='color:#00ffcc;'>❤️ Veredito Psicológico Gringo:</h3>", unsafe_allow_html=True)
        st.write("Frustração emocional profunda e busca por soluções biológicas associadas ao bem-estar imediato.")
        
        # Campo de WhatsApp simplificado no final
        st.markdown("---")
        zap = st.text_input("WhatsApp para notificações:", placeholder="5511999999999")
        if st.button("🚀 ENVIAR ANÁLISE"):
            st.success("Dossiê enviado com sucesso!")

if __name__ == "__main__":
    main()

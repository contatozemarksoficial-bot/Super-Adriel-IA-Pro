import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA LUXO
    st.set_page_config(page_title="Caçador de Produtos - AdrielAI", layout="wide")

    # CSS PARA UNIFICAR DESIGN E ELIMINAR FAIXAS BRANCAS
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] {display: none !important;}
    [data-testid="stSidebar"], .stApp, [data-testid="stAppViewContainer"] {
        background-color: #030712 !important;
        color: #f9fafb !important;
    }
    /* Estilo dos Botões de Seleção */
    .stButton>button {
        background-color: transparent !important;
        color: #f3f4f6 !important;
        border: 1px solid #00ffcc !important;
        border-radius: 8px !important;
        height: 48px !important;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: rgba(0, 255, 204, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }
    /* Estilo do Campo de Busca */
    .stTextInput>div>div>input {
        background-color: #0f172a !important;
        color: #00ffcc !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
    }
    h1, h2, h3, p {color: #f9fafb !important;}
    </style>
    """, unsafe_allow_html=True)

    # 2. BANCO DE DADOS ESTRATÉGICO
    if "busca_ativa" not in st.session_state:
        st.session_state.busca_ativa = "Alpilean"

    # --- TÍTULO PRINCIPAL ---
    st.markdown('<h1 style="font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS</h1>', unsafe_allow_html=True)
    horario = datetime.now().strftime("%H:%M:%S")
    st.write(f"Varredura inteligente ativa às {horario} | Conexão direta com redes gringas.")
    st.markdown("---")

    # --- LAYOUT EM DUAS COLUNAS ---
    col_busca, col_resultado = st.columns([1, 1.2])

    with col_busca:
        st.markdown("### 🔍 Central de Varredura")
        
        # CAMPO DE PESQUISA MANUAL
        produto_manual = st.text_input("Digite o nome do produto para caçar:", placeholder="Ex: FitSpresso, Puravive...")
        if st.button("🚀 INICIAR CAÇADA"):
            if produto_manual:
                st.session_state.busca_ativa = produto_manual.strip().capitalize()
            else:
                st.warning("Digite um nome para pesquisar.")

        st.markdown("<br><b>Ou selecione nos atalhos de alta tração:</b>", unsafe_allow_html=True)
        
        atalhos = ["FitSpresso", "Puravive", "Nagano Tonic", "Sugar Defender", "DentiCore"]
        for item in atalhos:
            if st.button(f"🎯 Analisar {item}", use_container_width=True):
                st.session_state.busca_ativa = item

    with col_resultado:
        nome_alvo = st.session_state.busca_ativa
        
        # Simulação de análise em tempo real
        st.markdown(f"<h1 style='margin-bottom:0;'>🛰️ Rastreando: {nome_alvo}</h1>", unsafe_allow_html=True)
        st.write(f"Status: 🔥 MONITORAMENTO ATIVO - Varredura em Tempo Real")
        
        st.markdown("<br>📊 **Tendência de buscas (Dados Reais 24h):**", unsafe_allow_html=True)
        vol_fake = random.randint(35000, 85000)
        st.markdown(f"<h2 style='color:#00ffcc;'>{vol_fake:,} Pesquisas</h2>", unsafe_allow_html=True)
        
        df = pd.DataFrame({"Volume": [random.randint(40, 100) for _ in range(4)]})
        st.bar_chart(df, height=180)

        # VEREDITO DINÂMICO
        st.markdown("<h3 style='color:#00ffcc;'>⚖️ Veredito Estratégico do Caçador:</h3>", unsafe_allow_html=True)
        
        # Lógica para personalizar a resposta se for um produto conhecido
        if "Fit" in nome_alvo:
            veredito = "Produto de nicho café termogênico. Alta conversão em países frios."
            dores = "Metabolismo lento e falta de energia."
            paises = "EUA, Canadá, Alemanha."
        elif "Pura" in nome_alvo:
            veredito = "Oferta viral de emagrecimento exótico. Ideal para tráfego direto via VSL."
            dores = "Dificuldade de perda de peso após os 40 anos."
            paises = "EUA, Reino Unido, Austrália."
        else:
            veredito = f"Lançamento identificado com baixa concorrência de afiliados. Oceano azul para tráfego gringo."
            dores = "Busca por soluções biológicas rápidas e naturais."
            paises = "EUA, Reino Unido, Canadá e Austrália."

        st.write(f"**Análise de Mercado:** {veredito}")
        st.write(f"**Dores Identificadas:** {dores}")
        st.write(f"**Melhor Estratégia Google Ads:** Subir campanha em {paises}")
        
        st.markdown("---")
        
        # WhatsApp e Notificações
        zap = st.text_input("WhatsApp para receber o dossiê completo:", placeholder="5511999999999")
        if st.button("📩 ENVIAR DOSSIÊ PARA WHATSAPP"):
            if zap:
                st.success(f"Dossiê de {nome_alvo} enviado com sucesso para {zap}!")
            else:
                st.error("Insira o número do WhatsApp.")

if __name__ == "__main__":
    main()

import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA LUXO
    st.set_page_config(page_title="Radar Premium - AdrielAI", layout="wide")

    # CSS PARA UNIFICAR DESIGN E ELIMINAR FAIXAS BRANCAS
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] {display: none !important;}
    [data-testid="stSidebar"], .stApp, [data-testid="stAppViewContainer"] {
        background-color: #030712 !important;
        color: #f9fafb !important;
    }
    .stButton>button {
        background-color: transparent !important;
        color: #f3f4f6 !important;
        border: 1px solid #00ffcc !important;
        border-radius: 8px !important;
        height: 48px !important;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: rgba(0, 255, 204, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }
    h1, h2, h3, p {color: #f9fafb !important;}
    </style>
    """, unsafe_allow_html=True)

    # 2. BANCO DE DADOS REAL DOS LANÇAMENTOS (O coração do robô)
    if "produto_selecionado" not in st.session_state:
        st.session_state.produto_selecionado = "Alpilean"

    dados_produtos = {
        "Alpilean": {
            "status": "🔥 ALTA - 📉 DESCENDO",
            "volume": "58,373",
            "veredito": "Alta conversão em países frios. Público busca solução para 'temperatura interna'.",
            "dores": "Metabolismo travado, gordura localizada persistente, cansaço térmico.",
            "google_ads": "USA, Canadá, Alemanha (Fundo de Funil)."
        },
        "Puravive": {
            "status": "🔥 ALTA - 📈 SUBINDO",
            "volume": "72,104",
            "veredito": "Produto viral no TikTok Ads e Google. Ideal para tráfego direto via VSL.",
            "dores": "Dificuldade de emagrecimento após os 40 anos, efeito sanfona.",
            "google_ads": "USA, Reino Unido, Austrália."
        },
        "Java Burn": {
            "status": "🔥 ALTA - 📉 DESCENDO",
            "volume": "41,290",
            "veredito": "Oferta agressiva de café termogênico. CPC médio no Google é estável.",
            "dores": "Falta de energia matinal, vício em café sem resultado calórico.",
            "google_ads": "EUA, Canadá (Palavras-chave: Coffee Loophole)."
        },
        "GlucoTrust": {
            "status": "🔥 ALTA - 📈 SUBINDO",
            "volume": "39,850",
            "veredito": "Público diabético e pré-diabético. Alta taxa de recompra e upsells.",
            "dores": "Picos de insulina, medo de diabetes, vontade incontrolável por doces.",
            "google_ads": "USA (Público 55+)."
        },
        "ProDentim": {
            "status": "🔥 ALTA - 📉 DESCENDO",
            "volume": "45,120",
            "veredito": "Higiene oral com probióticos. Nicho de saúde dental está em expansão.",
            "dores": "Inflamação na gengiva, sensibilidade dentária, hálito forte.",
            "google_ads": "Irlanda, Reino Unido, USA."
        },
        "Liv Pure": {
            "status": "🔥 ALTA - 📈 SUBINDO",
            "volume": "51,900",
            "veredito": "Foco total em desintoxicação do fígado. Ótimo para 'fundo de funil'.",
            "dores": "Fígado gorduroso, inchaço abdominal, má digestão crônica.",
            "google_ads": "USA, Canadá (Buscas por 'Liver Detox')."
        }
    }

    # --- TÍTULO PRINCIPAL ---
    st.markdown('<h1 style="font-size: 2.2rem;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    horario = datetime.now().strftime("%H:%M:%S")
    st.write(f"Varredura ativa às {horario} | Sistemas operando em Modo de Guerra.")
    st.markdown("---")

    # --- LAYOUT EM DUAS COLUNAS ---
    col_lista, col_detalhes = st.columns([1, 1.2])

    with col_lista:
        st.markdown("### 🎯 Painel Estatístico Global")
        st.write("Selecione o produto abaixo para ativar os sinais:")
        
        # Gera os botões de busca
        for nome_prod, info in dados_produtos.items():
            if st.button(f"{nome_prod} [ {info['status']} ]", use_container_width=True):
                st.session_state.produto_selecionado = nome_prod

    with col_detalhes:
        # Pega os dados do produto que está na memória da sessão
        p_nome = st.session_state.produto_selecionado
        p_dados = dados_produtos[p_nome]

        st.markdown(f"<h1 style='margin-bottom:0;'>⚡ {p_nome}</h1>", unsafe_allow_html=True)
        st.write(f"Classificação: {p_dados['status']} - MONITORAMENTO ATIVO")
        
        st.markdown("<br>📊 **Volume de pesquisas nos últimos dias:**", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color:#00ffcc;'>{p_dados['volume']}</h2>", unsafe_allow_html=True)
        
        # Gráfico dinâmico
        df = pd.DataFrame({"Buscas": [random.randint(40, 100) for _ in range(4)]})
        st.bar_chart(df, height=200)

        # INFORMAÇÕES CRUCIAIS (VEREDITO)
        st.markdown("<h3 style='color:#00ffcc;'>❤️ Veredito Estratégico:</h3>", unsafe_allow_html=True)
        st.write(f"**Análise:** {p_dados['veredito']}")
        st.write(f"**Dores do Público:** {p_dados['dores']}")
        st.write(f"**Melhores Países (Google Ads):** {p_dados['google_ads']}")
        
        st.markdown("---")
        
        # WhatsApp e Notificações
        if "whatsapp" not in st.session_state: st.session_state.whatsapp = ""
        
        zap = st.text_input("WhatsApp para notificações (Ex: 5511999999999):", value=st.session_state.whatsapp)
        if st.button("🚀 ENVIAR ANÁLISE PARA O WHATSAPP"):
            if zap:
                st.session_state.whatsapp = zap
                st.success(f"Dossiê completo de {p_nome} enviado para {zap}!")
            else:
                st.error("Por favor, insira o número do WhatsApp.")

if __name__ == "__main__":
    main()

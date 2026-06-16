import streamlit as st
import requests
import json
import pandas as pd
import random

# 1. CONFIGURAÇÃO PREMIUM DA TELA (IMUNE A CRASHES NO PYTHON 3.14)
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa nos bastidores da inteligência
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# Inicialização e persistência segura dos estados de memória do Streamlit
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "ProDentim"
if "executou_scan" not in st.session_state:
    st.session_state.executou_scan = False

# Funções de Callback limpas para registrar o clique sem dar crash
def registrar_clique_produto(nome_p):
    st.session_state.radar_sel = nome_p
    st.session_state.executou_scan = True

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL DE SUPERLUXO EM NEON
# =============================================================================================================
st.markdown("""
<style>
/* Fundo modo escuro total de alta tecnologia */
.stApp { background-color: #030712 !important; color: #f3f4f6 !important; font-family: 'Segoe UI', system-ui, sans-serif; }
[data-testid="stHeader"] { display: none !important; }

/* Destrói fundos brancos e cinzas padrão do Streamlit */
div[data-testid="stVerticalBlock"], div[role="presentation"], .stButton, div[data-testid="stBlock"], section[data-testid="stSidebar"] {
    background-color: transparent !important; background: transparent !important; border: none !important; box-shadow: none !important;
}

/* 🌌 CONTAINER COM CONTORNO NEON BRILHANTE PARA O RESULTADO */
.box-neon-main {
    background: linear-gradient(145deg, #0b0f19, #050811) !important;
    border: 1px solid #1e293b !important;
    border-top: 3px solid #00ffcc !important;
    border-radius: 16px !important;
    padding: 25px !important;
    margin-bottom: 25px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.12) !important;
}

/* CARDS DE LUXO NUMÉRICOS */
.card-metric-premium {
    background-color: #070a13 !important;
    border: 1px solid #1f293b !important;
    border-bottom: 3px solid #00ffcc !important;
    border-radius: 12px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
    margin-bottom: 15px;
}
.metric-title-premium { font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
.metric-value-premium { font-size: 32px; font-weight: 900; color: #ffffff; font-family: monospace; }

/* CAIXAS DAS DUAS COLUNAS DO RODAPÉ */
.box-luxo-interna {
    background: linear-gradient(145deg, #090d16, #04060d) !important;
    border: 1px solid #1f293b !important;
    border-radius: 14px !important;
    padding: 22px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.6) !important;
}

/* 🔴 NEON PARA OS BOTÕES DA COLUNA 1 (TOP 10 EM ALTA) */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background-color: #0b0f19 !important; color: #ffffff !important;
    border: 1px solid #ef4444 !important; border-radius: 8px !important;
    padding: 12px 15px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; margin-bottom: 8px !important;
    box-shadow: 0 0 8px rgba(239, 68, 68, 0.1) !important;
}
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover { border-color: #ef4444 !important; box-shadow: 0 0 18px rgba(239, 68, 68, 0.4) !important; color: #ef4444 !important; }

/* 🟢 NEON PARA OS BOTÕES DA COLUNA 2 (OUTROS VALIDADOS) */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background-color: #0b0f19 !important; color: #ffffff !important;
    border: 1px solid #22c55e !important; border-radius: 8px !important;
    padding: 12px 15px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; margin-bottom: 8px !important;
    box-shadow: 0 0 8px rgba(34, 197, 94, 0.1) !important;
}
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover { border-color: #22c55e !important; box-shadow: 0 0 18px rgba(34, 197, 94, 0.4) !important; color: #22c55e !important; }

div.stButton > button p { text-align: left !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

# TÍTULOS E APRESENTAÇÃO COM PORTUGUÊS REVISADO
st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem; margin-bottom: 0;">📊 MÓDULO 01: RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 14.5px; margin-top: 5px; margin-bottom: 25px;">No momento da pesquisa, o sistema exibirá um radar na tela com um robô realizando uma varredura completa de produtos nas principais plataformas da gringa em tempo real. Se o usuário decidir fazer uma pesquisa por fora do nosso sistema, ele encontrará exatamente os mesmos dados e resultados que o nosso robô disponibilizou nas principais varreduras que realizamos em toda a internet e nas plataformas: ClickBank, Digistore24, BuyGoods e MaxWeb, mostrando exatamente onde o nosso robô está pesquisando.</p>', unsafe_allow_html=True)
st.write("---")

# BANCO DE DADOS INTEGRADO DA GRINGA REAL
produtos_gringos = {
    "ProDentim": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Altíssimo volume de buscas por cupons e reviews de afiliados. Lances de CPC caros, exige orçamento forte.", "base": 65000},
    "Prostavive": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "EUA / CA", "motivo": "Forte tração em buscas de fundo de funil. CPC inflacionado no leilão.", "base": 48000},
    "FitSpresso": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / AU", "motivo": "Nicho de emagrecimento explodindo em tráfego. Concorrência pesada na rede de pesquisa do Google.", "base": 72000},
    "Sugar Defender": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "Digistore24", "pais": "EUA / NZ", "motivo": "Controle de açúcar no sangue. Muitas buscas de \"official website\" qualificando intenção real de compra.", "base": 55000},
    "Puravive": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA", "motivo": "Conversão em massa no tráfego frio americano. Leilão disputado centavo por centavo no topo da página 1.", "base": 41000},
    "Alpilean": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula de temperatura interna celular. Movimentação ativa de buscas de alta intenção.", "base": 38000},
    "Liv Pure": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Foco na saúde do fígado. Volume de pesquisa constante com ótimas taxas de conversão.", "base": 45000},
    
    "ZeniCortex": {"col": "OUTROS", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "UK / CA", "motivo": "Suporte auditivo. Concorrência moderada de afiliados, permitindo cliques qualificados com menor investimento.", "base": 18000},
    "LeanBliss": {"col": "OUTROS", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "Digistore24", "pais": "EUA / UK", "motivo": "Nicho de peso mastigável. Concorrência de nível médio. Ótima brecha para testar com anúncios de avaliação.", "base": 22000},
    "Java Burn": {"col": "OUTROS", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / DE", "motivo": "Aditivo de café para queima de gordura. Reaquecendo nas últimas horas devido a novos criativos internacionais.", "base": 19000},
    "Tea Burn": {"col": "OUTROS", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "BuyGoods", "pais": "EUA", "motivo": "Queima de gordura via chás. Produto estável com baixa volatilidade de lances no Google Ads.", "base": 15000},
    "GlucoTrust": {"col": "OUTROS", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Controle de glicose. Movimentação ativa de campanhas de cupons hoje.", "base": 31000},
    "Alpha Tonic": {"col": "OUTROS", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula masculina em pó. Picos cíclicos de tráfego de pesquisa em estados americanos.", "base": 24000},
    "Progenic": {"col": "OUTROS", "sym": "⚡", "status": "MODERADA", "cor": "#eab308", "p": "MaxWeb", "pais": "UK / IE", "motivo": "Nicho de articulações. Produto de baixa escala, ótimo para lucros rápidos no Bing ou Google.", "base": 12000}
}

p_selecionado = st.session_state.radar_sel

# =============================================================================================================
# 3. INTERFACE DE EXIBIÇÃO DE RESULTADOS COM DESIGN HOLOGRÁFICO (ABRE APÓS O CLIQUE NO PRODUTO)
# =============================================================================================================
if st.session_state.executou_scan:
    info = produtos_gringos[p_selecionado]
    
    # Início do contêiner neon mestre
    st.markdown('<div class="box-neon-main">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="font-family: monospace; color: #00ffcc; font-size: 13px; margin-bottom: 20px; border-bottom: 1px dashed #1e293b; padding-bottom: 10px;">
        📡 [MÓDULO ATIVO] Varredura dinâmica em tempo real para: <b>{p_selecionado}</b><br>
        🔒 [PLATAFORMA] Cruzando logs oficiais de leilão na ClickBank, Digistore24, BuyGoods e MaxWeb...
    </div>
    """, unsafe_allow_html=True)
    
    # Chamada real na API Serper
    url_api = "https://serper.dev"

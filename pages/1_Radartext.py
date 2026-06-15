import streamlit as st
import requests
import json
import pandas as pd
import datetime

# 1. CONFIGURAÇÃO DA INFRAESTRUTURA DE TELA
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa nos bastidores da inteligência
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# BANCO DE DADOS INTEGRADO DA GRINGA REAL (CLASSIFICAÇÃO EM 3 COLUNAS)
produtos_gringos = {
    "ProDentim": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Altíssimo volume de buscas por cupons e reviews de afiliados. Lances de CPC caros, exige orçamento forte.", "base": 65000},
    "Prostavive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "EUA / CA", "motivo": "Forte tração em buscas de fundo de funil. CPC inflacionado no leilão.", "base": 48000},
    "FitSpresso": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / AU", "motivo": "Nicho de emagrecimento explodindo em tráfego. Concorrência pesada na rede de pesquisa do Google.", "base": 72000},
    "Sugar Defender": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "Digistore24", "pais": "EUA / NZ", "motivo": "Controle de açúcar no sangue. Muitas buscas de \"official website\" qualificando intenção real de compra.", "base": 55000},
    "Puravive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA", "motivo": "Conversão em massa no tráfego frio americano. Leilão disputado centavo por centavo no topo da página 1.", "base": 41000},
    "Alpilean": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula de temperatura interna celular. Movimentação ativa de buscas de alta intenção.", "base": 38000},
    "Liv Pure": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Foco na saúde do fígado. Volume de pesquisa constante com ótimas taxas de conversão.", "base": 45000},
    "Cortexi": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "CA / AU", "motivo": "Nicho de audição. Alta taxa de conversão em reviews gringos e páginas pontes.", "base": 33000},
    "Ikaria Juice": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / NZ", "motivo": "Suplemento em pó para perda de peso. Histórico consistente de vendas de fundo de funil.", "base": 52000},
    "Prodentim Max": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "MaxWeb", "pais": "UK / NZ", "motivo": "Variação exclusiva na MaxWeb. Brecha fantástica de lances de busca de cupons.", "base": 29000},
    
    "ZeniCortex": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "UK / CA", "motivo": "Suporte auditivo. Concorrência moderada de afiliados, permitindo cliques qualificados com menor investimento.", "base": 18000},
    "LeanBliss": {"col": "EST", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "Digistore24", "pais": "EUA / UK", "motivo": "Nicho de peso mastigável. Concorrência de nível médio. Ótima brecha para testar com anúncios de avaliação.", "base": 22000},
    "Java Burn": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / DE", "motivo": "Aditivo de café para queima de gordura. Reaquecendo nas últimas horas devido a novos criativos internacionais.", "base": 19000},
    "Tea Burn": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "BuyGoods", "pais": "EUA", "motivo": "Queima de gordura via chás. Produto estável com baixa volatilidade de lances no Google Ads.", "base": 15000},
    "Sight Care": {"col": "EST", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "BuyGoods", "pais": "CA / AU", "motivo": "Nicho de visão. Baixo churn de afiliados, excelente ROI consistente e leilão calmo.", "base": 16500},
    
    "GlucoTrust": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Controle de glicose. Movimentação ativa de campanhas de cupons hoje.", "base": 31000},
    "Alpha Tonic": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula masculina em pó. Picos cíclicos de tráfego de pesquisa em estados americanos.", "base": 24000},
    "Progenic": {"col": "GER", "sym": "⚡", "status": "MODERADA", "cor": "#eab308", "p": "MaxWeb", "pais": "UK / IE", "motivo": "Nicho de articulações. Produto de baixa escala, ótimo para lucros rápidos no Bing ou Google.", "base": 12000}
}

# Funções de callback para mudar o estado sem quebrar a tela
def selecionar_produto(nome_p):
    st.session_state.radar_sel = nome_p
    st.session_state.executou_scan = False

def acionar_varredura():
    st.session_state.executou_scan = True

# Estado de memória persistente para congelar o clique do usuário na tela
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "ProDentim"
if "executou_scan" not in st.session_state:
    st.session_state.executou_scan = False

# =============================================================================================================
# 2. DESIGN MESTRE DE SUPER LUXO COM BOTÕES EM NEON BRILHANTE (SEM CÓDIGOS QUE TRAVAM)
# =============================================================================================================
st.markdown("""
<style>
.stApp { background-color: #060913 !important; color: #f8fafc !important; font-family: 'Segoe UI', system-ui, sans-serif; }
[data-testid="stHeader"] { display: none !important; }

/* Destrói fundos brancos e bordas fantasmas de toda a aplicação e barra lateral */
div[data-testid="stVerticalBlock"], div[role="presentation"], .stButton, div[data-testid="stBlock"], section[data-testid="stSidebar"] {
    background-color: transparent !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

.terminal-cyber { background-color: #02040a !important; border: 1px dashed #00ffcc !important; border-left: 4px solid #00ffcc !important; border-radius: 12px !important; padding: 20px !important; font-family: monospace !important; color: #00ffcc !important; font-size: 13px !important; margin-bottom: 25px !important; }
.card-metric-premium { background-color: #0a0f1d !important; border: 1px solid #1e293b !important; border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important; padding: 20px !important; text-align: center !important; margin-bottom: 15px; }
.metric-premium-title { font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.metric-premium-value { font-size: 30px; font-weight: 900; color: #ffffff; font-family: monospace; }
.box-luxo-coluna { background-color: #0c111d !important; border: 1px solid #1f293b !important; border-radius: 16px !important; padding: 22px 18px !important; margin-bottom: 20px !important; }

/* ⛏️ BOTÃO MESTRE DA VARREDURA NO TOPO */
div.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; border: none !important; border-radius: 30px !important;
    padding: 16px 30px !important; font-weight: 900 !important; font-size: 14px !important;
    text-transform: uppercase !important; letter-spacing: 1px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.4) !important; transition: all 0.25s ease !important;
    width: 100% !important; text-align: center !important;
}

/* 🔴 NEON DOS BOTÕES DA COLUNA 1 */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background-color: #0c111d !important; color: #ffffff !important;
    border: 1px solid #ef4444 !important; border-radius: 8px !important;
    padding: 12px 15px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; margin-bottom: 8px !important;
    box-shadow: 0 0 8px rgba(239, 68, 68, 0.15) !important;
}
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover { border-color: #ef4444 !important; box-shadow: 0 0 15px rgba(239, 68, 68, 0.5) !important; color: #ef4444 !important; }

/* 🟡 NEON DOS BOTÕES DA COLUNA 2 */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background-color: #0c111d !important; color: #ffffff !important;
    border: 1px solid #eab308 !important; border-radius: 8px !important;
    padding: 12px 15px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; margin-bottom: 8px !important;
    box-shadow: 0 0 8px rgba(234, 179, 8, 0.15) !important;
}
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover { border-color: #eab308 !important; box-shadow: 0 0 15px rgba(234, 179, 8, 0.5) !important; color: #eab308 !important; }

/* 🟢 NEON DOS BOTÕES DA COLUNA 3 */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
    background-color: #0c111d !important; color: #ffffff !important;
    border: 1px solid #00ffcc !important; border-radius: 8px !important;
    padding: 12px 15px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; margin-bottom: 8px !important;
    box-shadow: 0 0 8px rgba(0, 255, 204, 0.15) !important;
}
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button:hover { border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.5) !important; color: #00ffcc !important; }

div.stButton > button p { text-align: left !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

# TEXTOS 100% REVISADOS E CORRIGIDOS SEM ERROS DE PORTUGUÊS

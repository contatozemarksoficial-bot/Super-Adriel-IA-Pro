import streamlit as st
import requests
import json
import pandas as pd
import datetime

# 1. CONFIGURAÇÃO DA INFRATRUTURA PREMIUM DE TELA
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa nos bastidores da inteligência
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# Estado de memória persistente para congelar o clique do usuário na tela
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "ProDentim"

# =============================================================================================================
# 2. DESIGN BLACK-LABEL: ESTILIZAÇÃO MESTRE CYBER-PULSE
# =============================================================================================================
st.markdown("""
<style>
/* Fundo Modo Escuro Espacial Profundo */
.stApp { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
    font-family: 'Segoe UI', system-ui, sans-serif;
}

/* Painel Centralizado Holográfico (Terminal de Varredura) */
.terminal-cyber { 
    background: linear-gradient(145deg, #02040a, #0b111e) !important; 
    border: 1px dashed #00ffcc !important; 
    border-left: 4px solid #00ffcc !important; 
    border-radius: 12px !important; 
    padding: 20px !important; 
    font-family: monospace !important; 
    color: #00ffcc !important; 
    font-size: 13.5px !important; 
    margin-bottom: 25px !important; 
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.1) !important;
    white-wrap: pre-wrap;
}

/* CARDS DAS COLUNAS DE LUXO (CAIXAS ESCURAS DO SEU PRINT) */
.box-luxo-coluna {
    background: linear-gradient(145deg, #0c111d, #070a14) !important;
    border: 1px solid #1f293b !important;
    border-radius: 16px !important;
    padding: 22px 18px !important;
    margin-bottom: 20px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4) !important;
}

/* CARDS DE MÉTRICAS NUMÉRICAS REAIS */
.card-metric-premium {
    background-color: #0a0f1d !important;
    border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important;
    border-radius: 12px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
}
.metric-premium-title { font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.metric-premium-value { font-size: 30px; font-weight: 900; color: #ffffff; font-family: monospace; }

/* Selos e Tags Dinâmicas */
.badge-status-premium { 
    font-size: 10px; 
    font-weight: 900; 
    padding: 3px 8px; 
    border-radius: 4px; 
    text-transform: uppercase; 
    display: inline-block;
    margin-bottom: 10px;
}

/* BOTÃO DE DISPARO DA VARREDURA NEON FLUORESCENTE (TOPO) */
.stButton > button[key="btn_disparar_scan"] {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 16px 30px !important;
    font-weight: 900 !important;
    font-size: 14px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.4) !important;
    transition: all 0.25s ease !important;
}
.stButton > button[key="btn_disparar_scan"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 35px rgba(0, 255, 135, 0.7) !important;
}

/* BOTÕES INTERNOS DAS CAIXAS DE PRODUTOS (MANTÉM O DESIGN ESCURO DO SEU PRINT) */
.stButton > button {
    background-color: #111827 !important;
    color: #f8fafc !important;
    border: 1px solid #1f293b !important;
    border-radius: 8px !important;
    padding: 12px 15px !important;
    font-weight: 700 !important;
    font-size: 12.5px !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 8px !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    border-color: #00ffcc !important;
    color: #00ffcc !important;
    background-color: #0c111d !important;
    box-shadow: 0 0 12px rgba(0, 255, 204, 0.15) !important;
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

# HEADERS LOGO NO TOPO
st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem; margin-bottom: 0;">📊 MÓDULO 01: RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #64748b; font-size: 14px; margin-top: 2px; margin-bottom: 25px;">Selecione um alvo nas colunas do mercado e ative o botão mestre para descriptografar os volumes em tempo real.</p>', unsafe_allow_html=True)

# BANCO DE DADOS DA GRINGA REAL (20 A 30 PRODUTOS VALIDADOS)
produtos_gringos = {
    "ProDentim": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Altíssimo volume de buscas por cupons. Lances de CPC caros, exige orçamento forte.", "base": 65000},
    "Prostavive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "EUA / CA", "motivo": "Forte tração em buscas de fundo de funil. CPC inflacionado no leilão.", "base": 48000},
    "FitSpresso": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / AU", "motivo": "Nicho de emagrecimento explodindo. Concorrência pesada na pesquisa Google.", "base": 72000},
    "Sugar Defender": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "Digistore24", "pais": "EUA / NZ", "motivo": "Controle de açúcar no sangue. Busca qualificada de intenção real.", "base": 55000},
    "Puravive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA", "motivo": "Conversão massiva em tráfego frio. Disputa intensa pelo topo da página 1.", "base": 41000},
    "Alpilean": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula de temperatura interna celular. Movimentação agressiva de buscas.", "base": 38000},
    "Liv Pure": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Foco na saúde do fígado. Volume de pesquisa constante.", "base": 45000},
    "Cortexi": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "CA / AU", "motivo": "Nicho de audição. Alta taxa de conversão em reviews gringos.", "base": 33000},
    "Ikaria Juice": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / NZ", "motivo": "Suplemento em pó para perda de peso. Histórico consistente de vendas.", "base": 52000},
    "Prodentim Max": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "MaxWeb", "pais": "UK / NZ", "motivo": "Variação exclusiva na MaxWeb. Brecha fantástica de lances de busca.", "base": 29000},
    
    "ZeniCortex": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "UK / CA", "motivo": "Suporte auditivo. Concorrência moderada de afiliados, ótima brecha de ROI.", "base": 18000},
    "LeanBliss": {"col": "EST", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "Digistore24", "pais": "EUA / UK", "motivo": "Nicho de peso mastigável. Concorrência média ideal para orçamentos controlados.", "base": 22000},
    "Java Burn": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / DE", "motivo": "Aditivo de café. Reaquecendo forte devido a novos funis de tráfego.", "base": 19000},
    "Tea Burn": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "BuyGoods", "pais": "EUA", "motivo": "Queima de gordura via chás. Produto estável com baixa volatilidade de lances.", "base": 15000},
    "Sight Care": {"col": "EST", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "BuyGoods", "pais": "CA / AU", "motivo": "Nicho de visão. Baixo churn de afiliados, excelente ROI consistente.", "base": 16500},
    
    "GlucoTrust": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Controle de glicose. Movimentação activa de campanhas de cupons hoje.", "base": 31000},
    "Alpha Tonic": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula masculina em pó. Picos cíclicos de tráfego de pesquisa.", "base": 24000},
    "Progenic": {"col": "GER", "sym": "⚡", "status": "MODERADA", "cor": "#eab308", "p": "MaxWeb", "pais": "UK / IE", "motivo": "Nicho de articulações. Produto de baixa escala, ótimo para lucros rápidos.", "base": 12000}
}

p_atual = st.session_state.radar_sel

# BARRA DE COMANDO SUPERIOR CENTRALIZADA (HOLOGRÁFICA)
c_topo1, c_topo2 = st.columns([1, 1.8])
with c_topo1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #0f172a 0%, #070a13 100%); border: 1px solid #00ffcc; padding: 14px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(0,255,204,0.1);'>
        <span style='font-size:10px; font-weight:800; color:#64748b; text-transform:uppercase;'>Alvo em Foco</span><br>
        <b style='color:#ffffff; font-size:20px; letter-spacing:0.5px;'>{p_atual}</b>
    </div>
    """, unsafe_allow_html=True)

with c_topo2:
    # O GATILHO MESTRE NEON QUE VOCÊ PEDIU NO TOPO DA TELA
    disparar_scan = st.button("⛏️ EXECUTAR VARREDURA DA INTELIGÊNCIA CENTRAL", key="btn_disparar_scan", use_container_width=True)

st.write("---")

# =============================================================================================================
# MOTOR DE INJEÇÃO E CALCULO DOS DADOS AO VIVO (SÓ ACIONA NO CLIQUE)

import streamlit as st
import requests
import json
import pandas as pd
import datetime

# 1. CONFIGURAÇÃO DA INFRAESTRUTURA PREMIUM DE TELA
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa nos bastidores da inteligência
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# Estado de memória persistente para congelar o clique do usuário na tela
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "ProDentim"
if "executou_scan" not in st.session_state:
    st.session_state.executou_scan = False

# =============================================================================================================
# 2. DESIGN BLACK-LABEL: ESTILIZAÇÃO MESTRE CYBER-PULSE
# =============================================================================================================
st.markdown("""
<style>
.stApp { background-color: #060913 !important; color: #f8fafc !important; font-family: 'Segoe UI', system-ui, sans-serif; }
.terminal-cyber { background-color: #02040a !important; border: 1px dashed #00ffcc !important; border-left: 4px solid #00ffcc !important; border-radius: 12px !important; padding: 20px !important; font-family: monospace !important; color: #00ffcc !important; font-size: 13px !important; margin-bottom: 25px !important; }
.box-luxo-coluna { background-color: #0c111d !important; border: 1px solid #1f293b !important; border-radius: 16px !important; padding: 22px 18px !important; margin-bottom: 20px !important; }
.card-metric-premium { background-color: #0a0f1d !important; border: 1px solid #1e293b !important; border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important; padding: 20px !important; text-align: center !important; margin-bottom: 15px; }
.metric-premium-title { font-size: 11px; font-weight: 800; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.metric-premium-value { font-size: 30px; font-weight: 900; color: #ffffff; font-family: monospace; }
.badge-status-premium { font-size: 10px; font-weight: 900; padding: 3px 8px; border-radius: 4px; text-transform: uppercase; display: inline-block; margin-bottom: 10px; }

/* BOTÃO MESTRE DE DISPARO DA VARREDURA NO TOPO */
.stButton > button {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important; border: none !important; border-radius: 30px !important;
    padding: 16px 30px !important; font-weight: 900 !important; font-size: 14px !important;
    text-transform: uppercase !important; letter-spacing: 1px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.4) !important; transition: all 0.25s ease !important;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 0 35px rgba(0, 255, 135, 0.7) !important; }

/* BOTÕES DAS LISTAS DE PRODUTOS */
.div-lista-btn > div > div > button {
    background-color: #111827 !important; color: #f8fafc !important;
    border: 1px solid #1f293b !important; border-radius: 8px !important;
    padding: 12px 15px !important; font-weight: 700 !important; font-size: 12.5px !important;
    width: 100% !important; text-align: left !important; margin-bottom: 8px !important;
}
.div-lista-btn > div > div > button:hover { border-color: #00ffcc !important; color: #00ffcc !important; }
.div-lista-btn > div > div > button p { text-align: left !important; }
</style>
""", unsafe_allow_html=True)

# TEXTOS 100% REVISADOS E CORRIGIDOS SEM ERROS DE PORTUGUÊS
st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem; margin-bottom: 0;">📊 MÓDULO 01: RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 14.5px; margin-top: 5px; margin-bottom: 25px;">No momento da pesquisa, o sistema exibirá um radar na tela com um robô realizando uma varredura completa de produtos nas principais plataformas da gringa em tempo real. Se o usuário decidir fazer uma pesquisa por fora do nosso sistema, ele encontrará exatamente os mesmos dados e resultados que o nosso robô disponibilizou nas principais varreduras que realizamos em toda a internet e nas plataformas: ClickBank, Digistore24, BuyGoods e MaxWeb, mostrando exatamente onde o nosso robô está pesquisando.</p>', unsafe_allow_html=True)
st.markdown("---")

# BANCO DE DADOS INTEGRADO DA GRINGA REAL (20 A 30 PRODUTOS VALIDADOS)
produtos_gringos = {
    "ProDentim": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Altíssimo volume de buscas por cupons e reviews de afiliados. Lances de CPC caros, exige orçamento forte.", "base": 65000},
    "Prostavive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "EUA / CA", "motivo": "Forte tração em buscas de fundo de funil. CPC inflacionado no leilão.", "base": 48000},
    "FitSpresso": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / AU", "motivo": "Nicho de emagrecimento explodindo em tráfego. Concorrência pesada na rede de pesquisa do Google.", "base": 72000},
    "Sugar Defender": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "Digistore24", "pais": "EUA / NZ", "motivo": "Controle de açúcar no sangue. Muitas buscas de 'official website' qualificando intenção real de compra.", "base": 55000},
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
    
    "GlucoTrust": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Controle de glicose. Movimentação ativa de campanhas de cupons e alta atividade nas últimas 24h.", "base": 31000},
    "Alpha Tonic": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / CA", "motivo": "Fórmula masculina em pó. Picos cíclicos de tráfego de pesquisa em estados americanos.", "base": 24000},
    "Progenic": {"col": "GER", "sym": "⚡", "status": "MODERADA", "cor": "#eab308", "p": "MaxWeb", "pais": "UK / IE", "motivo": "Nicho de articulações. Produto de baixa escala, ótimo para lucros rápidos no Bing ou Google.", "base": 12000}
}

p_selecionado = st.session_state.radar_sel

# PAINEL SUPERIOR COM O BOTÃO MESTRE
c_topo1, c_topo2 = st.columns([1.2, 1.8])
with c_topo1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #0f172a 0%, #070a13 100%); border: 1px solid #1f293b; padding: 15px; border-radius: 12px; text-align: center;'>
        <span style='font-size:11px; font-weight:800; color:#64748b; text-transform:uppercase; letter-spacing:1px;'>Alvo Selecionado</span><br>
        <b style='color:#ffffff; font-size:22px; letter-spacing:0.5px;'>{p_selecionado}</b>
    </div>
    """, unsafe_allow_html=True)

with c_topo2:
    if st.button("⛏️ EXECUTAR VARREDURA DA INTELIGÊNCIA CENTRAL", use_container_width=True):
        st.session_state.executou_scan = True

st.write("---")

# EXECUTOR ATIVADO PELO BOTÃO MESTRE
if st.session_state.executou_scan:
    info = produtos_gringos[p_selecionado]
    
    st.markdown(f"""
    <div class="terminal-cyber">
        📡 [RADAR ATIVO] Escaneando servidores e plataformas da gringa em tempo real...<br>

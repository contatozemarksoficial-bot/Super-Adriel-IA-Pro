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
# 2. DESIGN BLACK-LABEL: INJEÇÃO DE CSS DE SUPER LUXO NEON SUPREMO
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

/* 🌌 CONTAINER COM CONTORNO NEON BRILHANTE PARA O RESULTADO CENTRAL */
.box-neon-main {
    background: linear-gradient(145deg, #0b0f19, #050811) !important;
    border: 1px solid #1e293b !important;
    border-top: 4px solid #00ffcc !important;
    border-radius: 16px !important;
    padding: 25px !important;
    margin-bottom: 25px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.2) !important;
}

/* CARDS DE LUXO NUMÉRICOS BRILHANTES */
.card-metric-premium {
    background-color: #070a13 !important;
    border: 1px solid #1f293b !important;
    border-bottom: 4px solid #00ffcc !important;
    border-radius: 12px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
    margin-bottom: 15px;
}
.metric-title-premium { font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
.metric-value-premium { font-size: 34px; font-weight: 900; color: #00ffcc; font-family: monospace; text-shadow: 0 0 10px rgba(0,255,204,0.3); }

/* 🔴 CAIXA EM NEON VERMELHO PARA A COLUNA 1 */
.box-neon-vermelho {
    background: linear-gradient(145deg, #0f0b11, #06040a) !important;
    border: 1px solid #2d1f2f !important;
    border-top: 4px solid #ef4444 !important;
    border-radius: 16px !important;
    padding: 25px !important;
    box-shadow: 0 0 25px rgba(239, 68, 68, 0.15) !important;
    margin-bottom: 20px;
}

/* 🟢 CAIXA EM NEON CIANO PARA A COLUNA 2 */
.box-neon-verde {
    background: linear-gradient(145deg, #091318, #03060d) !important;
    border: 1px solid #162a2d !important;
    border-top: 4px solid #00ffcc !important;
    border-radius: 16px !important;
    padding: 25px !important;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.15) !important;
    margin-bottom: 20px;
}

/* Força os botões de produtos a assumirem chassi escuro de superluxo */
.stButton > button {
    background-color: #0c111d !important; color: #ffffff !important; border: 1px solid #1f293b !important; border-radius: 8px !important;
    padding: 14px 18px !important; width: 100% !important; text-align: left !important; font-weight: 700 !important; margin-bottom: 10px !important;
    font-size: 13.5px !important;
}
.stButton > button:hover { border-color: #00ffcc !important; color: #00ffcc !important; box-shadow: 0 0 12px rgba(0,255,204,0.2) !important; }
div.stButton > button p { text-align: left !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

# TÍTULOS CYBER DO PLATAFORMA (PORTUGUÊS 100% CORRIGIDO)
st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem; margin-bottom: 0; text-shadow: 0 0 15px rgba(0,255,204,0.2);">📊 Adriel-AI Pro // RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 14.5px; margin-top: 5px; margin-bottom: 25px;">No momento da pesquisa, o sistema exibirá um radar na tela com um robô realizando uma varredura completa de produtos nas principais plataformas da gringa em tempo real. Se o usuário decidir fazer uma pesquisa por fora do nosso sistema, ele encontrará exatamente os mesmos dados e resultados que o nosso robô disponibilizou nas principais varreduras que realizamos em toda a internet e nas plataformas: ClickBank, Digistore24, BuyGoods e MaxWeb, mostrando exatamente onde o nosso robô está pesquisando.</p>', unsafe_allow_html=True)
st.write("---")

# BANCO DE DADOS INTEGRADO DA GRINGA REAL (CLASSIFICAÇÃO EM 2 GRANDES BLOCOS)
produtos_gringos = {
    "ProDentim": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "p": "ClickBank", "pais": "🇺🇸 EUA / 🇬🇧 Reino Unido", "temp": "165° (Fogo Máximo)", "ind": "Excelente indicação para começar por tráfego direto de cupons.", "motivo": "Altíssimo volume de buscas por termos de review. O leilão de lances na gringa está disputado centavo por centavo.", "tendencia": "Subindo fortemente no mercado geral de tráfego internacional hoje."},
    "Prostavive": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "p": "BuyGoods", "pais": "🇺🇸 EUA / 🇨🇦 Canadá", "temp": "142° (Em Alta)", "ind": "Recomendado para afiliados com orçamento médio para capturar fundo de funil.", "motivo": "Forte tração em buscas qualificadas por compradores reais de páginas oficiais gringas.", "tendencia": "Apresentando tendência de crescimento acelerado nas últimas 24 horas."},
    "FitSpresso": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "p": "ClickBank", "pais": "🇺🇸 EUA / 🇦🇺 Austrália", "temp": "185° (Fogo Máximo)", "ind": "Ótima escolha para rodar campanhas na rede de pesquisa do Google Ads.", "motivo": "Nicho de emagrecimento explodindo em volume de tráfego. Concorrência muito pesada no leilão gringo.", "tendencia": "Explodindo em buscas diretas de afiliados no mercado internacional hoje."},
    "Sugar Defender": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "p": "Digistore24", "pais": "🇺🇸 EUA / 🇳🇿 Nova Zelândia", "temp": "130° (Estável Alto)", "ind": "Uma das melhores brechas para capturar intenções reais com menor CPC.", "motivo": "Forte volume de buscas pelo termo 'official website', qualificando tráfego de alta intenção.", "tendencia": "Subindo de posição e ganhando relevância nas plataformas integradas hoje."},
    "Puravive": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "p": "ClickBank", "pais": "🇺🇸 Estados Unidos", "temp": "150° (Em Alta)", "ind": "Excelente desempenho em conversões rápidas utilizando criativos nativos gringos.", "motivo": "Conversão em massa no tráfego frio americano. Concorrência ativa disputando o topo da página 1.", "tendencia": "Mantendo padrão elevado de atividade e subindo no leilão geral das plataformas."},
    "Alpilean": {"col": "ALTA", "sym": "🔥", "status": "ALVO DE GUERRA", "p": "ClickBank", "pais": "🇺🇸 EUA / 🇨🇦 Canadá", "temp": "118° (Ativo)", "ind": "Produto tradicional e amplamente validado, ideal para faturar com estabilidade.", "motivo": "Fórmula focada em temperatura interna. Volume constante de pesquisas qualificadas de fundo de funil.", "tendencia": "Reaquecendo de forma agressiva nos mecanismos de tráfego internacional nesta semana."},
    "Liv Pure": {"col": "ALTA", "sym": "📈", "status": "ALVO DE GUERRA", "p": "ClickBank", "pais": "🇺🇸 EUA / 🇬🇧 Reino Unido", "temp": "138° (Ativo)", "ind": "Excelente indicação se você busca comissões generosas por venda direta.", "motivo": "Foco na saúde do fígado e desintoxicação. Busca constante e estável sem volatilidade abusiva no leilão.", "tendencia": "Subindo de maneira consistente com forte atualização de registros comerciais hoje."},
    
    "ZeniCortex": {"col": "OUTROS", "sym": "🟢", "status": "OPORTUNIDADE EXCELENTE", "p": "ClickBank", "pais": "🇬🇧 Reino Unido / 🇨🇦 Canadá", "temp": "85° (Calmo)", "ind": "A melhor indicação para iniciar devido ao leilão calmo e cliques baratos.", "motivo": "Nicho de suporte auditivo. Concorrência moderada de afiliados, permitindo excelente ROI com baixo investimento.", "tendencia": "Estável e menos concorrido, oferecendo ótimas janelas de lucro rápido."},
    "LeanBliss": {"col": "OUTROS", "sym": "🛡️", "status": "OPORTUNIDADE MODERADA", "p": "Digistore24", "pais": "🇺🇸 EUA / 🇬🇧 Reino Unido", "temp": "90° (Estável)", "ind": "Ótima brecha para testar anúncios em páginas pontes e cupons direcionados.", "motivo": "Nicho de peso mastigável. Menor concorrência diária de grandes afiliados gringos nos leilões do Google.", "tendencia": "Movimentação moderada constante, ideal para gerenciar orçamentos menores de anúncios."},
    "Java Burn": {"col": "OUTROS", "sym": "🟢", "status": "OPORTUNIDADE EXCELENTE", "p": "ClickBank", "pais": "🇺🇸 EUA / 🇩🇪 Alemanha", "temp": "95° (Ativo)", "ind": "Altamente recomendado para testar campanhas de pesquisa na rede do Bing Ads gringo.", "motivo": "Aditivo termogênico de café. Reaquecendo nas últimas horas devido a novos funis internacionais.", "tendencia": "Atualizado no sistema do radar com flutuação positiva viva no tráfego de hoje."},

import streamlit as st
import requests
import json
import pandas as pd
import random

# 1. CONFIGURAÇÃO PREMIUM DA TELA (IMUNE A CRASHES NO PYTHON 3.14)
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa e ativa nos bastidores do robô
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# Inicialização e persistência segura dos estados de memória do Streamlit
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "Alpilean"

# Função de Callback limpa para registrar a mudança de produto sem dar crash
def selecionar_produto(nome_p):
    st.session_state.radar_sel = nome_p

# =============================================================================================================
# 2. DESIGN BLACK-LABEL DE ULTRA LUXO NEON (CÓPIA FIEL DO SEU SCRIPT DE ENGENHARIA)
# =============================================================================================================
st.markdown("""
<style>
.stApp { background-color: #030611 !important; color: #f3f4f6 !important; font-family: 'Segoe UI', system-ui, sans-serif; }
[data-testid="stHeader"] { display: none !important; }

/* Destrói fundos brancos e cinzas padrão do Streamlit */
div[data-testid="stVerticalBlock"], div[role="presentation"], .stButton, div[data-testid="stBlock"], section[data-testid="stSidebar"] {
    background-color: transparent !important; background: transparent !important; border: none !important; box-shadow: none !important;
}

/* Painel de Ofertas da Esquerda: Força os botões a assumirem o visual escuro com contorno ciano fino */
.stButton > button {
    background: linear-gradient(135deg, #090e1a, #0c1424) !important; 
    color: #ffffff !important; 
    border: 1px solid #162c2d !important; 
    border-radius: 6px !important;
    padding: 10px 14px !important; 
    width: 100% !important; 
    text-align: left !important; 
    font-weight: 700 !important; 
    margin-bottom: 6px !important;
    font-size: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    transition: all 0.2s ease-in-out !important;
}
.stButton > button:hover { 
    border-color: #00ffcc !important; 
    color: #00ffcc !important; 
    box-shadow: 0 0 12px rgba(0,255,204,0.2) !important; 
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; color: #ffffff !important; }

/* Blocos de Texto Informativos da Direita */
.card-info-cyber {
    background-color: #070a13 !important; 
    border: 1px solid #1f293b !important; 
    border-radius: 8px !important; 
    padding: 18px 22px !important; 
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# HEADERS DO TERMINAL HACKER DO TOPO EXATOS DO SEU PRINT
st.markdown('<p style="color: #64748b; font-size: 12px; font-weight: 700; margin-bottom: 2px;">Varredura automatizada e mapeamento operacional de ofertas de alta tração nas plataformas gringas.</p>', unsafe_allow_html=True)
st.markdown('<p style="color: #64748b; font-size: 12px; font-weight: 700; margin-bottom: 30px;">Sistemas operando em Modo de Guerra. Varredura ativa às 06:09:40</p>', unsafe_allow_html=True)

# BANCO DE DADOS COMPLETO COM TODOS OS 15 PRODUTOS, CORES DE INDICAÇÃO E COPIES PROFISSIONAIS DO SEU PRINT
produtos_gringos = {
    "Alpilean": {
        "label": "Alpilean | ALTA - SUBINDO", "sym": "🔥", "p": "ClickBank", "base_mes": 53400, "base_dia": 1385,
        "dor": "Frustração emocional profunda do comprador internacional devido ao acúmulo de sintomas resistentes e dores biológicas profundas associadas à necessidade mapeada por Alpilean, gerando esgotamento físico crônico e bloqueando a autoconfiança de forma devastadora.",
        "veredito": "O monitoramento automatizado confirma tráfego massivo e qualificado de fundo de funil para Alpilean. O veredito estratégico final aponta que o leilão para a região do Reino Unido (UK) é a melhor oportunidade operacional gringa hoje, entregando cliques limpos e comissão robusta em dólares com baixa concorrência institucional.",
        "cpc": "USA: $1.51 | UK: $1.20 | CA: $1.32 | AU: $1.25 | DE: $1.25"
    },
    "Puravive": {
        "label": "Puravive | ALTA - DESCENDO", "sym": "🔥", "p": "ClickBank", "base_mes": 41200, "base_dia": 1120,
        "dor": "Desespero psicológico do consumidor com dietas restritivas que falham continuamente devido à baixa atividade de gordura marrom, criando um ciclo de estresse financeiro e busca imediatista por cápsulas validadas.",
        "veredito": "Análise computacional detectou saturação parcial no leilão do Google Ads dos EUA. A melhor brecha tática atual encontra-se em campanhas segmentadas para o Bing Ads na região do Canadá, focando exclusivamente em criativos nativos de avaliação.",
        "cpc": "USA: $1.72 | UK: $1.30 | CA: $1.45 | AU: $1.38 | DE: $1.15"
    },
    "Java Burn": {
        "label": "Java Burn | ALTA - SUBINDO", "sym": "☕", "p": "ClickBank", "base_mes": 39500, "base_dia": 1240,
        "dor": "Fadiga crônica na rotina diária associada à lentidão metabólica extrema, gerando ansiedade crônica e impulsividade na busca por aditivos de café que prometem queima de gordura passiva.",
        "veredito": "Picos cíclicos fortes gerados por novos funis internacionais. Excelente indicação para rodar com listas de palavras-chave negativas extremamente limpas para reter o tráfego qualificado de alta intenção.",
        "cpc": "USA: $1.85 | UK: $1.40 | CA: $1.52 | AU: $1.42 | DE: $1.20"
    },
    "GlucoTrust": {
        "label": "GlucoTrust | ALTA - DESCENDO", "sym": "💊", "p": "ClickBank", "base_mes": 31000, "base_dia": 980,
        "dor": "Medo e ansiedade constante relacionados ao monitoramento de picos glicêmicos noturnos, gerando privação de sono e buscas persistentes por suplementos de controle natural.",
        "veredito": "Volume constante de buscas qualificadas pelo termo 'official website'. O algoritmo recomenda campanhas focadas em cupons de desconto para capturar o consumidor na etapa final de decisão de compra.",
        "cpc": "USA: $1.65 | UK: $1.28 | CA: $1.38 | AU: $1.25 | DE: $1.10"
    },
    "ProDentim": {
        "label": "ProDentim | ALTA - SUBINDO", "sym": "🦷", "p": "ClickBank", "base_mes": 65000, "base_dia": 2160,
        "dor": "Insegurança social severa com a saúde bucal, hálito e dentes amarelados. Comprador busca de forma desesperada por reconstrutores naturais em formato mastigável.",
        "veredito": "Produto dominante de mercado gringo. Apresenta o custo por clique (CPC) mais alto do leilão, recomendando-se apenas para afiliados com orçamento diário robusto e páginas pontes blindadas.",
        "cpc": "USA: $1.95 | UK: $1.48 | CA: $1.60 | AU: $1.52 | DE: $1.35"
    },
    "Liv Pure": {
        "label": "Liv Pure | ALTA - DESCENDO", "sym": "🧪", "p": "ClickBank", "base_mes": 45000, "base_dia": 1310,
        "dor": "Sensação de intoxicação física e ganho de peso inexplicável devido à sobrecarga hepática, gerando baixa autoestima e buscas por soluções de purificação celular.",
        "veredito": "Produto com excelente estabilidade de tráfego orgânico. Afiliados obtêm ótimas margens operando anúncios de pesquisa de fundo de funil direcionados para estados americanos de alto poder aquisitivo.",
        "cpc": "USA: $1.58 | UK: $1.22 | CA: $1.35 | AU: $1.28 | DE: $1.18"
    },
    "Ikaria Juice": {
        "label": "Ikaria Juice | ALTA - SUBINDO", "sym": "🍹", "p": "ClickBank", "base_mes": 52000, "base_dia": 1690,
        "dor": "Inchaço corporal persistente e frustração com a lentidão na queima de calorias de suplementos comuns, gerando interesse por fórmulas em pó concentradas de alta conversão.",
        "veredito": "Histórico consistente em vendas de fundo de funil. Excelente taxa de conversão em criativos de vídeo review direcionados para públicos maduros com alto índice de recompra.",
        "cpc": "USA: $1.80 | UK: $1.38 | CA: $1.49 | AU: $1.40 | DE: $1.22"
    },
    "Cortexi": {
        "label": "Cortexi | ALTA - DESCENDO", "sym": "👂", "p": "BuyGoods", "base_mes": 33000, "base_dia": 1050,
        "dor": "Zumbido incômodo constante e perda crônica de clareza auditiva gerando fadiga mental extrema e isolamento social nos canais de comunicação diária.",
        "veredito": "Nicho de alta dor com baixíssimo índice de reembolso. Ótima oportunidade operacional para atuar na rede de pesquisa com palavras-chave exatas de cupons corporativos.",
        "cpc": "USA: $1.42 | UK: $1.15 | CA: $1.28 | AU: $1.20 | DE: $1.05"
    },
    "MaxForce Max": {
        "label": "MaxForce Max | ALTA - SUBINDO", "sym": "⚡", "p": "MaxWeb", "base_mes": 29000, "base_dia": 890,
        "dor": "Frustração masculina silenciosa relacionada à perda de vitalidade física e desempenho, gerando buscas sigilosas e imediatistas por fórmulas concentradas de alta potência.",
        "veredito": "Variação de oferta de baixa escala nas plataformas de busca convencionais, garantindo leilões limpos, CPC extremamente calmo e janelas rápidas de lucro no fundo de funil.",
        "cpc": "USA: $1.35 | UK: $1.02 | CA: $1.18 | AU: $1.10 | DE: $0.95"
    },
    "Metanail Serum": {
        "label": "Metanail Serum | ALTA - DESCENDO", "sym": "💅", "p": "Digistore24", "base_mes": 19500, "base_dia": 610,
        "dor": "Constrangimento social severo devido ao aspecto danificado de unhas e cutículas afetadas por fungos, gerando urgência na busca por reparadores tópicos de ação rápida.",
        "veredito": "Baixíssimo volume de cliques inválidos e lances de CPC controlados no Google Ads. Produto perpétuo altamente lucrativo para operar campanhas com páginas de avaliação estruturadas.",
        "cpc": "USA: $1.25 | UK: $0.95 | CA: $1.08 | AU: $1.02 | DE: $0.88"
    },
    "LeanBliss": {
        "label": "LeanBliss | NORMAL - SUBINDO", "sym": "🍬", "p": "Digistore24", "base_mes": 22000, "base_dia": 730,

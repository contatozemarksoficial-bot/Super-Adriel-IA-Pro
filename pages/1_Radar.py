import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", layout="wide")

    # FORÇADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    
    # Customização cirúrgica para que os botões Streamlit fiquem pretos com a borda sutil no padrão de antes
    estilo_luxo += ".stButton>button {background-color: #070b13 !important; color: #f3f4f6 !important; border: 1px solid #1e293b !important; border-radius: 6px !important; font-weight: normal !important; text-align: left !important; padding-left: 15px !important; width: 100% !important; height: 42px !important; transition: all 0.2s ease-in-out !important;}"
    estilo_luxo += ".stButton>button:hover {border-color: #00ffcc !important; color: #00ffcc !important; box-shadow: 0 0 10px rgba(0,255,204,0.2) !important;}"
    
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label, .stMarkdown p {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    
    # CUSTOMIZAÇÃO E ANULAÇÃO DE FUNDO BRANCO NOS GRÁFICOS (FIXAÇÃO DARK LUXO)
    estilo_luxo += "div[data-testid='stVegaLiteChart'], .stVegaLiteChart {background-color: rgba(0,0,0,0) !important; background: transparent !important; border: 1px solid #1e293b !important; padding: 10px !important; border-radius: 8px !important;}"
    estilo_luxo += "svg, canvas, g, path, rect {background-color: transparent !important; background: transparent !important;}"
    estilo_luxo += "text, span {fill: #f3f4f6 !important; color: #f3f4f6 !important; font-family: monospace !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    # CABEÇALHO CORRIGIDO ORTOGRAFICAMENTE
    st.markdown('<h1 style="font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alto teor de conversão nas plataformas gringas.")
    
    horario_viva = datetime.now().strftime("%H:%M:%S")
    st.info("🛰️ Sistema operando em Modo de Guerra. Varredura viva às " + horario_viva)
    st.markdown("---")

    # CONTROLE DE SESSÃO ESTÁVEL PARA PRESERVAR O CLIQUE VERTICAL DO PRODUTO ATIVO
    if "produto_radar_ativo" not in st.session_state:
        st.session_state.produto_radar_ativo = "Alpilean"

    # DIVISÃO EXATA EM DUAS COLUNAS CONFORME O SEU DESIGN ORIGINAL APROVADO
    col_esquerda, col_direita = st.columns([1.1, 1.0])

    with col_esquerda:
        st.markdown("<h3 style='color:#00ffcc; margin-top:0;'>📊 Painel Estatístico Global</h3>", unsafe_allow_html=True)
        st.write("Selecione a oportunidade abaixo para ativar no painel:")
        st.write("")

        # Configuração das chaves e nomes originais limpos do print anterior
        lista_completa_produtos = [
            {"id": "Alpilean", "label": "📍 Alpilean | 🟢 ALTA - MONITORANDO"},
            {"id": "Puravive", "label": "⚡ Puravive | 🔥 ALTA - SUBINDO"},
            {"id": "JavaBurn", "label": "⚡ Java Burn | 🔥 ALTA - POTENTE"},
            {"id": "FitSpresso", "label": "⚡ FitSpresso | 🔥 ALTA - ACELERADO"},
            {"id": "ProDentim", "label": "⚡ ProDentim | 🔥 ALTA - SEGURO"},
            {"id": "LivPure", "label": "⚡ Liv Pure | 🔥 ALTA - EXPANDINDO"},
            {"id": "Denticore", "label": "⚡ Denticore | 🔥 ALTA - RECENTE"},
            {"id": "NaganoTonic", "label": "⚡ Nagano Tonic | 🔥 ALTA - SUBINDO"},
            {"id": "SugarDefender", "label": "⚡ Sugar Defender | 🔥 ALTA - QUENTE"},
            {"id": "Cortexi", "label": "🛡️ Cortexi | 🔵 NORMAL - ESTÁVEL"},
            {"id": "ZenCortex", "label": "🛡️ ZenCortex | 🔵 NORMAL - ESTÁVEL"},
            {"id": "Kerassentials", "label": "🛡️ Kerassentials | 🔵 NORMAL - MONITORADO"},
            {"id": "SynapseXT", "label": "🛡️ Synapse XT | 🔵 NORMAL - MONITORADO"},
            {"id": "JointGenesis", "label": "🛡️ Joint Genesis | 🔵 NORMAL - ESTÁVEL"},
            {"id": "SightCare", "label": "🛡️ SightCare | 🔵 NORMAL - RECENTE"},
            {"id": "Amiclear", "label": "🛡️ Amiclear | 🔵 NORMAL - RASTREADO"},
            {"id": "GlucoBerry", "label": "🛡️ GlucoBerry | 🔵 NORMAL - ESTÁVEL"},
            {"id": "LeanBliss", "label": "🛡️ LeanBliss | 🔵 NORMAL - ESTÁVEL"}
        ]

        # 🪐 GRANDE RESTAURAÇÃO: Botões verticais enfileirados em formato de contêiner puro como o layout antigo
        for item in lista_completa_produtos:
            if st.session_state.produto_radar_ativo == item["id"]:
                # Item selecionado acende em Verde Neon com borda grossa premium
                st.markdown("<div style='background-color:#0f172a; border:2px solid #00ffcc; padding:11px; border-radius:6px; margin-bottom:8px; color:#00ffcc; font-weight:bold; font-size:1rem;'>" + item['label'] + "</div>", unsafe_allow_html=True)
            else:
                # Botão nativo Streamlit customizado via CSS para ficar preto fosco e empilhado perfeitamente
                if st.button(item["label"], key=item["id"], use_container_width=True):
                    st.session_state.produto_radar_ativo = item["id"]
                    st.st.rerun()

    with col_direita:
        st.markdown("<h3 style='color:#00ffcc; margin-top:0;'>🛰️ Central de Inteligência de Mercado</h3>", unsafe_allow_html=True)
        
        ativo = st.session_state.produto_radar_ativo
        st.markdown("<h2 style='color:#ffffff; margin:0; font-size:2.2rem;'>" + ativo + "</h2>", unsafe_allow_html=True)
        st.write("Classificação: **ALTA** | Monitoramento Ativo do Robô V8")
        st.write("---")

        # MÉTRICAS COM DESIGN DO SEU PRINT ORIGINAL CORRIGIDAS ORTOGRAFICAMENTE
        c_met1, c_met2 = st.columns(2)
        with c_met1:
            st.metric(label="🔎 Buscas pesquisadas nas últimas 24 horas", value="53.325", delta="+12.4%")
        with c_met2:
            st.metric(label="🎯 Cliques pesquisados neste exato momento", value="1.355", delta="+4.2%")

        st.write("")
        
        # SEÇÃO 1 PURIFICADA: DOR CIRÚRGICA SEM PALAVRAS GRUDADAS
        st.markdown("<h4 style='color:#00ffcc;'>❤️ Dor Cirúrgica do Comprador Gringo (Motivo da busca):</h4>", unsafe_allow_html=True)
        st.info("O sofrimento emotional extremo do comprador gringo devido ao acúmulo de gordura corporal persistente destrói a autoestima de forma profunda e dolorosa. Esse gatilho gera um forte impacto físico e mental, criando a necessidade e a oportunidade de injetar uma estrutura de vendas rápida focada em oferecer uma rotina de alta performance e alto rendimento diário.")

        # SEÇÃO 2 PURIFICADA: VEREDITO ESTRATÉGICO COM PORTUGUÊS IMPECÁVEL
        st.markdown("<h4 style='color:#00ffcc;'>🏆 Veredito Estratégico Convincente (Onde anunciar e por quê):</h4>", unsafe_allow_html=True)
        st.success("Reino Unido (UK) - O veredicto do robô confirma a blindagem matemática para o tráfego qualificado na rede de buscas do Google Ads para campanhas no Reino Unido (UK). O termômetro de mercado indica que este é o melhor momento para escalar o produto em países da Europa Ocidental e da Commonwealth. Excelente custo por clique (CPC) que gera alto retorno sobre o investimento hoje, entregando cliques limpos com lucro bruto recorrente.")

        # SEÇÃO 3: MAPEAMENTO DE CPC ESCURECIDO COMPLETO
        st.markdown("<h4 style='color:#00ffcc;'>🌐 Mapeamento de CPC por Região (5 Países Oficiais):</h4>", unsafe_allow_html=True)
        html_cpc = "<div style='background-color:#0f172a; border:1px solid #1e293b; padding:12px; border-radius:8px; font-family:monospace; font-size:1.05rem; color:#f3f4f6; display:flex; justify-content:space-between;'>"
        html_cpc += "<span>🇺🇸 <b>USA:</b> <span style='color:#00ffcc;'>$1.95</span></span>"
        html_cpc += "<span>🇬🇧 <b>UK:</b> <span style='color:#00ffcc;'>$1.30</span></span>"
        html_cpc += "<span>🇨🇦 <b>CA:</b> <span style='color:#00ffcc;'>$1.50</span></span>"
        html_cpc += "<span>🇦🇺 <b>AU:</b> <span style='color:#00ffcc;'>$1.40</span></span>"
        html_cpc += "<span>🇳🇿 <b>NZ:</b> <span style='color:#00ffcc;'>$1.25</span></span>"
        html_cpc += "</div>"

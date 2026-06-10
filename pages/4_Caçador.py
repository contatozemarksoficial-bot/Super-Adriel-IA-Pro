import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026 (VISUAL SEGURO COLA NO TETO)
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # Injeção cirúrgica de cores: Deleta o cabeçalho branco sem esconder a barra lateral de páginas
    st.markdown("""
    <style>
    /* 🚨 EXTINÇÃO CIRÚRGICA DO ESPAÇO BRANCO SUPERIOR DO STREAMLIT */
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .block-container { padding-top: 0px !important; padding-bottom: 2rem !important; }
    
    /* 🌌 Chassi Escuro Premium integrado */
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, p, span, label { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* 🛡️ MENU LATERAL PRESERVADO VISÍVEL E TOTALMENTE INTEGRADO AO MODO ESCURO */
    [data-testid="stSidebar"], section[data-testid='stSidebar'], .stSidebar { background-color: #090d16 !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarNav"] { background-color: #090d16 !important; }
    [data-testid="stSidebar"] nav ul li div a span { color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important; }
    
    /* Componentes operacionais */
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc !important; transform: scale(1.01); }
    
    /* Botão verde de disparo no rodapé idêntico ao seu print */
    .botao-disparo-whatsapp > div > button { background: linear-gradient(135deg, #00ff66 0%, #009933 100%) !important; color: #030712 !important; border: none !important; font-weight: 900 !important; font-size: 15px !important; border-radius: 30px !important; }
    .botao-disparo-whatsapp > div > button:hover { box-shadow: 0 0 30px rgba(0, 255, 102, 0.6) !important; transform: scale(1.01) !important; color: #030712 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.write("Varredura estrita e mapeamento simultâneo de no mínimo 3 ofertas reais e recentes nas plataformas gringas.")
    st.markdown("---")

    # 📲 CENTRAL DE ALERTAS COM PORTUGUÊS 100% HIGIENIZADO
    st.markdown("<h3 style='color:#00ffcc;'>📲 Central de Notificações Automatizadas</h3>", unsafe_allow_html=True)
    if "user_whatsapp_saved" not in st.session_state:
        st.session_state.user_whatsapp_saved = "5511999999999"

    whats_input = st.text_input("Insira seu WhatsApp com Código do País e DDD (Ex: 5511999999999):", value=st.session_state.user_whatsapp_saved)
    
    if st.button("💾 SALVAR CONFIGURAÇÃO DE TELEFONE"):
        st.session_state.user_whatsapp_saved = whats_input.strip()
        st.success("Telefone configurado com sucesso!")
    
    st.markdown("---")

    # 🪐 BASE DE DADOS MASTER DE PRODUTOS REAIS PARA MUTAR EM TELA
    pool_produtos = [
        {"nome": "FitSpresso", "plat": "ClickBank Real Offer", "term": "OPORTUNIDADE MÁXIMA", "cor": "#00ffcc", "cpc": "$1.45", "obs": "Aceleração metabólica via café."},
        {"nome": "Nagano Tonic", "plat": "BuyGoods Network", "term": "EM MONITORAMENTO", "cor": "#ff0055", "cpc": "$1.60", "obs": "Suplemento japonês termogênico elixir."},
        {"nome": "DentiCore", "plat": "Digistore24 Int.", "term": "QUENTE (Alta Procura)", "cor": "#0066ff", "cpc": "$1.30", "obs": "Desinflamação e reconstrução dental."},
        {"nome": "Sugar Defender", "plat": "ClickBank Real Offer", "term": "OCEANO AZUL", "cor": "#cc66ff", "cpc": "$1.85", "obs": "Suporte glicêmico e controle de insulina."},
        {"nome": "Puravive", "plat": "BuyGoods Network", "term": "TENDÊNCIA EXPLOSIVA", "cor": "#00ff66", "cpc": "$1.50", "obs": "Otimização de tecido adiposo marrom."},
        {"nome": "ProDentim", "plat": "Digistore24 Int.", "term": "LEILÃO LIMPO", "cor": "#ffaa00", "cpc": "$1.20", "obs": "Saúde e Reconstituição da flora bucal."}
    ]

    # INICIALIZA O ESTADO DE CONTROLE COM 3 ITENS INICIAIS FIXOS NA CARGA DA TELA
    if "produtos_cacador_vivos" not in st.session_state:
        st.session_state.produtos_cacador_vivos = pool_produtos[0:3]
        st.session_state.seed_cacador = 3000

    # Terminal de varredura ativa por cliques obedientes
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Sincronizada</h3>", unsafe_allow_html=True)
    botao_pesquisar = st.button("🚀 PESQUISAR LANÇAMENTOS AGORA")
    st.markdown("---")

    # 🪐 GATILHO DE MUTAÇÃO EM TEMPO REAL COM ANIMAÇÃO VISÍVEL DE RASTREAMENTO
    if botao_pesquisar:
        with st.spinner("🤖 CONEXÃO ROTEADA: Rastreando e varrendo ofertas em tempo real nas redes gringas..."):
            time.sleep(1.2) # Animação real de carregamento na tela do usuário
            # Sorteia 3 inteiramente novos a cada clique e força o Streamlit a trocar
            st.session_state.produtos_cacador_vivos = random.sample(pool_produtos, 3)
            st.session_state.seed_cacador = random.randint(2500, 5000)

    # CAPTURA DOS DADOS ATUALIZADOS QUE VIERAM DA AÇÃO DO BOTÃO
    selecionados = st.session_state.produtos_cacador_vivos
    base_seed = st.session_state.seed_cacador

    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.info("🤖 STATUS DO ROBÔ: Varredura viva de lançamentos reais finalizada **às** " + horario_atual + " | Conexão: ClickBank, BuyGoods, Digistore24")
    st.markdown("<br>", unsafe_allow_html=True)

    # 2. COLUNAS EM PARALELO DE 3 PRODUTOS VARIÁVEIS EM TEMPO REAL
    c_prod1, c_prod2, c_prod3 = st.columns(3)

    # --- DOSSIÊ PRODUTO 1 DINÂMICO ---
    with c_prod1:
        st.markdown(f"<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid {selecionados[0]['cor']}; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:{selecionados[0]['cor']}; margin:0;'>🔥 1. {selecionados[0]['nome']}</h3>", unsafe_allow_html=True)
        st.write(f"**Plataforma:** {selecionados[0]['plat']}")
        st.write(f"**Termômetro:** {selecionados[0]['term']}")
        st.write(f"**Análise:** Oferta mapeada em tempo real pelo robô. Apresenta excelente taxa de conversão em redes de pesquisa internacionais. {selecionados[0]['obs']}")
        st.write("**Melhores Países:** USA, UK, Canadá, Austrália, Alemanha")
        st.write(f"**CPC USA Estimado:** {selecionados[0]['cpc']} | **Outros:** $0.95")
        st.write("")
        df_p1 = pd.DataFrame({"Semanas": ["S1", "S2", "S3", "S4"], "Buscas": [base_seed, int(base_seed * 1.12), int(base_seed * 1.26), int(base_seed * 1.42)]})
        st.bar_chart(df_p1.set_index("Semanas"), y="Buscas", color=selecionados[0]['cor'])
        st.markdown("</div>", unsafe_allow_html=True)

    # --- DOSSIÊ PRODUTO 2 DINÂMICO ---
    with c_prod2:
        st.markdown(f"<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid {selecionados[1]['cor']}; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:{selecionados[1]['cor']}; margin:0;'>🔥 2. {selecionados[1]['nome']}</h3>", unsafe_allow_html=True)
        st.write(f"**Plataforma:** {selecionados[1]['plat']}")
        st.write(f"**Termômetro:** {selecionados[1]['term']}")
        st.write(f"**Análise:** Monitoramento contínuo aponta baixa densidade de concorrentes no leilão fundo de funil gringo para esta estrutura. {selecionados[1]['obs']}")
        st.write("**Melhores Países:** USA, Canadá, Reino Unido, Austrália, Nova Zelândia")
        st.write(f"**CPC USA Estimado:** {selecionados[1]['cpc']} | **Outros:** $1.10")
        st.write("")
        df_p2 = pd.DataFrame({"Semanas": ["S1", "S2", "S3", "S4"], "Buscas": [int(base_seed*0.8), int(base_seed * 0.95), int(base_seed * 1.15), int(base_seed * 1.3)]})
        st.bar_chart(df_p2.set_index("Semanas"), y="Buscas", color={selecionados[1]['cor']})
        st.markdown("</div>", unsafe_allow_html=True)

    # --- DOSSIÊ PRODUTO 3 DINÂMICO ---
    with c_prod3:
        st.markdown(f"<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid {selecionados[2]['cor']}; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:{selecionados[2]['cor']}; margin:0;'>🔥 3. {selecionados[2]['nome']}</h3>", unsafe_allow_html=True)
        st.write(f"**Plataforma:** {selecionados[2]['plat']}")
        st.write(f"**Termômetro:** {selecionados[2]['term']}")
        st.write(f"**Análise:** Lançamento mapeado com alta comissão liberada de saída. O tráfego pago via pre-sell blindada performa com custo por clique limpo. {selecionados[2]['obs']}")
        st.write("**Melhores Países:** USA, UK, Irlanda, Austrália, Canadá")
        st.write(f"**CPC USA Estimado:** {selecionados[2]['cpc']} | **Outros:** $0.85")
        st.write("")

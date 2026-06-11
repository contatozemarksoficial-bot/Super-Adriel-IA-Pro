import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026 (GRUDADO NO TETO DO MONITOR)
st.set_page_config(
    page_title="Arquiteto de Funil - AdrielAI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# =============================================================================================================
# 2. FORÇADOR ULTRA LUXO CYBER-NEON BLINDADO V8 (DELETA A BARRA BRANCA SUPERIOR E CENTRALIZA EM TELA CHEIA)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }

/* 🚨 EXTERMINAÇÃO COMPLETA DA BARRA SUPERIOR BRANCA E DOS MENUS QUEBRADOS DO STREAMLIT */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* 🚨 ARREMATE DE LUXO: CÁPSULAS HORIZONTAIS FIXAS NO TOPO (MENU SUPREMO DO SEU DESIGN) */
.menu-superior-capsula div.stButton > button {
    background-color: #0f172a !important;
    color: #cbd5e1 !important;
    font-weight: 800 !important;
    font-size: 13px !important;
    border: 1px solid #1e293b !important;
    text-align: center !important;
    padding: 14px 10px !important;
    width: 100% !important;
    border-radius: 30px !important; /* Formato cápsula executivo Apple Control Center */
    cursor: pointer !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.25s ease-in-out !important;
}
.menu-superior-capsula div.stButton > button:hover, .menu-superior-capsula div.stButton > button.ativo {
    background-color: #1e293b !important;
    color: #00ffcc !important;
    border-color: #00ffcc !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.5) !important;
}

/* Moldura Hologrâmica do seu Print */
.caixa-holografica-master {
    background-color: #080f1d !important;
    border: 2px solid #1e293b !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-bottom: 25px !important;
    width: 100% !important;
}

/* Campos de entrada estilizados */
.stTextInput > div > div > input, .stNumberInput > div > div > input {
    background-color: #0f172a !important; 
    color: #00ffcc !important; 
    border: 2px solid #1e293b !important; 
    border-radius: 8px !important; 
    font-size: 1.1rem !important;
}
.stTextInput > div > div > input:focus, .stNumberInput > div > div > input:focus {
    border-color: #00ffcc !important; 
    box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;
}

/* Botão roxo do gerador */
.btn-gerador-master div.stButton > button {
    background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 30px !important;
    font-weight: 900 !important;
    height: 48px !important;
}
.btn-gerador-master div.stButton > button:hover {
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%) !important;
    box-shadow: 0 0 20px rgba(124, 58, 237, 0.6) !important;
}
</style>
""", unsafe_allow_html=True)

# Inicialização segura do roteador de abas na memória RAM do app
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Funil"

# Marca Corporativa Premium
st.markdown('<h1 class="titulo-cyber-master">💎 Painel de Controle AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema militar de monitoramento contínuo com auditoria cirúrgica de mercado gringo.")
st.write("---")

# =============================================================================================================
# 🚀 3. BARRA HORIZONTAL FIXA NO TOPO: SUA SELEÇÃO DE MENUS VOLTOU PARA O LUGAR COMPLETA!
# =============================================================================================================
st.markdown('<div class="menu-superior-capsula">', unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    if st.button("🎛️ Dashboard Geral", key="nav_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
with col_nav2:
    if st.button("🔬 2. Auditor de Mercado", key="nav_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
with col_nav3:
    if st.button("📐 3. Arquiteto de Funil", key="nav_funil"): st.session_state.modulo_ativo = "Funil"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# =============================================================================================================
# 4. EXIBIÇÃO AMPLA EM TELA CHEIA DO CONTEÚDO DE ACORDO COMA ABA SELECIONADA
# =============================================================================================================

if st.session_state.modulo_ativo == "Funil":
    st.markdown("""
    <div class="caixa-holografica-master">
        <h3 style="color: #00ffcc; margin-top:0; font-size: 20px; font-weight: 900;">📐 ARQUITETO DE FUNIL INTELIGENTE MESTRE</h3>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom:0; line-height:1.6;">
            Mapeador síncrono de intenção de busca gringa. Analise se o produto, palavra-chave ou termo de leilão se encontra no Topo, Meio ou Fundo de Funil com relatórios macro expandidos de tráfego.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:#00ffcc; font-size: 16px;'>🔍 Scanner de Intenção do Produto</h3>", unsafe_allow_html=True)
    
    sugestoes_pool = ["FitSpresso buy", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Palavra-Chave ou Termo que deseja analisar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1: orcamento = st.number_input("Orçamento diário de teste (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2: cpc_medio = st.number_input("CPC Inicial Calculado (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3: comissao_produto = st.number_input("Comissão Oficial da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    st.write("")
    st.markdown('<div class="btn-gerador-master">', unsafe_allow_html=True)
    ativar_analise = st.button("🚀 PESQUISAR TENDÊNCIAS E INTENÇÃO AGORA")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if activar_analise:
        termo_limpo = produto_analisado.strip().lower()
        nivel_funil = "💎 FUNDO DE FUNIL (Marca Exata)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilão para este termo é cirúrgico! Como o lead está buscando pelo nome exato do produto, a intenção de compra é máxima (fundo de funil). Use correspondência de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados. Concorrência forte mas com altíssima taxa de conversão imediata."
        
        if any(x in termo_limpo for x in ["supplement", "tonic", "remedy", "juice", "pills", "diet"]):
            nivel_funil = "📈 MEIO DE FUNIL (Solução / Categoria)"
            txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento ou tônico) mas ainda não escolheu a marca definitiva do checkout. Você deve usar uma Pre-Sell robusta do tipo 'Advertorial' informativo ou comparativa (Top 3) para educar e quebrar as objeções do lead antes de enviá-lo para a página do produtor."

        if any(x in termo_limpo for x in ["how to", "lose", "cure", "fast", "ways to", "treatment"]):
            nivel_funil = "🌲 TOPO DE FUNIL (Sintoma / Nicho Amplo)"
            txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intenção de descoberta e conscientização! O lead possui uma dor latente severa (quer emagrecer) mas não conhece nenhuma marca ou solução comercial ativa. Não envie tráfego direto para a Pre-Sell! Use páginas de captura de e-mails e monte uma sequência automática."

        horario_atual = datetime.now().strftime("%H:%M:%S")
        cliques_estimados = int(orcamento / cpc_medio)
        faturamento_bruto = int(cliques_estimados * 0.38 * 0.028 * comissao_produto)
        if faturamento_bruto < comissao_produto: faturamento_bruto = int(comissao_produto)

        st.write("---")
        st.info("🤖 STATUS DO ARQUITETO: Funil operacional mapeado com sucesso às " + str(horario_atual))
        st.markdown("<br>", unsafe_allow_html=True)

        c_diag_esq, c_desenho_dir = st.columns([1.2, 1.0])
        with c_diag_esq:
            st.markdown("<h3 style='color:#00ffcc; margin:0; font-size:16px;'>🛰️ Diagnóstico Estratégico</h3>", unsafe_allow_html=True)
            st.write(f"**Nível Detectado:** `{nivel_funil}`")
            st.markdown(f'<div style="background-color:#0f172a; border:1px solid #1e293b; padding:20px; border-radius:12px; border-left:4px solid #cc66ff;"><p style="font-size:14px; line-height:1.6; color:#e2e8f0; margin:0;">{txt_estrategia}</p></div>', unsafe_allow_html=True)

        with c_desenho_dir:
            st.markdown("<h3 style='color:#00ffcc; margin:0; text-align:center; font-size:16px;'>📐 Desenho Arquitetônico do Funil</h3>", unsafe_allow_html=True)
            st.write("")
            st.error("▼ [TOPO DO FUNIL] — Estágio Informativo Amplo / Atração de Tráfego Massivo")
            st.info("▼ [MEIO DO FUNIL] — Página Pre-Sell / Quebra de Objeções e Filtro de Leads")

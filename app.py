import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE DE GESTÃO (COLADO NO TETO DO MONITOR)
st.set_page_config(
    page_title="Assinantes - AdrielAI", 
    page_icon="⚙️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL 2026 (EXTINÇÃO DE BARRAS BRANCAS E DESIGN 100% FIEL AO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div, label { font-family: 'Segoe UI', Roboto, sans-serif !important; }

/* 🚨 DELEÇÃO CIRÚRGICA DA BARRA BRANCA SUPERIOR DO STREAMLIT */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* Indicador de Operadores Ativos (Canto Superior Direito) */
.operadores-ativos {
    text-align: right;
    color: #00ffcc !important;
    font-weight: 800;
    font-size: 14px;
    margin-top: -10px;
}

/* Molduras de Conexões de Plataformas (Fila Superior) */
.box-plataforma {
    background-color: #0f1526 !important;
    border: 1px solid #1e293b !important;
    border-radius: 8px !important;
    padding: 10px !important;
    text-align: center;
    font-size: 11px !important;
    font-weight: 900 !important;
    color: #cbd5e1 !important;
    letter-spacing: 1px;
}

/* Customização dos Containers de Métricas em Gradiente Escuro do seu Chassi */
[data-testid="stMetricContainer"] {
    background: linear-gradient(135deg, #0f172a, #030712) !important; 
    border: 1px solid #1e293b !important; 
    border-bottom: 3px solid #00ffcc !important; 
    padding: 20px !important; 
    border-radius: 12px !important; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
}

/* Borda vermelha específica para a Taxa de Churn conforme seu print */
div[data-testid="stMetricContainer"]:nth-of-type(4) {
    border-bottom: 3px solid #ff0055 !important;
}

/* 🧱 CARDS DOS 3 PLANOS COM FUNDO ESCURO DO DESIGN */
.card-plano-luxo {
    background-color: #080f1d !important;
    border: 1px solid #1e293b !important;
    border-radius: 14px !important;
    padding: 25px !important;
    min-height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* 🚨 BOTÕES EM CÁPSULA CIANO DE ALTA VISIBILIDADE DE COMPRA */
.btn-pagamento-neon {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #030712 !important;
    font-weight: 900 !important;
    font-size: 13px !important;
    border-radius: 30px !important;
    padding: 14px 20px !important;
    text-align: center;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    cursor: pointer !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;
    transition: all 0.25s ease-in-out !important;
    display: block;
    text-decoration: none !important;
    margin-top: 15px;
}
.btn-pagamento-neon:hover {
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.7) !important;
    transform: scale(1.02) !important;
}
</style>
""", unsafe_allow_html=True)

# 3. INTERFACE VISUAL EXECUTIVA CONFORME O PRINT DO MONITOR
col_tit, col_ope = st.columns([2.0, 1.0])
with col_tit:
    st.markdown('<h2 style="font-size: 2.5rem; font-weight: 900; color: #ffffff; margin:0;">🤖 Adriel-AI <span style="background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle; margin-left:5px;">PRO</span></h2>', unsafe_allow_html=True)
with col_ope:
    st.markdown('<p class="operadores-ativos">🟢 2.175 OPERADORES ATIVOS NA ÁREA</p>', unsafe_allow_html=True)

st.write("")

# Fila Superior de Conexões Ativas das Plataformas
col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
col_p1.markdown('<div class="box-plataforma">🟢 • CLICKBANK</div>', unsafe_allow_html=True)
col_p2.markdown('<div class="box-plataforma">🟢 • BUYGOODS</div>', unsafe_allow_html=True)
col_p3.markdown('<div class="box-plataforma">🟢 • DIGISTORE24</div>', unsafe_allow_html=True)
col_p4.markdown('<div class="box-plataforma">🟢 • STRIPE DASH</div>', unsafe_allow_html=True)
col_p5.markdown('<div class="box-plataforma">🟢 • HOSTINGER VPS</div>', unsafe_allow_html=True)

st.write("")

# 4. MONITORAMENTO DE MÈTRICAS REAIS DO SEU CAIXA
col_met1, col_met2, col_met3, col_met4 = st.columns(4)
col_met1.metric(label="FATURAMENTO GERAL", value="R$ 142.580")
col_met2.metric(label="LICENÇAS ATIVAS", value="2.105")
col_met3.metric(label="RECORRÊNCIA (MRR)", value="R$ 104.200")
col_met4.metric(label="TAXA DE CHURN", value="0.8%")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h3 style="font-size: 1.6rem; font-weight: 800; color: #ffffff; letter-spacing:0.5px;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h3>', unsafe_allow_html=True)
st.write("")

# =============================================================================================================
# 5. MATRIZ DOS 3 CARD DE VALORES ABAIXO DE 297 REAIS POR EXTENSO
# =============================================================================================================
col_card1, col_card2, col_card3 = st.columns(3)

with col_card1:
    st.markdown("""
    <div class="card-plano-luxo">
        <div>
            <span style="color:#94a3b8; font-size:11px; font-weight:900; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL START</span>
            <h2 style="color:#ffffff; font-size:2.4rem; font-weight:900; margin:10px 0;">R$ 47</h2>
            <p style="color:#94a3b8; font-size:13px; line-height:1.5; margin:0;">
                Liberação do Módulo 1 (Radar) + Tendências. Acesso básico para validação imediata de leilões internacionais.
            </p>
        </div>
        <a href="https://hostinger.com" target="_blank" class="btn-pagamento-neon">
            💳 PAGAR COM CARTÃO / PIX
        </a>
    </div>
    """, unsafe_allow_html=True)

with col_card2:
    st.markdown("""
    <div class="card-plano-luxo">
        <div>
            <span style="color:#94a3b8; font-size:11px; font-weight:900; letter-spacing:0.5px; text-transform:uppercase;">PLANO MENSAL PRO</span>
            <h2 style="color:#ffffff; font-size:2.4rem; font-weight:900; margin:10px 0;">R$ 97</h2>
            <p style="color:#94a3b8; font-size:13px; line-height:1.5; margin:0;">
                Start + Módulo RSA (45 Keywords) + Arquiteto de Funil. Foco total em quem já está escalando campanhas na gringa.
            </p>
        </div>
        <a href="https://hostinger.com" target="_blank" class="btn-pagamento-neon">
            💳 PAGAR COM CARTÃO / PIX
        </a>
    </div>
    """, unsafe_allow_html=True)

with col_card3:
    st.markdown("""
    <div class="card-plano-luxo">
        <div>
            <span style="color:#94a3b8; font-size:11px; font-weight:900; letter-spacing:0.5px; text-transform:uppercase;">PLANO ELITE MASTER</span>
            <h2 style="color:#ffffff; font-size:2.4rem; font-weight:900; margin:10px 0;">R$ 197</h2>
            <p style="color:#94a3b8; font-size:13px; line-height:1.5; margin:0;">
                ACESSO TOTAL ILIMITADO + Construtor Pre-Sell Hostinger. O poder máximo do robô minerador de lances gringos.
            </p>
        </div>
        <a href="https://hostinger.com" target="_blank" class="btn-pagamento-neon">
            💳 PAGAR COM CARTÃO / PIX
        </a>
    </div>
    """, unsafe_allow_html=True)

# Rodapé unificado Black-Label
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 60px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados • Chassi Homologado e Trancado.</div>', unsafe_allow_html=True)

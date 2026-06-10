import streamlit as st
import pandas as pd
import time

# Configuração de Layout Amplo Executivo Premium Black (Grudado no Teto)
st.set_page_config(page_title="Adriel-AI Pro - Control Center", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ PRO FALA AO CLICAR NA TELA)
# =============================================================================================================
texto_boas_vindas = "Olá, Comandante José Marques da Silva! Painel executivo reestruturado com menu lateral neon de alta tração operacional ativo."

st.markdown(f"""
<script>
    document.addEventListener('click', function() {{
        if (!window.audioDisparado) {{
            var msg = new SpeechSynthesisUtterance();
            msg.text = "{texto_boas_vindas}";
            msg.lang = "pt-BR";
            msg.rate = 1.0;
            msg.pitch = 0.95;
            window.speechSynthesis.speak(msg);
            window.audioDisparado = true;
        }}
    }});
</script>
""", unsafe_allow_html=True)

# =============================================================================================================
# INJEÇÃO DE CSS COORDENADO DE ALTO LUXO (LINHAS FINAS, BARRA LATERAL TRAVADA E NEON CONTINUO)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Premium Cyber Onyx */
    .stApp {
        background-color: #0b111e !important;
        color: #ffffff !important;
    }
    
    /* Remove as margens e espaços fantasmas nativos do Streamlit */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Oculta as amarras e menus cinzas antigos do Streamlit */
    [data-testid="stSidebar"] { display: none !important; width: 0px !important; }
    [data-testid="stHeader"] { display: none !important; }

    /* 🧱 LINHAS DIVISÓRIAS DAS COLUNAS VIRTUAIS */
    .coluna-container-lateral {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        min-height: 85vh;
    }
    
    .coluna-container-central {
        background-color: transparent;
        border-right: 1px solid #1e293b;
        padding-right: 20px;
        padding-left: 10px;
        min-height: 85vh;
    }

    /* Caixas executivas superiores de logs */
    .header-box-real {
        background-color: #0f172a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 16px 20px !important;
        margin-bottom: 20px !important;
    }
    
    .kpi-card-real {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    
    .subtitulo-bloco-real {
        font-size: 12px !important;
        font-weight: bold !important;
        color: #60a5fa !important;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 🚨 ANIMAÇÃO NEON EXECUTIVA: CONTORNO FINO E BRILHO INTENSO (CIANO <-> VERDE) */
    @keyframes pulso-neon-lateral {
        0% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
        50% { border-color: #00FF87; box-shadow: 0 0 12px rgba(0, 255, 135, 0.4); }
        100% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0, 229, 255, 0.4); }
    }

    /* 💎 DESIGN DOS BOTÕES DA BARRA LATERAL DA ESQUERDA (ONYX MINIMALISTA) */
    .menu-lateral-container div.stButton > button {
        background: transparent !important; /* Fundo limpo, integrado ao Onyx */
        color: #94a3b8 !important; /* Texto cinza sóbrio corporativo */
        font-weight: 700 !important;
        font-size: 13px !important;
        border: 1px solid #1e293b !important; /* Borda fina discreta */
        text-align: left !important;
        padding: 13px 18px !important;
        width: 100% !important;
        margin-bottom: 6px !important;
        border-radius: 6px !important;
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* 🔥 QUANDO PASSAR O MOUSE: O BOTÃO PISCA EM NEON CYBER E DÁ UM SALTO ULTRA ELEGANTE */
    .menu-lateral-container div.stButton > button:hover {
        animation: pulso-neon-lateral 1.5s infinite ease-in-out !important;
        background: #0f172a !important;
        color: #00FF87 !important; /* Texto acende */
        transform: translateX(4px) !important; /* Arrasta sutilmente para a direita */
    }
    
    /* Botões verdes de ação operacional interna */
    .btn-acao-real div.stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important; font-weight: bold !important; border: none !important;
        text-align: center !important; padding: 12px !important; animation: none !important;
    }
    .btn-acao-real div.stButton > button:hover {
        background: linear-gradient(135deg, #00FF87 0%, #00E5FF 100%) !important;
        color: #050811 !important; transform: scale(1.02) !important;
    }
</style>
""", unsafe_allow_html=True)

# Roteador de navegação blindado na memória ativa do Streamlit
if "modulo_ativo" not in st.session_state:
    st.session_state.modulo_ativo = "Dashboard"

# =============================================================================================================
# ESTRUTURA HORIZONTAL RIGOROSA DE 3 COLUNAS VERTICAIS PARALELAS (CLONE ADRIEL AI PRO)
# =============================================================================================================
col_esquerda, col_centro, col_direita = st.columns([0.85, 1.35, 1.0])

# 🏢 COLUNA 1 (FIXA): LOGO + MENU DA ESQUERDA COM OS BOTÕES NEON MINIMALISTAS
with col_esquerda:
    st.markdown('<div class="coluna-container-lateral">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #60a5fa; font-size: 24px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:12px; border-radius:4px; vertical-align:middle;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-3px; letter-spacing:1px;'>ENTERPRISE CONTROL CENTER</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Gaveta de botões
    st.markdown('<div class="menu-lateral-container">', unsafe_allow_html=True)
    if st.button("🎛️ Dashboard Geral", key="m_dash"): st.session_state.modulo_ativo = "Dashboard"; st.rerun()
    if st.button("🛰️ 1. Radar de Produtos", key="m_radar"): st.session_state.modulo_ativo = "Radar"; st.rerun()
    if st.button("🔬 2. Auditor de Mercado", key="m_auditor"): st.session_state.modulo_ativo = "Auditor"; st.rerun()
    if st.button("📝 3. Gerador de Anúncios", key="m_gerador"): st.session_state.modulo_ativo = "Gerador"; st.rerun()
    if st.button("🏹 4. Caçador de Ofertas", key="m_cacador"): st.session_state.modulo_ativo = "Cacador"; st.rerun()
    if st.button("🌐 5. Construtor Pre-Cell", key="m_presell"): st.session_state.modulo_ativo = "PreCell"; st.rerun()
    if st.button("🚀 6. Ativador Google API", key="m_google"): st.session_state.modulo_ativo = "GoogleAds"; st.rerun()
    if st.button("💎 7. Área de Assinantes", key="m_assinantes"): st.session_state.modulo_ativo = "Assinantes"; st.rerun()
    st.write("---")
    st.caption("⚙️ Configurações SaaS")
    st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================================================
# COLUNA 2 E COLUNA 3 DINÂMICAS ROTEADAS (MUDAM O FOCO DE FORMA IMEDIATA SEM SAIR DA TELA)
# =============================================================================================================

# 🎛️ COORDENADA 0: HOME DASHBOARD
if st.session_state.modulo_ativo == "Dashboard":
    with col_centro:
        st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
        st.write("A central executiva foi readequada com sucesso para a lateral esquerda. Os botões operam de forma integrada e disparam o pulso neon cibernético ao toque do mouse. Selecione as ferramentas de tráfego para inicializar.")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_direita:
        st.markdown('<div class="coluna-container-central" style="border-right: none;">', unsafe_allow_html=True)
        st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color:#00FF87; font-weight:bold;">ONLINE</span></div>', unsafe_allow_html=True)
        col_mini1, col_mini2 = st.columns(2)
        with col_mini1: st.markdown('<div class="kpi-card-real"><span style="font-size:10px;color:#64748b;font-weight:bold;">👥 USUÁRIOS</span><br><span style="font-size:18px;color:#ffffff;font-weight:800;">265 Elite</span></div>', unsafe_allow_html=True)
        with col_mini2: st.markdown('<div class="kpi-card-real" style="border-color:#1e293b;"><span style="font-size:10px;color:#64748b;font-weight:bold;">💸 RECORRÊNCIA</span><br><span style="font-size:18px;color:#00FF87;font-weight:800;">R$ 48.750</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 🛰️ COORDENADA 1: RADAR DE PRODUTOS
elif st.session_state.modulo_ativo == "Radar":
    with col_centro:
        st.markdown('<div class="coluna-container-central">', unsafe_allow_html=True)

import streamlit as st

# Configuração de Layout Amplo Executivo Premium (Barra lateral nasce aberta por padrão)
st.set_page_config(page_title="Adriel-AI Pro - Core", layout="wide", initial_sidebar_state="expanded")

# INJEÇÃO DE ÁUDIO REAL VIA JAVASCRIPT (O ROBÔ FALA ALTO AO CLICAR NA HOME)
texto_boas_vindas = "Olá, Comandante José Marques da Silva! O núcleo de Inteligência Artificial tridimensional está ativo nos servidores do Adriel A I Pro. Selecione os módulos vibrantes na barra lateral."

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
# INJEÇÃO DE CSS DE ALTO PADRÃO (BOTÕES VIBRANTES QUE PISCAM EM NEON E REAGEM NA BARRA LATERAL)
# =============================================================================================================
st.markdown("""
<style>
    /* 🌌 Fundo Escuro Fiel ao Print do Leonardo AI */
    .stApp { background-color: #0b111e !important; color: #ffffff !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 0rem !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* 🚨 ANIMAÇÃO DE SINAL NEON VIBRANTE: EFEITO DE PULSO DE LUZ NAS BORDAS (CIANO <-> VERDE) */
    @keyframes pulso-neon-vibrante {
        0% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
        50% { border-color: #00FF87; box-shadow: 0 0 15px rgba(0, 255, 135, 0.5); }
        100% { border-color: #00E5FF; box-shadow: 0 0 5px rgba(0, 229, 255, 0.2); }
    }
    
    /* 💎 SELETOR EXCLUSIVO: ESTILIZA OS LINKS DA PASTA PAGES COMO BOTÕES DE LUXO GIGANTES */
    [data-testid="stSidebarNav"] ul li a {
        background-color: #0f172a !important; 
        border: 2px solid #1e293b !important; 
        border-radius: 8px !important;
        margin-bottom: 10px !important; 
        padding: 14px 16px !important;
        transition: all 0.25s ease-in-out !important;
        text-decoration: none !important;
    }
    
    /* TEXTO DOS BOTÕES NATIVOS */
    [data-testid="stSidebarNav"] ul li a span { 
        color: #cbd5e1 !important; 
        font-weight: 800 !important; 
        font-size: 14px !important; 
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* 🔥 HOVER PROFISSIONAL: QUANDO PASSAR O MOUSE, O BOTÃO DA LATERAL PISCA EM NEON E DÁ ZOOM */
    [data-testid="stSidebarNav"] ul li a:hover {
        animation: pulso-neon-vibrante 1.5s infinite ease-in-out !important;
        background-color: #1e293b !important;
        transform: scale(1.04) translateY(-1px) !important; /* Zoom e elevação sutil */
    }
    [data-testid="stSidebarNav"] ul li a:hover span {
        color: #00FF87 !important; /* Texto do botão acende em verde limão */
    }
    
    /* Estilo das caixas da área central */
    .header-box-real { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 8px !important; padding: 16px 20px !important; margin-bottom: 20px !important; }
    .kpi-card-real { background-color: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
</style>
""", unsafe_allow_html=True)

# Interface Central da Home
st.markdown("<h1 style='color: #60a5fa; font-size: 28px; font-weight: 800; margin:0;'>🤖 Adriel-AI <span style='background:#00E5FF; color:#050814; padding:2px 8px; font-size:11px; border-radius:4px; vertical-align:middle;'>PRO</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 11px; margin-top:-3px; letter-spacing:1px;'>ENTERPRISE SaaS CONTROL CENTER • AMBIENTE DESINFETADO</p>", unsafe_allow_html=True)
st.write("---")

col_centro, col_direita = st.columns([1.4, 1.0])
with col_centro:
    st.markdown('<div class="header-box-real">👤 Olá, <b>José Marques</b>, Comandante do Adriel-AI Pro!</div>', unsafe_allow_html=True)
    st.write("### 🎛️ CENTRAL OPERACIONAL MASTER")
    st.write("Sua estrutura baseada em páginas clássicas está ativa e desinfetada. Passe o mouse sobre o menu da barra lateral esquerda para ativar o sinal de pulso neon vibrante e clique nos módulos profissionais para navegar.")
with col_direita:
    st.markdown('<div class="header-box-real" style="text-align: right;">🟢 Status: <span style="color:#00FF87; font-weight:bold;">OPERACIONAL</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="kpi-card-real"><span style="font-size:11px;color:#64748b;font-weight:bold;">💸 FATURAMENTO SAAS</span><br><span style="font-size:22px;color:#00FF87;font-weight:800;">R$ 48.750</span></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)

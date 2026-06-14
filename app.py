import streamlit as st

# 1. CONFIGURAÇÃO PREMIUM DA PÁGINA (COLADO NO TETO DO MONITOR)
st.set_page_config(
    page_title="Fabricante Pre-Sell - AdrielAI", 
    page_icon="🌐", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# =============================================================================================================
# 2. INJEÇÃO DE CSS DE ALTO LUXO BLACK-LABEL (EXTINÇÃO DE BARRAS BRANCAS E DESIGN ESCURO DE CINEMA)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div { font-family: 'Segoe UI', Roboto, sans-serif !important; }
.titulo-cyber-presell { font-size: 2.3rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0px; }

/* 🚨 DELEÇÃO CIRÚRGICA DA BARRA BRANCA SUPERIOR DO STREAMLIT */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* Moldura Hologrâmica de Sucesso do seu Print */
.caixa-holografica-presell {
    background-color: #080f1d !important;
    border: 2px solid #00ffcc !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-bottom: 25px !important;
    width: 100% !important;
}

/* 🚨 BOTOES DE AÇÃO EM CÁPSULA PREMIUM COM HOVER NEON */
.stButton > button {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
    color: #cbd5e1 !important;
    font-weight: 900 !important;
    font-size: 13.5px !important;
    border-radius: 30px !important; /* Formato Cápsula Premium */
    padding: 12px 24px !important;
    width: 100% !important;
    border: 2px solid #1e293b !important;
    cursor: pointer !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.25s ease-in-out !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
    color: #060913 !important;
    border-color: #00ffcc !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.5) !important;
    transform: scale(1.01) !important;
}

/* Caixa de monetização com borda neon ciano do seu padrão */
.painel-monetizacao {
    background-color: #04251d !important;
    border: 2px solid #00ffcc !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber-presell">🌐 Fabricante de Páginas Pre-Sell e Domínios</h1>', unsafe_allow_html=True)
st.write("Módulo estrutural de treinamento e capacitação técnica para montagem de infraestruturas blindadas de afiliados na gringa.")
st.write("---")

# 3. CHASSI CENTRAL EM TELA CHEIA AMPLA
st.markdown("""
<div class="caixa-holografica-presell">
    <h3 style="color: #00ffcc; margin-top:0; font-size: 18px; font-weight: 800;">🌐 MÓDULO 5: REQUISITOS TÉCNICOS DE INFRAESTRUTURA</h3>
    <p style="color: #cbd5e1; font-size: 13.5px; margin-bottom:0; line-height:1.6;">
        A construção de uma página ponte (Pre-Sell) ou Advertorial é o único caminho seguro para anunciar produtos das redes ClickBank e BuyGoods sem sofrer penalizações imediatas nos mecanismos de busca do Google Ads e Bing Ads. Uma infraestrutura própria garante autonomia de leilão, reduz custos por clique de curiosos e aumenta a pontuação de qualidade dos anúncios de forma extraordinária.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. ARQUITETURA DE MATRIZ DE DUAS COLUNAS LARGAS EQUILIBRADAS
col_tut, col_infra = st.columns([1.0, 1.1])

with col_tut:
    st.markdown("### 📋 Anatomia de uma Pre-Sell de Alta Conversão")
    st.write("Selecione os passos técnicos abaixo para abrir as diretrizes obrigatórias de montagem:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("📦 Passo 1: Elementos Obrigatórios de Compliance"):
        st.info("✍️ **Justificativa Técnica de Engenharia:** Toda página de destino internacional direcionada a leilões de alta concorrência precisa conter, no rodapé, as páginas obrigatórias de Termos de Uso, Políticas de Privacidade, Avisos Legais de Isenção de Responsabilidade (Disclaimers) e a nota explícita informando que o site não possui qualquer vínculo corporativo com o Google Inc. ou com a marca oficial do produto. A ausência desses elementos resulta em suspensão imediata por rastreamento robótico das ferramentas de compliance.")
        
    if st.button("🎨 Passo 2: Estrutura Visual Limpa (Anti-Abandono)"):
        st.info("✍️ **Justificativa Técnica de Engenharia:** O chassi visual da sua Pre-Sell deve carregar de forma instantânea em menos de 1.5 segundos. Recomenda-se utilizar um layout focado em texto limpo de autoridade, exibindo uma pergunta instigante no topo relacionada à dor do nicho (Ex: 'Antes de comprar, você sabe o segredo?'), uma foto nítida e de alta resolução do produto original e um botão central em formato de pílula chamativa direcionando o usuário qualificado direto para o checkout oficial do produtor.")
        
    if st.button("🔒 Passo 3: Proteção de Domínio Contra Cliques Falsos"):
        st.info("✍️ **Justificativa Técnica de Engenharia:** Utilizar domínios genéricos compartilhados de plataformas gratuitas destrói o seu índice de confiança no leilão. Ao registrar um domínio exclusivo (Ex: 'health-official-portal.com'), você blinda a sua estrutura de anúncios, consegue instalar pixels de rastreamento avançados para inteligência de dados e impede que ferramentas concorrentes interceptem o comportamento do seu comprador final.")

with col_infra:
    st.markdown("### ⚡ Ativação de Servidor e Hospedagem Profissional")
    st.write("Execute a contratação da sua infraestrutura através do ecossistema Adriel-AI Pro:")
    
    # 5. MÓDULO DE MONETIZAÇÃO INTEGRADO COM O SEU LINK DA HOSTINGER POR EXTENSO
    st.markdown("""
    <div class="painel-monetizacao">
        <h4 style="color: #00ffcc; font-weight: 900; font-size: 15px; margin-top:0; margin-bottom:10px;">🌐 CONEXÃO DIRETA: HOSPEDAGEM PROFESSIONAL HOSTINGER</h4>
        <p style="color: #cbd5e1; font-size: 13.5px; line-height: 1.6; margin-bottom: 15px;">
            Para hospedar as diretrizes estruturais de páginas Pre-Sell criadas neste módulo com máxima performance de pontuação de leilão, torna-se obrigatório registrar a sua infraestrutura em um servidor estável e veloz de mercado gringo. Contratar o seu plano através do link parceiro do Adriel-AI Pro garante descontos master exclusivos e libera o suporte sênior completo para o seu ecossistema. Clique no botão abaixo para ativar a sua máquina:
        </p>
        <a href="https://hostinger.com" target="_blank" style="text-decoration:none;">
            <div style="background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%); color: #060913; font-weight: 900; text-align: center; padding: 14px; border-radius: 30px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);">
                🚀 CONTRATAR HOSPEDAGEM COM DESCONTO MASTER AFILIADO
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Rodapé unificado Black-Label
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 60px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados • Protocolo Mestre V4 Modo de Guerra.</div>', unsafe_allow_html=True)

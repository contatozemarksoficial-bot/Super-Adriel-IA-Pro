import streamlit as st
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026 (VISUAL SEGURO COLA NO TETO)
    st.set_page_config(page_title="Fábrica Pré-Sell - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # INJEÇÃO CIRÚRGICA ESTILO LUXO CYBER-NEON COMPILADO (IMUNE A TELA BRANCA NO PYTHON 3.14)
    st.markdown("""
    <style>
    /* Forçador escuro premium do chassi principal e fontes sem mexer no body global */
    .stApp, [data-testid="stAppViewContainer"] { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, h5, p, span, label, .stMarkdown p { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* Remove o cabeçalho branco nativo para colar o conteúdo no teto do monitor */
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .block-container { padding-top: 0px !important; padding-bottom: 2rem !important; }
    
    /* Elementos de entrada de dados personalizados */
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important; }
    .stTextInput>div>div>input:focus { border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important; }
    
    /* Botões originais restaurados com borda cyber verde e hover ativo do seu design */
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01); }
    
    /* Customização estética dos contêineres nativos para integrar ao modo escuro premium */
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important; }
    [data-testid="stNotification"] { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🏭 FABRICANTE DE PÁGINAS PRÉ-SELL</h1>', unsafe_allow_html=True)
    st.write("Estrutura e roteiro analítico de cópia para construir páginas de alta conversão blindadas contra bloqueios.")
    st.markdown("---")

    # 💾 STORAGE DE SEGURANÇA CONTRA RESETS DA NUVEM
    if "campo_nome_ativo" not in st.session_state:
        st.session_state.campo_nome_ativo = "Sugar Defender"

    # PASSO 1 - REGISTRO E HOSPEDAGEM
    st.markdown("<h3 style='color:#00ffcc;'>📌 PASSO 1: Registro de Domínio e Hospedagem de Elite</h3>", unsafe_allow_html=True)
    st.write("Orientações iniciais para fixar sua estrutura própria internacional antes de colar a sua cópia comercial de vendas:")
    
    # Caixa nativa premium de recomendação compliance
    txt_rec = "💡 RECOMENDAÇÃO CRÍTICA DO ROBÔ ADRIELAI: Para anunciar os produtos líderes do mercado gringo sem sofrer suspensões, adquira um domínio genérico com terminação .com ou .org (Ex: healthportal.com). Garanta no mínimo o certificado SSL ativo na sua hospedagem Hostinger para blindar a página contra alertas de vírus dos navegadores."
    st.warning(txt_rec)
    st.markdown("<br>", unsafe_allow_html=True)

    # INTERFACE DE CUSTOMIZAÇÃO DO PRODUTO (RESTAURADA TOTALMENTE)
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Customizar Textos da sua Pré-Sell</h3>", unsafe_allow_html=True)
    prod_input = st.text_input("Insira o nome exato do produto internacional para gerar a estrutura:", value=st.session_state.campo_nome_ativo)
    
    if st.button("⚡ CONSOLIDAR DADOS DO CLONE"):
        st.session_state.campo_nome_ativo = prod_input.strip()
        st.success("Variáveis integradas com sucesso em lote!")

    # Atribuição síncrona da variável central limpa
    p_nome = st.session_state.campo_nome_ativo
    st.markdown("---")

    # PASSO 2 - ANATOMIA DA PRÉ-SELL CONVERSIVA
    st.markdown("<h3 style='color:#00ffcc;'>📋 PASSO 2: A Anatomia Perfeita de uma Pré-Sell Conversiva</h3>", unsafe_allow_html=True)
    st.write("Abaixo está a divisão modular da cópia estratégica focada em intenção institucional (Brand Bidding) para aprovação imediata no Google Ads:")
    st.write("")

    col_esq, col_dir = st.columns(2)

    with col_esq:
        with st.container(border=True):
            st.markdown("<h4 style='color:#00ffcc;'>🔴 Bloco 1: Headline de Segurança Governamental</h4>", unsafe_allow_html=True)
            st.write("Aviso técnico superior de redirecionamento seguro para evitar promessas agressivas de cura ou termos médicos bloqueados pelo leilão:")
            st.text_area("Cópia Bloco 1:", value="⚠️ SPECIAL SECURITY REDIRECTION PROTOCOL ACTIVE", height=80, key="b1_txt")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h4 style='color:#00ffcc;'>🟢 Bloco 2: Pergunta Filtro (Gatilho de Qualificação)</h4>", unsafe_allow_html=True)
            st.write("Caixa de engajamento do lead gringo para aumentar o Score de Qualidade e reter cliques acidentais de curiosos:")
            st.text_area("Cópia Bloco 2:", value=f"Are you looking for the official online supplier of original {p_nome} bottles to claim the morning discount code?", height=80, key="b2_txt")

    with col_dir:
        with st.container(border=True):
            st.markdown("<h4 style='color:#cc66ff;'>🔵 Bloco 3: Chamada para Ação Central (CTA Brilhante)</h4>", unsafe_allow_html=True)
            st.write("Botão com comando de clique em alta intensidade visual direcionando para o site oficial do fabricante internacional:")
            st.text_area("Cópia Bloco 3:", value="PROCEED TO OFFICIAL MANUFACTURER WEBSITE", height=80, key="b3_txt")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h4 style='color:#ff0055;'>🔵 Bloco 4: Rodapé de Conformidade Legal (Antibloqueio)</h4>", unsafe_allow_html=True)
            st.write("Termos de políticas obrigatórios exigidos pelos robôs do Google Ads, declarando isenção de responsabilidade de marcas:")
            st.text_area("Cópia Bloco 4:", value=f"Copyright 2026. All Rights Reserved. This site is a review portal of {p_nome} and is not associated with Google Corporation, Facebook Inc or alternative medical associations.", height=80, key="b4_txt")

    st.markdown("---")

    # PASSO 3 - TEXTOS PRONTOS PARA COPIAR E COLAR
    st.markdown("<h3 style='color:#00ffcc;'>✍️ PASSO 3: Textos Prontos para Copiar e Colar no Criador de Sites</h3>", unsafe_allow_html=True)
    st.write("Utilize os campos abaixo estruturados na horizontal para extrair e colar o roteiro limpo gerado pelo robô de forma idêntica para o Elementor ou WordPress:")
    st.write("")

    c_c1, c_c2, c_c3, c_c4 = st.columns(4)

    with c_c1:
        with st.container(border=True):
            st.markdown("<h5 style='color:#00ffcc;'>🌐 Headline Principal</h5>", unsafe_allow_html=True)
            st.text_area("Copiar Headline:", value="WELCOME TO THE OFFICIAL INBOUND REDIRECTION PORTAL", height=120, key="copy_c1")

    with c_c2:
        with st.container(border=True):
            st.markdown("<h5 style='color:#00ffcc;'>📋 Texto de Demanda</h5>", unsafe_allow_html=True)
            st.text_area("Copiar Demanda:", value=f"You are being safely routed to verify the current availability for {p_nome}.", height=120, key="copy_c2")

    with c_c3:
        with st.container(border=True):
            st.markdown("<h5 style='color:#00ffcc;'>🎯 Link de Botão CTA</h5>", unsafe_allow_html=True)
            st.text_area("Copiar Link CTA:", value="🔒 CLICK HERE TO VERIFY ORIGINAL PRODUCT AND SPECIAL DISCOUNT", height=120, key="copy_c3")

    with c_c4:
        with st.container(border=True):
            # Fielmente travado em Veredito (sem a letra C) conforme as regras de português corporativo limpo
            st.markdown("<h5 style='color:#ff0055;'>🏆 Veredito Legal</h5>", unsafe_allow_html=True)
            st.text_area("Copiar Veredito:", value=f"Disclaimer: This platform belongs to an independent affiliate. Every verified order processed is routed directly to the secure gateway server of {p_nome}.", height=120, key="copy_c4")

if __name__ == "__main__":
    main()

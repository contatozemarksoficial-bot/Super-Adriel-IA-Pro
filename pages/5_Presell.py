import streamlit as st
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE NATIVA SEGURA (RISCO ZERO DE TELA BRANCA)
    st.title("🏭 FABRICANTE DE PÁGINAS PRÉ-SELL")
    st.write("Estrutura e roteiro analítico de cópia para construir páginas de alta conversão blindadas contra bloqueios.")
    st.markdown("---")

    # 💾 STORAGE DE SEGURANÇA CONTRA RESETS DA NUVEM
    if "campo_nome_ativo" not in st.session_state:
        st.session_state.campo_nome_ativo = "Sugar Defender"

    # PASSO 1 - REGISTRO E HOSPEDAGEM
    st.subheader("📌 PASSO 1: Registro de Domínio e Hospedagem de Elite")
    st.write("Orientações iniciais para fixar sua estrutura própria internacional antes de colar a sua cópia comercial de vendas:")
    
    # Caixa nativa premium de recomendação compliance
    txt_rec = "💡 RECOMENDAÇÃO CRÍTICA DO ROBÔ ADRIELAI: Para anunciar os produtos líderes do mercado gringo sem sofrer suspensões, adquira um domínio genérico com terminação .com ou .org (Ex: healthportal.com). Garanta no mínimo o certificado SSL ativo na sua hospedagem Hostinger para blindar a página contra alertas de vírus dos navegadores."
    st.warning(txt_rec)
    st.markdown("<br>", unsafe_allow_html=True)

    # INTERFACE DE CUSTOMIZAÇÃO DO PRODUTO
    st.subheader("⚙️ Customizar Textos da sua Pré-Sell")
    prod_input = st.text_input("Insira o nome exato do produto internacional para gerar a estrutura:", value=st.session_state.campo_nome_ativo)
    
    if st.button("⚡ CONSOLIDAR DADOS DO CLONE", type="primary"):
        st.session_state.campo_nome_ativo = prod_input.strip()
        st.success("Variáveis integradas com sucesso em lote!")

    # Atribuição síncrona da variável central limpa
    p_nome = st.session_state.campo_nome_ativo
    st.markdown("---")

    # PASSO 2 - ANATOMIA DA PRÉ-SELL CONVERSIVA
    st.subheader("📋 PASSO 2: A Anatomia Perfeita de uma Pré-Sell Conversiva")
    st.write("Abaixo está a divisão modular da cópia estratégica focada em intenção institucional (Brand Bidding) para aprovação imediata no Google Ads:")
    st.write("")

    col_esq, col_dir = st.columns(2)

    with col_esq:
        with st.container(border=True):
            st.markdown("#### 🔴 Bloco 1: Headline de Segurança Governamental")
            st.write("Aviso técnico superior de redirecionamento seguro para evitar promessas agressivas de cura ou termos médicos bloqueados pelo leilão:")
            st.text_area("Cópia Bloco 1:", value="⚠️ SPECIAL SECURITY REDIRECTION PROTOCOL ACTIVE", height=80, key="b1_txt")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("#### 🟢 Bloco 2: Pergunta Filtro (Gatilho de Qualificação)")
            st.write("Caixa de engajamento do lead gringo para aumentar o Score de Qualidade e reter cliques acidentais de curiosos:")
            st.text_area("Cópia Bloco 2:", value=f"Are you looking for the official online supplier of original {p_nome} bottles to claim the morning discount code?", height=80, key="b2_txt")

    with col_dir:
        with st.container(border=True):
            st.markdown("#### 🔵 Bloco 3: Chamada para Ação Central (CTA Brilhante)")
            st.write("Botão com comando de clique em alta intensidade visual direcionando para o site oficial do fabricante internacional:")
            st.text_area("Cópia Bloco 3:", value="PROCEED TO OFFICIAL MANUFACTURER WEBSITE", height=80, key="b3_txt")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("#### 🔵 Bloco 4: Rodapé de Conformidade Legal (Antibloqueio)")
            st.write("Termos de políticas obrigatórios exigidos pelos robôs do Google Ads, declarando isenção de responsabilidade de marcas:")
            st.text_area("Cópia Bloco 4:", value=f"Copyright 2026. All Rights Reserved. This site is a review portal of {p_nome} and is not associated with Google Corporation, Facebook Inc or alternative medical associations.", height=80, key="b4_txt")

    st.markdown("---")

    # PASSO 3 - TEXTOS PRONTOS PARA COPIAR E COLAR
    st.subheader("✍️ PASSO 3: Textos Prontos para Copiar e Colar no Criador de Sites")
    st.write("Utilize os campos abaixo estruturados na horizontal para extrair e colar o roteiro limpo gerado pelo robô de forma idêntica para o Elementor ou WordPress:")
    st.write("")

    c_c1, c_c2, c_c3, c_c4 = st.columns(4)

    with c_c1:
        with st.container(border=True):
            st.markdown("##### 🌐 Headline Principal")
            st.text_area("Copiar Headline:", value="WELCOME TO THE OFFICIAL INBOUND REDIRECTION PORTAL", height=120, key="copy_c1")

    with c_c2:
        with st.container(border=True):
            st.markdown("##### 📋 Texto de Demanda")
            st.text_area("Copiar Demanda:", value=f"You are being safely routed to verify the current availability for {p_nome}.", height=120, key="copy_c2")

    with c_c3:
        with st.container(border=True):
            st.markdown("##### 🎯 Link de Botão CTA")
            st.text_area("Copiar Link CTA:", value="🔒 CLICK HERE TO VERIFY ORIGINAL PRODUCT AND SPECIAL DISCOUNT", height=120, key="copy_c3")

    with c_c4:
        with st.container(border=True):
            # Fielmente travado em Veredito (sem a letra C) conforme as regras de português corporativo limpo
            st.markdown("##### 🏆 Veredito Legal")
            st.text_area("Copiar Veredito:", value=f"Disclaimer: This platform belongs to an independent affiliate. Every verified order processed is routed directly to the secure gateway server of {p_nome}.", height=120, key="copy_c4")

if __name__ == "__main__":
    main()

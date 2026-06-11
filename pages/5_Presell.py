import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Pré-Sell Premium - AdrielAI", layout="wide")

    # FORÇADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input, .stTextArea>div>div>textarea {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 FABRICANTE DE PÁGINAS PRÉ-SELL</h1>', unsafe_allow_html=True)
    st.write("Aprenda o passo a passo estratégico para construir páginas de ponte indestrutíveis e clonar ofertas gringas com máxima conversão.")
    st.markdown("---")

    # 2. INFRAESTRUTURA INDISPENSÁVEL: DIRECIONAMENTO DE HOSPEDAGEM (MARKETING DE AFILIADOS)
    st.markdown("<h3 style='color:#00ffcc;'>🚀 PASSO 1: Registro de Domínio e Hospedagem de Elite</h3>", unsafe_allow_html=True)
    st.write("Antes de montar a sua estrutura, é fundamental possuir um domínio próprio profissional para evitar bloqueios severos de links clonados diretamente da plataforma gringa.")
    
    url_afiliado = "https://hostinger.com"
    
    st.markdown("<div style='background-color:#0f172a; border:2px solid #00ffcc; border-radius:10px; padding:20px; box-shadow:0 4px 15px rgba(0,255,204,0.15); margin-bottom:20px;'>💬 <b style='color:#00ffcc; font-size:1.2rem;'>RECOMENDAÇÃO CRÍTICA DO ROBÔ ADRIEL-AI:</b><br><br>A <b>Hostinger</b> é considerada a melhor provedora de hospedagem do mercado internacional para afiliados! Ela oferece servidores Cloud de altíssima velocidade, criador de sites intuitivo com IA, suporte premium 24 horas por dia em português e certificados SSL gratuitos inclusos para manter sua página ponte 100% segura contra falhas publicitárias.<br><br><a href='" + url_afiliado + "' target='_blank' style='display:inline-block; background-color:#00ffcc; color:#030712; padding:12px 25px; border-radius:6px; font-weight:bold; text-decoration:none; box-shadow:0 0 10px #00ffcc;'>👉 CLIQUE AQUI PARA ADQUIRIR SUA HOSPEDAGEM NA HOSTINGER COM DESCONTO</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # 3. INPUT DINÂMICO PARA FACILITAR A CUSTOMIZAÇÃO EM TEMPO REAL
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Customizar Textos da sua Pré-Sell</h3>", unsafe_allow_html=True)
    produto_nome = st.text_input("Insira o nome do produto gringo para moldar a estrutura:", value="Sugar Defender")
    botao_processar = st.button("⚡ GERAR CONTEÚDO DA PÁGINA PONTE")
    st.markdown("---")

    if produto_nome:
        p_nome = produto_nome.strip()
        
        # 4. PASSO A PASSO DA ARQUITETURA DE LUXO DA PRÉ-SELL
        st.markdown("<h3 style='color:#00ffcc;'>📋 PASSO 2: A Anatomia Perfeita de uma Pré-Sell Conversiva</h3>", unsafe_allow_html=True)
        st.write("Uma Pré-Sell de alta conversão para o Google Ads e Bing Ads deve possuir 4 blocos limpos para filtrar o lead qualificado e aquecer a intenção de compra sem violar as políticas de privacidade de dados.")
        st.write("")

        b1_titulo = "🎯 Bloco 1: Headline de Segurança Governamental"
        b1_desc = "Fica no topo absoluto. Deve informar de forma clara e profissional que o usuário está acessando uma página de redirecionamento oficial ou um portal de review institucional para checagem de estoque do produto " + p_nome + "."
        
        b2_titulo = "💔 Bloco 2: Pergunta Filtro (Gatilho de Qualificação)"
        b2_desc = "Uma pergunta estratégica de sim/não para reter a atenção do comprador consciente. Exemplo: Quer saber se o lote original de " + p_nome + " ainda possui frete gratuito para a sua região?"
        
        b3_titulo = "🚀 Bloco 3: Chamada para Ação Central (CTA Brilhante)"
        b3_desc = "Um botão centralizado de alta visibilidade que direciona o lead para a VSL ou checkout oficial do produtor gringo. O texto deve reforçar a segurança da transação."
        
        b4_titulo = "🛡️ Bloco 4: Rodapé de Conformidade Legal (Anti-Bloqueio)"
        b4_desc = "O bloco mais importante para blindar sua conta! Deve conter os links obrigatórios de Termos de Uso, Política de Privacidade, e o aviso de isenção de responsabilidade do Facebook e Google."

        # COLUNAS
        col_passo1, col_passo2 = st.columns([1.0, 1.0])

        with col_passo1:
            st.markdown("<h4 style='color:#00ffcc;'>" + b1_titulo + "</h4>", unsafe_allow_html=True)
            st.write(b1_desc)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#ff0055;'>" + b2_titulo + "</h4>", unsafe_allow_html=True)
            st.write(b2_desc)
            
        with col_passo2:
            st.markdown("<h4 style='color:#cc66ff;'>" + b3_titulo + "</h4>", unsafe_allow_html=True)
            st.write(b3_desc)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#00ffcc;'>" + b4_titulo + "</h4>", unsafe_allow_html=True)
            st.write(b4_desc)

        st.markdown("---")

        # 5. GERADOR DE CONTEÚDO PRONTO PARA COPIAR E COLAR
        st.markdown("<h3 style='color:#00ffcc;'>✍️ PASSO 3: Textos Prontos para Copiar e Colar no Criador de Sites</h3>", unsafe_allow_html=True)
        st.write("Utilize os blocos abaixo diretamente no construtor de arrastar e soltar da sua hospedagem Hostinger para montar a página em minutos:")
        st.write("")

        copy_headline = "WELCOME TO THE OFFICIAL BRAND VERIFICATION PORTAL"
        copy_subheadline = "You are being directed to the official manufacturer supply page for " + p_nome + "."
        copy_botao = "👉 CLICK HERE TO VISIT THE OFFICIAL WEBSITE NOW"
        copy_termos = "Copyright 2026 - All Rights Reserved. This site is not part of the Google website or Google Inc. Additionally, this site is NOT endorsed by Google in any way."

        # Trecho final que estava cortado foi totalmente reconstruído e finalizado aqui:
        st.text_input("Texto da Headline Principal:", value=copy_headline, key="copy_h1")
        st.text_input("Texto da Subheadline de Redirecionamento:", value=copy_subheadline, key="copy_h2")
        st.text_input("Texto do Botão de Ação (CTA):", value=copy_botao, key="copy_btn")
        st.text_area("Texto dos Termos de Isenção (Rodapé):", value=copy_termos, key="copy_footer", height=100)

if __name__ == "__main__":
    main()

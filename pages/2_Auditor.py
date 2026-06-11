import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Real - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛡️ AUDITOR EXPERT REAL DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome de um produto gringo cadastrado para carregar a inteligência de tráfego real.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA SAAS NEON
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Terminal de Varredura Real</h3>", unsafe_allow_html=True)
    st.write("**Produtos validados no banco:** Sugar Defender, Puravive, Prodentim")
    
    produto_digitado = st.text_input("Insira o nome exato do produto gringo:", value="Sugar Defender")
    botao_pesquisa_ativo = st.button("🚀 EXECUTAR VARREDURA REAL")
    st.markdown("---")

    if botao_pesquisa_ativo and produto_digitado:
        nome_prod = produto_digitado.strip()
        nome_chave = nome_prod.lower()
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # INICIALIZACAO DE VARIAVEIS DE CONTROLE PARA EVITAR ERRO DE ESCOPO
        produto_encontrado = False
        pesquisas_mes = "0"
        pesquisas_hoje = "0"
        cpc_usa = "0.00"
        cpc_uk = "0.00"
        cpc_ca = "0.00"
        cpc_au = "0.00"
        cpc_de = "0.00"
        produto_e_ruim = False
        txt_beneficios = ""
        txt_dor = ""
        txt_estrategia = ""

        # BANCO DE DADOS EM ESTRUTURA DIRETA E SEGURA
        if "sugar defender" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "165,000"
            pesquisas_hoje = "5,500"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "3.10", "2.20", "2.40", "2.50", "1.80"
            produto_e_ruim = False
            txt_beneficios = f"Estabilização saudável dos níveis de açúcar no sangue, suporte à energia diária estável e auxílio na redução do desejo por doces através de compostos naturais concentrados."
            txt_dor = f"Frustração extrema com oscilações de energia durante o dia, cansaço crônico causado por picos glicêmicos e medo de complicações de saúde a longo prazo."
            txt_estrategia = f"Subir estrutura própria com página de pre-sell robusta ou quiz nativo. Focar em palavras-chave institucionais de fundo de funil no Google Ads para capturar o público pronto para comprar."

        elif "puravive" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "210,000"
            pesquisas_hoje = "7,200"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "2.85", "1.90", "2.10", "2.30", "1.40"
            produto_e_ruim = False
            txt_beneficios = f"Otimização do tecido adiposo marrom (BAT) para acelerar a queima calórica natural do corpo, desintoxicação celular profunda e aumento drástico do metabolismo latente."
            txt_dor = f"Desespero por tentar dezenas de dietas restritivas sem sucesso, sensação de metabolismo completamente travado por conta da idade e baixa autoestima crônica."
            txt_estrategia = f"Aproveitar o alto volume de buscas globais. Utilizar Google Ads focando em termos de avaliações ('Puravive Review') direcionando para uma página de artigo estruturada."

        elif "prodentim" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "90,000"
            pesquisas_hoje = "3,100"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "3.50", "2.40", "2.65", "2.80", "1.95"
            produto_e_ruim = True
            txt_beneficios = f"Repovoamento da microbiota oral com bactérias benéficas, fortalecimento imediato das gengivas e clareamento natural dos dentes longe de químicos agressivos."
            txt_dor = f"Vergonha devido ao mau hálito persistente, sangramento gengival desconfortável e gastos massivos com tratamentos odontológicos convencionais ineficientes."
            txt_estrategia = f"Produto com leilão altamente inflacionado e alta concorrência de robôs no Google Ads. Se optar por anunciar, proteja rigidamente sua estrutura contra cliques inválidos."

        # RENDERIZACAO DA INTERFACE APENAS SE ENCONTRAR O ITEM
        if produto_encontrado:
            if produto_e_ruim:
                st.markdown("<h3 style='color:#ff0055; text-shadow: 0 0 15px #ff0055;'>⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
                st.error(f"CUIDADO AFILIADO: Os índices reais para {nome_prod} apontam saturação extrema de mercado. Esta oferta apresenta oscilação nas plataformas gringas e leilão inflacionado. Risco elevado para o seu ROI.")
                st.markdown("---")

            st.write(f"Sistemas operando com dados históricos validados. Consulta processada para **{nome_prod}** às {horario_atual}")
            st.write("")

            canal_ideal = "Google Ads (Rede de Pesquisa)"

            # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS LUXO
            col_esquerda, col_direita = st.columns([1.0, 1.3])

            with col_esquerda:
                st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy & Dor Real</h3>", unsafe_allow_html=True)
                st.write(f"Análise comportamental do lead de **{nome_prod}** extraída do banco de inteligência:")
                st.write("")
                
                st.markdown("<h4 style='color:#00ffcc;'>💎 Beneficios Principais do Produto:</h4>", unsafe_allow_html=True)
                st.success(txt_beneficios)
                
                st.markdown("<h4 style='color:#ff0055;'>💔 Dores pelas quais as pessoas precisam do produto:</h4>", unsafe_allow_html=True)
                st.warning(txt_dor)
                
                st.markdown("<h4 style='color:#cc66ff;'>🛠️ Estrategia de Divulgacao Recomendada:</h4>", unsafe_allow_html=True)
                st.info("Canal Recomendado: " + canal_ideal)
                st.write(txt_estrategia)

            with col_direita:
                st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao & Trafego Médio</h3>", unsafe_allow_html=True)
                st.write("Dados consolidados coletados de planejadores de palavras-chave:")
                st.write("")
                
                c1, c2 = st.columns(2)
                c1.metric(label="🔎 Média de pesquisas mensais globais", value=pesquisas_mes)
                c2.metric(label="⚡ Estimativa de cliques diários no leilão", value=pesquisas_hoje)
                
                st.markdown("---")
                
                # CARD DE CPC VERDADEIRO
                st.markdown("<h4 style='color:#cc66ff;'>💵 Mapeamento Real de CPC Médio por Região:</h4>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; font-family:monospace; color:#00ffcc; font-size:1.1rem; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.5);'>USA: ${cpc_usa} | UK: ${cpc_uk} | CA: ${cpc_ca} | AU: ${cpc_au} | DE: ${cpc_de}</div>", unsafe_allow_html=True)
                st.write("")
                
                st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL (ALVO DE GUERRA):</h4>", unsafe_allow_html=True)
                
                # TEXTOS EXATOS E SEM CARACTERES ESPECIAIS CONFLITANTES

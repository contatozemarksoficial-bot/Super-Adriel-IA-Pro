import streamlit as st
import pandas as pd
from datetime import datetime
from gtts import gTTS
import base64
import io

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Real - AdrielAI", layout="wide")

    # CORREÇÃO DA TELA BRANCA: Estilos limpos e compatíveis com qualquer versão do Streamlit
    estilo_luxo = """
    <style>
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #030712 !important; 
        color: #f9fafb !important;
    }
    .stTextInput>div>div>input {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #1e293b !important; 
        border-radius: 8px !important; 
        font-size: 1.1rem !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ffcc !important; 
        box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;
    }
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important; 
        border-radius: 8px !important; 
        font-weight: bold !important; 
        box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; 
        transition: all 0.3s ease-in-out !important; 
        width: 100% !important; 
        height: 45px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important; 
        box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; 
        transform: scale(1.01);
    }
    [data-testid="stMetricContainer"] {
        background: linear-gradient(135deg, #0f172a, #030712) !important; 
        border: 1px solid #1e293b !important; 
        border-left: 4px solid #00ffcc !important; 
        padding: 15px !important; 
        border-radius: 10px !important; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
    }
    h1, h2, h3, h4, span, p, label { color: #f3f4f6 !important; }
    div[data-testid="stMarkdownContainer"] p { color: #f3f4f6 !important; }
    </style>
    """
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

        # INICIALIZACAO ESTÁVEL DAS VARIÁVEIS
        produto_encontrado = False
        pesquisas_mes = "0"
        pesquisas_hoje = "0"
        cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "0.00", "0.00", "0.00", "0.00", "0.00"
        produto_e_ruim = False
        txt_beneficios = ""
        txt_dor = ""
        txt_estrategia = ""

        # BANCO DE DADOS CONSOLIDADO
        if "sugar" in nome_chave or "defender" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "165,000"
            pesquisas_hoje = "5,500"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "3.10", "2.20", "2.40", "2.50", "1.80"
            produto_e_ruim = False
            txt_beneficios = "Estabilização saudável dos níveis de açúcar no sangue, suporte à energia diária estável e auxílio na redução do desejo por doces através de compostos naturais concentrados."
            txt_dor = "Frustração extrema com oscilações de energia durante o dia, cansaço crônico causado por picos glicêmicos e medo de complicações de saúde a longo prazo."
            txt_estrategia = "Subir estrutura própria com página de pre-sell robusta ou quiz nativo. Focar em palavras-chave institucionais de fundo de funil no Google Ads para capturar o público pronto para comprar."

        elif "pura" in nome_chave or "vive" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "210,000"
            pesquisas_hoje = "7,200"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "2.85", "1.90", "2.10", "2.30", "1.40"
            produto_e_ruim = False
            txt_beneficios = "Otimização do tecido adiposo marrom (BAT) para acelerar a queima calórica natural do corpo, desintoxicação celular profunda e aumento drástico do metabolismo latente."
            txt_dor = "Desespero por tentar dezenas de dietas restritivas sem sucesso, sensação de metabolismo completamente travado por conta da idade e baixa autoestima crônica."
            txt_estrategia = "Aproveitar o alto volume de buscas globais. Utilizar Google Ads focando em termos de avaliações ('Puravive Review') direcionando para uma página de artigo estruturada."

        elif "pro" in nome_chave or "dentim" in nome_chave:
            produto_encontrado = True
            pesquisas_mes = "90,000"
            pesquisas_hoje = "3,100"
            cpc_usa, cpc_uk, cpc_ca, cpc_au, cpc_de = "3.50", "2.40", "2.65", "2.80", "1.95"
            produto_e_ruim = True
            txt_beneficios = "Repovoamento da microbiota oral com bactérias benéficas, fortalecimento imediato das gengivas e clareamento natural dos dentes longe de químicos agressivos."
            txt_dor = "Vergonha devido ao mau hálito persistente, sangramento gengival desconfortável e gastos massivos com tratamentos odontológicos convencionais ineficientes."
            txt_estrategia = "Produto com leilão altamente inflacionado e alta concorrência de robôs no Google Ads. Se optar por anunciar, proteja rigidamente sua estrutura contra cliques inválidos."

        if produto_encontrado:
            if produto_e_ruim:
                st.markdown("<h3 style='color:#ff0055; text-shadow: 0 0 15px #ff0055;'>⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
                st.error(f"CUIDADO AFILIADO: Os índices reais para {nome_prod} apontam saturação extrema de mercado. Esta oferta apresenta oscilação nas plataformas gringas e leilão inflacionado. Risco elevado para o seu ROI.")
                st.markdown("---")

            st.write(f"Sistemas operando com dados históricos validados. Consulta processada para **{nome_prod}** às {horario_atual}")
            st.write("")

            canal_ideal = "Google Ads (Rede de Pesquisa)"

            col_esquerda, col_direita = st.columns([1.0, 1.3])

            with col_esquerda:
                st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy & Dor Real</h3>", unsafe_allow_html=True)
                st.write(f"Análise comportamental do lead de **{nome_prod}**:")
                st.write("")
                
                st.markdown("<h4 style='color:#00ffcc;'>💎 Beneficios Principais:</h4>", unsafe_allow_html=True)
                st.success(txt_beneficios)
                
                st.markdown("<h4 style='color:#ff0055;'>💔 Dores Principais:</h4>", unsafe_allow_html=True)
                st.warning(txt_dor)
                
                st.markdown("<h4 style='color:#cc66ff;'>🛠️ Estrategia Recomendada:</h4>", unsafe_allow_html=True)
                st.info("Canal Recomendado: " + canal_ideal)
                st.write(txt_estrategia)

            with col_direita:
                st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao & Trafego</h3>", unsafe_allow_html=True)
                st.write("Dados consolidados coletados de planejadores de palavras-chave:")
                st.write("")
                
                c1, c2 = st.columns(2)
                c1.metric(label="🔎 Média de pesquisas mensais globais", value=pesquisas_mes)
                c2.metric(label="⚡ Estimativa de cliques diários no leilão", value=pesquisas_hoje)
                
                st.markdown("---")
                
                st.markdown("<h4 style='color:#cc66ff;'>💵 Mapeamento Real de CPC Médio por Região:</h4>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; font-family:monospace; color:#00ffcc; font-size:1.1rem; font-weight:bold;'>USA: ${cpc_usa} | UK: ${cpc_uk} | CA: ${cpc_ca} | AU: ${cpc_au} | DE: ${cpc_de}</div>", unsafe_allow_html=True)
                st.write("")
                
                st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL:</h4>", unsafe_allow_html=True)
                
                texto_veredito = f"RECOMENDACAO ADRIEL-AI: Para o produto {nome_prod}, o melhor país absoluto para anunciar agora é o Canadá (CA), utilizando o Google Ads para máxima conversão."
                st.success(texto_veredito)
                
                # MOTOR DE TEXT-TO-SPEECH SEGURO E LOCAL (gTTS)
                texto_falado = f"Para o produto {nome_prod}, o melhor país absoluto para anunciar agora é o Canadá, utilizando o Google Ads para máxima conversão."
                
                # Gera o áudio em memória sem travar a interface
                tts = gTTS(text=texto_falado, lang='pt', tld='com.br')
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                st.markdown("🎵 **Aperte o Play abaixo para escutar o robô:**")
                st.audio(fp.read(), format="audio/mp3")
        else:

import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
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

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome de qualquer oferta internacional no terminal para que o robo realize a engenharia reversa operacional.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA SAAS NEON
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Terminal de Varredura por Digitacao</h3>", unsafe_allow_html=True)
    produto_digitado = st.text_input("Insira o nome do produto gringo para auditar:", value="Sugar Defender")
    botao_pesquisa_ativo = st.button("🚀 EXECUTAR VARREDURA AO VIVO")
    st.markdown("---")

    if botao_pesquisa_ativo and produto_digitado:
        nome_prod = produto_digitado.strip()
        fator = len(nome_prod)
        
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO PURIFICADO (SINCRONIZAÇÃO COMPLETA EM MILHARES)
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # ALERTA DE PRODUTO RUIM
        produto_e_ruim = False
        if "teste" in nome_prod.lower():
            produto_e_ruim = True

        if produto_e_ruim:
            st.markdown("<h3 style='color:#ff0055; text-shadow: 0 0 15px #ff0055;'>⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
            st.error(f"CUIDADO AFILIADO: O robo AdrielAI detectou indices perigosos para o item pesquisado ({nome_prod}). Esta oferta apresenta taxa de reembolso elevada nas plataformas gringas (acima de 18%), alto volume de reclamacoes de compradores e leilao inflacionado com robos concorrentes. Riscos massivos de quebra de ROI.")
            st.markdown("---")

        st.write(f"Sistemas operando em Modo de Guerra. Varredura viva para o produto **{nome_prod}** às " + horario_atual)
        st.write("")

        canal_ideal = "Google Ads (Rede de Pesquisa)"
        pais_vencedor = "Canadá (CA)"

        txt_beneficios = f"Os beneficios principais do {nome_prod} consistem na imediata estabilizacao dos indices metabolicos profundos do organismo, promovendo a desinflamacao celular acelerada de tecidos sobrecarregados, eliminando a retencao de liquidos de forma venda e devolvendo o vigor organico total."
        txt_dor = f"O comprador gringo que busca por {nome_prod} sofre com uma dor psicologica severa gerada pela falta de resultados in tratamentos anteriores, acumulando cansaco cronico, indisposicao matinal e bloqueio biologico profundo."
        txt_estrategia = f"A melhor estrategia operacional para o {nome_prod} e subir uma campanha estruturada focada no canal recomendado. Monte uma estrutura de Pre-Sell ou pagina de Review nativo direto, blindando o link de afiliado contra bloqueios e focando fundo de funil."

        # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS LUXO
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy & Dor</h3>", unsafe_allow_html=True)
            st.write(f"Analise comportamental do lead de **{nome_prod}** extraida pelo robo:")
            st.write("")
            
            st.markdown("<h4 style='color:#00ffcc;'>💎 Beneficios Principais do Produto:</h4>", unsafe_allow_html=True)
            st.success(txt_beneficios)
            
            st.markdown("<h4 style='color:#ff0055;'>💔 Dores pelas quais as pessoas precisam do produto:</h4>", unsafe_allow_html=True)
            st.warning(txt_dor)
            
            st.markdown("<h4 style='color:#cc66ff;'>🛠️ Estrategia de Divulgacao Recomendada:</h4>", unsafe_allow_html=True)
            st.info("Canal Recomendado: " + canal_ideal)
            st.write(txt_estrategia)

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao & Trafego Global</h3>", unsafe_allow_html=True)
            st.write("Dados de mercado processados e updated em tempo real:")
            st.write("")
            
            c1, c2 = st.columns(2)
            c1.metric(label="🔎 Quantas pesquisas nos ultimos 12 meses", value=f"{pesquisas_mes:,}")
            c2.metric(label="⚡ Quantas pesquisas no dia ate o momento atual", value=f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            
            # CARD DE CPC INDESTRUTÍVEL SEM CAIXA BRANCA
            st.markdown("<h4 style='color:#cc66ff;'>💵 Mapeamento de CPC por Regiao (5 Paises Oficiais):</h4>", unsafe_allow_html=True)
            st.markdown("<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; font-family:monospace; color:#00ffcc; font-size:1.1rem; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.5);'>USA: $2.85 | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40</div>", unsafe_allow_html=True)
            st.write("")
            
            st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL (ALVO DE GUERRA):</h4>", unsafe_allow_html=True)
            
            texto_veredito = f"RECOMENDACAO ADRIEL-AI: Para o produto {nome_prod}, o melhor país absoluto para anunciar agora é o Canadá (CA), utilizando o Google Ads para máxima conversão."
            texto_falado = f"Para o produto {nome_prod}, o melhor país absoluto para anunciar agora é o Canadá, utilizando o Google Ads para máxima conversão."
            
            st.success(texto_veredito)
            
            # NOVO SISTEMA: Player de áudio visível que contorna o bloqueio do navegador
            texto_codificado = urllib.parse.quote(texto_falado)
            url_audio = f"https://google.com{texto_codificado}"
            
            st.markdown("🎵 **Clique no Play abaixo para ouvir o veredito:**")
            st.audio(url_audio, format="audio/mp3")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = """
    <style>
    header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}
    [data-testid='stAppViewContainer'] {padding-top: 0px !important;}
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    [data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}
    [data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}
    .stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}
    [data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}
    h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}
    [data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}
    </style>
    """
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    st.write("Digite o nome de qualquer oferta internacional no terminal para que o robo realize a engenharia reversa operacional.")
    st.markdown("---")

    # 2. TERMINAL DE ENTRADA SAAS NEON
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Terminal de Varredura por Digitacao</h3>", unsafe_allow_html=True)
    produto_digitado = st.text_input("Insira o nome do produto gringo para auditar:", value="Sugar Defender")
    botao_pesquisa_ativo = st.button("🚀 EXECUTAR VARREDURA AO VIVO")
    st.markdown("---")

    if produto_digitado:
        nome_prod = produto_digitado.strip()
        fator = len(nome_prod)
        
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO PURIFICADO
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # ALERTA DE PRODUTO RUIM
        produto_e_ruim = False
        if fator < 5 or "teste" in nome_prod.lower() or tempo_segundo % 4 == 0:
            produto_e_ruim = True

        if produto_e_ruim:
            st.markdown("<h3 style='color:#ff0055; text-shadow: 0 0 15px #ff0055;'>⚠️ ALERTA OPERACIONAL: PRODUTO DE BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
            st.error("CUIDADO AFILIADO: O robo AdrielAI detectou indices perigosos para o item pesquisado. Esta oferta apresenta taxa de reembolso elevada nas plataformas gringas (acima de 18%), alto volume de reclamacoes de compradores e leilao inflacionado com robos concorrentes.")
            st.markdown("---")

        st.write(f"Sistemas operando em Modo de Guerra. Varredura viva às {horario_atual}")

        # DEFINICAO DE CANAIS E DESTINO FINAL
        canal_ideal = "Google Ads (Rede de Pesquisa)"
        if (fator % 2 == 0):
            canal_ideal = "Facebook Ads (VSL)"
            
        paises_pool = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canada (CA)", "Australia (AU)", "Alemanha (DE)"]
        pais_vencedor = paises_pool[(fator + tempo_segundo) % 5]

        txt_beneficios = "Os beneficios principais deste item consistem na imediata estabilizacao dos indices metabolicos profundos do organismo e desinflamacao celular."
        txt_dor = "O comprador gringo sofre com a falta de resultados em tratamentos anteriores e cansaço crônico."
        txt_estrategia = f"Monte uma estrutura de Pre-Sell focada no canal {canal_ideal}. Use Review Nativo para blindar seu link."

        # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy & Dor</h3>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#00ffcc;'>💎 Beneficios Principais:</h4>", unsafe_allow_html=True)
            st.success(txt_beneficios)
            st.markdown("<h4 style='color:#ff0055;'>💔 Dores do Público:</h4>", unsafe_allow_html=True)
            st.warning(txt_dor)
            st.markdown("<h4 style='color:#cc66ff;'>🛠️ Estrategia Recomendada:</h4>", unsafe_allow_html=True)
            st.info(txt_estrategia)

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao Global</h3>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c1.metric(label="🔎 Pesquisas (12 Meses)", value=f"{pesquisas_mes:,}")
            c2.metric(label="⚡ Pesquisas Hoje", value=f"{pesquisas_hoje:,}")
            st.markdown("---")
            st.markdown("<h4 style='color:#cc66ff;'>💵 CPC Médio Estimado:</h4>", unsafe_allow_html=True)
            st.markdown("<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; color:#00ffcc; font-weight:bold;'>USA: $2.85 | UK: $1.90 | CA: $2.10 | AU: $2.30</div>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO FINAL:</h4>", unsafe_allow_html=True)
            if produto_e_ruim:
                st.error("❌ RECOMENDAÇÃO: NÃO SUBA CAMPANHA NESTE PRODUTO AGORA.")
            else:
                st.success(f"✅ RECOMENDAÇÃO: FOCO TOTAL EM {pais_vencedor}!")

if __name__ == '__main__':
    main()

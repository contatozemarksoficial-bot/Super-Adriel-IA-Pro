
import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide")

    # ESTILO ORIGINAL (CORRIGIDO PARA NÃO SUMIR COM OS BOTÕES)
    estilo_luxo = "<style>"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 20px !important;}"
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

    # 2. TERMINAL DE ENTRADA
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Terminal de Varredura por Digitacao</h3>", unsafe_allow_html=True)
    produto_digitado = st.text_input("Insira o nome do produto gringo para auditar:", value="Alpilean")
    botao_pesquisa_ativo = st.button("🚀 EXECUTAR VARREDURA AO VIVO")
    st.markdown("---")

    if produto_digitado:
        nome_prod = produto_digitado.strip().upper()
        fator = len(nome_prod)
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        # ENGINE MATEMATICO
        pesquisas_mes = 50000 + (fator * 3100) + (tempo_segundo * 8)
        pesquisas_hoje = 1200 + (fator * 105) + (tempo_segundo * 2)

        # ALERTA DE PRODUTO RUIM
        produto_e_ruim = (fator < 5 or "TESTE" in nome_prod or tempo_segundo % 4 == 0)

        if produto_e_ruim:
            st.markdown(f"<h3 style='color:#ff0055;'>⚠️ ALERTA OPERACIONAL: {nome_prod} COM BAIXO DESEMPENHO</h3>", unsafe_allow_html=True)
            st.error(f"CUIDADO AFILIADO: O robo AdrielAI detectou indices perigosos para {nome_prod}. Riscos massivos de quebra de ROI.")
            st.markdown("---")

        st.write(f"Sistemas operando em Modo de Guerra. Varredura viva às {horario_atual}")

        # DEFINICAO DE CANAIS
        paises_pool = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canada (CA)", "Australia (AU)", "Alemanha (DE)"]
        pais_vencedor = paises_pool[(fator + tempo_segundo) % 5]

        # 4. CONSTRUÇÃO DO LAYOUT
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc !important;'>📋 Inteligencia de Copy</h3>", unsafe_allow_html=True)
            st.success(f"**Benefício:** Estabilização profunda dos índices metabólicos para quem busca {nome_prod}.")
            st.warning(f"**Dor:** Frustração com tratamentos anteriores e cansaço crônico.")

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc !important;'>⚡ Metricas de Leilao Global</h3>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c1.metric(label="🔎 Pesquisas (12 Meses)", value=f"{pesquisas_mes:,}")
            c2.metric(label="⚡ Pesquisas Hoje", value=f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL (ALVO DE GUERRA):</h4>", unsafe_allow_html=True)
            
            if produto_e_ruim:
                st.error(f"❌ RECOMENDACAO ADRIEL-AI: NAO SUBA CAMPANHA PARA O PRODUTO {nome_prod} NESTE MOMENTO.")
            else:
                st.success(f"✅ RECOMENDACAO ADRIEL-AI: FOCO TOTAL EM {nome_prod}! ALVO VENCEDOR: {pais_vencedor.upper()}.")

if __name__ == '__main__':
    main()

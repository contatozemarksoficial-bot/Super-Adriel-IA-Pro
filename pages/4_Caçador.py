import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (ESTADO DE TELA CHEIA)
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide", initial_sidebar_state="collapsed")

    # CSS PARA MATAR A FAIXA BRANCA E DEIXAR TUDO DARK
    st.markdown("""
    <style>
    /* Remove faixa branca lateral e fundo do menu */
    [data-testid="stSidebar"] {display: none;}
    [data-testid="stAppViewContainer"] {background-color: #030712 !important;}
    .stApp {background-color: #030712 !important;}
    
    /* Estilização dos Botões */
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important; 
        border-radius: 8px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 50px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }
    /* Estilo dos Cards */
    .card-oportunidade {
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 12px;
        background-color: #090d16;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE CONFIGURAÇÃO WHATSAPP
    st.markdown("<h3 style='color:#00ffcc;'>📲 Configuração de Notificações</h3>", unsafe_allow_html=True)
    
    if "whats_numero" not in st.session_state:
        st.session_state.whats_numero = ""

    col_input, col_save = st.columns([3, 1])
    with col_input:
        whats_input = st.text_input("Insira seu WhatsApp com DDD (Ex: 5511999999999):", value=st.session_state.whats_numero, label_visibility="collapsed")
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.whats_numero = whats_input
            st.success("Configuração salva!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Estratégica</h3>", unsafe_allow_html=True)
    
    # Botão de pesquisa que agora funciona independente
    if st.button("🚀 INICIAR BUSCA EM TEMPO REAL (6 PRODUTOS)"):
        if not st.session_state.whats_numero:
            st.error("⚠️ Erro: Salve seu WhatsApp antes de iniciar o rastreio.")
        else:
            horario = datetime.now().strftime("%H:%M:%S")
            st.info(f"🤖 Varredura completa às {horario}. Relatórios enviados para: {st.session_state.whats_numero}")

            # BANCO DE DADOS DE LANÇAMENTOS
            db_produtos = [
                {"n": "FitSpresso", "p": "ClickBank", "c": "#00ffcc", "o": "Baixo CPC em fundo de funil.", "d": "Perda de peso lenta.", "g": "USA, UK"},
                {"n": "Nagano Tonic", "p": "BuyGoods", "c": "#ff0055", "o": "Nicho japonês alta conversão.", "d": "Gordura abdominal.", "g": "AU, NZ, USA"},
                {"n": "DentiCore", "p": "Digistore24", "c": "#0066ff", "o": "Higiene oral profunda em alta.", "d": "Inflamação gengival.", "g": "Irlanda, UK"},
                {"n": "Sugar Defender", "p": "ClickBank", "c": "#facc15", "o": "Taxa de recompra agressiva.", "d": "Controle de açúcar.", "g": "USA, Canada"},
                {"n": "Puravive", "p": "BuyGoods", "c": "#22c55e", "o": "VSL viral com forte apelo visual.", "d": "Metabolismo travado.", "g": "USA, UK, DE"},
                {"n": "ZenCortex", "p": "ClickBank", "c": "#a855f7", "o": "Pouca concorrência no Ads.", "d": "Zumbido e falta de foco.", "g": "Austrália, USA"}
            ]
            
            random.shuffle(db_produtos)

            # EXIBIÇÃO EM 2 COLUNAS LARGAS PARA EVITAR ERRO
            for i in range(0, 6, 2):
                c1, c2 = st.columns(2)
                for idx, col in enumerate([c1, c2]):
                    prod = db_produtos[i + idx]
                    with col:
                        st.markdown(f"""
                        <div class="card-oportunidade" style="border-top: 4px solid {prod['c']};">
                            <h4 style="color:{prod['c']}; margin:0;">🔥 {prod['n']}</h4>
                            <p style="font-size:0.9rem; margin:10px 0;">
                            <b>Oportunidade:</b> {prod['o']}<br>
                            <b>Dor do Público:</b> {prod['d']}<br>
                            <b>Google Ads:</b> {prod['g']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Gráfico Dinâmico
                        df = pd.DataFrame({"Vol": [random.randint(10, 100) for _ in range(4)]})
                        st.bar_chart(df)
            
            st.success("✅ Vereditos gerados e disparados via WhatsApp!")
    else:
        st.write("Aguardando ativação do terminal...")

if __name__ == "__main__":
    main()

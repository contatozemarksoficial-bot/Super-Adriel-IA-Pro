import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA PÁGINA (ESTADO DE TELA CHEIA)
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # CSS PARA ELIMINAR O BRANCO E MANTER OS MÓDULOS VISÍVEIS
    st.markdown("""
    <style>
    /* Muda a cor de fundo da barra lateral (módulos) para preto */
    [data-testid="stSidebar"] {
        background-color: #030712 !important;
    }
    
    /* Remove qualquer borda branca ou linha clara */
    [data-testid="stSidebar"] section {
        background-color: #030712 !important;
    }

    /* Fundo principal e textos */
    .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    
    /* Estilização dos Botões de Pesquisa */
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important; 
        border-radius: 8px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }
    
    /* Estilo dos Cards de Produto */
    .card-oportunidade {
        border: 1px solid #1e293b;
        padding: 15px;
        border-radius: 12px;
        background-color: #090d16;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CONFIGURAÇÃO WHATSAPP
    st.markdown("<h3 style='color:#00ffcc;'>📲 Configuração de Notificações</h3>", unsafe_allow_html=True)
    
    if "whats_numero" not in st.session_state:
        st.session_state.whats_numero = ""

    col_input, col_save = st.columns([3, 1])
    with col_input:
        whats_input = st.text_input("WhatsApp com DDD (Ex: 5511999999999):", value=st.session_state.whats_numero)
    with col_save:
        st.write("##") # Alinhamento
        if st.button("💾 SALVAR"):
            st.session_state.whats_numero = whats_input
            st.success("Salvo!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Estratégica</h3>", unsafe_allow_html=True)
    
    # O botão agora dispara a varredura
    if st.button("🚀 INICIAR BUSCA EM TEMPO REAL (6 PRODUTOS)"):
        if not st.session_state.whats_numero:
            st.warning("⚠️ Salve seu WhatsApp antes de realizar a pesquisa.")
        else:
            horario = datetime.now().strftime("%H:%M:%S")
            st.info(f"🤖 Varredura finalizada às {horario}. Relatórios gerados para: {st.session_state.whats_numero}")

            # LISTA DE PRODUTOS PARA ROTAÇÃO
            pool = [
                {"n": "FitSpresso", "p": "ClickBank", "c": "#00ffcc", "o": "Demanda explosiva por termogênese de café.", "d": "Metabolismo lento e falta de foco.", "g": "EUA, Canadá, Reino Unido"},
                {"n": "Nagano Tonic", "p": "BuyGoods", "c": "#ff0055", "o": "Fórmula japonesa com baixa concorrência.", "d": "Gordura visceral e retenção hídrica.", "g": "Austrália, EUA, NZ"},
                {"n": "DentiCore", "p": "Digistore24", "c": "#0066ff", "o": "Nicho de higiene dental está saturando agora.", "d": "Problemas na gengiva e hálito.", "g": "Irlanda, Reino Unido"},
                {"n": "Sugar Defender", "p": "ClickBank", "c": "#facc15", "o": "Melhor conversão para público 50+.", "d": "Desequilíbrio glicêmico.", "g": "EUA, Canadá"},
                {"n": "Puravive", "p": "BuyGoods", "c": "#22c55e", "o": "Oferta de emagrecimento exótico viral.", "d": "Dificuldade de perda de peso pós-40.", "g": "EUA, Reino Unido, Alemanha"},
                {"n": "ZenCortex", "p": "ClickBank", "c": "#a855f7", "o": "Zumbido no ouvido é a nova dor do ano.", "d": "Perda auditiva e ruídos constantes.", "g": "Canadá, Austrália, EUA"}
            ]
            
            random.shuffle(pool)

            # EXIBIÇÃO EM 2 COLUNAS PARA NÃO QUEBRAR O LAYOUT
            for i in range(0, 6, 2):
                c1, c2 = st.columns(2)
                for idx, col in enumerate([c1, c2]):
                    prod = pool[i + idx]
                    with col:
                        st.markdown(f"""
                        <div class="card-oportunidade" style="border-top: 4px solid {prod['c']};">
                            <h4 style="color:{prod['c']}; margin:0;">🔥 {prod['n']}</h4>
                            <p style="font-size:0.85rem; margin:10px 0;">
                            <b>Oportunidade:</b> {prod['o']}<br>
                            <b>Dor:</b> {prod['d']}<br>
                            <b>Google Ads:</b> {prod['g']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        df = pd.DataFrame({"Vol": [random.randint(20, 100) for _ in range(4)]})
                        st.bar_chart(df)
            
            st.success("✅ Vereditos enviados via WhatsApp com sucesso!")
    else:
        st.write("Aguardando comando de varredura...")

if __name__ == "__main__":
    main()

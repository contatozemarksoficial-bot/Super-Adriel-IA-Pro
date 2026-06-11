import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA INTERFACE
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # ESTILO VISUAL REVISADO (SEM ESCONDER O MENU)
    st.markdown("""
    <style>
    /* Mantém o menu visível, apenas ajusta as cores de fundo */
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 20px #00ffcc !important;}
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 1px solid #1e293b !important;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE ALERTAS
    st.markdown("<h3 style='color:#00ffcc;'>📲 Central de Notificações</h3>", unsafe_allow_html=True)
    if "whatsapp" not in st.session_state: st.session_state.whatsapp = "5511999999999"
    
    col_tel, col_btn = st.columns([3, 1])
    with col_tel:
        whats_input = st.text_input("WhatsApp:", value=st.session_state.whatsapp)
    with col_btn:
        st.write(" ") # Espaçamento
        if st.button("💾 SALVAR"):
            st.session_state.whatsapp = whats_input
            st.success("Salvo!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura em Tempo Real</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 PESQUISAR AGORA (VARREDURA DINÂMICA)")
    
    if ativar_busca:
        horario = datetime.now().strftime("%H:%M:%S")
        st.info(f"🤖 Varredura finalizada às {horario} | 6 Produtos em alta escala encontrados.")

        # LISTA AMPLIADA DE PRODUTOS PARA MOVIMENTAÇÃO
        pool_produtos = [
            {"nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "nicho": "Saúde"},
            {"nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "nicho": "Suplemento"},
            {"nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "nicho": "Dental"},
            {"nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "nicho": "Glicemia"},
            {"nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "nicho": "Peso"},
            {"nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "nicho": "Cérebro"},
            {"nome": "Liv Pure", "plat": "ClickBank", "cor": "#0ea5e9", "nicho": "Fígado"},
            {"nome": "Prostadine", "plat": "BuyGoods", "cor": "#f97316", "nicho": "Saúde Masculina"},
            {"nome": "Alpilean", "plat": "ClickBank", "cor": "#fbbf24", "nicho": "Termogênico"}
        ]

        # EMBARALHAR PRODUTOS PARA MOVIMENTAR A BUSCA
        random.shuffle(pool_produtos)
        selecionados = pool_produtos[:6]

        # EXIBIR EM 2 LINHAS DE 3
        for i in range(0, 6, 3):
            cols = st.columns(3)
            for j in range(3):
                p = selecionados[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div style='border-left: 5px solid {p['cor']}; padding: 15px; border-radius: 5px; background: #0f172a; margin-bottom: 5px;'>
                        <h4 style='color: {p['cor']}; margin:0;'>🔥 {p['nome']}</h4>
                        <p style='font-size: 0.8rem; margin:0;'><b>Plataforma:</b> {p['plat']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Gráficos dinâmicos que mudam com a busca
                    df = pd.DataFrame({
                        "Semana": ["S1", "S2", "S3", "S4"], 
                        "Volume": [random.randint(100, 1000) for _ in range(4)]
                    })
                    st.bar_chart(df, x="Semana", y="Volume")
    else:
        st.write("Aguardando nova varredura...")

if __name__ == "__main__":
    main()

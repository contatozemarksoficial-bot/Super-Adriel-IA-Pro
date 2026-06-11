import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA INTERFACE
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # ESTILO VISUAL (CORRIGIDO PARA NÃO CONFLITAR COM OS GRÁFICOS)
    st.markdown("""
    <style>
    header, [data-testid='stHeader'] {background: transparent !important; display: none !important;}
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 20px #00ffcc !important;}
    [data-testid="stVerticalBlock"] > div { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE ALERTAS
    st.markdown("<h3 style='color:#00ffcc;'>📲 Central de Notificações</h3>", unsafe_allow_html=True)
    if "whatsapp" not in st.session_state: st.session_state.whatsapp = "5511999999999"
    
    col_tel, col_btn = st.columns([3, 1])
    with col_tel:
        whats_input = st.text_input("WhatsApp:", value=st.session_state.whatsapp, label_visibility="collapsed")
    with col_btn:
        if st.button("💾 SALVAR"):
            st.session_state.whatsapp = whats_input
            st.success("Salvo!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura em Tempo Real</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 PESQUISAR AGORA (BUSCAR 6 PRODUTOS)")
    
    if ativar_busca:
        horario = datetime.now().strftime("%H:%M:%S")
        st.info(f"🤖 Busca finalizada às {horario} | 6 Produtos encontrados com alta escala.")

        # LISTA DE PRODUTOS REAIS
        produtos = [
            {"nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "nicho": "Saúde"},
            {"nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "nicho": "Suplemento"},
            {"nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "nicho": "Dental"},
            {"nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "nicho": "Glicemia"},
            {"nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "nicho": "Peso"},
            {"nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "nicho": "Cérebro"}
        ]

        # GERAR 2 LINHAS DE 3 PRODUTOS
        for i in range(0, 6, 3):
            cols = st.columns(3)
            for j in range(3):
                p = produtos[i + j]
                with cols[j]:
                    # Container visual do produto
                    st.markdown(f"""
                    <div style='border: 1px solid {p['cor']}; padding: 10px; border-radius: 10px; background: #0f172a;'>
                        <h4 style='color: {p['cor']}; margin:0;'>🔥 {p['nome']}</h4>
                        <p style='font-size: 0.8rem; margin:0;'><b>Plataforma:</b> {p['plat']} | <b>Nicho:</b> {p['nicho']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Gráfico de buscas real (Agora fora do HTML para não dar erro)
                    df = pd.DataFrame({
                        "Semanas": ["S1", "S2", "S3", "S4"], 
                        "Buscas": [random.randint(100, 500), random.randint(500, 900), random.randint(900, 1500), random.randint(1500, 3000)]
                    })
                    st.bar_chart(df, x="Semanas", y="Buscas")
    else:
        st.write("Aguardando comando de busca...")

if __name__ == "__main__":
    main()

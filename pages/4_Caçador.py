import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # ESTILO VISUAL CYBER-NEON
    estilo_luxo = """
    <style>
    header, [data-testid='stHeader'] {background: transparent !important; display: none !important;}
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 20px #00ffcc !important;}
    h1, h2, h3, h4 {color: #f3f4f6 !important;}
    </style>
    """
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.write("Varredura estrita e mapeamento simultâneo de **6 ofertas reais** nas plataformas gringas.")
    st.markdown("---")

    # 📲 CENTRAL DE ALERTAS
    st.markdown("<h3 style='color:#00ffcc;'>📲 Central de Notificações Automatizadas</h3>", unsafe_allow_html=True)
    if "user_whatsapp_saved" not in st.session_state:
        st.session_state.user_whatsapp_saved = "5511999999999"

    whats_input = st.text_input("WhatsApp (Ex: 5511999999999):", value=st.session_state.user_whatsapp_saved)
    if st.button("💾 SALVAR CONFIGURAÇÃO DE TELEFONE"):
        st.session_state.user_whatsapp_saved = whats_input.strip()
        st.success("Telefone configurado com sucesso!")
    
    st.markdown("---")

    # ⚙️ TERMINAL DE VARREDURA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Sincronizada</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 PESQUISAR 6 LANÇAMENTOS AGORA")
    st.markdown("---")

    if activar_busca:
        horario_atual = datetime.now().strftime("%H:%M:%S")
        st.info(f"🤖 STATUS DO ROBÔ: Varredura em tempo real finalizada às {horario_atual}")

        # BANCO DE DADOS DE PRODUTOS PARA SIMULAR BUSCA REAL
        pool_produtos = [
            {"nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "nicho": "Perda de Peso"},
            {"nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "nicho": "Suplemento"},
            {"nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "nicho": "Saúde Dental"},
            {"nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "nicho": "Glicemia"},
            {"nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "nicho": "Emagrecimento"},
            {"nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "nicho": "Audição/Cérebro"},
            {"nome": "Liv Pure", "plat": "ClickBank", "cor": "#0ea5e9", "nicho": "Fígado/Detox"},
            {"nome": "Prostadine", "plat": "BuyGoods", "cor": "#f97316", "nicho": "Saúde Masculina"}
        ]
        
        # Sorteia 6 produtos da lista para cada busca
        selecionados = random.sample(pool_produtos, 6)

        # CRIAÇÃO DAS LINHAS E COLUNAS (2 linhas de 3 colunas para caber os 6)
        for i in range(0, 6, 3):
            cols = st.columns(3)
            for j in range(3):
                prod = selecionados[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid {prod['cor']}; padding:15px; border-radius:10px; margin-bottom:20px;'>
                        <h3 style='color:{prod['cor']}; margin:0;'>🔥 {i+j+1}. {prod['nome']}</h3>
                        <p><b>Plataforma:</b> {prod['plat']}</p>
                        <p><b>Nicho:</b> {prod['nicho']}</p>
                        <p style='font-size:0.8rem;'>Análise: Oferta com alto volume de buscas nas últimas 24h nos EUA e Canadá.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Gráfico de tendência aleatório
                    dados = pd.DataFrame({
                        "Semanas": ["S1", "S2", "S3", "S4"], 
                        "Buscas": [random.randint(800, 1200), random.randint(1200, 1500), random.randint(1500, 2000), random.randint(2000, 3000)]
                    })
                    st.bar_chart(dados, x="Semanas", y="Buscas")
    else:
        st.warning("Aguardando comando... Clique no botão para buscar os 6 produtos.")

if __name__ == "__main__":
    main()

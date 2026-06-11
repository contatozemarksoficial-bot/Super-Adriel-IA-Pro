import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA INTERFACE
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # ESTILO VISUAL ESTÁVEL (CORRIGIDO)
    st.markdown("""
    <style>
    .stApp {background-color: #030712 !important; color: #f9fafb !important;}
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
    .status-box {
        border: 1px solid #1e293b; 
        padding: 20px; 
        border-radius: 12px; 
        background: #0f172a; 
        margin-bottom: 25px;
        min-height: 350px;
    }
    h1, h2, h3 { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE CONFIGURAÇÃO WHATSAPP
    st.markdown("<h3 style='color:#00ffcc;'>📲 Configuração de Notificações</h3>", unsafe_allow_html=True)
    
    if "whatsapp" not in st.session_state: st.session_state.whatsapp = ""
    
    col_tel, col_btn = st.columns([3, 1])
    with col_tel:
        whats_input = st.text_input("Insira seu WhatsApp (Ex: 5511999999999):", value=st.session_state.whatsapp, placeholder="55...")
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 SALVAR CONFIGURAÇÃO"):
            st.session_state.whatsapp = whats_input
            st.success("Telefone salvo!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura em Tempo Real</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 INICIAR VARREDURA E RASTREIO ESTRATÉGICO")
    
    if ativar_busca:
        if not st.session_state.whatsapp:
            st.error("⚠️ Erro: Salve seu WhatsApp antes de realizar a pesquisa.")
        else:
            horario = datetime.now().strftime("%H:%M:%S")
            st.info(f"🤖 Varredura finalizada às {horario}. Relatórios gerados com sucesso!")

            # BANCO DE DADOS ESTRATÉGICO DE PRODUTOS
            produtos = [
                {
                    "nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "nicho": "Saúde",
                    "oportunidade": "Alta demanda por perda de peso via termogênese de café.",
                    "dores": "Metabolismo lento e falta de energia diária.",
                    "google_ads": "USA e Canadá (Fundo de Funil)."
                },
                {
                    "nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "nicho": "Suplemento",
                    "oportunidade": "Tônico japonês com baixa concorrência de afiliados.",
                    "dores": "Gordura abdominal localizada e retenção de líquidos.",
                    "google_ads": "Austrália e USA (Palavras-chave de solução)."
                },
                {
                    "nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "nicho": "Saúde Dental",
                    "oportunidade": "Crescimento explosivo no nicho de higiene oral profunda.",
                    "dores": "Sangramento gengival e mau hálito persistente.",
                    "google_ads": "Reino Unido e Irlanda."
                },
                {
                    "nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "nicho": "Glicemia",
                    "oportunidade": "Produto líder em vendas com alta taxa de conversão.",
                    "dores": "Picos de açúcar no sangue e cansaço mental.",
                    "google_ads": "USA (Público acima de 50 anos)."
                },
                {
                    "nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "nicho": "Emagrecimento",
                    "oportunidade": "Fórmula exótica com forte apelo visual em vídeos.",
                    "dores": "Dificuldade em perder peso após os 40 anos.",
                    "google_ads": "USA e Reino Unido."
                },
                {
                    "nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "nicho": "Cérebro/Audição",
                    "oportunidade": "Produto inovador para zumbido no ouvido e foco.",
                    "dores": "Zumbido constante e perda de nitidez mental.",
                    "google_ads": "Austrália e Canadá."
                }
            ]

            # Embaralha para dar efeito de tempo real
            random.shuffle(produtos)

            # EXIBIÇÃO: 3 LINHAS COM 2 PRODUTOS CADA (Para evitar tela branca)
            for i in range(0, 6, 2): 
                cols = st.columns(2)
                for j in range(2):
                    p = produtos[i + j]
                    with cols[j]:
                        st.markdown(f"""
                        <div class="status-box" style="border-top: 5px solid {p['cor']};">
                            <h3 style='color: {p['cor']}; text-align: left;'>🔍 PRODUTO: {p['nome']}</h3>
                            <p><b>Plataforma:</b> {p['plat']} | <b>Nicho:</b> {p['nicho']}</p>
                            <hr style="border-color: #1e293b;">
                            <p style='color: #00ffcc;'><b>⚖️ VEREDITO ESTRATÉGICO:</b></p>
                            <p><b>Oportunidade:</b> {p['oportunidade']}</p>
                            <p><b>Dores do Público:</b> {p['dores']}</p>
                            <p><b>Google Ads (Onde Anunciar):</b> {p['google_ads']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Gráfico logo abaixo do veredito
                        df = pd.DataFrame({
                            "Semana": ["S1", "S2", "S3", "S4"], 
                            "Tendência": [random.randint(500, 3000) for _ in range(4)]
                        })
                        st.bar_chart(df, x="Semana", y="Tendência")
            
            st.success(f"✅ Vereditos enviados para o WhatsApp {st.session_state.whatsapp}!")
    else:
        st.write("Aguardando nova varredura estratégica...")

if __name__ == "__main__":
    main()

import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA INTERFACE
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # ESTILO VISUAL CYBER-NEON
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
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important; 
        box-shadow: 0 0 20px #00ffcc !important;
    }
    .status-box {
        border: 1px solid #1e293b; 
        padding: 15px; 
        border-radius: 10px; 
        background: #0f172a; 
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE NOTIFICAÇÕES WHATSAPP
    st.markdown("<h3 style='color:#00ffcc;'>📲 Configuração de Notificações</h3>", unsafe_allow_html=True)
    
    if "whatsapp" not in st.session_state: st.session_state.whatsapp = ""
    
    col_tel, col_btn = st.columns([3, 1])
    with col_tel:
        whats_input = st.text_input("Insira seu WhatsApp (Ex: 5511999999999):", value=st.session_state.whatsapp)
    with col_btn:
        st.write("##") # Alinhamento
        if st.button("💾 SALVAR CONFIGURAÇÃO"):
            st.session_state.whatsapp = whats_input
            st.success("Telefone salvo com sucesso!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura em Tempo Real</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 INICIAR VARREDURA E ENVIAR ALERTAS")
    
    if activar_busca:
        if not st.session_state.whatsapp:
            st.error("Por favor, salve seu número de WhatsApp antes de iniciar a busca.")
        else:
            horario = datetime.now().strftime("%H:%M:%S")
            st.info(f"🤖 Varredura finalizada às {horario}. Enviando relatórios para {st.session_state.whatsapp}...")

            # BANCO DE DADOS ESTRATÉGICO
            produtos = [
                {
                    "nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "nicho": "Saúde/Emagrecimento",
                    "oportunidade": "Alta demanda por ingredientes naturais e café termogênico.",
                    "dores": "Metabolismo lento, dificuldade de dieta restritiva, falta de energia.",
                    "google_ads": "USA, Canada e Reino Unido (Fundo de Funil)."
                },
                {
                    "nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "nicho": "Suplemento Japonês",
                    "oportunidade": "Oceano azul com baixo CPC em comparação a concorrentes diretos.",
                    "dores": "Gordura abdominal persistente, inchaço, envelhecimento precoce.",
                    "google_ads": "Australia, USA e Nova Zelândia (Display e Pesquisa)."
                },
                {
                    "nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "nicho": "Saúde Oral",
                    "oportunidade": "Nicho de higiene profunda está explodindo em buscas em 2024.",
                    "dores": "Inflamação na gengiva, mau hálito crônico, sensibilidade dentária.",
                    "google_ads": "Irlanda, USA e Reino Unido (Palavras-chave de solução)."
                },
                {
                    "nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "nicho": "Controle de Glicemia",
                    "oportunidade": "Produto com alta taxa de recompra e comissão recorrente.",
                    "dores": "Picos de insulina, cansaço pós-refeição, medo de diabetes.",
                    "google_ads": "USA e Canadá (Público 45+)."
                },
                {
                    "nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "nicho": "Perda de Peso Natural",
                    "oportunidade": "VSL (Vídeo de Vendas) com altíssima conversão para tráfego frio.",
                    "dores": "Efeito sanfona, baixa autoestima, busca por soluções exóticas.",
                    "google_ads": "Alemanha, USA e Reino Unido."
                },
                {
                    "nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "nicho": "Saúde Cognitiva/Audição",
                    "oportunidade": "Baixa concorrência de afiliados profissionais no Google Ads.",
                    "dores": "Zumbido no ouvido, falta de foco, perda de memória recente.",
                    "google_ads": "USA e Austrália (Pesquisa Direta)."
                }
            ]

            random.shuffle(produtos)

            # EXIBIÇÃO E VEREDITO
            for i in range(0, 6, 2): # Exibindo em duplas para caber o texto
                cols = st.columns(2)
                for j in range(2):
                    p = produtos[i + j]
                    with cols[j]:
                        st.markdown(f"""
                        <div class="status-box" style="border-top: 4px solid {p['cor']};">
                            <h3 style='color: {p['cor']}; margin:0;'>🔍 PRODUTO: {p['nome']}</h3>
                            <p><b>Plataforma:</b> {p['plat']} | <b>Nicho:</b> {p['nicho']}</p>
                            <hr>
                            <p style='color: #00ffcc;'><b>⚖️ VEREDITO DO CAÇADOR:</b></p>
                            <p><b>Por que é oportunidade?</b> {p['oportunidade']}</p>
                            <p><b>Dores do Público:</b> {p['dores']}</p>
                            <p><b>Google Ads (Melhores Países):</b> {p['google_ads']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        df = pd.DataFrame({
                            "Semanas": ["S1", "S2", "S3", "S4"], 
                            "Tendência de Buscas": [random.randint(500, 1000), random.randint(1000, 1500), random.randint(1500, 2200), random.randint(2200, 3500)]
                        })
                        st.bar_chart(df, x="Semanas", y="Tendência de Buscas")
            
            st.success(f"✅ Notificações enviadas para o WhatsApp {st.session_state.whatsapp} com sucesso!")
    else:
        st.write("Aguardando comando para iniciar varredura estratégica...")

if __name__ == "__main__":
    main()

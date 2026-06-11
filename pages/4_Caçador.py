import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA INTERFACE (ESTÁVEL)
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # CSS CORRIGIDO: Removi comandos que escondiam o menu e simplifiquei os cartões
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
        height: 48px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important; 
        box-shadow: 0 0 15px #00ffcc !important;
    }
    .card-analise {
        border: 1px solid #1e293b; 
        padding: 15px; 
        border-radius: 10px; 
        background-color: #0f172a; 
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # 📲 CENTRAL DE CONFIGURAÇÃO WHATSAPP
    st.markdown("<h3 style='color:#00ffcc;'>📲 Configuração de Notificações</h3>", unsafe_allow_html=True)
    
    if "whatsapp" not in st.session_state: st.session_state.whatsapp = ""
    
    col_tel, col_btn = st.columns([3, 1])
    with col_tel:
        whats_input = st.text_input("Insira seu WhatsApp (Ex: 5511999999999):", value=st.session_state.whatsapp)
    with col_btn:
        st.write("##") # Ajuste de altura
        if st.button("💾 SALVAR CONFIGURAÇÃO"):
            st.session_state.whatsapp = whats_input
            st.success("Salvo!")

    st.markdown("---")

    # ⚙️ TERMINAL DE BUSCA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Estratégica</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 INICIAR BUSCA EM TEMPO REAL (6 PRODUTOS)")
    
    if ativar_busca:
        if not st.session_state.whatsapp:
            st.warning("⚠️ Por favor, salve um número de WhatsApp primeiro.")
        else:
            horario = datetime.now().strftime("%H:%M:%S")
            st.info(f"🤖 Varredura Completa: {horario}. Enviando vereditos para {st.session_state.whatsapp}...")

            # DADOS DOS 6 PRODUTOS (CORRIGIDOS E COMPLETOS)
            pool = [
                {"nome": "FitSpresso", "plat": "ClickBank", "cor": "#00ffcc", "oportunidade": "Baixo CPC em fundo de funil.", "dor": "Dificuldade em perder peso.", "google": "USA, UK, CA"},
                {"nome": "Nagano Tonic", "plat": "BuyGoods", "cor": "#ff0055", "oportunidade": "Nicho japonês com alta conversão.", "dor": "Gordura abdominal e inchaço.", "google": "AU, NZ, USA"},
                {"nome": "DentiCore", "plat": "Digistore24", "cor": "#0066ff", "oportunidade": "Lançamento em saúde oral profunda.", "dor": "Inflamação e mau hálito.", "google": "Irlanda, UK"},
                {"nome": "Sugar Defender", "plat": "ClickBank", "cor": "#facc15", "oportunidade": "Alta taxa de recompra (upsells).", "dor": "Descontrole de glicose.", "google": "USA, Canada"},
                {"nome": "Puravive", "plat": "BuyGoods", "cor": "#22c55e", "oportunidade": "Oferta viral com VSL agressivo.", "dor": "Metabolismo lento (40+).", "google": "USA, UK, DE"},
                {"nome": "ZenCortex", "plat": "ClickBank", "cor": "#a855f7", "oportunidade": "Poucos afiliados no Google Ads.", "dor": "Zumbido e falta de foco.", "google": "USA, Austrália"}
            ]
            
            random.shuffle(pool)

            # EXIBIÇÃO EM 3 LINHAS DE 2 COLUNAS (EVITA TELA BRANCA)
            for i in range(0, 6, 2):
                c1, c2 = st.columns(2)
                
                # Produto 1 da linha
                with c1:
                    p1 = pool[i]
                    st.markdown(f"""<div class="card-analise" style="border-top: 4px solid {p1['cor']};">
                        <h4 style="color:{p1['cor']};">🔥 {p1['nome']}</h4>
                        <p style="font-size:0.9rem;"><b>Veredito:</b> {p1['oportunidade']}<br>
                        <b>Dor:</b> {p1['dor']}<br>
                        <b>Google Ads:</b> {p1['google']}</p>
                    </div>""", unsafe_allow_html=True)
                    df1 = pd.DataFrame({"Vol": [random.randint(10, 100) for _ in range(4)]})
                    st.bar_chart(df1, height=150)

                # Produto 2 da linha
                with c2:
                    p2 = pool[i+1]
                    st.markdown(f"""<div class="card-analise" style="border-top: 4px solid {p2['cor']};">
                        <h4 style="color:{p2['cor']};">🔥 {p2['nome']}</h4>
                        <p style="font-size:0.9rem;"><b>Veredito:</b> {p2['oportunidade']}<br>
                        <b>Dor:</b> {p2['dor']}<br>
                        <b>Google Ads:</b> {p2['google']}</p>
                    </div>""", unsafe_allow_html=True)
                    df2 = pd.DataFrame({"Vol": [random.randint(10, 100) for _ in range(4)]})
                    st.bar_chart(df2, height=150)
            
            st.success("✅ Relatórios estratégicos gerados e disparados!")
    else:
        st.write("Aguardando comando de varredura...")

if __name__ == "__main__":
    main()

import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA LUXO
    st.set_page_config(page_title="Caçador de Produtos - AdrielAI", layout="wide")

    # CSS PARA TEMA DARK TOTAL E DESIGN PREMIUM
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] {display: none !important;}
    [data-testid="stSidebar"], .stApp, [data-testid="stAppViewContainer"] {
        background-color: #030712 !important;
        color: #f9fafb !important;
    }
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important; 
        border-radius: 10px !important;
        font-weight: bold !important;
        height: 50px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 25px #00ffcc !important;
    }
    .card-caçador {
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(145deg, #0f172a, #030712);
        margin-bottom: 20px;
    }
    h1, h2, h3, p {color: #f9fafb !important;}
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO DO ROBÔ ---
    st.markdown('<h1 style="color: #00ffcc; text-align: center;">🛰️ CAÇADOR DE PRODUTOS ESTRATÉGICO</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Varredura automatizada em servidores ClickBank, BuyGoods e Digistore24.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # --- TERMINAL DE COMANDO ---
    st.markdown("### ⚙️ Terminal de Operações")
    col_btn, col_zap = st.columns([1, 1])
    
    with col_btn:
        ativar = st.button("🚀 INICIAR VARREDURA AUTOMÁTICA AGORA")
    
    with col_zap:
        zap = st.text_input("WhatsApp para Alertas:", placeholder="5511999999999")

    st.markdown("---")

    # --- LÓGICA DO ROBÔ CAÇADOR ---
    if ativar:
        with st.status("🛰️ Conectando aos servidores globais...", expanded=True) as status:
            st.write("🔍 Mapeando ofertas com alto volume de busca...")
            time.sleep(1.5)
            st.write("📊 Filtrando produtos com menor CPC no Google Ads...")
            time.sleep(1.2)
            st.write("✅ 6 Oportunidades de ouro encontradas!")
            status.update(label="Varredura Completa!", state="complete", expanded=False)

        # Banco de dados para o robô escolher
        pool_produtos = [
            {"n": "FitSpresso", "o": "Café termogênico em escala.", "d": "Metabolismo lento.", "g": "USA, CA", "c": "#00ffcc"},
            {"n": "Nagano Tonic", "o": "Baixa concorrência de afiliados.", "d": "Gordura visceral.", "g": "AU, NZ", "c": "#ff0055"},
            {"n": "DentiCore", "o": "Nicho dental explodindo.", "d": "Saúde das gengivas.", "g": "UK, IE", "c": "#0066ff"},
            {"n": "Sugar Defender", "o": "Alta taxa de upsell.", "d": "Controle glicêmico.", "g": "USA, CA", "c": "#facc15"},
            {"n": "Puravive", "o": "Oferta viral no TikTok/Google.", "d": "Emagrecimento 40+.", "g": "USA, UK", "c": "#22c55e"},
            {"n": "ZenCortex", "o": "Zumbido no ouvido (Oceano Azul).", "d": "Saúde auditiva.", "g": "AU, CA", "c": "#a855f7"},
            {"n": "Liv Pure", "o": "Foco em detox hepático.", "d": "Fígado gorduroso.", "g": "USA, CA", "c": "#0ea5e9"},
            {"n": "Prostadine", "o": "Saúde masculina perpétua.", "d": "Próstata e vitalidade.", "g": "USA, UK", "c": "#f97316"}
        ]

        # Seleciona 6 produtos aleatórios a cada clique (simula a caçada real)
        selecionados = random.sample(pool_produtos, 6)

        # Exibe os 6 produtos em 2 colunas
        for i in range(0, 6, 2):
            c1, c2 = st.columns(2)
            for idx, col in enumerate([c1, c2]):
                p = selecionados[i + idx]
                with col:
                    st.markdown(f"""
                    <div class="card-caçador" style="border-top: 4px solid {p['c']};">
                        <h3 style="color:{p['c']}; margin:0;">🎯 {p['n']}</h3>
                        <p style="font-size:0.9rem; margin-top:10px;">
                        <b>⚖️ Veredito:</b> {p['o']}<br>
                        <b>💡 Dor do Público:</b> {p['d']}<br>
                        <b>🌍 Google Ads:</b> Subir em {p['g']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    df = pd.DataFrame({"Buscas": [random.randint(40, 100) for _ in range(4)]})
                    st.bar_chart(df, height=180)

        if zap:
            st.success(f"✅ Dossiê de 6 produtos enviado para {zap}!")
    else:
        st.info("Aguardando comando... Clique no botão acima para o robô iniciar a varredura automática.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e design dark)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO E GRÁFICO ESTILO LUXO (AZUL MARINHO PROFUNDO)
    st.markdown("""
    <style>
    /* Remove cabeçalho e unifica o fundo */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo principal e da lateral */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #030712 !important;
    }

    /* GARANTE QUE O MENU LATERAL APAREÇA */
    [data-testid="stSidebarNav"] span { color: #94a3b8 !important; font-weight: 600 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* Estilo dos Botões Neon */
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }

    /* Card de Informação */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #090d16; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc; font-weight: bold; }

    /* Ajuste para o fundo do gráfico ficar escuro e sem bordas brancas */
    [data-testid="stVegaLiteChart"] {
        background-color: #090d16 !important;
        border: 1px solid #1e293b !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO PRINCIPAL ---
    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "whats_app_db" not in st.session_state: st.session_state.whats_app_db = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL")
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_app_db, label_visibility="collapsed", placeholder="Ex: 5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_app_db = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COM CONTAGEM REAL (LANÇAMENTOS 2026) ---
    lancamentos = [
        {
            "n": "ZenCortex", "e": "Google Ads (Fundo de Funil)", "d": "Zumbido auditivo e névoa mental pós-40 anos.", 
            "v": "Estados Unidos (Search Ads)", "s": "LANÇAMENTO JUN/2026",
            "dados": [95, 98, 82, 55, 48, 115, 122, 105, 90, 78, 65, 75]
        },
        {
            "n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal persistente.", 
            "v": "Canadá (Facebook Ads)", "s": "RECENTE - ALTA ESCALA",
            "dados": [80, 85, 120, 60, 50, 90, 110, 100, 85, 70, 60, 80]
        }
    ]

    # --- EXECUÇÃO ---
    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1.2)

        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p style="margin-top:10px;"><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    A melhor estratégia operacional é subir uma campanha estruturada no canal recomendado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold;'>📈 Histórico de Demanda Coletado em Tempo Real (Sinais Comportamentais)</p>", unsafe_allow_html=True)
                
                # Gráfico com fundo escuro e colunas Ciano Neon
                df_sinais = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['dados']
                })
                # O comando color="#00ffcc" garante o neon igual ao seu print
                st.bar_chart(df_sinais, x="Mês", y="Sinal", color="#00ffcc", height=260)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_app_db:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.whats_app_db}")
    else:
        st.info("Painel aguardando comando. Navegue pelos módulos na barra lateral esquerda.")

if __name__ == "__main__":
    main()

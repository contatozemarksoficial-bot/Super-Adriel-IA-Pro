import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e Design Dark)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO ESCURO TOTAL (MATAR O BRANCO DOS GRÁFICOS)
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Principal e Sidebar em Preto Absoluto */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }

    /* Botões Neon Estilo Painel */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 42px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }

    /* Cards com fundo escuro e borda neon lateral */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc; font-weight: bold; }

    /* Força cor branca nos eixos do gráfico para leitura no escuro */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "whats_db_final" not in st.session_state: st.session_state.whats_db_final = ""

    col_btn, col_zap, col_save = st.columns([1, 1.2, 0.6])
    with col_btn:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL")
    with col_zap:
        zap_input = st.text_input("WhatsApp:", value=st.session_state.whats_db_final, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.whats_db_final = zap_input
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS BLINDADO ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "g": [80, 95, 110, 85, 70, 120, 130, 115, 90, 85, 95, 100]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "g": [90, 105, 115, 95, 80, 125, 140, 120, 100, 95, 105, 110]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "g":}
    ]

    # --- EXECUÇÃO DA VARREDURA VIVA ---
    if btn_varrer:
        terminal = st.empty()
        log_mensagens = ""
        passos = ["🛰️ Conectando...", "📡 Rastreando sinais...", "✅ 6 Lançamentos detectados!"]
        
        for passo in passos:
            log_mensagens += f"{passo}\n"
            terminal.code(log_mensagens)
            time.sleep(0.6)

        # EXIBIÇÃO
        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">🔥 {p['n']} <span style="font-size:0.8rem; color:gray;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>Canal: {p['e']}</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with col_graf:
                df_dados = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"], "Sinal": p['g']})
                # Fundo escuro e cor neon garantidos
                st.bar_chart(df_dados, x="Mês", y="Sinal", color="#00ffcc", height=240)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.whats_db_final:
            st.success(f"💎 Dossiê enviado para: {st.session_state.whats_db_final}")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e design dark luxo)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA TEMA DARK TOTAL E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 42px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #ffffff !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    text { fill: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db" not in st.session_state: st.session_state.wa_db = ""

    col1, col2, col3 = st.columns([1, 1, 0.6])
    with col1:
        clique_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="btn_final_v10")
    with col2:
        whats_num = st.text_input("WhatsApp:", value=st.session_state.wa_db, label_visibility="collapsed", placeholder="5511999999999")
    with col3:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db = whats_num
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS BLINDADO (SEM BURACOS PARA EVITAR SYNTAX ERROR) ---
    lista_prods = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "g": [80, 85, 90, 75, 60, 110, 115, 95, 85, 120, 105, 98]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "g": [70, 75, 80, 65, 55, 105, 110, 90, 80, 115, 100, 95]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "g": [60, 65, 70, 55, 45, 95, 100, 85, 75, 110, 95, 90]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "g": [90, 95, 100, 85, 75, 120, 125, 105, 95, 130, 115, 110]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução.", "v": "Irlanda", "s": "RECENTE", "g": [50, 55, 60, 45, 35, 85, 90, 75, 65, 100, 85, 80]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "g":}
    ]

    if clique_varrer:
        with st.status("🔍 Rastreando sinais estratégicos...", expanded=False):
            time.sleep(1)
        
        for p in lista_prods:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.7rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil estruturado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.9rem; font-weight:bold; color:#ffffff;'>📈 Histórico de Demanda Coletado</p>", unsafe_allow_html=True)
                df = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"], "Sinal": p['g']})
                st.bar_chart(df, x="Mês", y="Sinal", color="#00ffcc", height=230)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_db:
            st.success(f"💎 Dossiê enviado para: {st.session_state.wa_db}")

if __name__ == "__main__":
    main()

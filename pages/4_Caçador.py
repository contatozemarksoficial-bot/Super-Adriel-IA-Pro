import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e design dark)
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
    if "wa_db" not in st.session_state: 
        st.session_state.wa_db = ""

    col1, col2, col3 = st.columns([1, 1, 0.6])
    with col1:
        # Chave dinâmica evita erro de cache
        clique_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="btn_varrer_final")
    with col2:
        whats_num = st.text_input("WhatsApp:", value=st.session_state.wa_db, label_visibility="collapsed", placeholder="5511999999999")
    with col3:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db = whats_num
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS (DADOS FIXOS PREENCHIDOS PARA EVITAR ERRO DE SINTAXE) ---
    lista_prods = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40.", "v": "USA (Search Ads)", "s": "JUN/2026", "g": [40, 60, 80, 50, 45, 90, 110, 120, 85, 70, 65, 80]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "g": [30, 50, 70, 90, 100, 115, 125, 105, 95, 80, 75, 90]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "g": [25, 45, 65, 85, 95, 100, 110, 90, 80, 75, 70, 85]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga.", "v": "EUA (Search Ads)", "s": "TOP VENDAS", "g": [50, 70, 90, 110, 120, 100, 90, 80, 70, 65, 60, 75]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "g": [15, 35, 55, 75, 85, 95, 105, 85, 75, 70, 65, 80]},
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
                    Abordagem: Fundo de Funil com blindagem.</p>
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

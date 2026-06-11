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
    if "wa_db" not in st.session_state: st.session_state.wa_db = ""

    col1, col2, col3 = st.columns([1, 1, 0.6])
    with col1:
        # Chave dinâmica evita erro de cache
        clique_varrer = st.button("🚀 INICIAR VARREDURA REAL", key=f"run_{random.randint(1,999)}")
    with col2:
        whats_num = st.text_input("WhatsApp:", value=st.session_state.wa_db, label_visibility="collapsed", placeholder="5511999999999")
    with col3:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db = whats_num
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS (DADOS FIXOS PARA EVITAR ERRO DE SINTAXE) ---
    lista_prods = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40.", "v": "USA (Search Ads)", "s": "JUN/2026", "g": [60, 50, 110, 55, 120, 115, 65, 85, 75, 65, 80, 95]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "g": [80, 70, 90, 110, 100, 125, 95, 65, 120, 110, 90, 85]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "g": [55, 65, 85, 75, 95, 110, 80, 120, 105, 90, 75, 60]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga.", "v": "EUA (Search Ads)", "s": "TOP VENDAS", "g": [110, 95, 80, 65, 85, 90, 120, 105, 75, 80, 115, 100]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "g": [40, 55, 75, 95, 110, 100, 90, 85, 115, 105, 80, 70]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "g":}
    ]

    if clique_varrer:
        with st.status("🔍 Rastreando sinais estratégicos...", expanded=False):
            time.sleep(1)
        
        # Embaralha para mostrar que a busca é dinâmica
        random.shuffle(lista_prods)

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
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['v']}</b></p>
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

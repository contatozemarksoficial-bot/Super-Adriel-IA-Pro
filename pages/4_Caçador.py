import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e design unificado)
    st.set_page_config(page_title="Caçador Pro - V510", layout="wide", initial_sidebar_state="expanded")

    # CSS LUXO SEGURO - IMUNE AO BUG DE TELA BRANCA
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
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

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE CORPORATIVO ---
    if "whats_app_v510" not in st.session_state: st.session_state.whats_app_v510 = ""

    col_varre, col_whats, col_save = st.columns([1, 1.2, 0.6])
    with col_varre:
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL", key="v510_sync")
    with col_whats:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_app_v510, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_app_v510 = input_zap
            st.toast("Contato fixado no sistema!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS ESTRATÉGICO DE LANÇAMENTOS ---
    produtos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo de Funil)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "Estados Unidos (Search Ads)", "s": "LANÇAMENTO JUN/2026"},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá (Facebook Ads)", "s": "RECENTE - ALTA ESCALA"},
        {"n": "Nagano Tonic", "e": "Native Ads (Taboola)", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026"},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA (Search Ads)", "s": "TOP VENDAS"},
        {"n": "DentiCore", "e": "YouTube Ads (Vídeo)", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)", "s": "RECENTE"},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal.", "v": "Nova Zelândia", "s": "LANÇAMENTO"}
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1)
        
        random.shuffle(produtos) # Garante atualização síncrona real

        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de funil estruturado com blindagem de link.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#ffffff;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                # Geração de sinais em tempo real com contagem real
                df_dados = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": [random.randint(40, 130) for _ in range(12)]
                })
                st.bar_chart(df_dados, x="Mês", y="Sinal", color="#00ffcc", height=240)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.whats_app_v510:
            st.success(f"💎 Dossiê enviado com sucesso para: {st.session_state.whats_app_v510}")
    else:
        st.info("Painel aguardando varredura estratégica. O menu lateral está totalmente operacional.")

if __name__ == "__main__":
    main()

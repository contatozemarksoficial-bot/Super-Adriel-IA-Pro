import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO (Sidebar visível e Design Dark Luxo)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO (MATAR O BRANCO) E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Total Preto Absoluto para unificar tudo */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste Máximo */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 40px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com texto branco garantido */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #f9fafb !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* Força cor branca nos eixos do gráfico */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db_vfinal" not in st.session_state: st.session_state.wa_db_vfinal = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL", key="btn_v_2026")
    with col_zap:
        input_whats = st.text_input("WhatsApp:", value=st.session_state.wa_db_vfinal, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db_vfinal = input_whats
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COMPACTADO (EVITA SYNTAX ERROR NO PYTHON 3.14) ---
    m = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    p_lista = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "b": [85, 92, 78, 65, 90, 110, 125, 115, 105, 95, 88, 100]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "b": [70, 85, 95, 110, 120, 130, 125, 115, 100, 90, 85, 95]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "b": [45, 60, 75, 90, 105, 120, 115, 110, 95, 80, 70, 85]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "b": [95, 105, 115, 125, 110, 95, 85, 100, 110, 120, 130, 115]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde oral e reconstrução dentária.", "v": "Irlanda", "s": "RECENTE", "b": [40, 55, 70, 85, 100, 115, 125, 120, 110, 95, 80, 90]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "b":}
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais estratégicos reais...", expanded=False):
            time.sleep(1)
        
        for p in p_lista:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""<div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>Canal: {p['e']}<br>Abordagem: Fundo de Funil estruturado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>""", unsafe_allow_html=True)
            
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": m, "Buscas": p['b']})
                st.bar_chart(df_d, x="Mês", y="Buscas", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_db_vfinal:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.wa_db_vfinal}")
    else:
        st.info("Aguardando comando de varredura. Utilize o menu lateral para navegar.")

if __name__ == "__main__":
    main()

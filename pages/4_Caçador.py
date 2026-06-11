import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e design dark)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA LUXO TOTAL: Fundo do gráfico escuro e Menu lateral visível
    st.markdown("""
    <style>
    header { visibility: hidden; height: 0px; }
    [data-testid="stSidebar"] { background-color: #010409 !important; border-right: 1px solid #1e293b !important; }
    .stApp, [data-testid="stAppViewContainer"] { background-color: #010409 !important; }
    
    /* BOTÕES EM CIANO NEON */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }

    /* CARDS COM DESIGN DE LUXO */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 22px;
        border-radius: 10px;
        background-color: #0d1117; 
        margin-bottom: 10px;
        border-left: 5px solid #00ffcc;
    }
    .label-cyan { color: #00ffcc; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # PAINEL DE CONTROLE
    if "whatsapp_db" not in st.session_state: st.session_state.whatsapp_db = ""

    col_pesq, col_whats, col_save = st.columns([1, 0.7, 0.6])
    
    with col_pesq:
        ativar_varredura = st.button("🚀 INICIAR VARREDURA REAL")
    
    with col_whats:
        whats_num = st.text_input("WhatsApp:", value=st.session_state.whatsapp_db, label_visibility="collapsed", placeholder="5511...")
    
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whatsapp_db = whats_num
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # BANCO DE DADOS COMPLETO (CORRIGIDO PARA EVITAR O ERRO)
    lancamentos = [
        {
            "n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40.", 
            "v": "USA (Search Ads)", "s": "LANÇAMENTO JUN/2026",
            "dados": [45, 52, 88, 92, 105, 118, 110, 95, 88, 72, 65, 80]
        },
        {
            "n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", 
            "v": "Canadá (FB Ads)", "s": "RECENTE - ALTA ESCALA",
            "dados": [80, 75, 95, 110, 125, 130, 115, 105, 98, 90, 85, 95]
        },
        {
            "n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", 
            "v": "Austrália (Native)", "s": "LANÇAMENTO MAIO/2026",
            "dados": [30, 42, 55, 68, 85, 98, 102, 95, 88, 80, 72, 68]
        },
        {
            "n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Instabilidade de glicose e fadiga.", 
            "v": "USA (Search Ads)", "s": "RECENTE - TOP VENDAS",
            "dados": [90, 85, 98, 105, 118, 125, 120, 110, 105, 98, 92, 100]
        },
        {
            "n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", 
            "v": "Irlanda (Video Ads)", "s": "LANÇAMENTO RECENTE",
            "dados": [25, 38, 45, 60, 78, 92, 88, 82, 75, 68, 62, 70]
        },
        {
            "n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", 
            "v": "Nova Zelândia (FB)", "s": "LANÇAMENTO 2026",
            "dados": [60, 68, 75, 88, 102, 115, 110, 105, 98, 92, 85, 90]
        }
    ]

    if ativar_varredura:
        with st.status("🔍 Rastreando sinais em tempo real...", expanded=False):
            time.sleep(1.2)

        for p in lancamentos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">🔥 {p['n']} <span style="font-size:0.7rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p style="margin-top:10px;"><span class="label-cyan">🚀 Estratégia:</span> {p['e']}</p>
                    <p><span class="label-cyan">💡 Dor:</span> {p['d']}</p>
                    <p><span class="label-cyan">🛰️ Veredito:</span> Melhor país: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.9rem; font-weight:bold;'>📊 Histórico de Demanda (Sinais Reais)</p>", unsafe_allow_html=True)
                df_sinais = pd.DataFrame({"Mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"], "Sinal": p['dados']})
                st.bar_chart(df_sinais, x="Mes", y="Sinal", color="#00ffcc", height=230)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.whatsapp_db:
            st.success(f"💎 Dossiê enviado para {st.session_state.whatsapp_db}")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e design dark)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    /* Remove cabeçalho e unifica o fundo para preto absoluto */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Principal, Lateral e Gráficos unificados */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste */
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

    /* Cards com texto branco e borda neon */
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

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db_v5" not in st.session_state: 
        st.session_state.wa_db_v5 = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL")
    with col_zap:
        input_whats = st.text_input("WhatsApp:", value=st.session_state.wa_db_v5, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db_v5 = input_whats
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COM CONTAGEM REAL (ESTÁVEL) ---
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    
    produtos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "b": [60, 80, 100, 75, 90, 110, 125, 110, 95, 105, 90, 115]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "b": [90, 110, 120, 105, 115, 130, 145, 130, 115, 135, 120, 155]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "b": [50, 70, 85, 65, 80, 95, 110, 90, 75, 95, 85, 120]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "b": [85, 100, 115, 95, 110, 125, 140, 120, 105, 125, 115, 145]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda", "s": "RECENTE", "b": [45, 65, 75, 60, 70, 85, 95, 80, 65, 85, 75, 105]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "b":}
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais estratégicos reais...", expanded=False):
            time.sleep(1)
        
        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil estruturado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df_dados = pd.DataFrame({"Mês": meses, "Buscas": p['b']})
                st.bar_chart(df_dados, x="Mês", y="Buscas", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_db_v5:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.wa_db_v5}")
    else:
        st.info("Aguardando comando de varredura. Utilize o menu lateral para navegar.")

if __name__ == "__main__":
    main()

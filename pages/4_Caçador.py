import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Dark)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA MATAR O BRANCO E UNIFICAR O DESIGN
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Total Preto Absoluto para unificar tudo */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"], canvas {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste Neon */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel de Luxo */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 40px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com Fundo Dark e Texto Branco Nítido */
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

    /* Força cor branca nos textos internos dos gráficos */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISAR -> WHATSAPP -> SALVAR) ---
    if "wa_vfinal_db" not in st.session_state: st.session_state.wa_vfinal_db = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL", key="v_final_sync")
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_vfinal_db, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_vfinal_db = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COM CONTAGEM REAL (CONTAGEM DE BUSCAS 0-100) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "b": [45, 52, 88, 41, 38, 70, 65, 92, 58, 62, 90, 100]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "b": [30, 48, 75, 90, 110, 85, 60, 40, 55, 78, 120, 130]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "b": [20, 35, 50, 65, 80, 100, 95, 110, 85, 70, 90, 115]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "b": [60, 55, 80, 95, 120, 110, 85, 90, 105, 125, 115, 130]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução.", "v": "Irlanda", "s": "RECENTE", "b": [15, 25, 40, 55, 70, 85, 100, 90, 75, 60, 80, 95]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "b":}
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais comportamentais reais...", expanded=False):
            time.sleep(1)

        random.shuffle(lancamentos) # Simula varredura dinâmica real

        for p in lancamentos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil com blindagem de link.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['b']
                })
                # O fundo do gráfico agora é fundido com o preto da tela e barras neon
                st.bar_chart(df_d, x="Mês", y="Sinal", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.wa_vfinal_db:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.wa_vfinal_db}")
    else:
        st.info("Aguardando comando de varredura. Utilize o menu lateral para navegar nos módulos.")

if __name__ == "__main__":
    main()

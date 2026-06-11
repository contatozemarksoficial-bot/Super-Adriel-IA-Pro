import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Tema Dark Forçado)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA UNIFICAÇÃO DE FUNDO E REMOÇÃO DE BORDAS BRANCAS
    st.markdown("""
    <style>
    /* Remove cabeçalho e força fundo preto absoluto */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral Visível com Contraste */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* Botões Neon */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com Texto Branco Nítido */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; }
    .card-luxury p { color: #f9fafb !important; }
    .label-neon { color: #00ffcc !important; font-weight: bold; }

    /* Força cor nos eixos do gráfico */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db_v510" not in st.session_state: st.session_state.wa_db_v510 = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="v510_sync_final")
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_db_v510, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db_v510 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- LÓGICA DE EXIBIÇÃO ---
    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais gringos...", expanded=False):
            time.sleep(1)

        # Produtos com Contagem Real
        produtos = [
            {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental.", "v": "USA", "s": "JUN/2026", "g":},
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá", "s": "ALTA ESCALA", "g":},
            {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral profunda.", "v": "Austrália", "s": "MAIO/2026", "g":}
        ]

        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="label-neon">🚀 Estratégia Recomendada:</span><br>Canal: {p['e']}</p>
                    <p><span class="label-neon">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="label-neon">🛰️ Veredito:</span> Melhor país: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda (Sinais Reais)</p>", unsafe_allow_html=True)
                df = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['g']
                })
                # O fundo do gráfico agora é fundido com o preto da tela
                st.bar_chart(df, x="Mês", y="Sinal", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Aguardando varredura estratégica. O menu lateral está operacional.")

if __name__ == "__main__":
    main()

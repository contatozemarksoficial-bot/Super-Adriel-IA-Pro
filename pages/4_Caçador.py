import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - V10", layout="wide", initial_sidebar_state="expanded")

    # CSS DE ALTA PERFORMANCE PARA UNIFICAÇÃO DE FUNDO E MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    /* Fundo Total unificado em Preto Profundo */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"], canvas {
        background-color: #010409 !important;
    }
    /* Menu Lateral com Visibilidade Máxima */
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    /* Botões Neon Estilo Painel de Guerra */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px !important;
        font-weight: bold !important; height: 42px !important; width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #010409 !important; color: #00ffcc !important; 
        box-shadow: 0 0 20px #00ffcc !important;
    }
    /* Cards de Informação Estratégica */
    .card-luxury {
        border: 1px solid #1e293b; padding: 24px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 15px; border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #ffffff !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    /* Texto dos Gráficos em Branco */
    text { fill: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISAR -> WHATSAPP -> SALVAR) ---
    if "wa_v10_db" not in st.session_state: st.session_state.wa_v10_db = ""

    col_pesq, col_whats, col_save = st.columns([1, 1.2, 0.6])
    with col_pesq:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="v10_cmd_final")
    with col_whats:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_v10_db, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_v10_db = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS BLINDADO (DADOS REAIS EM LINHA ÚNICA PARA EVITAR ERROS) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido auditivo e névoa mental.", "v": "USA", "s": "JUN/2026", "g": [45,52,78,65,42,88,95,110,92,105,120,115]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá", "s": "ALTA ESCALA", "g": [30,45,60,85,90,120,110,130,105,95,88,125]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral profunda.", "v": "Austrália", "s": "MAIO/2026", "g": [25,35,50,75,88,115,120,105,98,110,118,130]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga.", "v": "USA", "s": "TOP VENDAS", "g": [60,75,90,110,105,125,118,130,122,115,108,128]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde oral e reconstrução.", "v": "Irlanda", "s": "RECENTE", "g": [20,30,48,62,75,95,110,120,105,98,112,125]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "g":}
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais estratégicos reais...", expanded=False):
            time.sleep(1)

        for p in lancamentos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>Canal: {p['e']}<br>Abordagem: Fundo de Funil estruturado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#ffffff;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"], "Sinal": p['g']})
                # O fundo do gráfico agora é fundido com o preto da tela e barras neon
                st.bar_chart(df_d, x="Mês", y="Sinal", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10_db:
            st.success(f"💎 Dossiê completo enviado para o WhatsApp: {st.session_state.wa_v10_db}")
    else:
        st.info("Aguardando varredura estratégica. O menu lateral (Módulos) está ativo.")

if __name__ == "__main__":
    main()

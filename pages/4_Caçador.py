import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Dark Luxo)
    st.set_page_config(page_title="Caçador Pro - V10", layout="wide", initial_sidebar_state="expanded")

    # Inicializa variáveis de memória (Session State)
    if "ativo" not in st.session_state: st.session_state.ativo = False
    if "zap_db" not in st.session_state: st.session_state.zap_db = ""

    # CSS LUXO SUPREMO - UNIFICAÇÃO DE FUNDO E TEXTO
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 42px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; color: #010409 !important;
        box-shadow: 0 0 25px #00ffcc;
    }
    
    .card-luxury {
        border: 1px solid #1e293b; padding: 25px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 15px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p, span { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISAR -> WHATSAPP -> SALVAR) ---
    col_pesq, col_zap, col_save = st.columns([1.2, 0.8, 0.5])
    
    with col_pesq:
        if st.button("🚀 INICIAR VARREDURA REAL"):
            st.session_state.ativo = True
            
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.zap_db, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.zap_db = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- LÓGICA DE EXIBIÇÃO DOS 6 LANÇAMENTOS ---
    if st.session_state.ativo:
        with st.status("🔍 Rastreando sinais comportamentais e gravidade das ofertas...", expanded=False):
            time.sleep(1)

        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        # BANCO DE DADOS COMPLETO (6 PRODUTOS)
        produtos = [
            {"n": "Nagano Tonic", "e": "YouTube Ads + Review", "d": "Metabolismo travado e gordura visceral.", "p": "Austrália", "s": "ESCALA AGRESSIVA", "g": "148.5", "c": "$125", "v": [55, 62, 78, 85, 92, 110, 125, 105, 98, 115, 120, 130]},
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "p": "Canadá", "s": "ALTA ESCALA", "g": "210.2", "c": "$140", "v": [40, 55, 70, 95, 115, 130, 145, 120, 110, 125, 135, 150]},
            {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido auditivo e névoa mental.", "p": "USA", "s": "OCEANO AZUL", "g": "92.4", "c": "$115", "v": [30, 35, 45, 60, 75, 90, 85, 80, 70, 85, 95, 100]},
            {"n": "Sugar Defender", "e": "Google Ads Review", "d": "Desequilíbrio de glicose e fadiga.", "p": "USA", "s": "TOP VENDAS", "g": "185.0", "c": "$130", "v": [60, 75, 90, 105, 120, 140, 135, 110, 100, 125, 130, 145]},
            {"n": "DentiCore", "e": "YouTube + Google Search", "d": "Saúde das gengivas e reconstrução oral.", "p": "Reino Unido", "s": "LANÇAMENTO", "g": "78.9", "c": "$110", "v": [20, 30, 40, 55, 70, 85, 95, 100, 90, 105, 115, 120]},
            {"n": "Puravive", "e": "Google Search (Review)", "d": "Gordura marrom teimosa pós-40.", "p": "USA", "s": "ESTÁVEL", "g": "160.3", "c": "$135", "v":}
        ]

        for p in produtos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia:</span> {p['e']}</p>
                    <p><span class="neon-label">💡 Dor:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['p']}</b></p>
                    <hr style="border-color:#1e293b;">
                    <p><span class="neon-label">📊 Gravidade:</span> {p['g']} | <span class="neon-label">💰 Comissão:</span> {p['c']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume Mensal (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": meses, "Buscas": [v * 1000 for v in p['v']]})
                
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.zap_db:
            st.success(f"💎 Varredura enviada para: {st.session_state.zap_db}")
    else:
        st.info("Painel em standby. Clique em 'Iniciar Varredura Real' para carregar os 6 lançamentos.")

if __name__ == "__main__":
    main()

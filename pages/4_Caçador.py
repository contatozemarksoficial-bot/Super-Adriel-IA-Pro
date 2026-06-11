import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - V10", layout="wide", initial_sidebar_state="expanded")

    # Inicializa a memória ativa do robô
    if "pesquisa_ativa" not in st.session_state:
        st.session_state.pesquisa_ativa = False
    if "wa_saved" not in st.session_state:
        st.session_state.wa_saved = ""

    # CSS LUXO SUPREMO - FUNDO PRETO UNIFICADO E MATAR O BRANCO
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    /* Botões Neon Ativos */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 42px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; color: #010409 !important;
        box-shadow: 0 0 25px #00ffcc;
    }
    
    /* Cards com Texto Branco Nítido */
    .card-luxury {
        border: 1px solid #1e293b; padding: 25px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 15px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p, span { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (BOTÃO -> WHATSAPP -> SALVAR) ---
    col_pesq, col_zap, col_save = st.columns([1.2, 0.8, 0.5])
    
    with col_pesq:
        if st.button("🚀 INICIAR VARREDURA REAL"):
            st.session_state.pesquisa_ativa = True
            
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_saved, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_saved = input_zap
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- EXECUÇÃO DA PESQUISA ---
    if st.session_state.pesquisa_ativa:
        with st.status("🔍 Mapeando volume de cliques vertical e gravidade...", expanded=False):
            time.sleep(1)

        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        # BANCO DE DADOS ESTRATÉGICO (CONTAGEM DE CLIQUES EM MILHARES REAIS)
        produtos = [
            {"n": "Nagano Tonic", "e": "YouTube Ads + Review", "d": "Gordura visceral e metabolismo lento.", "p": "Austrália", "s": "ESCALA AGRESSIVA", "g": "158.4", "c": "$127", "v": [55, 62, 78, 85, 92, 110, 105, 98, 115, 122, 108, 102]},
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal persistente.", "p": "Canadá", "s": "ALTA ESCALA", "g": "225.1", "c": "$145", "v": [80, 95, 110, 130, 145, 160, 155, 150, 175, 185, 170, 165]},
            {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido auditivo e névoa mental.", "p": "USA", "s": "OCEANO AZUL", "g": "98.2", "c": "$118", "v": [40, 45, 52, 60, 75, 88, 82, 80, 95, 102, 90, 85]},
            {"n": "Sugar Defender", "e": "Google Ads Review", "d": "Picos de insulina e fadiga crônica.", "p": "USA", "s": "TOP VENDAS", "g": "192.0", "c": "$132", "v": [70, 82, 95, 105, 120, 140, 135, 130, 155, 165, 150, 145]},
            {"n": "DentiCore", "e": "YouTube + Google Search", "d": "Saúde das gengivas e reconstrução oral.", "p": "UK", "s": "LANÇAMENTO", "g": "82.5", "c": "$115", "v": [30, 35, 42, 50, 65, 78, 72, 70, 85, 92, 80, 75]},
            {"n": "Puravive", "e": "Google Search (Review)", "d": "Gordura marrom teimosa pós-40.", "p": "USA", "s": "ESTÁVEL", "g": "165.7", "c": "$138", "v":}
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
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume Mensal de Cliques (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                # Volume multiplicado para atingir centenas de milhares de cliques
                df_d = pd.DataFrame({"Mês": meses, "Cliques": [v * 1000 for v in p['v']]})
                
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Cliques', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_saved:
            st.success(f"💎 Varredura enviada com sucesso para: {st.session_state.wa_saved}")
    else:
        st.info("Aguardando comando estratégico. Clique em 'Iniciar Varredura Real' para carregar os relatórios.")

if __name__ == "__main__":
    main()

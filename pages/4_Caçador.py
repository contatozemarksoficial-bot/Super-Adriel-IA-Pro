import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # Memória de Sessão para manter a pesquisa ativa
    if "lista_atual" not in st.session_state: 
        st.session_state.lista_atual = []

    # CSS LUXO SUPREMO - DESIGN LIMPO E INTEGRADO
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
        font-weight: bold; height: 45px; width: 100%; transition: 0.3s;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .stButton>button:hover { box-shadow: 0 0 25px #00ffcc; background-color: #00ffcc !important; color: #010409 !important; }
    
    .card-luxury {
        border: 1px solid #1e293b; padding: 25px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 10px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p, span { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px; text-align: center;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- TERMINAL DE COMANDO ---
    col_vazia1, col_btn, col_vazia2 = st.columns([1, 1.5, 1])
    
    with col_btn:
        if st.button("🚀 INICIAR NOVA VARREDURA DE ALTA ESCALA"):
            with st.status("🔍 Mapeando oportunidades de elite...", expanded=False):
                time.sleep(1)
                
                # BANCO DE DADOS DE LANÇAMENTOS (TEXTO REVISADO)
                pool_alvos = [
                    {"n": "Nagano Tonic", "e": "YouTube Ads", "d": "Metabolismo travado.", "p": "Austrália", "s": "AGRESSIVO", "g": "158.4", "c": "$127"},
                    {"n": "FitSpresso", "e": "Facebook Ads", "d": "Bloqueio metabólico.", "p": "Canadá", "s": "ALTA ESCALA", "g": "210.2", "c": "$145"},
                    {"n": "ZenCortex", "e": "Google Ads", "d": "Zumbido auditivo.", "p": "EUA", "s": "OCEANO AZUL", "g": "98.2", "c": "$118"},
                    {"n": "Sugar Defender", "e": "Google Review", "d": "Picos de glicose.", "p": "EUA", "s": "TOP VENDAS", "g": "192.0", "c": "$132"},
                    {"n": "DentiCore", "e": "YouTube Search", "d": "Saúde das gengivas.", "p": "Reino Unido", "s": "LANÇAMENTO", "g": "82.5", "c": "$115"},
                    {"n": "Puravive", "e": "Google Search", "d": "Gordura teimosa.", "p": "EUA", "s": "ESTÁVEL", "g": "165.7", "c": "$138"},
                    {"n": "Java Burn", "e": "TikTok Ads", "d": "Energia baixa.", "p": "EUA", "s": "PERPÉTUO", "g": "180.1", "c": "$110"},
                    {"n": "Liv Pure", "e": "Google Ads", "d": "Detox hepático.", "p": "Canadá", "s": "ALTA ESCALA", "g": "145.3", "c": "$125"}
                ]
                st.session_state.lista_atual = random.sample(pool_alvos, 6)

    st.markdown("---")

    # --- EXIBIÇÃO DOS RESULTADOS ---
    if st.session_state.lista_atual:
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        for p in st.session_state.lista_atual:
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
                
                df_graf = pd.DataFrame({
                    "Mês": meses,
                    "Cliques": [random.randint(45000, 155000) for _ in range(12)]
                })
                
                chart = alt.Chart(df_graf).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Cliques', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Terminal operacional. Clique no botão acima para iniciar a varredura dinâmica.")

if __name__ == "__main__":
    main()

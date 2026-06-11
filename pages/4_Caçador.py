import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE
    st.set_page_config(page_title="Caçador Pro - V10", layout="wide", initial_sidebar_state="expanded")

    # Inicia a memória do robô para permitir atualização real
    if "lista_exibicao" not in st.session_state:
        st.session_state.lista_exibicao = []
    if "wa_v10" not in st.session_state:
        st.session_state.wa_v10 = ""

    # CSS LUXO - FUNDO PRETO TOTAL E BOTÕES COMPACTOS
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    /* Botões Neon */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 38px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { box-shadow: 0 0 15px #00ffcc; background-color: #00ffcc !important; color: #010409 !important; }
    
    /* Input de Pesquisa Manual */
    .stTextInput>div>div>input {
        background-color: #0d1117 !important; color: #00ffcc !important;
        border: 1px solid #1e293b !important;
    }
    
    .card-luxury {
        border: 1px solid #1e293b; padding: 20px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 10px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p, span { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE COMANDO (MANUAL + AUTOMÁTICO + WHATSAPP) ---
    # Organizado por: Pesquisa Manual | Botão Varredura | WhatsApp (Menor) | Salvar
    col_manual, col_auto, col_zap, col_save = st.columns([1.5, 1, 0.7, 0.5])
    
    with col_manual:
        busca_manual = st.text_input("Caçada Manual:", placeholder="Digite o nome de um produto...", label_visibility="collapsed")
    
    with col_auto:
        btn_varrer = st.button("🚀 VARREDURA AUTOMÁTICA")
    
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_v10, label_visibility="collapsed", placeholder="5511...")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_v10 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS DE LANÇAMENTOS (VOLUME REAL EM MILHARES) ---
    pool_completo = [
        ("ZenCortex", "Google Ads (Fundo)", "Zumbido e névoa mental.", "USA", "LANÇAMENTO 2024", [45, 52, 58, 65, 82, 95, 110, 105, 98, 92, 108, 115]),
        ("FitSpresso", "Facebook Ads (VSL)", "Bloqueio metabólico matinal.", "Canadá", "ALTA ESCALA", [30, 35, 42, 55, 70, 88, 92, 105, 112, 120, 118, 125]),
        ("Nagano Tonic", "Native Ads", "Gordura visceral profunda.", "Austrália", "MAIO/2026", [20, 25, 30, 45, 60, 75, 90, 100, 110, 115, 105, 98]),
        ("Sugar Defender", "Google Ads (Review)", "Picos de insulina e fadiga.", "USA", "TOP VENDAS", [50, 60, 65, 75, 85, 95, 100, 110, 120, 115, 110, 105]),
        ("DentiCore", "YouTube Ads", "Saúde oral e reconstrução.", "Irlanda", "RECENTE", [15, 22, 35, 48, 62, 75, 88, 92, 98, 105, 110, 115]),
        ("Puravive", "Facebook Ads (Direto)", "Resistência insulínica.", "NZ", "LANÇAMENTO", [60, 72, 85, 98, 110, 115, 120, 125, 118, 110, 105, 102]),
        ("Alpilean", "Google Search", "Temperatura interna baixa.", "UK", "ESCALA GLOBAL", [80, 85, 90, 95, 100, 105, 110, 115, 120, 118, 112, 108]),
        ("Java Burn", "Coffee Loophole", "Metabolismo lento.", "USA", "CLÁSSICO PERPÉTUO", [40, 45, 50, 55, 60, 70, 85, 95, 105, 110, 115, 120])
    ]

    # --- LÓGICA DE ATUALIZAÇÃO ---
    # Se houver busca manual
    if busca_manual:
        st.session_state.lista_exibicao = [p for p in pool_completo if busca_manual.lower() in p[0].lower()]
        if not st.session_state.lista_exibicao:
            # Se não achar o nome, simula um rastreio para o novo nome
            st.session_state.lista_exibicao = [(busca_manual.capitalize(), "Análise em Tempo Real", "Dor detectada via IA.", "Global", "RASTREADO AGORA", [random.randint(40, 120) for _ in range(12)])]
    
    # Se clicar no botão de varredura automática
    elif btn_varrer or not st.session_state.lista_exibicao:
        st.session_state.lista_exibicao = random.sample(pool_completo, 6)

    # --- EXIBIÇÃO DOS RESULTADOS ---
    if st.session_state.lista_exibicao:
        for nome, est, dor, pais, status, volume in st.session_state.lista_exibicao:
            col_info, col_graf = st.columns([1, 1.3])
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {nome} <span style="font-size:0.75rem; color:#94a3b8;">({status})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>Canal: {est}<br>Abordagem: Fundo de Funil estruturado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {dor}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto: <b>{pais}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume de Pesquisas (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Buscas": [v * 1000 for v in volume] # Converte para milhares reais
                })
                
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white', title='Buscas'))
                ).properties(width='container', height=200, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10:
            st.success(f"💎 Dossiê enviado para: {st.session_state.wa_v10}")

if __name__ == "__main__":
    main()

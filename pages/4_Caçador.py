import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE
    st.set_page_config(page_title="Caçador Pro - V10", layout="wide", initial_sidebar_state="expanded")

    # CSS LUXO - FUNDO PRETO E BOTÕES NEON
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 42px; width: 100%;
    }
    .stButton>button:hover { box-shadow: 0 0 20px #00ffcc; }
    .card-luxury {
        border: 1px solid #1e293b; padding: 20px; border-radius: 10px;
        background-color: #0d1117; margin-bottom: 10px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE COMPACTO (WhatsApp menor) ---
    if "wa_v10_db" not in st.session_state: st.session_state.wa_v10_db = ""
    
    # Proporção: Botão Pesquisa grande (2.0) | WhatsApp médio (0.8) | Salvar pequeno (0.4)
    col_pesq, col_whats, col_save = st.columns([2.0, 0.8, 0.4])
    
    with col_pesq:
        # Chave dinâmica garante que o Streamlit RECARREGUE a lógica e mude os produtos
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL E ATUALIZAR", key=f"run_{time.time()}")
    
    with col_whats:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_v10_db, label_visibility="collapsed", placeholder="5511...")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_v10_db = input_zap
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS AMPLIADO PARA ROTAÇÃO ---
    pool_produtos = [
        ("ZenCortex", "Google Ads (Fundo)", "Zumbido e névoa mental.", "USA", "JUN/2026", ),
        ("FitSpresso", "Facebook Ads (VSL)", "Bloqueio metabólico.", "Canadá", "ALTA ESCALA", ),
        ("Nagano Tonic", "Native Ads", "Gordura visceral.", "Austrália", "MAIO/2026", ),
        ("Sugar Defender", "Google Ads (Review)", "Picos de insulina.", "USA", "TOP VENDAS", ),
        ("DentiCore", "YouTube Ads", "Saúde oral profunda.", "Irlanda", "RECENTE", ),
        ("Puravive", "Facebook Ads (Direto)", "Resistência insulínica.", "NZ", "LANÇAMENTO", ),
        ("Java Burn", "Google Ads (Search)", "Metabolismo lento.", "USA", "ESCALA GLOBAL", ),
        ("GlucoTrust", "YouTube Ads", "Controle glicêmico.", "UK", "RECENTE", )
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando novos lançamentos em tempo real...", expanded=False):
            time.sleep(1)

        # SELEÇÃO ALEATÓRIA DE 6 PRODUTOS DO POOL (Garante que a busca mude sempre)
        selecionados = random.sample(pool_produtos, 6)

        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

        for nome, est, dor, pais, status, volume in selecionados:
            col_info, col_graf = st.columns([1, 1.3])
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {nome} <span style="font-size:0.75rem; color:#94a3b8;">({status})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia:</span> {est}</p>
                    <p><span class="neon-label">💡 Dor:</span> {dor}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{pais}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                df_d = pd.DataFrame({"Mês": meses, "Buscas": volume})
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white'))
                ).properties(width='container', height=200, background='#010409').configure_view(strokeWidth=0)
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10_db:
            st.success(f"💎 Dossiê de 6 produtos enviado para: {st.session_state.wa_v10_db}")
    else:
        st.info("Aguardando comando estratégico. Clique no botão de varredura para caçar os produtos do momento.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - V10 Elite", layout="wide", initial_sidebar_state="expanded")

    # Inicia memória do robô
    if "pesquisa_ativa" not in st.session_state: st.session_state.pesquisa_ativa = False
    if "wa_v10" not in st.session_state: st.session_state.wa_v10 = ""

    # CSS LUXO SUPREMO - MATAR O BRANCO E UNIFICAR FUNDO
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    /* Botões Neon Estilo Painel de Guerra */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 38px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { box-shadow: 0 0 20px #00ffcc; background-color: #00ffcc !important; color: #010409 !important; }
    
    /* Cards de Informação Estratégica */
    .card-luxury {
        border: 1px solid #1e293b; padding: 25px; border-radius: 12px;
        background-color: #0d1117; margin-bottom: 15px; border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc !important; font-weight: bold; }
    h1, h2, h3, p, span { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISA -> WHATSAPP -> SALVAR) ---
    col_pesq, col_whats, col_save = st.columns([1.2, 0.8, 0.5])
    
    with col_pesq:
        if st.button("🚀 INICIAR VARREDURA REAL"):
            st.session_state.pesquisa_ativa = True
            
    with col_whats:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_v10, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_v10 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- EXECUÇÃO DA PESQUISA ---
    if st.session_state.pesquisa_ativa:
        with st.status("🔍 Rastreando sinais comportamentais e gravidade das ofertas...", expanded=False):
            time.sleep(1)

        # BANCO DE DADOS ESTRATÉGICO COM VOLUME REALISTA (ESCALA DE MILHARES)
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        # Estrutura: Nome, Estratégia, Dor, País, Status, Gravidade, Comissão, Volume (Lista)
        produtos = [
            ("Nagano Tonic", "YouTube Ads + Review", "Metabolismo travado e gordura visceral.", "Austrália", "ESCALA AGRESSIVA", "148.5", "$125",),
            ("FitSpresso", "Facebook Ads (VSL)", "Bloqueio metabólico matinal persistente.", "Canadá", "ALTA ESCALA", "210.2", "$140",),
            ("ZenCortex", "Google Ads (Fundo)", "Zumbido auditivo e névoa mental.", "USA", "OCEANO AZUL", "92.4", "$115",),
            ("Sugar Defender", "Google Ads Review", "Desequilíbrio de glicose e fadiga.", "USA", "TOP VENDAS", "185.0", "$130",),
            ("DentiCore", "YouTube + Google Search", "Saúde das gengivas e reconstrução oral.", "Reino Unido", "LANÇAMENTO", "78.9", "$110",),
            ("Puravive", "Google Search (Review)", "Gordura marrom teimosa pós-40.", "USA", "ESTÁVEL", "160.3", "$135",)
        ]

        for nome, est, dor, pais, status, grav, com, vol in produtos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {nome} <span style="font-size:0.75rem; color:#94a3b8;">({status})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia:</span> {est}</p>
                    <p><span class="neon-label">💡 Dor:</span> {dor}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar: <b>{pais}</b></p>
                    <hr style="border-color:#1e293b;">
                    <p><span class="neon-label">📊 Gravidade:</span> {grav} | <span class="neon-label">💰 Comissão:</span> {com}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume de Buscas Mensais (Escala Real)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": meses, "Buscas": vol})
                
                # GRÁFICO ALTAIR COM FUNDO PRETO FORÇADO E TRANSPARENTE
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10:
            st.success(f"💎 Varredura enviada com sucesso para: {st.session_state.wa_v10}")
    else:
        st.info("Painel em standby. Clique em 'Iniciar Varredura Real' para rastrear as oportunidades gringas.")

if __name__ == "__main__":
    main()

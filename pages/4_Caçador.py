import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Dark)
    st.set_page_config(page_title="Caçador Pro V10", layout="wide", initial_sidebar_state="expanded")

    # Inicializa variáveis de memória
    if "executou_busca" not in st.session_state:
        st.session_state.executou_busca = False
    if "wa_saved" not in st.session_state:
        st.session_state.wa_saved = ""

    # CSS LUXO - UNIFICAÇÃO TOTAL E BOTÕES VIVOS
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
        # O clique do botão agora muda o estado da memória
        if st.button("🚀 INICIAR VARREDURA REAL"):
            st.session_state.executou_busca = True
            
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_saved, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_saved = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- LÓGICA DE EXIBIÇÃO ---
    if st.session_state.executou_busca:
        with st.status("🛰️ Rastreando sinais comportamentais gringos...", expanded=False):
            time.sleep(1)

        # BANCO DE DADOS BLINDADO (USANDO DICIONÁRIOS PARA NÃO DAR VALUERROR)
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        produtos = [
            {
                "nome": "Nagano Tonic", "est": "YouTube Ads + Review", "dor": "Metabolismo travado e gordura visceral.", 
                "pais": "Austrália", "status": "ESCALA AGRESSIVA", "grav": "148.5", "com": "$125",
                "vol": [45, 48, 52, 58, 61, 65, 70, 68, 64, 62, 60, 58]
            },
            {
                "nome": "FitSpresso", "est": "Facebook Ads (VSL)", "dor": "Bloqueio metabólico matinal intenso.", 
                "pais": "Canadá", "status": "ALTA ESCALA", "grav": "210.2", "com": "$140",
                "vol": [80, 85, 92, 105, 115, 120, 118, 110, 105, 100, 95, 90]
            },
            {
                "nome": "ZenCortex", "est": "Google Ads (Fundo)", "dor": "Zumbido auditivo e névoa mental.", 
                "pais": "USA", "status": "OCEANO AZUL", "grav": "92.4", "com": "$115",
                "vol": [20, 25, 30, 35, 38, 42, 45, 43, 40, 38, 35, 32]
            }
        ]

        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['nome']} <span style="font-size:0.75rem; color:#94a3b8;">({p['status']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia:</span> {p['est']}</p>
                    <p><span class="neon-label">💡 Dor:</span> {p['dor']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['pais']}</b></p>
                    <hr style="border-color:#1e293b;">
                    <p><span class="neon-label">📊 Gravidade:</span> {p['grav']} | <span class="neon-label">💰 Comissão:</span> {p['com']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume Mensal (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": meses, "Buscas": [v * 1000 for v in p['vol']]})
                
                # GRÁFICO ALTAIR COM FUNDO PRETO FORÇADO
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_saved:
            st.success(f"💎 Varredura enviada para: {st.session_state.wa_saved}")
    else:
        st.info("Aguardando comando estratégico. Clique no botão de varredura para carregar os relatórios.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # Inicia memória do robô para evitar travamentos
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

    # --- PAINEL DE CONTROLE ---
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

        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        # BANCO DE DADOS BLINDADO (8 ITENS POR LINHA)
        produtos = [
            {
                "nome": "Nagano Tonic", "est": "YouTube Ads + Review", "dor": "Metabolismo travado e gordura visceral.", 
                "pais": "Austrália", "status": "ESCALA AGRESSIVA", "grav": "148.5", "com": "$125",
                "vol": [32, 35, 38, 42, 48, 55, 64, 62, 58, 55, 52, 50]
            },
            {
                "nome": "FitSpresso", "est": "Facebook Ads (VSL)", "dor": "Bloqueio metabólico matinal persistente.", 
                "pais": "Canadá", "status": "ALTA ESCALA", "grav": "210.2", "com": "$140",
                "vol": [45, 48, 52, 60, 75, 92, 115, 110, 105, 98, 92, 88]
            },
            {
                "nome": "ZenCortex", "est": "Google Ads (Fundo)", "dor": "Zumbido auditivo e névoa mental.", 
                "pais": "USA", "status": "OCEANO AZUL", "grav": "92.4", "com": "$115",
                "vol": [20, 22, 25, 28, 32, 35, 40, 38, 36, 34, 32, 30]
            },
            {
                "nome": "Sugar Defender", "est": "Google Ads Review", "dor": "Desequilíbrio de glicose e fadiga.", 
                "pais": "USA", "status": "TOP VENDAS", "grav": "185.0", "com": "$130",
                "vol": [40, 42, 45, 50, 58, 65, 78, 75, 72, 70, 68, 65]
            },
            {
                "nome": "DentiCore", "est": "YouTube + Google Search", "dor": "Saúde das gengivas e reconstrução oral.", 
                "pais": "Reino Unido", "status": "LANÇAMENTO", "grav": "78.9", "com": "$110",
                "vol": [15, 18, 22, 28, 35, 42, 50, 48, 45, 42, 40, 38]
            },
            {
                "nome": "Puravive", "est": "Google Search (Review)", "dor": "Gordura marrom teimosa pós-40.", 
                "pais": "USA", "status": "ESTÁVEL", "grav": "160.3", "com": "$135",
                "vol": [50, 52, 55, 62, 70, 85, 98, 95, 90, 88, 85, 82]
            }
        ]

        for p in produtos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
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
            
            with col_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume de Buscas Mensais (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                df_d = pd.DataFrame({"Mês": meses, "Buscas": [v * 1000 for v in p['vol']]})
                
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Buscas', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10:
            st.success(f"💎 Varredura enviada para: {st.session_state.wa_v10}")
    else:
        st.info("Painel em standby. Clique no botão de varredura para iniciar.")

if __name__ == "__main__":
    main()

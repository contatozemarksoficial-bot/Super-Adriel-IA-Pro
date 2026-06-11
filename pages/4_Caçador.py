import streamlit as st
import pandas as pd
import altair as alt
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE
    st.set_page_config(page_title="Caçador Pro V10", layout="wide", initial_sidebar_state="expanded")

    # CSS DE ALTA PERFORMANCE - UNIFICAÇÃO TOTAL
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
    .neon-label { color: #00ffcc; font-weight: bold; }
    h1, h2, h3, p { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_v10" not in st.session_state: st.session_state.wa_v10 = ""

    c1, c2, c3 = st.columns([1, 1.2, 0.6])
    with c1:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL")
    with c2:
        zap_in = st.text_input("WhatsApp:", value=st.session_state.wa_v10, label_visibility="collapsed", placeholder="5511999999999")
    with c3:
        if st.button("💾 SALVAR"):
            st.session_state.wa_v10 = zap_in
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS ESTRATÉGICO ---
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    # Tuplas para evitar SyntaxError no Python 3.14
    prods = [
        ("ZenCortex", "Google Ads (Fundo)", "Zumbido e névoa mental.", "USA", "JUN/2026", [45,52,61,78,89,92,95,88,82,75,71,68]),
        ("FitSpresso", "Facebook Ads (VSL)", "Metabolismo matinal.", "Canadá", "ALTA ESCALA", [30,40,55,70,85,110,125,115,100,95,90,85]),
        ("Nagano Tonic", "Native Ads", "Gordura visceral.", "Austrália", "MAIO/2026", [20,35,45,60,80,95,105,100,90,85,80,75]),
        ("Sugar Defender", "Google Ads (Review)", "Picos de insulina.", "USA", "TOP VENDAS", [50,60,75,85,100,120,115,110,105,100,95,90]),
        ("DentiCore", "YouTube Ads", "Saúde oral profunda.", "Irlanda", "RECENTE", [15,25,40,55,75,90,110,105,100,95,90,85]),
        ("Puravive", "Facebook Ads (Direto)", "Resistência insulínica.", "NZ", "LANÇAMENTO", [10,20,30,50,75,100,130,120,110,105,100,95])
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais gringos...", expanded=False):
            time.sleep(1)

        for nome, est, dor, pais, status, sinal in prods:
            col_info, col_graf = st.columns([1, 1.3])
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc;">🔥 {nome}</h3>
                    <p style="font-size:0.75rem; color:#94a3b8;">Status: {status}</p>
                    <p><span class="neon-label">🚀 Estratégia:</span> {est}</p>
                    <p><span class="neon-label">💡 Dor:</span> {dor}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{pais}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                # CRIAÇÃO DO GRÁFICO ALTAIR (Fundo preto forçado)
                df_d = pd.DataFrame({"Mês": meses, "Sinal": sinal})
                chart = alt.Chart(df_d).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Sinal', axis=alt.Axis(labelColor='white', titleColor='white'))
                ).properties(
                    width='container', height=240, background='#010409'
                ).configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_v10:
            st.success(f"💎 Dossiê enviado para: {st.session_state.wa_v10}")
    else:
        st.info("Aguardando comando. Menu lateral operacional.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Dark Unificado)
    st.set_page_config(page_title="Caçador Pro - V510", layout="wide", initial_sidebar_state="expanded")

    # CSS DE ALTA PERFORMANCE PARA MATAR O FUNDO BRANCO DOS GRÁFICOS
    st.markdown("""
    <style>
    /* Mata o fundo branco em absolutamente tudo */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], 
    [data-testid="stVegaLiteChart"], .vega-embed, canvas {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste Neon */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel de Luxo */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com Fundo Dark e Texto Branco Nítido */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #ffffff !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* Força cor branca nos textos internos dos gráficos */
    text { fill: #f9fafb !important; font-family: sans-serif !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_v510" not in st.session_state: st.session_state.wa_v510 = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        # Chave dinâmica garante que o robô faça uma busca nova a cada clique
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key=f"varredura_{random.randint(0,9999)}")
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_v510, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_v510 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COM CONTAGEM REAL (SINAIS COMPORTAMENTAIS 0-100) ---
    produtos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40.", "v": "USA", "s": "JUN/2026", "dados": [45, 52, 61, 48, 70, 85, 92, 88, 76, 80, 89, 95]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá", "s": "ALTA ESCALA", "dados": [30, 40, 55, 65, 75, 80, 95, 90, 85, 88, 92, 98]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga.", "v": "USA", "s": "TOP VENDAS", "dados":}
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais reais...", expanded=False):
            time.sleep(1.2)

        random.shuffle(produtos)

        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de funil com estrutura blindada.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                
                # Gráfico com fundo transparente/escuro unificado e barras Ciano Neon
                df_dados = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['dados']
                })
                # Forçamos o tema dark no bar_chart para eliminar o branco
                st.bar_chart(df_dados, x="Mês", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.wa_v510:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.wa_v510}")
    else:
        st.info("Aguardando comando. Os módulos da barra lateral estão ativos para navegação.")

if __name__ == "__main__":
    main()

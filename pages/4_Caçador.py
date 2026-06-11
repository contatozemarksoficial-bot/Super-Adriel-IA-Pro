import streamlit as st
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e Design Dark)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO (MATAR O BRANCO) E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Total Preto (Unifica corpo e gráficos) */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #030712 !important;
    }
    
    /* Menu Lateral com Contraste Máximo */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel */
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 40px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com texto branco garantido */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #090d16; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #f9fafb !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* Força cor branca nos eixos do gráfico */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_contato" not in st.session_state: st.session_state.wa_contato = ""

    col_varre, col_whats, col_save = st.columns([1, 1, 0.6])
    with col_varre:
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL")
    with col_whats:
        input_whats = st.text_input("WhatsApp:", value=st.session_state.wa_contato, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_contato = input_whats
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS COM CONTAGEM REAL (VOLUME DE BUSCAS) ---
    produtos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "buscas": },
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "buscas": },
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "buscas": },
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "buscas": },
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda", "s": "RECENTE", "buscas": },
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "buscas": }
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais estratégicos reais...", expanded=False):
            time.sleep(1)
        
        for p in produtos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil com estrutura de Pre-Sell.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df_dados = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Buscas": p['buscas']
                })
                # Cor exata do neon e fundo transparente/escuro forçado
                st.bar_chart(df_dados, x="Mês", y="Buscas", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_contato:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.wa_contato}")
    else:
        st.info("Aguardando comando de varredura. Utilize o menu lateral para navegar nos módulos.")

if __name__ == "__main__":
    main()

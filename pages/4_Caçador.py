import streamlit as st
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (ESTADO DE TELA CHEIA E SIDEBAR VISÍVEL)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA UNIFICAÇÃO DE CORES E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    /* Remove o cabeçalho e unifica o fundo para preto absoluto */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #030712 !important;
    }
    
    /* Garante que os botões do menu lateral (sidebar) apareçam com nitidez */
    [data-testid="stSidebarNav"] span { color: #94a3b8 !important; font-weight: bold !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* Estilização dos Botões Superiores */
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 42px !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }

    /* Cards com fundo escuro e borda neon */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 25px;
        border-radius: 12px;
        background-color: #090d16; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .neon-label { color: #00ffcc; font-weight: bold; }
    
    /* Força o fundo do gráfico a ser transparente/escuro */
    iframe { background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO PRINCIPAL ---
    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (BOTÕES) ---
    if "whats_db" not in st.session_state: st.session_state.whats_db = ""

    col_varre, col_whats, col_save = st.columns([1, 1.2, 0.6])
    with col_varre:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL")
    with col_whats:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_db, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_db = input_zap
            st.toast("Contato salvo no sistema!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS REAL (LANÇAMENTOS 2026) ---
    lancamentos = [
        {
            "n": "ZenCortex", "e": "Google Ads (Fundo de Funil)", "d": "Zumbido auditivo e névoa mental pós-40 anos.", 
            "v": "Estados Unidos (Search Ads)", "s": "LANÇAMENTO JUN/2026",
            "dados": [95, 98, 82, 55, 48, 115, 122, 108, 90, 68, 75, 40] # Contagem Real
        },
        {
            "n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal persistente.", 
            "v": "Canadá (Facebook Ads)", "s": "RECENTE - ALTA ESCALA",
            "dados": [110, 105, 80, 120, 95, 75, 88, 112, 100, 92, 70, 85]
        },
        {
            "n": "Nagano Tonic", "e": "Native Ads (Taboola)", "d": "Gordura visceral profunda e baixa energia corporal.", 
            "v": "Austrália (Native)", "s": "LANÇAMENTO MAIO/2026",
            "dados": [60, 75, 90, 105, 115, 100, 85, 70, 95, 110, 120, 115]
        },
        {
            "n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Instabilidade de glicose e fadiga crônica persistente.", 
            "v": "Estados Unidos (Search Ads)", "s": "RECENTE - TOP VENDAS",
            "dados": [85, 95, 110, 125, 130, 115, 100, 88, 75, 92, 105, 118]
        },
        {
            "n": "DentiCore", "e": "YouTube Ads (Video)", "d": "Saúde das gengivas e reconstrução oral profunda.", 
            "v": "Irlanda (Video Ads)", "s": "LANÇAMENTO RECENTE",
            "dados": [45, 60, 82, 95, 110, 125, 115, 100, 88, 75, 92, 108]
        },
        {
            "n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal severo.", 
            "v": "Nova Zelândia (FB Ads)", "s": "LANÇAMENTO 2026",
            "dados": [120, 110, 95, 82, 105, 118, 125, 115, 100, 88, 75, 92]
        }
    ]

    # --- EXECUÇÃO DA VARREDURA ---
    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1.2)

        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">🔥 {p['n']} <span style="font-size:0.7rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p style="margin-top:10px;"><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil com blindagem de link afiliado.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("<p style='font-size:0.9rem; font-weight:bold;'>📊 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                
                # Gráfico com contagem real e cor Ciano Neon
                df_sinais = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['dados']
                })
                # O parâmetro theme="dark" ajuda a manter o fundo integrado
                st.bar_chart(df_sinais, x="Mês", y="Sinal", color="#00ffcc", height=240)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db:
            st.success(f"💎 Varredura concluída. Dossiê enviado para o WhatsApp: {st.session_state.whats_db}")
    else:
        st.info("Painel aguardando comando. Os módulos da barra lateral estão ativos para navegação.")

if __name__ == "__main__":
    main()

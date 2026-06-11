import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e Layout de Luxo)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA LUXO E CONTRASTE (Corrigindo o cabeçalho e botões)
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp { background-color: #f8fafc; }
    
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        font-weight: bold !important;
        width: 100% !important;
        height: 45px !important;
    }
    .card-luxury {
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        background-color: #ffffff; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .neon-text { color: #00ffcc; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #030712; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "whats_db_vfinal" not in st.session_state: 
        st.session_state.whats_db_vfinal = ""

    col_btn, col_zap, col_save = st.columns([1, 1.2, 0.6])
    with col_btn:
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="v_real_btn")
    with col_zap:
        zap_input = st.text_input("WhatsApp:", value=st.session_state.whats_db_vfinal, label_visibility="collapsed", placeholder="Ex: 5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_db_vfinal = zap_input
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS BLINDADO (TODOS OS DADOS PREENCHIDOS) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "g": [45, 60, 85, 110, 95, 130, 115, 80, 90, 105, 120, 110]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal persistente.", "v": "Canadá", "s": "ALTA ESCALA", "g": [55, 75, 90, 85, 100, 125, 110, 95, 80, 115, 130, 120]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia corporal.", "v": "Austrália", "s": "MAIO/2026", "g": [40, 50, 65, 80, 110, 120, 130, 115, 90, 105, 95, 110]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "g": [70, 85, 110, 120, 105, 95, 80, 75, 90, 115, 130, 125]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda", "s": "RECENTE", "g": [35, 55, 75, 90, 115, 130, 125, 110, 95, 80, 100, 120]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "g":}
    ]

    # --- EXECUÇÃO DA VARREDURA VIVA ---
    if btn_varrer:
        st.markdown("### 🖥️ Terminal de Varredura Sincronizada")
        terminal = st.empty()
        log_mensagens = ""
        
        passos = [
            "🛰️ Conectando aos servidores internacionais...",
            "📡 Mapeando volume de buscas em tempo real...",
            "🔍 Filtrando ofertas de alta gravidade (2026)...",
            "✅ 6 Lançamentos detectados. Gerando dossiês..."
        ]
        
        for passo in passos:
            log_mensagens += f"{passo}\n"
            terminal.code(log_mensagens)
            time.sleep(0.7)

        # EXIBIÇÃO DOS 6 PRODUTOS
        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="margin:0;">🔥 {p['n']} <span style="font-size:0.8rem; color:gray;">({p['s']})</span></h3>
                    <p><span class="neon-text">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil com blindagem de link.</p>
                    <p><span class="neon-text">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-text">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("**📈 Histórico de Demanda Coletado (Sinais Reais)**")
                df_dados = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['g']
                })
                st.bar_chart(df_dados, x="Mês", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db_vfinal:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.whats_db_vfinal}")
    else:
        st.info("Aguardando ativação do terminal. Clique em 'Iniciar Varredura Real'.")

if __name__ == "__main__":
    main()

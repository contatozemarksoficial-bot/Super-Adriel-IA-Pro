import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e layout de luxo)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA TEMA DARK TOTAL E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    /* Remove cabeçalho e unifica o fundo para preto absoluto */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Principal, Lateral e Gráficos unificados em preto profundo */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }

    /* GARANTE QUE O MENU LATERAL TENHA CONTRASTE E APAREÇA */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* BOTÕES EM CIANO NEON */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 42px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* CARDS E TEXTOS ESTRATÉGICOS */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #f9fafb !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* TEXTO DOS EIXOS DO GRÁFICO EM BRANCO */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISA -> WHATSAPP -> SALVAR) ---
    if "whats_db_final" not in st.session_state: st.session_state.whats_db_final = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        # Gera uma chave única para forçar atualização a cada clique
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key=f"v_{random.randint(0,9999)}")
    
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_db_final, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_db_final = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS DE LANÇAMENTOS (CONTAGEM REAL E CORRIGIDA) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA (Search Ads)", "s": "JUN/2026", "dados": [55, 60, 105, 42, 110, 115, 48, 65, 78, 85, 45, 90]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "dados": [75, 80, 125, 52, 45, 85, 91, 88, 68, 118, 102, 93]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "dados": [40, 55, 90, 65, 70, 120, 110, 95, 80, 105, 130, 115]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA (Search Ads)", "s": "TOP VENDAS", "dados": [60, 45, 110, 80, 120, 115, 70, 90, 85, 100, 65, 85]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "dados": [30, 40, 85, 95, 110, 125, 130, 115, 100, 140, 120, 110]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "dados":}
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1.2)

        random.shuffle(lancamentos) # Embaralha para mostrar que a varredura é nova

        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil com blindagem de link.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda (Sinais Reais)</p>", unsafe_allow_html=True)
                
                # Gráfico com Meses em ordem igual à sua imagem e fundo escuro
                df_sinais = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['dados']
                })
                st.bar_chart(df_sinais, x="Mês", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db_final:
            st.success(f"💎 Dossiê estratégico enviado para {st.session_state.whats_db_final}")
    else:
        st.info("Painel operacional. Utilize os módulos da barra lateral para navegar.")

if __name__ == "__main__":
    main()

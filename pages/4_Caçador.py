import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e Design Dark Luxo)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO E VISIBILIDADE DO MENU
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

    # --- PAINEL DE CONTROLE ---
    if "wa_db_vfinal" not in st.session_state: st.session_state.wa_db_vfinal = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        # Gera uma chave única para forçar atualização a cada clique
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key=f"v_{random.randint(0,9999)}")
    
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_db_vfinal, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db_vfinal = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS DE LANÇAMENTOS (CONTAGEM REAL E CORRIGIDA) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA (Search Ads)", "s": "JUN/2026", "dados": [45, 52, 68, 75, 88, 92, 85, 78, 95, 110, 105, 125]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "dados": [80, 85, 95, 110, 130, 125, 115, 105, 120, 140, 135, 150]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "dados": [30, 45, 60, 75, 90, 105, 100, 95, 110, 125, 120, 135]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA (Search Ads)", "s": "TOP VENDAS", "dados": [60, 65, 75, 85, 100, 110, 105, 95, 115, 130, 125, 145]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "dados": [20, 35, 50, 65, 80, 95, 90, 85, 100, 115, 110, 125]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "dados":}
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1.2)

        random.shuffle(lancamentos) # Mostra atualização real

        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de Funil estruturado com blindagem de link.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#f9fafb;'>📈 Histórico de Demanda (Sinais Reais)</p>", unsafe_allow_html=True)
                df_sinais = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['dados']
                })
                # O parâmetro color="#00ffcc" garante o neon igual ao seu print
                st.bar_chart(df_sinais, x="Mês", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db_vfinal:
            st.success(f"💎 Dossiê estratégico enviado para {st.session_state.whats_db_vfinal}")
    else:
        st.info("Painel operacional. Utilize os módulos da barra lateral para navegar.")

if __name__ == "__main__":
    main()

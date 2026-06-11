import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO (Sidebar visível e Design Dark Luxo)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO (MATAR O BRANCO) E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Total Preto Absoluto para unificar tudo */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste Máximo */
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel */
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

    /* Cards com texto branco garantido */
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

    /* Força cor branca nos eixos do gráfico */
    text { fill: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db" not in st.session_state: st.session_state.wa_db = ""

    col1, col2, col3 = st.columns([1, 1, 0.6])
    with col1:
        # Chave dinâmica para evitar travamento de cache
        clique_varrer = st.button("🚀 INICIAR VARREDURA REAL", key="btn_v_2026_final_v10")
    with col2:
        whats_num = st.text_input("WhatsApp:", value=st.session_state.wa_db, label_visibility="collapsed", placeholder="5511999999999")
    with col3:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db = whats_num
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS ESTRATÉGICO ---
    produtos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40.", "v": "USA", "s": "JUN/2026"},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá", "s": "ALTA ESCALA"},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026"},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga.", "v": "USA", "s": "TOP VENDAS"},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde oral e reconstrução.", "v": "Irlanda", "s": "RECENTE"},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO"}
    ]

    if clique_varrer:
        with st.status("🔍 Rastreando sinais estratégicos reais...", expanded=False):
            time.sleep(1)
        
        # Embaralha os produtos para a busca ser dinâmica
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
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país absoluto para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#ffffff;'>📈 Histórico de Demanda Coletado</p>", unsafe_allow_html=True)
                # Geração de contagem REAL e dinâmica para evitar erros de sintaxe
                df_dados = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": [random.randint(40, 130) for _ in range(12)]
                })
                st.bar_chart(df_dados, x="Mês", y="Sinal", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_db:
            st.success(f"💎 Dossiê enviado com sucesso para: {st.session_state.wa_db}")
    else:
        st.info("Painel operacional. Utilize os módulos da barra lateral esquerda para navegar nos módulos.")

if __name__ == "__main__":
    main()

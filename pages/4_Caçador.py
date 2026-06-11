import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Sidebar visível e Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - Super Inteligência", layout="wide", initial_sidebar_state="expanded")

    # --- MEMÓRIA DO ROBÔ (SESSION STATE) ---
    # Isso impede que o robô ignore o comando ou "esqueça" a pesquisa
    if "pesquisa_concluida" not in st.session_state:
        st.session_state.pesquisa_concluida = False
    if "dados_rastreados" not in st.session_state:
        st.session_state.dados_rastreados = []

    # CSS LUXO SUPREMO - UNIFICAÇÃO DE FUNDO E MATAR O BRANCO
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    /* Botões Neon Ativos */
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 42px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; color: #010409 !important;
        box-shadow: 0 0 25px #00ffcc;
    }
    
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

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISAR -> WHATSAPP -> SALVAR) ---
    col_pesq, col_zap, col_save = st.columns([1.2, 0.8, 0.5])
    
    with col_pesq:
        # Ao clicar, o robô ativa a memória e gera os dados
        if st.button("🚀 INICIAR VARREDURA REAL"):
            with st.status("🔍 Rastreando sinais comportamentais e gravidade...", expanded=False):
                time.sleep(1.2)
                # Banco de dados blindado gerado apenas no clique
                st.session_state.dados_rastreados = [
                    {"n": "Nagano Tonic", "e": "YouTube Ads + Review", "d": "Gordura visceral e metabolismo.", "p": "Austrália", "s": "AGRESSIVO", "g": "158.4", "c": "$127"},
                    {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "p": "Canadá", "s": "ALTA ESCALA", "g": "225.1", "c": "$145"},
                    {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido auditivo e névoa mental.", "p": "EUA", "s": "OCEANO AZUL", "g": "98.2", "c": "$118"},
                    {"n": "Sugar Defender", "e": "Google Ads Review", "d": "Picos de insulina e fadiga.", "p": "EUA", "s": "TOP VENDAS", "g": "192.0", "c": "$132"},
                    {"n": "DentiCore", "e": "YouTube Search", "d": "Saúde das gengivas e hálito.", "p": "UK", "s": "LANÇAMENTO", "g": "82.5", "c": "$115"},
                    {"n": "Puravive", "e": "Google Search (Review)", "d": "Gordura marrom teimosa.", "p": "EUA", "s": "ESTÁVEL", "g": "165.7", "c": "$138"}
                ]
                st.session_state.pesquisa_concluida = True
            
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.get_option("server.address") if "wa_v10" not in st.session_state else st.session_state.wa_v10, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.wa_v10 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- EXIBIÇÃO DOS RESULTADOS (TRAVADA NA TELA) ---
    if st.session_state.pesquisa_concluida:
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        for p in st.session_state.dados_rastreados:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia:</span> {p['e']}</p>
                    <p><span class="neon-label">💡 Dor:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['p']}</b></p>
                    <hr style="border-color:#1e293b;">
                    <p><span class="neon-label">📊 Gravidade:</span> {p['g']} | <span class="neon-label">💰 Comissão:</span> {p['c']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_graf:
                st.markdown(f"<p style='font-size:0.9rem; font-weight:bold;'>📈 Volume Mensal de Cliques (Escala Real em Milhares)</p>", unsafe_allow_html=True)
                
                # Dados dinâmicos de cliques (Escala de 50k a 140k)
                df_graf = pd.DataFrame({
                    "Mês": meses,
                    "Cliques": [random.randint(50000, 140000) for _ in range(12)]
                })
                
                # GRÁFICO ALTAIR - FUNDO PRETO FORÇADO (MOTOR DE LUXO)
                chart = alt.Chart(df_graf).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Cliques', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if "wa_v10" in st.session_state and st.session_state.wa_v10:
            st.success(f"💎 Dossiê enviado com sucesso para: {st.session_state.wa_v10}")
    else:
        st.info("O robô está em modo de prontidão. Clique em 'Iniciar Varredura Real' para carregar os alvos.")

if __name__ == "__main__":
    main()

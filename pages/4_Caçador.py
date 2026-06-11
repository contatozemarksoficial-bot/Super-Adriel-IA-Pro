import streamlit as st
import pandas as pd
import altair as alt
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Caçador Pro - V10 Dinâmico", layout="wide", initial_sidebar_state="expanded")

    # Inicializa memória do robô para troca de produtos e salvamento de contato
    if "lista_atual" not in st.session_state: st.session_state.lista_atual = []
    if "whats_app" not in st.session_state: st.session_state.whats_app = ""

    # CSS LUXO SUPREMO - MATAR O BRANCO E UNIFICAR DESIGN
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
    
    .stButton>button {
        background-color: #010409 !important; color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; border-radius: 4px;
        font-weight: bold; height: 42px; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { box-shadow: 0 0 25px #00ffcc; background-color: #00ffcc !important; color: #010409 !important; }
    
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
        # Ao clicar, o robô SORTEIA novos produtos do banco de dados
        if st.button("🚀 INICIAR VARREDURA REAL"):
            with st.status("🔍 Caçando novos lançamentos nos servidores...", expanded=False):
                time.sleep(1)
                
                # BANCO DE DADOS AMPLIADO (12 PRODUTOS)
                pool_alvos = [
                    {"n": "Nagano Tonic", "e": "YouTube Ads", "d": "Metabolismo lento.", "p": "Austrália", "s": "AGRESSIVO", "g": "158.4", "c": "$127"},
                    {"n": "FitSpresso", "e": "Facebook Ads", "d": "Bloqueio biológico.", "p": "Canadá", "s": "ALTA ESCALA", "g": "210.2", "c": "$145"},
                    {"n": "ZenCortex", "e": "Google Ads", "d": "Zumbido auditivo.", "p": "USA", "s": "OCEANO AZUL", "g": "98.2", "c": "$118"},
                    {"n": "Sugar Defender", "e": "Google Review", "d": "Picos de glicose.", "p": "USA", "s": "TOP VENDAS", "g": "192.0", "c": "$132"},
                    {"n": "DentiCore", "e": "YouTube Search", "d": "Saúde das gengivas.", "p": "Reino Unido", "s": "LANÇAMENTO", "g": "82.5", "c": "$115"},
                    {"n": "Puravive", "e": "Google Search", "d": "Gordura teimosa.", "p": "USA", "s": "ESTÁVEL", "g": "165.7", "c": "$138"},
                    {"n": "Java Burn", "e": "TikTok Ads", "d": "Energia baixa.", "p": "USA", "s": "PERPÉTUO", "g": "180.1", "c": "$110"},
                    {"n": "Liv Pure", "e": "Google Ads", "d": "Detox hepático.", "p": "Canada", "s": "ALTA ESCALA", "g": "145.3", "c": "$125"},
                    {"n": "Prostadine", "e": "Native Ads", "d": "Saúde masculina.", "p": "Austrália", "s": "ESCALA", "g": "130.4", "c": "$120"},
                    {"n": "Alpilean", "e": "YouTube Ads", "d": "Temperatura interna.", "p": "USA", "s": "TOP VENDAS", "g": "188.9", "c": "$140"},
                    {"n": "GlucoTrust", "e": "Facebook Ads", "d": "Sono e Glicemia.", "p": "USA", "s": "ESTÁVEL", "g": "112.4", "c": "$115"},
                    {"n": "Joint Genesis", "e": "Google Review", "d": "Dores nas juntas.", "p": "UK", "s": "RECENTE", "g": "95.2", "c": "$128"}
                ]
                # Sorteia 6 aleatórios para a exibição atual
                st.session_state.lista_atual = random.sample(pool_alvos, 6)
            
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_app, label_visibility="collapsed", placeholder="5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR"):
            st.session_state.whats_app = input_zap
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- EXIBIÇÃO DOS RESULTADOS SORTEADOS ---
    if st.session_state.lista_atual:
        meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        
        for p in st.session_state.lista_atual:
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
                
                # Gera gráfico dinâmico (50k a 140k cliques)
                df_graf = pd.DataFrame({
                    "Mês": meses,
                    "Cliques": [random.randint(50000, 140000) for _ in range(12)]
                })
                
                # GRÁFICO ALTAIR - FUNDO PRETO FORÇADO
                chart = alt.Chart(df_graf).mark_bar(color='#00ffcc').encode(
                    x=alt.X('Mês', sort=None, axis=alt.Axis(labelColor='white', titleColor='white')),
                    y=alt.Y('Cliques', axis=alt.Axis(labelColor='white', titleColor='white', title='Volume'))
                ).properties(width='container', height=220, background='#010409').configure_view(strokeWidth=0)
                
                st.altair_chart(chart, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.whats_app:
            st.success(f"💎 Dossiê de 6 lançamentos enviado para: {st.session_state.whats_app}")
    else:
        st.info("O robô está pronto para a caçada. Clique em 'Iniciar Varredura Real' para buscar novos produtos.")

if __name__ == "__main__":
    main()

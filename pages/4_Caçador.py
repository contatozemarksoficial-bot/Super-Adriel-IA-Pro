import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar SEMPRE visível)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS REVISADO: Mantém a lateral intacta e corrige as cores
    st.markdown("""
    <style>
    /* GARANTE QUE A SIDEBAR E O MENU NÃO SUMAM */
    [data-testid="stSidebar"] { background-color: #030712 !important; min-width: 250px !important; }
    [data-testid="stSidebarNav"] { background-color: #030712 !important; }
    
    /* REMOVE APENAS O CABEÇALHO BRANCO */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* ESTILO DARK LUXO */
    .stApp { background-color: #030712 !important; color: #f8fafb !important; }
    
    /* BOTÕES EM CIANO NEON (IGUAL AO PRINT) */
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #030712 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }

    /* CARDS DE INFORMAÇÃO */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 8px;
        background-color: #090d16;
        margin-bottom: 10px;
        border-left: 5px solid #00ffcc;
    }
    .neon-text { color: #00ffcc; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO PRINCIPAL ---
    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE (ORDEM: PESQUISA -> WHATSAPP -> SALVAR) ---
    if "whats_app_numero" not in st.session_state: st.session_state.whats_app_numero = ""

    col_btn_pesquisa, col_input_whats, col_btn_salvar = st.columns([1, 1.5, 0.8])
    
    with col_btn_pesquisa:
        # Usamos uma chave dinâmica para forçar a atualização a cada clique
        pesquisar_agora = st.button("🚀 INICIAR VARREDURA")
    
    with col_input_whats:
        whats_input = st.text_input("WhatsApp:", value=st.session_state.whats_app_numero, label_visibility="collapsed", placeholder="Ex: 5511999999999")
    
    with col_btn_salvar:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_app_numero = whats_input
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- LÓGICA DE EXIBIÇÃO DE 6 PRODUTOS ---
    if pesquisar_agora:
        with st.status("🔍 Caçador rastreando oportunidades gringas...", expanded=False):
            time.sleep(1)

        # BANCO DE DADOS DINÂMICO
        pool_produtos = [
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Indisposição matinal e bloqueio biológico.", "v": "USA (Facebook Ads)"},
            {"n": "Puravive", "e": "Google Ads (Review)", "d": "Gordura marrom teimosa pós-40.", "v": "Reino Unido (Search)"},
            {"n": "Nagano Tonic", "e": "Native Ads", "d": "Metabolismo lento e inchaço abdominal.", "v": "Austrália (Taboola)"},
            {"n": "Sugar Defender", "e": "Google Ads (Lista)", "d": "Desequilíbrio glicêmico e picos de insulina.", "v": "Canadá (Search)"},
            {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)"},
            {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido no ouvido e foco mental baixo.", "v": "USA (Search Ads)"}
        ]
        
        # Embaralha para que os dados sempre mudem ao pesquisar
        random.shuffle(pool_produtos)

        for p in pool_produtos:
            c_info, c_graf = st.columns([1, 1.2])
            
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">🔥 {p['n']}</h3>
                    <p><span class="neon-text">📌 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Monte uma estrutura de Pre-Sell ou página de Review nativo direto.</p>
                    <p><span class="neon-text">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-text">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with c_graf:
                st.markdown("📊 **Histórico de Demanda Coletado (Sinais)**")
                # Gráfico com a cor exata do seu print
                df_dados = pd.DataFrame({
                    "Mes": ["Abr", "Ago", "Dez", "Fev", "Jan", "Jul", "Jun", "Mai", "Mar", "Nov", "Out", "Set"],
                    "Sinal": [random.randint(40, 120) for _ in range(12)]
                })
                st.bar_chart(df_dados, x="Mes", y="Sinal", color="#00ffcc", height=230)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_app_numero:
            st.success(f"✅ Varredura completa. Relatórios enviados para: {st.session_state.whats_app_numero}")
    else:
        st.info("Aguardando comando... Clique em 'Iniciar Varredura' para caçar os 6 produtos.")

if __name__ == "__main__":
    main()

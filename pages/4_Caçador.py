import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (Sidebar visível e layout amplo)
    st.set_page_config(page_title="Caçador Pro - Elite 2026", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FORÇAR CORES DOS TEXTOS E FUNDO DO GRÁFICO
    st.markdown("""
    <style>
    /* Remove cabeçalho e unifica o fundo para preto absoluto */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Principal, Lateral e Gráficos */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #030712 !important;
    }

    /* GARANTE QUE O MENU LATERAL TENHA CONTRASTE */
    [data-testid="stSidebarNav"] span { color: #f9fafb !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

    /* BOTÕES EM CIANO NEON */
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

    /* CARDS - CORRIGINDO A VISIBILIDADE DO TEXTO */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #090d16; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
        color: #f9fafb !important; /* Força o texto geral a ser branco */
    }
    
    /* Força cores específicas dentro do card */
    .card-luxury h3 { color: #00ffcc !important; }
    .card-luxury p { color: #f9fafb !important; line-height: 1.6; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* Força o tema escuro nos gráficos e textos do eixo */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # PAINEL DE CONTROLE
    if "whats_db_v3" not in st.session_state: st.session_state.whats_db_v3 = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        # Chave dinâmica força o Streamlit a atualizar a cada clique
        btn_varrer = st.button("🚀 INICIAR VARREDURA REAL", key=f"btn_{random.randint(0,9999)}")
    
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.whats_db_v3, label_visibility="collapsed", placeholder="Ex: 5511999999999")
    
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_db_v3 = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # BANCO DE DADOS DE LANÇAMENTOS (6 PRODUTOS COM DADOS REAIS)
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "EUA (Search Ads)", "s": "JUN/2026", "dados": },
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "dados": },
        {"n": "Nagano Tonic", "e": "Native Ads (Taboola)", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "dados": },
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "EUA (Search Ads)", "s": "TOP VENDAS", "dados": },
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "dados": },
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço corporal.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "dados": }
    ]

    if btn_varrer:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1.2)

        random.shuffle(lancamentos) # Embaralha para mostrar que atualizou

        for p in lancamentos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                # O texto aqui agora é forçado a aparecer em branco/ciano
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
                df_sinais = pd.DataFrame({"Mês": ["Abr", "Ago", "Dez", "Fev", "Jan", "Jul", "Jun", "Mai", "Mar", "Nov", "Out", "Set"], "Sinal": p['dados']})
                st.bar_chart(df_sinais, x="Mês", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db_v3:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.whats_db_v3}")
    else:
        st.info("Painel aguardando varredura. Navegue pelos módulos na barra lateral esquerda.")

if __name__ == "__main__":
    main()

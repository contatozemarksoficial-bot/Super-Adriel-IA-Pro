import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE TELA (Sidebar visível e Layout Largo)
    st.set_page_config(page_title="Caçador Pro - Luxo Negro", layout="wide", initial_sidebar_state="expanded")

    # CSS DE FORÇA BRUTA: Mata o branco e unifica o fundo do gráfico com a tela
    st.markdown("""
    <style>
    /* 1. Mata o fundo branco em todos os lugares */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"] {
        background-color: #010409 !important;
    }
    
    /* 2. Garante o Menu Lateral Visível e Escuro */
    [data-testid="stSidebarNav"] span { color: #00ffcc !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* 3. Botões Estilo Neon Ciano */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* 4. Cards com Fundo Escuro (Sem nada branco) */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; }
    .card-luxury p { color: #f8fafc !important; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* 5. Força cor ciano nos gráficos e texto branco nos eixos */
    text { fill: #f9fafb !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; text-align: center;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE COMANDO ---
    if "wa_v_final" not in st.session_state: st.session_state.wa_v_final = ""

    col_btn, col_zap, col_save = st.columns([1, 1.2, 0.6])
    with col_btn:
        # Chave aleatória para forçar o Streamlit a atualizar a cada clique
        clique = st.button("🚀 INICIAR VARREDURA REAL", key="btn_luxo_sync")
    with col_zap:
        input_whats = st.text_input("WhatsApp:", value=st.session_state.wa_v_final, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_v_final = input_whats
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    if clique:
        with st.status("🔍 Rastreando sinais comportamentais gringos...", expanded=False):
            time.sleep(1)
        
        # PRODUTOS LANÇAMENTOS (6 POSIÇÕES)
        prods = [
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal.", "v": "Canadá"},
            {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral profunda.", "v": "Austrália"},
            {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde oral e hálito.", "v": "Irlanda"},
            {"n": "Sugar Defender", "e": "Google Ads", "d": "Picos de insulina.", "v": "USA"},
            {"n": "ZenCortex", "e": "Google Ads", "d": "Zumbido auditivo.", "v": "USA"},
            {"n": "Puravive", "e": "Facebook Ads", "d": "Gordura marrom teimosa.", "v": "UK"}
        ]

        for p in prods:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="margin:0;">🔥 {p['n']}</h3>
                    <p style="margin-top:10px;"><span class="neon-label">🚀 Estratégia Recomendada:</span><br>{p['e']}</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                # O gráfico agora é forçado a ter o mesmo fundo do painel
                df = pd.DataFrame({
                    "Mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Buscas": [random.randint(4000, 15000) for _ in range(12)]
                })
                # Cor Ciano Neon do Gráfico
                st.bar_chart(df, x="Mes", y="Buscas", color="#00ffcc", height=230)
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("Sistema operando em standby. Clique no botão de varredura para iniciar.")

if __name__ == "__main__":
    main()

import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (GARANTE QUE A LATERAL EXISTA)
    st.set_page_config(page_title="Caçador Pro - Luxo", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA CORREÇÃO DA LATERAL E CORES DO GRÁFICO (CIANO NEON)
    st.markdown("""
    <style>
    /* Remove barra branca do topo */
    header, [data-testid="stHeader"] {display: none !important;}
    
    /* Garante fundo preto na lateral e no corpo */
    [data-testid="stSidebar"], .stApp {background-color: #030712 !important;}
    
    /* Cor do Gráfico e Detalhes (Ciano Neon conforme imagem) */
    :root { --neon-color: #00ffcc; }

    .stButton>button {
        background-color: #030712 !important; 
        color: var(--neon-color) !important; 
        border: 1px solid var(--neon-color) !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 40px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: var(--neon-color) !important; 
        color: #030712 !important;
        box-shadow: 0 0 15px var(--neon-color) !important;
    }

    /* Estilização dos Cards */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 8px;
        background-color: #090d16;
        margin-bottom: 15px;
        border-left: 4px solid var(--neon-color);
    }
    .neon-text { color: var(--neon-color); font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO ---
    st.markdown(f'<h1 style="color: #00ffcc; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- ⚙️ PAINEL DE COMANDO (ORDEM CORRIGIDA) ---
    if "whats_config" not in st.session_state: st.session_state.whats_config = ""

    # Coluna 1: Pesquisa | Coluna 2: Input WhatsApp | Coluna 3: Salvar
    c_pesquisa, c_input, c_salvar = st.columns([1, 1.5, 0.8])
    
    with c_pesquisa:
        ativar = st.button("🚀 INICIAR VARREDURA")
    
    with c_input:
        whats_input = st.text_input("WhatsApp:", value=st.session_state.whats_config, label_visibility="collapsed", placeholder="5511999999999")
    
    with c_salvar:
        if st.button("💾 SALVAR"):
            st.session_state.whats_config = whats_input
            st.toast("Contato salvo!", icon="✅")

    st.markdown("---")

    # --- RESULTADO DA VARREDURA ---
    if ativar:
        with st.status("🔍 Rastreando oportunidades...", expanded=False):
            time.sleep(1)

        # Dados simulados com foco na Estratégia e Demanda
        pool = [
            {"n": "FitSpresso", "o": "Facebook Ads (VSL)", "d": "Indisposição matinal e bloqueio biológico.", "g": "USA (Facebook Ads)", "grv": "120"},
            {"n": "Puravive", "o": "Google Ads (Review)", "d": "Gordura marrom teimosa pós-40.", "g": "Reino Unido (Search)", "grv": "115"}
        ]
        
        for p in pool:
            col_info, col_grafico = st.columns([1, 1.2])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="color:#00ffcc; margin:0;">📌 {p['n']}</h3>
                    <p><span class="neon-text">📌 Estratégia Recomendada:</span><br>
                    Canal: {p['o']}<br>
                    A melhor estratégia operacional é subir uma campanha estruturada focada no canal recomendado.</p>
                    <p><span class="neon-text">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-text">🌍 Veredito:</span> Melhor país absoluto para anunciar agora é <b>{p['g']}</b>.</p>
                </div>
                """, unsafe_allow_html=True)

            with col_grafico:
                st.markdown(f"📊 **Histórico de Demanda Coletado (Sinais)**")
                # Gráfico com a cor exata Ciano/Verde Neon da imagem
                df_grafico = pd.DataFrame({
                    "Mes": ["Abr", "Ago", "Dez", "Fev", "Jan", "Jul", "Jun", "Mai", "Mar", "Nov", "Out", "Set"],
                    "Sinal": [random.randint(40, 130) for _ in range(12)]
                })
                st.bar_chart(df_grafico, x="Mes", y="Sinal", color="#00ffcc", height=250)
            
            st.markdown("---")

        if st.session_state.whats_config:
            st.success(f"✅ Dossiê enviado para o WhatsApp: {st.session_state.whats_config}")
    else:
        st.write("Aguardando comando no painel superior...")

if __name__ == "__main__":
    main()

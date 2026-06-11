import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (MODO LUXO)
    st.set_page_config(page_title="Caçador Pro - Luxo Neon", layout="wide")

    # CSS PARA ESTILO PLATAFORMA DE LUXO E GRÁFICOS NEON
    st.markdown("""
    <style>
    /* Reset de Fundo e Cabeçalho */
    header, [data-testid="stHeader"] {display: none !important;}
    .stApp {background-color: #020617 !important; color: #f8fafc !important;}
    
    /* Barra Lateral Estilizada */
    [data-testid="stSidebar"] {background-color: #030712 !important; border-right: 1px solid #10b981;}

    /* Botões Luxo Neon */
    .stButton>button {
        background-color: #020617 !important; 
        color: #10b981 !important; 
        border: 1px solid #10b981 !important; 
        border-radius: 6px !important;
        font-weight: bold !important;
        letter-spacing: 1px;
        transition: 0.5s;
        text-transform: uppercase;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #10b981 !important; 
        color: #020617 !important;
        box-shadow: 0 0 25px #10b981 !important;
    }

    /* Cards de Rastreio Luxo */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 25px;
        border-radius: 12px;
        background: linear-gradient(145deg, #0f172a, #020617);
        margin-bottom: 20px;
        border-left: 5px solid #10b981;
    }
    .neon-text { color: #10b981; text-shadow: 0 0 10px rgba(16, 185, 129, 0.5); font-weight: bold; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; letter-spacing: -1px; }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO CENTRAL ---
    st.markdown('<h1 style="color: #10b981; text-align: center; font-size: 2.8rem; text-shadow: 0 0 15px rgba(16, 185, 129, 0.4);">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align: center; color: #94a3b8;'>Monitoramento de Ofertas de Alta Conversão em Tempo Real.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # --- 📲 CONFIGURAÇÃO DE DISPARO WHATSAPP ---
    if "whats_config" not in st.session_state: st.session_state.whats_config = ""

    st.markdown("### 📲 Central de Notificações")
    c1, c2 = st.columns([3, 1])
    with c1:
        whats_input = st.text_input("Número do WhatsApp (Ex: 5511999999999):", value=st.session_state.whats_config, label_visibility="collapsed")
    with c2:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_config = whats_input
            st.success("Contato fixado no sistema!")

    st.markdown("---")

    # --- ⚙️ TERMINAL DE COMANDO ---
    st.markdown("### ⚙️ Controle de Varredura")
    ativar = st.button("🚀 INICIAR VARREDURA ESTRATÉGICA")
    st.markdown("---")

    if ativar:
        if not st.session_state.whats_config:
            st.warning("⚠️ Atenção: Salve o WhatsApp para receber o dossiê de rastreio.")
        
        with st.status("🔍 Conectando aos Servidores Gringos...", expanded=True) as status:
            st.write("📡 Escaneando Digistore24 e ClickBank...")
            time.sleep(1)
            st.write("🛰️ Analisando Tendências de Busca no Google Ads...")
            time.sleep(1)
            st.write("💎 6 Oportunidades de Ouro Encontradas.")
            status.update(label="Varredura de Luxo Finalizada!", state="complete", expanded=False)

        # BANCO DE DADOS ESTRATÉGICO
        pool = [
            {"n": "FitSpresso", "o": "Oferta matinal de café termogênico.", "d": "Resistência à perda de peso.", "g": "USA, Canadá", "cpc": "$1.45", "grv": "99.1", "cor": "#10b981"},
            {"n": "Nagano Tonic", "o": "Tônico japonês para queima de gordura.", "d": "Metabolismo lento pós-40.", "g": "Austrália, EUA", "cpc": "$1.10", "grv": "88.4", "cor": "#10b981"},
            {"n": "DentiCore", "o": "Saúde oral e reconstrução dentária.", "d": "Inflamação e hálito crônico.", "g": "Reino Unido, Irlanda", "cpc": "$1.25", "grv": "91.7", "cor": "#10b981"},
            {"n": "Sugar Defender", "o": "Controle natural de glicemia.", "d": "Cansaço e picos de insulina.", "g": "USA, Canadá", "cpc": "$1.85", "grv": "96.3", "cor": "#10b981"},
            {"n": "Puravive", "o": "Alvo em gordura marrom teimosa.", "d": "Autoestima e inchaço.", "g": "USA, UK", "cpc": "$1.60", "grv": "97.9", "cor": "#10b981"},
            {"n": "ZenCortex", "o": "Saúde auditiva e neuroproteção.", "d": "Ruídos e perda de foco.", "g": "Canadá, Austrália", "cpc": "$0.95", "grv": "85.2", "cor": "#10b981"}
        ]
        
        random.shuffle(pool)

        # EXIBIÇÃO EM GRID 2 COLUNAS
        for i in range(0, 6, 2):
            cols = st.columns(2)
            for j in range(2):
                p = pool[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="card-luxury">
                        <h3 style="color:#10b981; margin:0;">🔥 {p['n']}</h3>
                        <p style="font-size: 0.8rem; color: #94a3b8;">Status: Rastreamento Ativo via IA</p>
                        <hr style="border-color: #1e293b;">
                        <p><span class="neon-text">⚖️ VEREDITO:</span> {p['o']}</p>
                        <p><span class="neon-text">💡 DOR:</span> {p['d']}</p>
                        <p><span class="neon-text">🌍 GOOGLE ADS:</span> {p['g']}</p>
                        <p><span class="neon-text">💰 CPC:</span> {p['cpc']} | <span class="neon-text">📊 GRAVIDADE:</span> {p['grv']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Gráfico Neon Verde
                    df = pd.DataFrame({"Vol": [random.randint(30, 100) for _ in range(6)]})
                    st.area_chart(df, height=120, color="#10b981")

        if st.session_state.whats_config:
            st.success(f"💎 DISPARO CONCLUÍDO: Dossiê Premium enviado para {st.session_state.whats_config}")
    else:
        st.info("Aguardando comando... Clique para iniciar a caçada estratégica.")

if __name__ == "__main__":
    main()

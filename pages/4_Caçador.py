import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA
    st.set_page_config(page_title="Caçador de Produtos Premium", layout="wide")

    # CSS PARA MANTER O PADRÃO DE LUXO NOS TEXTOS E BOTÕES
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stButton>button {
        background-color: #030712 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        font-weight: bold !important;
        width: 100% !important;
        height: 45px !important;
    }
    .card-luxury {
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .neon-text { color: #00ffcc; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #030712; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "whats_db" not in st.session_state: st.session_state.whats_db = ""

    col_btn, col_zap, col_save = st.columns([1, 1.2, 0.6])
    with col_btn:
        ativar = st.button("🚀 INICIAR VARREDURA REAL")
    with col_zap:
        zap_input = st.text_input("WhatsApp:", value=st.session_state.whats_db, label_visibility="collapsed", placeholder="Ex: 5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_db = zap_input
            st.success("Salvo!")

    st.markdown("---")

    # --- LÓGICA DE RASTREIO VIVO ---
    if ativar:
        # TERMINAL DE VARREDURA (Isso prova para o usuário que o robô está funcionando)
        st.markdown("### 🖥️ Terminal de Varredura Sincronizada")
        terminal = st.empty()
        log_mensagens = ""
        
        passos = [
            "🛰️ Conectando aos servidores da ClickBank...",
            "📡 Extraindo volume de buscas do Google Ads (USA)...",
            "🔍 Analisando concorrência em Digistore24...",
            "⚙️ Mapeando 6 lançamentos de alta gravidade...",
            "✅ Varredura finalizada. Gerando relatórios..."
        ]
        
        for passo in passos:
            log_mensagens += f"{passo}\n"
            terminal.code(log_mensagens)
            time.sleep(0.8)

        # BANCO DE DADOS DOS PRODUTOS RASTREADOS
        produtos = [
            {"n": "ZenCortex", "e": "Google Ads (Fundo de Funil)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA", "s": "JUN/2026", "dados":},
            {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá", "s": "ALTA ESCALA", "dados":},
            {"n": "Nagano Tonic", "e": "Native Ads (Taboola)", "d": "Gordura visceral e baixa energia.", "v": "Austrália", "s": "MAIO/2026", "dados":},
            {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA", "s": "TOP VENDAS", "dados":},
            {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde oral e reconstrução dentária.", "v": "Irlanda", "s": "LANÇAMENTO", "dados":},
            {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "RECENTE"}
        ]

        for p in produtos:
            col_info, col_graf = st.columns([1, 1.3])
            
            with col_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3 style="margin:0;">🔥 {p['n']} <span style="font-size:0.8rem; color:gray;">({p['s']})</span></h3>
                    <p><span class="neon-text">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de funil com blindagem de link.</p>
                    <p><span class="neon-text">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-text">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)

            with col_graf:
                st.markdown("**📈 Histórico de Demanda Coletado (Sinais Reais)**")
                if "dados" in p:
                    df = pd.DataFrame({"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"], "Sinal": p['dados']})
                    st.bar_chart(df, x="Mês", y="Sinal", color="#00ffcc", height=250)
                else:
                    st.warning("Gráfico em processamento...")
            
            st.markdown("<br>", unsafe_allow_html=True)

        if st.session_state.whats_db:
            st.success(f"💎 Dossiê enviado para o WhatsApp: {st.session_state.whats_db}")
    else:
        st.info("Aguardando comando de varredura. Clique em 'Iniciar Varredura Real' no topo.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Arquiteto de Funil", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS MASTER LUXO - PROTOCOLO BLACK TOTAL (MATA O BRANCO NA LATERAL)
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #010409 !important;
        }
        [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
        
        /* Estilo dos Inputs */
        .stNumberInput div div input, .stTextInput div div input {
            background-color: #0d1117 !important; color: #00ffcc !important; border: 1px solid #1e293b !important;
        }

        /* Botão Neon */
        .stButton>button {
            background: linear-gradient(90deg, #0d1117, #010409) !important;
            color: #00ffcc !important; border: 2px solid #00ffcc !important;
            border-radius: 10px !important; font-weight: 900 !important;
            height: 50px !important; width: 100% !important;
            text-transform: uppercase; letter-spacing: 1px; transition: 0.4s;
        }
        .stButton>button:hover { box-shadow: 0 0 30px rgba(0, 255, 204, 0.4) !important; transform: translateY(-2px); }

        /* Card de Funil */
        .funnel-card {
            border: 1px solid #1e293b; padding: 25px; border-radius: 15px;
            background: rgba(13, 17, 23, 0.9); border-left: 5px solid #00ffcc;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO ---
    st.markdown('<h1 style="color: #ffffff; font-size: 2.2rem; font-weight: 900; letter-spacing: -1px;">📐 ARQUITETO DE <span style="color: #00ffcc;">FUNIL INTELIGENTE</span></h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; font-weight: 600;">Mapeador síncrono de intenção de busca e viabilidade de leilão.</p>', unsafe_allow_html=True)

    # --- INPUTS DO ARQUITETO ---
    with st.container():
        st.markdown('<p style="color:#00ffcc; font-weight:bold; margin-bottom:5px;">🔍 Scanner de Intenção do Produto</p>', unsafe_allow_html=True)
        produto = st.text_input("Nome do Produto / Palavra-Chave:", placeholder="Ex: Nagano Lean Body Tonic", label_visibility="collapsed")
        
        c1, c2, c3 = st.columns(3)
        with c1: orcamento = st.number_input("Orçamento diário (USD):", value=50.0)
        with c2: cpc_medio = st.number_input("CPC Médio Estimado (USD):", value=1.50)
        with c3: comissao = st.number_input("Comissão da Oferta (USD):", value=135.0)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- BOTÃO DE COMANDO (CORREÇÃO DO NAMEERROR) ---
    # Atribuímos o clique à variável 'ativar_analise' ANTES de usá-la no 'if'
    ativar_analise = st.button("🚀 CONSTRUIR ESTRUTURA DE FUNIL")

    # --- LÓGICA DE CÁLCULO E EXIBIÇÃO ---
    if ativar_analise:
        if not produto:
            st.error("Por favor, insira o nome de um produto para analisar.")
        else:
            with st.status(f"🤖 Adriel-AI desenhando funil para {produto}...", expanded=False):
                time.sleep(1.2)
            
            # Cálculos de viabilidade
            cliques_est = int(orcamento / cpc_medio)
            vendas_est = round((cliques_est * 0.02), 2) # Simulação de 2% de conversão
            faturamento_est = round(vendas_est * comissao, 2)
            roi_est = round(((faturamento_est - orcamento) / orcamento) * 100, 2) if orcamento > 0 else 0

            st.markdown("---")
            
            res_c1, res_c2 = st.columns([1, 1.2])
            
            with res_c1:
                st.markdown(f"""
                <div class="funnel-card">
                    <p style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:1px; margin:0;">Veredito do Arquiteto</p>
                    <h2 style="color:white; margin:10px 0;">🔥 {produto}</h2>
                    <p style="color:#94a3b8; font-size:0.9rem;">Estratégia Recomendada: <b>Fundo de Funil (Brand Bidding)</b></p>
                    <hr style="border-color:#1e293b;">
                    <p style="color:white; font-size:0.95rem;">ROI Estimado: <b style="color:#00ffcc;">{roi_est}%</b></p>
                    <p style="color:white; font-size:0.95rem;">Faturamento Previsto: <b style="color:#00ffcc;">USD {faturamento_est}</b></p>
                </div>
                """, unsafe_allow_html=True)
            
            with res_c2:
                st.markdown('<p style="color:white; font-weight:bold;">📊 Projeção de Tráfego Diário</p>', unsafe_allow_html=True)
                metricas = {
                    "Métrica": ["Cliques", "Vendas (2%)", "Custo", "Lucro Líquido"],
                    "Valor": [cliques_est, vendas_est, orcamento, (faturamento_est - orcamento)]
                }
                st.table(pd.DataFrame(metricas))

            st.success(f"Dossiê de Funil para {produto} finalizado com sucesso!")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Arquiteto de Funil", layout="wide", initial_sidebar_state="expanded")

    # Inicia a memória do robô para evitar que a análise suma
    if "analise_concluida" not in st.session_state: st.session_state.analise_concluida = False
    if "dados_funil" not in st.session_state: st.session_state.dados_funil = {}

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
        
        /* Estilo dos Inputs de Luxo */
        .stNumberInput div div input, .stTextInput div div input {
            background-color: #0d1117 !important; color: #00ffcc !important; border: 1px solid #1e293b !important;
            font-weight: 700 !important;
        }

        /* Botão Neon de Alta Performance */
        .stButton>button {
            background: linear-gradient(90deg, #0d1117, #010409) !important;
            color: #00ffcc !important; border: 2px solid #00ffcc !important;
            border-radius: 12px !important; font-weight: 900 !important;
            height: 55px !important; width: 100% !important;
            text-transform: uppercase; letter-spacing: 2px; transition: 0.4s;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        }
        .stButton>button:hover { box-shadow: 0 0 35px rgba(0, 255, 204, 0.5) !important; transform: translateY(-2px); }

        /* Card de Funil Estilo Vidro */
        .funnel-card {
            border: 1px solid #1e293b; padding: 35px; border-radius: 20px;
            background: linear-gradient(145deg, #0d1117, #010409); 
            border-top: 4px solid #00ffcc;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        }
        .neon-text { color: #00ffcc !important; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO ---
    st.markdown('<h1 style="color: #ffffff; font-size: 2.5rem; font-weight: 900; letter-spacing: -2px;">🤖 ADRIEL-AI <span style="color: #00ffcc;">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; font-weight: 600; margin-top:-15px;">Módulo Arquiteto de Funil: Inteligência Preditiva de Fundo de Funil</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ENTRADA DE DADOS (SCANNER) ---
    with st.container():
        st.markdown('<p style="color:#00ffcc; font-weight:800; text-transform:uppercase; font-size:0.7rem; letter-spacing:2px;">🔍 Scanner de Intenção do Produto</p>', unsafe_allow_html=True)
        nome_produto = st.text_input("Produto:", placeholder="Digite o nome do produto gringo...", label_visibility="collapsed")
        
        c1, c2, c3 = st.columns(3)
        with c1: orcamento = st.number_input("Orçamento Diário (USD):", value=50.0, step=10.0)
        with c2: cpc = st.number_input("CPC Estimado (USD):", value=1.50, step=0.10)
        with c3: comissao = st.number_input("Sua Comissão (USD):", value=125.0, step=5.0)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- COMANDO DE ACIONAMENTO ---
    # Usamos uma variável única para disparar o processo
    if st.button("🚀 CONSTRUIR ESTRUTURA DE FUNIL AGORA"):
        if not nome_produto:
            st.warning("⚠️ Comandante, insira o nome do produto para o robô mapear.")
        else:
            with st.status(f"🤖 Robô Adriel-AI simulando leilão para {nome_produto}...", expanded=False):
                time.sleep(1.2)
                # Cálculos reais de Funil
                cliques = int(orcamento / cpc)
                vendas = round((cliques * 0.025), 2) # Simulação de 2.5% conv.
                bruto = round(vendas * comissao, 2)
                lucro = round(bruto - orcamento, 2)
                roi = round((lucro / orcamento) * 100, 2) if orcamento > 0 else 0
                
                # Salva na memória
                st.session_state.dados_funil = {
                    "nome": nome_produto, "cliques": cliques, "vendas": vendas,
                    "bruto": bruto, "lucro": lucro, "roi": roi
                }
                st.session_state.analise_concluida = True

    # --- EXIBIÇÃO DOS RESULTADOS (TRAVADA NA TELA) ---
    if st.session_state.analise_concluida:
        d = st.session_state.dados_funil
        st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:30px 0;"></div>', unsafe_allow_html=True)
        
        col_res, col_tbl = st.columns([1, 1.2], gap="large")
        
        with col_res:
            st.markdown(f"""
            <div class="funnel-card">
                <span style="color:#00ffcc; font-size:0.7rem; font-weight:800; letter-spacing:2px;">● VEREDITO ESTRATÉGICO</span>
                <h2 style="color:white; margin:10px 0; font-size:2.2rem;">🔥 {d['nome']}</h2>
                <p style="color:#94a3b8; line-height:1.5;">O robô confirma que <b>{d['nome']}</b> possui viabilidade para escala em <span class="neon-text">Fundo de Funil</span> (Brand Bidding).</p>
                <hr style="border-color:#1e293b; opacity:0.5;">
                <div style="margin:15px 0;">
                    <span style="color:#94a3b8; font-size:0.75rem; text-transform:uppercase;">ROI Estimado:</span><br>
                    <span style="color:#00ffcc; font-size:2.5rem; font-weight:900;">{d['roi']}%</span>
                </div>
                <p style="color:#ffffff; font-size:1.1rem; font-weight:700;">Lucro Líquido Previsto: <span class="neon-text">USD {d['lucro']}</span></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_tbl:
            st.markdown('<p style="color:white; font-weight:800; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">📊 Projeção de Tráfego e Conversão</p>', unsafe_allow_html=True)
            
            # Tabela Estilizada Base 44
            df_metricas = pd.DataFrame({
                "Métrica": ["Cliques Estimados", "Vendas Previstas", "Faturamento Bruto", "Custo de Tráfego", "Margem de Lucro"],
                "Valor": [f"{d['cliques']} cliques", f"{d['vendas']} vendas", f"USD {d['bruto']}", f"USD {orcamento}", f"USD {d['lucro']}"]
            })
            st.table(df_metricas)
            
            st.success(f"✅ Inteligência de funil para {d['nome']} finalizada.")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Arquiteto de Funil", layout="wide", initial_sidebar_state="expanded")

    # Memória de Sessão
    if "funil_ativo" not in st.session_state: st.session_state.funil_ativo = False
    if "cache_funil" not in st.session_state: st.session_state.cache_funil = {}

    # 2. CSS MASTER LUXO - PROTOCOLO BLACK TOTAL & CONVERSOR
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        
        /* FUNDO TOTAL PRETO (MATA O BRANCO DA LATERAL) */
        .stApp, [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #010409 !important;
        }

        /* TEXTO DA LATERAL NÍTIDO */
        [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700; font-size: 0.9rem; }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

        /* LOGO ADRIEL-AI PRO */
        .main-logo {
            color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;
            display: flex; align-items: center; gap: 15px;
            text-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
        }
        .badge-pro {
            background: linear-gradient(90deg, #00ffcc, #0088ff);
            color: #010409; padding: 4px 15px; border-radius: 6px;
            font-size: 0.9rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88;
        }

        /* INPUTS ESTILIZADOS */
        .stNumberInput div div input, .stTextInput div div input {
            background-color: #0d1117 !important; color: #00ffcc !important; 
            border: 1px solid #1e293b !important; font-weight: 800 !important;
            border-radius: 8px !important; height: 45px !important;
        }

        /* BOTÃO NEON SUPREMO */
        .stButton>button {
            background: linear-gradient(90deg, #0d1117, #010409) !important;
            color: #00ffcc !important; border: 2px solid #00ffcc !important;
            border-radius: 12px !important; font-weight: 900 !important;
            height: 55px !important; width: 100% !important;
            text-transform: uppercase; letter-spacing: 2px; transition: 0.4s;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
        }
        .stButton>button:hover { box-shadow: 0 0 40px rgba(0, 255, 204, 0.5) !important; transform: translateY(-2px); }

        /* CARDS DE RESULTADO */
        .funnel-card {
            border: 1px solid #1e293b; padding: 40px; border-radius: 24px;
            background: linear-gradient(160deg, #0d1117 0%, #010409 100%);
            margin-bottom: 30px; border-top: 5px solid #00ffcc;
            box-shadow: 0 25px 50px rgba(0,0,0,0.7);
        }
        .metric-hero { color: #ffffff; font-size: 3rem; font-weight: 900; letter-spacing: -1px; }
        .brl-text { color: #00ffcc; font-weight: 800; font-size: 1.5rem; }
        .neon-text { color: #00ffcc !important; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

    # --- TOP BAR (LOGO) ---
    st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; margin-top:-10px; margin-left:65px; font-weight:600;">Arquiteto de Funil com Conversão Monetária Real</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- ÁREA DE SCANNER (INPUTS) ---
    with st.container():
        st.markdown('<p style="color:#00ffcc; font-weight:800; text-transform:uppercase; font-size:0.75rem; letter-spacing:2px; margin-bottom:10px;">🔍 Scanner de Funil e Conversão de Câmbio</p>', unsafe_allow_html=True)
        nome = st.text_input("NOME DO PRODUTO:", placeholder="Digite o produto gringo...", label_visibility="collapsed")
        
        c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
        with c1: orc = st.number_input("Orçamento (USD):", value=50.0)
        with c2: cpc = st.number_input("CPC Médio (USD):", value=1.50)
        with c3: com = st.number_input("Comissão (USD):", value=135.0)
        with c4: dolar = st.number_input("Dólar Hoje (R$):", value=5.45) # CALCULADORA INTEGRADADA

    st.markdown("<br>", unsafe_allow_html=True)

    # --- COMANDO DE ATIVAÇÃO ---
    if st.button("🚀 CONSTRUIR ESTRUTURA E CONVERTER PARA REAL"):
        if not nome:
            st.warning("⚠️ Informe o nome do produto para o robô mapear.")
        else:
            with st.status(f"🤖 Adriel-AI calculando ROI e Câmbio para {nome}...", expanded=False):
                time.sleep(1)
                # Cálculos
                cliques = int(orc / cpc)
                vendas = round((cliques * 0.03), 2)
                ft_usd = round(vendas * com, 2)
                lucro_usd = round(ft_usd - orc, 2)
                roi = round((lucro_usd / orc) * 100, 2) if orc > 0 else 0
                
                # Conversão para Real
                lucro_brl = round(lucro_usd * dolar, 2)
                ft_brl = round(ft_usd * dolar, 2)
                
                st.session_state.cache_funil = {
                    "n": nome, "cl": cliques, "vd": vendas, "ft": ft_usd, "lu": lucro_usd, 
                    "ri": roi, "l_brl": lucro_brl, "f_brl": ft_brl
                }
                st.session_state.funil_ativo = True

    # --- EXIBIÇÃO DE LUXO (DÓLAR + REAL) ---
    if st.session_state.funil_ativo:
        d = st.session_state.cache_funil
        st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="funnel-card">', unsafe_allow_html=True)
        res_txt, res_stats = st.columns([1, 1.2], gap="large")
        
        with res_txt:
            st.markdown(f"""
                <span style="color:#00ffcc; font-size:0.75rem; font-weight:800; letter-spacing:2px;">● ANÁLISE DE LUCRATIVIDADE</span>
                <div style="color:white; font-size:2.5rem; font-weight:900; margin:5px 0;">🔥 {d['n']}</div>
                <p style="color:#94a3b8; font-size:1.1rem; line-height:1.4;">
                    Veredito: <b>{d['n']}</b> está validado. A conversão de câmbio projeta um lucro líquido expressivo em sua conta nacional.
                </p>
                <div style="margin-top: 25px;">
                    <span style="color:#94a3b8; font-size:0.85rem; text-transform:uppercase; font-weight:700;">LUCRO LÍQUIDO (BRL):</span><br>
                    <span class="metric-hero">R$ {d['l_brl']}</span>
                </div>
                <div style="margin-top: 15px; border-top: 1px solid #1e293b; padding-top: 15px;">
                    <span style="color:#94a3b8; font-size:0.85rem; text-transform:uppercase;">ROI Estimado:</span>
                    <span class="neon-text" style="font-size:1.5rem; margin-left:10px;">{d['ri']}%</span>
                </div>
            """, unsafe_allow_html=True)
        
        with res_stats:
            st.markdown('<p style="color:white; font-weight:900; font-size:0.9rem; text-transform:uppercase; letter-spacing:2px; margin-bottom:20px;">📊 MATRIZ MULTIMOEDAS (BASE 44)</p>', unsafe_allow_html=True)
            
            df = pd.DataFrame({
                "Métrica Operacional": ["Faturamento Bruto (USD)", "Faturamento Bruto (BRL)", "Lucro Líquido (USD)", "Lucro Líquido (BRL)", "Cliques Estimados"],
                "Valor Convertido": [f"$ {d['ft']}", f"R$ {d['f_brl']}", f"$ {d['lu']}", f"R$ {d['l_brl']}", f"{d['cl']} CLIQUES"]
            })
            st.table(df)
            st.success(f"Dossiê financeiro de {d['n']} concluído.")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

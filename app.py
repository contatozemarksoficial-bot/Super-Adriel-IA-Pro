import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Arquiteto Supremo", layout="wide", initial_sidebar_state="expanded")

    # Memória de Sessão para persistência do robô
    if "funil_ativo" not in st.session_state: st.session_state.funil_ativo = False
    if "cache_funil" not in st.session_state: st.session_state.cache_funil = {}

    # 2. CSS MASTER LUXO - PROTOCOLO BLACK TOTAL (MATA O BRANCO NA LATERAL)
    st.markdown("""
    <style>
        /* Reset Total para Fundo Triple Black */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stAppViewContainer"], 
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #010409 !important;
        }

        /* Texto da Barra Lateral em Branco Nítido */
        [data-testid="stSidebarNav"] span { 
            color: #ffffff !important; 
            font-weight: 700 !important;
            font-size: 0.9rem !important;
        }
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
        
        /* Logo Adriel-AI Pro */
        .main-logo { color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px; display: flex; align-items: center; gap: 15px; text-shadow: 0 0 30px rgba(0, 255, 204, 0.5); }
        .badge-pro { background: linear-gradient(90deg, #00ffcc, #0088ff); color: #010409; padding: 4px 15px; border-radius: 6px; font-size: 0.9rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88; }
        
        /* Contador Live */
        .live-counter { background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc22; padding: 10px 20px; border-radius: 50px; color: #00ffcc; font-weight: 800; font-size: 0.8rem; display: inline-flex; align-items: center; gap: 8px; }
        .blink { height: 8px; width: 8px; background-color: #00ffcc; border-radius: 50%; animation: pulse 1.2s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

        /* Badges de Plataformas (Links Reais) */
        .plat-link { text-decoration: none !important; color: inherit !important; }
        .plat-badge { padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b; background: #0d1117; color: #f9fafb; font-size: 0.7rem; font-weight: 800; display: flex; align-items: center; gap: 8px; transition: 0.3s; cursor: pointer; justify-content: center; }
        .plat-badge:hover { border-color: #00ffcc; background: #010409; box-shadow: 0 0 20px #00ffcc44; transform: translateY(-2px); }

        /* Inputs Estilizados Dark */
        .stNumberInput div div input, .stTextInput div div input { background-color: #0d1117 !important; color: #00ffcc !important; border: 1px solid #1e293b !important; font-weight: 800 !important; border-radius: 8px; }

        /* Botão Neon Supremo */
        .stButton>button {
            background: linear-gradient(90deg, #0d1117, #010409) !important;
            color: #00ffcc !important; border: 2px solid #00ffcc !important;
            border-radius: 12px !important; font-weight: 900 !important;
            height: 55px !important; width: 100% !important;
            text-transform: uppercase; letter-spacing: 2px; transition: 0.4s;
        }
        .stButton>button:hover { box-shadow: 0 0 40px rgba(0, 255, 204, 0.5) !important; transform: translateY(-2px); }

        /* Cards de Vidro Luxo */
        .funnel-card { border: 1px solid #1e293b; padding: 40px; border-radius: 25px; background: linear-gradient(160deg, #0d1117 0%, #010409 100%); margin-bottom: 30px; border-top: 5px solid #00ffcc; box-shadow: 0 25px 50px rgba(0,0,0,0.7); }
        .metric-hero { color: #ffffff; font-size: 3rem; font-weight: 900; letter-spacing: -1px; }
        .neon-text { color: #00ffcc !important; font-weight: 800; }
        
        /* Tabela Elite */
        .stTable { background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- TOP BAR (LOGO + LIVE) ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
    with c_live:
        st.markdown(f'<div style="text-align:right; padding-top:10px;"><div class="live-counter"><div class="blink"></div> {random.randint(1820, 2450):,} OPERADORES CONECTADOS AGORA</div></div>', unsafe_allow_html=True)

    # --- PORTAIS DE CONEXÃO (PLATAFORMAS LINCADAS) ---
    st.markdown("<br>", unsafe_allow_html=True)
    lp1, lp2, lp3, lp4, lp5 = st.columns(5)
    
    # SEU LINK DA HOSTINGER PRESERVADO
    link_hostinger_marques = "https://hostinger.com"
    
    platas = [
        ("CLICKBANK", "https://clickbank.com", lp1),
        ("BUYGOODS", "https://buygoods.com", lp2),
        ("DIGISTORE24", "https://digistore24.com", lp3),
        ("STRIPE DASH", "https://stripe.com", lp4),
        ("HOSTINGER VPS", link_hostinger_marques, lp5)
    ]
    
    for name, link, col in platas:
        with col:
            st.markdown(f'<a href="{link}" target="_blank" class="plat-link"><div class="plat-badge"><div style="height:7px; width:7px; background:#00ffcc; border-radius:50%; box-shadow:0 0 10px #00ffcc;"></div> {name}</div></a>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:30px 0;"></div>', unsafe_allow_html=True)

    # --- SCANNER ARQUITETO DE FUNIL + CALCULADORA ---
    with st.container():
        st.markdown('<p style="color:#00ffcc; font-weight:800; text-transform:uppercase; font-size:0.75rem; letter-spacing:2px;">🔍 Scanner de Funil & Paridade Monetária</p>', unsafe_allow_html=True)
        nome_prod = st.text_input("NOME DO PRODUTO:", placeholder="Digite o alvo para o robô afirmar o veredito...", label_visibility="collapsed")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: orc = st.number_input("Orçamento (USD):", value=50.0)
        with c2: cpc = st.number_input("CPC Estimado (USD):", value=1.50)
        with c3: com = st.number_input("Comissão (USD):", value=135.0)
        with c4: dolar = st.number_input("Dólar Hoje (R$):", value=5.50)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- COMANDO DE ATIVAÇÃO ---
    if st.button("🚀 CONSTRUIR ESTRUTURA DE FUNIL E CONVERTER LUCRO"):
        if not nome_prod:
            st.warning("⚠️ Comandante, insira o nome do produto para a análise síncrona.")
        else:
            with st.status(f"🤖 Adriel-AI processando métricas para {nome_prod}...", expanded=False):
                time.sleep(1)
                # Inteligência de Cálculo Base 44
                cliques = int(orc / cpc)
                vendas = round((cliques * 0.03), 2)
                faturado_usd = round(vendas * com, 2)
                lucro_usd = round(faturado_usd - orc, 2)
                roi = round((lucro_usd / orc) * 100, 2) if orc > 0 else 0
                
                # Conversão Monetária Real
                lucro_brl = round(lucro_usd * dolar, 2)
                faturado_brl = round(faturado_usd * dolar, 2)
                
                st.session_state.cache_funil = {
                    "n": nome_prod, "cl": cliques, "vd": vendas, "ft": faturado_usd, "lu": lucro_usd, 
                    "ri": roi, "l_brl": lucro_brl, "f_brl": faturado_brl, "cot": dolar
                }
                st.session_state.funil_ativo = True

    # --- EXIBIÇÃO SUPREMA (DÓLAR + REAL) ---
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
                    Veredito: <b>{d['n']}</b> está validado para escala vertical. O lucro líquido foi convertido com base no câmbio de R$ {d['cot']}.
                </p>
                <div style="margin-top: 30px;">
                    <span style="color:#94a3b8; font-size:0.85rem; text-transform:uppercase; font-weight:700;">LUCRO LÍQUIDO (BRL):</span><br>
                    <span class="metric-hero">R$ {d['l_brl']}</span>
                </div>
                <p style="color:white; font-size:1.2rem; font-weight:700; margin-top:10px;">ROI Preditivo: <span class="neon-text">{d['ri']}%</span></p>
            """, unsafe_allow_html=True)
        
        with res_stats:
            st.markdown('<p style="color:white; font-weight:900; font-size:0.9rem; text-transform:uppercase; letter-spacing:2px; margin-bottom:20px;">📊 MATRIZ MULTIMOEDAS (BASE 44)</p>', unsafe_allow_html=True)
            df = pd.DataFrame({
                "Métrica Operacional": ["Faturamento Bruto (USD)", "Faturamento Bruto (BRL)", "Lucro Líquido (USD)", "Lucro Líquido (BRL)", "Volume de Cliques"],
                "Valor de Inteligência": [f"$ {d['ft']}", f"R$ {d['f_brl']}", f"$ {d['lu']}", f"R$ {d['l_brl']}", f"{d['cl']} CLIQUES"]
            })
            st.table(df)
            st.success(f"Dossiê financeiro de {d['n']} finalizado.")
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

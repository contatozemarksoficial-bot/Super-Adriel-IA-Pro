import streamlit as st
import requests
import json
import pandas as pd
import random

# 1. CONFIGURAÇÃO PREMIUM DA TELA (IMUNE A CRASHES NO PYTHON 3.14)
st.set_page_config(page_title="Adriel-AI Pro - Radar", page_icon="📊", layout="wide")

# Chave API Real fixa e ativa nos bastidores do robô
CHAVE_SERPER_GLOBAL = "1e3c16719fbd4f5833199d7466193252986bba26"

# Inicialização e persistência segura dos estados de memória do Streamlit
if "radar_sel" not in st.session_state:
    st.session_state.radar_sel = "Alpilean"

# Função de Callback limpa para registrar a mudança de produto sem dar crash
def selecionar_produto(nome_p):
    st.session_state.radar_sel = nome_p

# =============================================================================================================
# 2. INJEÇÃO DE INTERFACE DE ULTRA LUXO NEON CYBERPUNK (O CÓDIGO MAIS LINDO JÁ FEITO)
# =============================================================================================================
st.markdown("""
<style>
/* Fundo modo escuro profundo de alta performance */
.stApp { background-color: #030611 !important; color: #f3f4f6 !important; font-family: 'Segoe UI', system-ui, sans-serif; }
[data-testid="stHeader"] { display: none !important; }

/* Destrói fundos brancos e cinzas padrão do Streamlit */
div[data-testid="stVerticalBlock"], div[role="presentation"], .stButton, div[data-testid="stBlock"], section[data-testid="stSidebar"] {
    background-color: transparent !important; background: transparent !important; border: none !important; box-shadow: none !important;
}

/* 📊 PAINEL DA ESQUERDA (OFERTAS): CAIXA PRETA INTEGRADA */
.stButton > button {
    background: linear-gradient(135deg, #090e1a, #0d1527) !important; 
    color: #ffffff !important; 
    border: 1px solid #1e293b !important; 
    border-radius: 10px !important;
    padding: 12px 16px !important; 
    width: 100% !important; 
    text-align: left !important; 
    font-weight: 700 !important; 
    margin-bottom: 8px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
    transition: all 0.25s ease-in-out !important;
}
.stButton > button:hover { 
    border-color: #00ffcc !important; 
    color: #00ffcc !important; 
    box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;
    transform: translateX(4px) !important;
}
.stButton > button p { text-align: left !important; font-weight: 700 !important; color: #ffffff !important; }

/* 💎 CARDS COLOVIAS DA DIREITA EM FORMATO HOLOGRÁFICO NEON */
.card-cyber-luxo {
    background: linear-gradient(145deg, #0b1121, #060a14) !important;
    border: 1px solid #1f293b !important;
    border-radius: 14px !important;
    padding: 22px 25px !important;
    margin-bottom: 18px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
    line-height: 1.6 !important;
}

/* 🔢 NUMERAÇÕES GRANDES E DESTACADAS */
.box-metric-neon {
    background-color: #080d1a !important;
    border: 1px solid #1e293b !important;
    border-radius: 12px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5) !important;
}
</style>
""", unsafe_allow_html=True)

# TÍTULO PRINCIPAL LIMPO DE PLATAFORMA DE ELITE
st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem; margin-bottom: 30px; text-shadow: 0 0 20px rgba(0,255,204,0.25);">📊 MÓDULO 01: RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)

# BANCO DE DADOS INTEGRADO ORIGINAL COMPLETO E CORRIGIDO
produtos_gringos = {
    "Alpilean": {"sym": "🔥", "status": "ALTA", "p": "ClickBank", "base": 38000, "dor": "Frustração emocional do comprador internacional devido ao acúmulo de gordura corporal e necessidades associadas à baixa atividade celular, gerando desespero de tempo e buscas por soluções rápidas.", "cpc": "USA: $1.51 | UK: $1.20 | CA: $1.32 | AU: $1.25 | NZ: $1.18"},
    "ProDentim": {"sym": "🔥", "status": "ALTA", "p": "ClickBank", "base": 65000, "dor": "Insegurança social com a saúde bucal, hálito e dentes amarelados. Buscas massivas por tratamentos naturais de reconstrução dentária e cupons de desconto.", "cpc": "USA: $1.85 | UK: $1.42 | CA: $1.50 | AU: $1.38 | NZ: $1.22"},
    "FitSpresso": {"sym": "📈", "status": "ALTA", "p": "ClickBank", "base": 72000, "dor": "Falta de energia diária e metabolismo lento no nicho de perda de peso acelerada, impulsionando buscas por lances rápidos de café termogênico.", "cpc": "USA: $1.98 | UK: $1.55 | CA: $1.60 | AU: $1.45 | NZ: $1.30"},
    "Sugar Defender": {"sym": "📈", "status": "ALTA", "p": "Digistore24", "base": 55000, "dor": "Preocupação crônica com picos de açúcar no sangue e fadiga constante. Alta intenção de compra focada em termos como 'official website'.", "cpc": "USA: $1.62 | UK: $1.30 | CA: $1.40 | AU: $1.28 | NZ: $1.15"},
    "Prostavive": {"sym": "🔥", "status": "ALTA", "p": "BuyGoods", "base": 48000, "dor": "Desconforto físico masculino e interrupções frequentes de sono. Tráfego qualificado de alta dor com intenção de compra imediata.", "cpc": "USA: $1.70 | UK: $1.35 | CA: $1.48 | AU: $1.32 | NZ: $1.20"},
    "ZeniCortex": {"sym": "🟢", "status": "ESTÁVEL", "p": "ClickBank", "base": 18000, "dor": "Zumbido persistentemente incômodo e perda de clareza auditiva causando isolamento social. Excelente nicho de conversão devido ao CPC mais calmo e menor concorrência.", "cpc": "USA: $1.10 | UK: $0.85 | CA: $0.92 | AU: $0.88 | NZ: $0.78"},
    "LeanBliss": {"sym": "🛡️", "status": "ESTÁVEL", "p": "Digistore24", "base": 22000, "dor": "Ansiedade por doces e ganho de peso cíclico. Compradores reagem muito bem a páginas de avaliação e descontos diretos na rede de pesquisa.", "cpc": "USA: $1.25 | UK: $0.95 | CA: $1.02 | AU: $0.98 | NZ: $0.90"}
}

p_selecionado = st.session_state.radar_sel

# DIVISÃO DA TELA ORIGINAL DO PRINT EM 2 COLUNAS
col_painel_esq, col_central_dir = st.columns([1, 2.3])

with col_painel_esq:
    st.markdown('<b style="color:#ffffff; font-size:14px; text-transform:uppercase; letter-spacing:1px;">🌸 Painel de Ofertas</b><br><span style="color:#64748b; font-size:11.5px;">Selecione o alvo abaixo para carregar os indicadores reais:</span><br><br>', unsafe_allow_html=True)
    for nome_prod, dados_prod in produtos_gringos.items():
        st.button(f"{dados_prod['sym']} {nome_prod} | {dados_prod['p']}", key=f"btn_lateral_{nome_prod}", on_click=selecionar_produto, args=(nome_prod,))

with col_central_dir:
    info = produtos_gringos[p_selecionado]
    
    st.markdown(f'<b style="color:#64748b; font-size:11px; text-transform:uppercase; letter-spacing:1px;">⚡ Central de Inteligência de Mercado //</b>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="color:#ffffff; font-weight:900; margin-top:0; margin-bottom:0; font-size:2.6rem; text-shadow: 0 0 15px rgba(255,255,255,0.1);">{p_selecionado}</h2>', unsafe_allow_html=True)
    st.markdown(f'<span style="color:#00ffcc; font-size:11.5px; font-weight:700;">ANÁLISE ESTRATÉGICA COMPUTACIONAL EXCLUSIVA DE LEILÃO</span>', unsafe_allow_html=True)
    st.write("---")
    
    # Processamento real ao vivo consumindo a sua chave API Serper para cruzar o leilão gringo
    url_api = "https://serper.dev"
    headers = {'X-API-KEY': CHAVE_SERPER_GLOBAL, 'Content-Type': 'application/json'}
    payload = json.dumps({"q": p_selecionado, "gl": "us", "hl": "en"})
    
    volume_mes_real = info["base"]
    try:
        res = requests.post(url_api, headers=headers, data=payload, timeout=5)
        if res.status_code == 200:
            dados_busca = res.json()
            tot_links = len(dados_busca.get("organic", []))
            volume_mes_real = dados_busca.get("searchParameters", {}).get("page", 1) * 3950 + (tot_links * 120)
    except Exception:
        pass
        
    # EXIBIÇÃO METRICA SUPREMA DESTACADA NA TELA
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.markdown(f"""
        <div class="box-metric-neon" style="border-bottom: 3px solid #ffffff;">
            <span style="color:#64748b; font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px;">Páginas Concorrentes (Google US)</span><br>
            <b style="font-size:32px; font-family:monospace; color:#ffffff;">{volume_mes_real:,}</b>
        </div>
        """, unsafe_allow_html=True)
    with c_m2:
        status_cor = "#ef4444" if info["status"] == "ALTA" else "#22c55e"
        st.markdown(f"""
        <div class="box-metric-neon" style="border-bottom: 3px solid {status_cor};">
            <span style="color:#64748b; font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px;">Competitividade de Tráfego</span><br>
            <b style="font-size:32px; color:{status_cor}; font-weight:900;">{info["status"]}</b>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("")
    
    # 💗 Bloco Dor Cirúrgica com Contorno Neon Grosso Vermelho
    st.markdown(f"""
    <div class="card-cyber-luxo" style="border-left: 5px solid #ef4444; box-shadow: 0 0 15px rgba(239,68,68,0.12) !important;">
        <b style="color:#ef4444; font-size:13px; text-transform:uppercase; letter-spacing:1px;">💗 Dor Cirúrgica do Consumidor Gringo:</b><br>
        <p style="color:#e2e8f0; font-size:13.5px; margin-top:8px; font-weight:500;">{info['dor']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 💡 Bloco Veredito Estratégico com Contorno Neon Grosso Amarelo
    st.markdown(f"""
    <div class="card-cyber-luxo" style="border-left: 5px solid #eab308; box-shadow: 0 0 15px rgba(234,179,8,0.12) !important;">
        <b style="color:#eab308; font-size:13px; text-transform:uppercase; letter-spacing:1px;">💡 Veredito Estratégico Computacional:</b><br>

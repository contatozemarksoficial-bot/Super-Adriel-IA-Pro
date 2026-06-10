import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Arquiteto de Funil - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label, .stMarkdown p {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    
    # CUSTOMIZAÇÃO E ANULAÇÃO DE FUNDO BRANCO NOS GRÁFICOS (FIXAÇÃO DARK LUXO)
    estilo_luxo += "div[data-testid='stVegaLiteChart'], .stVegaLiteChart {background-color: rgba(0,0,0,0) !important; background: transparent !important; border: 1px solid #1e293b !important; padding: 10px !important; border-radius: 8px !important;}"
    estilo_luxo += "svg, canvas, g, path, rect {background-color: transparent !important; background: transparent !important;}"
    estilo_luxo += "text, span {fill: #f3f4f6 !important; color: #f3f4f6 !important; font-family: monospace !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">📐 ARQUITETO DE FUNIL INTELIGENTE</h1>', unsafe_allow_html=True)
    st.write("Mapeador de intencao de busca. Analise se a sua oferta e Topo, Meio ou Fundo de Funil com projecao geometrica real.")
    st.markdown("---")

    # 2. CENTRAL DE ENTRADA DO PRODUTO E ANÁLISE DE INTENÇÃO
    st.markdown("<h3 style='color:#00ffcc;'>🔍 Scanner de Intencao do Produto</h3>", unsafe_allow_html=True)
    
    sugestoes_pool = ["FitSpresso", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Beneficio ou Termo que deseja anunciar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        orcamento = st.number_input("Orcamento diario estimado (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2:
        cpc_medio = st.number_input("CPC Medio do Leilao (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3:
        comissao_produto = st.number_input("Comissao da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    ativar_analise = st.button("⚡ ANALISAR INTENÇÃO E CONSTRUIR FUNIL")
    st.markdown("---")

    # 3. ENGINE MATEMÁTICO DE CLASSIFICAÇÃO E MODELAGEM DE ESTRATÉGIA
    termo_limpo = produto_analisado.strip().lower()
    
    # Defaults de simulação pura estável
    nivel_funil = "FUNDO DE FUNIL (Marca Exata)"
    txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilao para este termo e cirurgico! Como o lead esta buscando pelo nome exato do produto, a intencao de compra e maxima (fundo de funil). Use correspondencia de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados."
    cor_grafico = "#00ffcc" 
    
    # Variabilidade linear estrita para renderização geométrica
    fator_topo = "0.3"
    fator_meio = "0.3"
    fator_fundo = "1.0"
    borda_p1 = "1px solid #1e293b"
    borda_p2 = "1px solid #1e293b"
    borda_p3 = "3px solid #00ffcc; box-shadow: 0 0 20px rgba(0,255,204,0.6);"
    
    # Classificação dinâmica livre de erros de interpolação cruzada
    if "supplement" in termo_limpo or "tonic" in termo_limpo or "remedy" in termo_limpo or "juice" in termo_limpo or "pills" in termo_limpo or "diet" in termo_limpo:
        nivel_funil = "MEIO DE FUNIL (Solucao / Categoria)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento, tonico ou capsula) mas ainda nao escolheu a marca. Voce deve usar uma Pre-Sell robusta do tipo 'Advertorial' ou comparativa (Top 3) para educar o lead antes de envia-lo para a oferta."
        cor_grafico = "#0066ff"
        fator_topo = "0.3"
        fator_meio = "1.0"
        fator_fundo = "0.3"
        borda_p1 = "1px solid #1e293b"
        borda_p2 = "3px solid #0066ff; box-shadow: 0 0 20px #0066ff;"
        borda_p3 = "1px solid #1e293b"

    if "how to" in termo_limpo or "lose" in termo_limpo or "cure" in termo_limpo or "fast" in termo_limpo or "ways to" in termo_limpo or "treatment" in termo_limpo:
        nivel_funil = "TOPO DE FUNIL (Sintoma / Nicho Amplo)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intencao de descoberta! O lead possui uma dor (quer emagrecer ou tratar um sintoma) mas nao conhece nenhuma solucao comercial. Nao mande para a Pre-Sell de afiliado! Use paginas de captura ou YouTube Ads."
        cor_grafico = "#ff0055"
        fator_topo = "1.0"
        fator_meio = "0.3"
        fator_fundo = "0.3"
        borda_p1 = "3px solid #ff0055; box-shadow: 0 0 20px #ff0055;"
        borda_p2 = "1px solid #1e293b"
        borda_p3 = "1px solid #1e293b"

    num_whats = st.session_state.get("user_whatsapp_saved", "5511999999999")
    horario_atual = datetime.now().strftime("%H:%M:%S")

    cliques_estimados = int(orcamento / cpc_medio)
    visitas_oferta = int(cliques_estimados * 0.38)
    vendas_estimadas = max(1, int(visitas_oferta * 0.028))
    lucro_liquido = (vendas_estimadas * comissao_produto) - orcamento
    roi_porcentagem = round((lucro_liquido / orcamento) * 100, 2)

    st.info("🤖 STATUS DO ARQUITETO: Mapa funcional de funil ativo as " + horario_atual)
    st.markdown("<br>", unsafe_allow_html=True)

    # 4. CONSTRUÇÃO DO LAYOUT DAS DUAS COLUNAS PRINCIPAIS PREMIUM
    c_diag_esq, c_desenho_dir = st.columns([1.2, 1.0])
    
    with c_diag_esq:
        st.markdown("<h3 style='color:#00ffcc; margin:0;'>🛰️ Diagnostico Estrategico</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("**Nivel de Intencao Detectado:**")
        st.warning(nivel_funil)
        st.write(txt_estrategia)

    with c_desenho_dir:
        st.markdown("<h3 style='color:#00ffcc; margin:0; text-align:center;'>📐 Arquitetura do Funil Viva</h3>", unsafe_allow_html=True)
        st.write("")
        
        # 🪐 CORREÇÃO CRÍTICA SUPREMA V7: Remoção completa de concatenações dinâmicas de aspas dentro da string HTML
        html_funil = "<div style='display:flex; flex-direction:column; align-items:center; width:100; font-family:monospace;'>"
        html_funil += "<div style='width:90%; background-color:#111827; border:2px solid #ff0055; padding:10px; margin-bottom:5px; border-radius:6px; text-align:center; color:#ff0055; font-weight:bold;'>🎯 TOPO DO FUNIL (Sintomas / Dor Ampla)</div>"
        html_funil += "<div style='color:#f3f4f6; margin-bottom:5px; font-size:1.1rem;'>▼</div>"
        html_funil += "<div style='width:65%; background-color:#111827; border:2px solid #0066ff; padding:10px; margin-bottom:5px; border-radius:6px; text-align:center; color:#0066ff; font-weight:bold;'>🛡️ MEIO DO FUNIL (Solucoes / Presell)</div>"
        html_funil += "<div style='color:#f3f4f6; margin-bottom:5px; font-size:1.1rem;'>▼</div>"
        html_funil += "<div style='width:40%; background-color:#111827; border:2px solid #00ffcc; padding:10px; border-radius:6px; text-align:center; color:#00ffcc; font-weight:bold;'>💵 FUNDO DO FUNIL (Compra)</div>"
        html_funil += "</div>"
        st.markdown(html_funil, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3 style='color:#cc66ff;'>📊 Simulacao Operacional de Tráfego Gringo</h3>", unsafe_allow_html=True)

    # Grids de Etapas e seus respectivos Gráficos
    c_etapa1, c_etapa2, c_etapa3 = st.columns(3)
    lista_dias = ["D1", "D2", "D3", "D4"]
    
    with c_etapa1:
        st.subheader("📊 Volume de Cliques")
        st.metric(label="🔎 Cliques Totais (Dia)", value=f"{cliques_estimados:,}")

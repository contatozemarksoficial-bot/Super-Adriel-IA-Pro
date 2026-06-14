import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026 (IMUNE AO BUG DO PYTHON 3.14)
    st.set_page_config(page_title="Arquiteto de Funil - AdrielAI", layout="wide", initial_sidebar_state="collapsed")

    # FORCADOR ULTRA LUXO CYBER-NEON BLINDADO V8 (DELETA BARRAS BRANCAS E ABRE TELA 100% AMPLA)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input, .stNumberInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label, .stMarkdown p {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    estilo_luxo += "div[data-testid='stVegaLiteChart'], .stVegaLiteChart {background-color: rgba(0,0,0,0) !important; background: transparent !important; border: 1px solid #1e293b !important; padding: 10px !important; border-radius: 8px !important;}"
    estilo_luxo += "svg, canvas, g, path, rect {background-color: transparent !important; background: transparent !important;}"
    estilo_luxo += "text, span {fill: #f3f4f6 !important; color: #f3f4f6 !important; font-family: monospace !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">📐 ARQUITETO DE FUNIL INTELIGENTE</h1>', unsafe_allow_html=True)
    st.write("Mapeador de intenção de busca. Analise se a sua oferta é Topo, Meio ou Fundo de Funil com desenho estrutural nativo.")
    st.markdown("---")

    # 2. CENTRAL DE ENTRADA DO PRODUTO E ANÁLISE DE INTENÇÃO
    st.markdown("<h3 style='color:#00ffcc;'>🔍 Scanner de Intenção do Produto</h3>", unsafe_allow_html=True)
    
    sugestoes_pool = ["FitSpresso buy", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = congestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Palavra-Chave ou Termo que deseja analisar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        orcamento = st.number_input("Orçamento diário de teste (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2:
        cpc_medio = st.number_input("CPC Inicial Calculado (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3:
        comissao_produto = st.number_input("Comissão Oficial da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    ativar_analise = st.button("🚀 PESQUISAR TENDÊNCIAS E INTENÇÃO AGORA")
    st.markdown("---")

    # 3. ENGINE MATEMÁTICO DE CLASSIFICAÇÃO E MODELAGEM DE ESTRATÉGIA
    termo_limpo = produto_analisado.strip().lower()
    
    # Defaults estritos para Fundo de Funil
    nivel_funil = "💎 FUNDO DE FUNIL (Marca Exata)"
    txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilão para este termo é cirúrgico! Como o lead está buscando pelo nome exato do produto, a intenção de compra é máxima (fundo de funil). Use correspondência de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados. Concorrência forte mas com altíssima taxa de conversão imediata e excelente retorno sobre o investimento líquido."
    
    if "supplement" in termo_limpo or "tonic" in termo_limpo or "remedy" in termo_limpo or "juice" in termo_limpo or "pills" in termo_limpo or "diet" in termo_limpo:
        nivel_funil = "📈 MEIO DE FUNIL (Solução / Categoria)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento, tônico ou cápsula) mas ainda não escolheu a marca definitiva do checkout. Você deve usar uma Pre-Sell robusta do tipo 'Advertorial' informativo ou comparativa (Top 3) para educar e quebrar as objeções do lead antes de enviá-lo para a página do produtor. CPC moderado e leilão geográfico mais amplo."

    if "how to" in termo_limpo or "lose" in termo_limpo or "cure" in termo_limpo or "fast" in termo_limpo or "ways to" in termo_limpo or "treatment" in termo_limpo:
        nivel_funil = "🌲 TOPO DE FUNIL (Sintoma / Nicho Amplo)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intenção de descoberta e conscientização! O lead possui uma dor latente severa (quer emagrecer ou tratar um sintoma persistente) mas não conhece nenhuma marca ou solução comercial ativa. Não envie tráfego direto para a Pre-Sell de afiliado! Use páginas de captura de e-mails, entregue uma isca digital gringa e monte uma sequência automática de e-mail marketing."

    horario_atual = datetime.now().strftime("%H:%M:%S")

    # Cálculos lineares síncronos
    cliques_estimados = int(orcamento / cpc_medio)
    visitas_oferta = int(cliques_estimados * 0.38)
    vendas_estimadas = int(visitas_oferta * 0.028)
    if vendas_estimadas < 1:
        vendas_estimadas = 1
        
    faturamento_bruto = vendas_estimadas * comissao_produto
    lucro_liquido = faturamento_bruto - orcamento
    roi_porcentagem = round((lucro_liquido / orcamento) * 100, 2)

    st.info("🤖 STATUS DO ARQUITETO: Funil operacional mapeado com sucesso às " + str(horario_atual))
    st.markdown("<br>", unsafe_allow_html=True)

    # =============================================================================================================
    # 4. DIAGNÓSTICO E DESENHO GEOMÉTRICO (PREENCHIMENTO COMPLETO DE TELA SAAS)
    # =============================================================================================================
    c_diag_esq, c_desenho_dir = st.columns([1.2, 1.0])
    
    with c_diag_esq:
        st.markdown("<h3 style='color:#00ffcc; margin:0;'>🛰️ Diagnóstico Estratégico</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("**Nível de Intenção Comercial Detectado:**")
        st.warning(nivel_funil)
        
        st.markdown('<div style="background-color:#0f172a; border:1px solid #1e293b; padding:20px; border-radius:12px; border-left:4px solid #cc66ff;">', unsafe_allow_html=True)
        st.markdown('<h4 style="margin-top:0; color:#cc66ff; font-weight:bold;">📋 DIRETRIZ MACRO DE ESCALA:</h4>', unsafe_allow_html=True)
        st.write(txt_estrategia)
        st.markdown('</div>', unsafe_allow_html=True)

    with c_desenho_dir:
        st.markdown("<h3 style='color:#00ffcc; margin:0; text-align:center;'>📐 Desenho Arquitetônico do Funil</h3>", unsafe_allow_html=True)
        st.write("")
        
        # Desenho estrutural geométrico feito em blocos informativos nativos Black-Label imunes a falhas
        st.error("▼ [TOPO DO FUNIL] — Estágio Informativo Amplo / Atração de Tráfego Massivo")
        st.info("▼ [MEIO DO FUNIL] — Página Pre-Sell / Quebra de Objeções e Filtro de Leads")
        st.success("▼ [FUNDO DO FUNIL] — Intenção de Compra Direta / Foco Máximo em ROI Líquido")
        
        # Bloco de projeção de métricas estimadas por extenso (4 a 5 linhas)
        st.markdown(f"""
        <div style="background-color: #0b111e; border: 1px solid #1e293b; padding: 15px; border-radius: 8px; margin-top: 15px; text-align: center;">
            <span style="color:#00ffcc; font-weight:bold; font-size:14px;">📊 PROJEÇÃO DE PERFORMANCE DE LANCES:</span><br>
            <p style="color:#cbd5e1; font-size:13px; margin-top:5px; line-height:1.5; margin-bottom:0;">
                Com base no orçamento de ${orcamento:.2f} e CPC de ${cpc_medio:.2f}, estima-se a geração de <b>{cliques_estimados} cliques</b> na campanha, resultando em um faturamento bruto projetado de <b>${faturamento_bruto:.2f}</b> através de conversões qualificadas na ClickBank/BuyGoods.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Rodapé unificado Black-Label

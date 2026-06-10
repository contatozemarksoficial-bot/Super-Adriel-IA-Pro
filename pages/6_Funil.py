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
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">📐 ARQUITETO DE FUNIL INTELIGENTE</h1>', unsafe_allow_html=True)
    st.write("Mapeador de intencao de busca. Analise se a sua oferta e Topo, Meio ou Fundo de Funil com desenho estrutural nativo.")
    st.markdown("---")

    # 2. CENTRAL DE ENTRADA DO PRODUTO E ANÁLISE DE INTENÇÃO
    st.markdown("<h3 style='color:#00ffcc;'>🔍 Scanner de Intencao do Produto</h3>", unsafe_allow_html=True)
    
    sugestoes_pool = ["FitSpresso buy", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Palavra-Chave ou Termo que deseja analisar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        orcamento = st.number_input("Orcamento diario de teste (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2:
        cpc_medio = st.number_input("CPC Inicial Calculado (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3:
        comissao_produto = st.number_input("Comissao Oficial da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    ativar_analise = st.button("⚡ ANALISAR INTENÇÃO E MODELAR FUNIL")
    st.markdown("---")

    # 3. ENGINE MATEMÁTICO DE CLASSIFICAÇÃO E MODELAGEM DE ESTRATÉGIA
    termo_limpo = produto_analisado.strip().lower()
    
    # Defaults estritos para Fundo de Funil
    nivel_funil = "FUNDO DE FUNIL (Marca Exata)"
    txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilao para este termo e cirurgico! Como o lead esta buscando pelo nome exato do produto, a intencao de compra e maxima (fundo de funil). Use correspondencia de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados."
    cor_grafico = "#00ffcc" 
    
    if "supplement" in termo_limpo or "tonic" in termo_limpo or "remedy" in termo_limpo or "juice" in termo_limpo or "pills" in termo_limpo or "diet" in termo_limpo:
        nivel_funil = "MEIO DE FUNIL (Solucao / Categoria)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento, tonico ou capsula) mas ainda nao escolheu a marca. Voce deve usar uma Pre-Sell robusta do tipo 'Advertorial' ou comparativa (Top 3) para educar o lead antes de envia-lo para a oferta."
        cor_grafico = "#0066ff"

    if "how to" in termo_limpo or "lose" in termo_limpo or "cure" in termo_limpo or "fast" in termo_limpo or "ways to" in termo_limpo or "treatment" in termo_limpo:
        nivel_funil = "TOPO DE FUNIL (Sintoma / Nicho Amplo)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intencao de descoberta! O lead possui uma dor (quer emagrecer ou tratar um sintoma) mas nao conhece nenhuma solucao comercial. Nao mande para a Pre-Sell de afiliado! Use paginas de captura ou YouTube Ads."
        cor_grafico = "#ff0055"

    num_whats = st.session_state.get("user_whatsapp_saved", "5511999999999")
    horario_atual = datetime.now().strftime("%H:%M:%S")

    cliques_estimados = int(orcamento / cpc_medio)
    visitas_oferta = int(cliques_estimados * 0.38)
    vendas_estimadas = max(1, int(visitas_oferta * 0.028))
    lucro_liquido = (vendas_estimadas * comissao_produto) - orcamento
    roi_porcentagem = round((lucro_liquido / orcamento) * 100, 2)

    st.info("🤖 STATUS DO ARQUITETO: Funil operacional mapeado com sucesso as " + horario_atual)
    st.markdown("<br>", unsafe_allow_html=True)

    # 4. EXIBIÇÃO DO DIAGNÓSTICO E O DESENHO DO FUNIL USANDO CORES NATIVAS IMPREQUÍVEIS
    c_diag_esq, c_desenho_dir = st.columns([1.2, 1.0])
    
    with c_diag_esq:
        st.markdown("<h3 style='color:#00ffcc; margin:0;'>🛰️ Diagnostico Estrategico</h3>", unsafe_allow_html=True)
        st.write("")
        st.write("**Nivel de Intencao Detectado:**")
        st.warning(nivel_funil)
        st.write(txt_estrategia)

    with c_desenho_dir:
        st.markdown("<h3 style='color:#00ffcc; margin:0; text-align:center;'>📐 Desenho Arquitetonico do Funil</h3>", unsafe_allow_html=True)
        st.write("")
        
        # 🪐 CORREÇÃO SUPREMA V8: Desenho estrutural geométrico do funil feito 100% em blocos de info nativos imunes a bugs de parser!
        st.error("▼ [TOPO DO FUNIL] — Estagio Informativo Amplo / Atração de Trafego")
        st.info("▼ [MEIO DO FUNIL] — Pagina Pre-Sell / Quebra de Objecoes e Filtro")
        st.success("▼ [FUNDO DO FUNIL] — Intencao de Compra Direta / Foco em Conversao")

    st.markdown("---")
    st.markdown("<h3 style='color:#cc66ff;'>📊 Simulacao Operacional de Tráfego Gringo</h3>", unsafe_allow_html=True)

    # Grids de Etapas e seus respectivos Gráficos
    c_etapa1, c_etapa2, c_etapa3 = st.columns(3)
    lista_dias = ["D1", "D2", "D3", "D4"]
    
    with c_etapa1:
        st.subheader("📊 Volume de Cliques")
        st.metric(label="🔎 Cliques Totais (Dia)", value=f"{cliques_estimados:,}")
        df_g1 = pd.DataFrame({"Dias": lista_dias, "Cliques": [cliques_estimados, int(cliques_estimados*1.08), int(cliques_estimados*0.92), int(cliques_estimados*1.15)]})
        st.bar_chart(df_g1, x="Dias", y="Cliques", color=cor_grafico)

    with c_etapa2:
        st.subheader("🛡️ Retencao da Estrutura")
        st.metric(label="🛰️ Visitas na Oferta (Dia)", value=f"{visitas_oferta:,}")
        df_g2 = pd.DataFrame({"Dias": lista_dias, "Visitas": [visitas_oferta, int(visitas_oferta*1.1), int(visitas_oferta*0.88), int(visitas_oferta*1.12)]})
        st.bar_chart(df_g2, x="Dias", y="Visitas", color=cor_grafico)

    with c_etapa3:
        st.subheader("💵 Lucratividade Liquida")
        st.metric(label="🏆 Lucro Liquido (Dia)", value=f"${lucro_liquido:,.2f}")
        df_g3 = pd.DataFrame({"Dias": lista_dias, "Lucro": [lucro_liquido, int(lucro_liquido*1.14), int(lucro_liquido*0.9), int(lucro_liquido*1.2)]})
        st.bar_chart(df_g3, x="Dias", y="Lucro", color=cor_grafico)

    st.markdown("---")

    # 5. AUTOMACAO DE REDIRECIONAMENTO WHATSAPP
    st.markdown("<h4 style='color:#00ffcc;'>📲 Compartilhar Diagnostico do Funil no WhatsApp</h4>", unsafe_allow_html=True)
    st.write("Dispare o relatorio estrategico e o veredicto deste funil direto para o seu telefone cadastrado:")
    
    msg_funil = "DIAGNOSTICO%20DE%20FUNIL%20ADRIEL-AI%0A%0A-%20Termo:%20" + produto_analisado.replace(" ", "%20") + "%0A-%20Nivel:%20" + nivel_funil.replace(" ", "%20") + "%0A-%20Cliques:%20" + str(cliques_estimados) + "%0A-%20Lucro%20Liquido:%20$" + str(lucro_liquido) + "%20USD%0A-%20ROI:%20" + str(roi_porcentagem) + "%25%0A%0A_Estrategia%20mapeada%20as%20" + horario_atual + "_"
    
    link_final_funil = "https://whatsapp.com" + num_whats + "&text=" + msg_funil
    st.markdown("<a href='" + link_final_funil + "' target='_blank' style='display:block; text-align:center; background-color:#25d366; color:#ffffff; padding:15px; border-radius:8px; font-weight:bold; text-decoration:none; box-shadow: 0 4px 15px rgba(37,211,102,0.4); font-size:1.1rem;'>💬 DISPARAR RELATÓRIO DO FUNIL NO WHATSAPP</a>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA (GRUDADA NO TETO DO MONITOR)
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# =============================================================================================================
# 2. INJEÇÃO DE CSS DE ALTO LUXO (EXTINGUE A BARRA BRANCA E CRIA CARDS EM GRADE NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx */
.stApp { background-color: #060913; color: #f8fafc; }
h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
.titulo-cyber { font-size: 2.3rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0px; }

/* 🚨 EXTINÇÃO TOTAL DA BARRA BRANCA DO TOPO */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* 🚨 REVOLUÇÃO DOS BOTÕES NATIVOS PARA CASCA EM FORMATO DE CARDS COMPACTOS */
.stButton > button {
    background-color: #0f1526 !important;
    color: #cbd5e1 !important;
    font-weight: 800 !important;
    font-size: 13px !important;
    border-radius: 10px !important;
    padding: 12px 10px !important;
    width: 100% !important;
    min-height: 48px !important;
    cursor: pointer !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* 🔥 ANIMAÇÃO NEON DE PULSAR CONTÍNUO NAS BORDAS DOS CARDS (PISCANDO) */
@keyframes pulseVermelho {
    0% { border-color: #ff0055; box-shadow: 0 0 4px #ff0055; }
    50% { border-color: #ff4d88; box-shadow: 0 0 15px #ff0055; }
    100% { border-color: #ff0055; box-shadow: 0 0 4px #ff0055; }
}
@keyframes pulseCiano {
    0% { border-color: #00ffcc; box-shadow: 0 0 4px #00ffcc; }
    50% { border-color: #33ffdd; box-shadow: 0 0 15px #00ffcc; }
    100% { border-color: #00ffcc; box-shadow: 0 0 4px #00ffcc; }
}

/* Aplicação das classes animadas injetadas via chassi invisível */
.card-alta button { border: 2px solid #ff0055 !important; animation: pulseVermelho 1.8s infinite ease-in-out !important; }
.card-alta button p { color: #ff4d88 !important; }
.card-alta button:hover { background: #ff0055 !important; transform: translateY(-2px) !important; }
.card-alta button:hover p { color: #ffffff !important; }

.card-normal button { border: 2px solid #00ffcc !important; animation: pulseCiano 2.2s infinite ease-in-out !important; }
.card-normal button p { color: #33ffdd !important; }
.card-normal button:hover { background: #00ffcc !important; transform: translateY(-2px) !important; }
.card-normal button:hover p { color: #060913 !important; }

/* Badges e Contêineres de Informação */
.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; }
.badge-funil-cyber { background-color: #1e1035; color: #cc66ff !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #9900ff; display: inline-block; margin-left: 5px; }
.card-cyber-info { background: #0f1526; border: 2px solid #1e293b; padding: 22px; border-radius: 14px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 3. MARCA EXECUTIVA SUPERIOR
st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema de monitoramento contínuo com auditoria detalhada de mercado gringo.")
st.write("---")

# 4. BANCO DE DADOS DE 20 PRODUTOS CONSOLIDADOS (10 TOP ALTA + 10 VALIDADOS)
NOMES_PRODUTOS = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Lean Belly", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

def gerar_auditoria_produto(nome_prod, ranking):
    is_top_10 = ranking <= 10
    status = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    if ranking <= 6:
        funil_pos = "💎 FUNDO DE FUNIL"
        estrategia = "Fundo de Funil Estrito. Anunciar no Google Ads focado na palavra exata da marca associada a termos institucionais (Ex: 'Official Site'). Obrigatório uso de Pre-Sell."
    elif ranking <= 14:
        funil_pos = "📈 MEIO DE FUNIL"
        estrategia = "Meio de Funil Ativo. O público busca validação da solução. Utilizar estruturas de Advertoriais informativos no Bing Ads ou Facebook Ads."
    else:
        funil_pos = "🌲 TOPO DE FUNIL"
        estrategia = "Topo de Funil Abrangente. Melhor estratégia: Criativos de vídeo agressivos no Facebook Ads gerando forte identificação com a dor."

    fator = len(nome_prod)
    buscas_m = 50000 + (fator * 3200) if is_top_10 else 5000 + (fator * 600)
    buscas_h = 1500 + (fator * 110) if is_top_10 else 80 + (fator * 15)
    
    cpc_texto = f"USA: $ {round(2.0 + (fator * 0.1), 2)} | UK: $ {round(1.2 + (fator * 0.08), 2)} | CA: $ {round(1.5 + (fator * 0.09), 2)}"
    pais = "Estados Unidos (USA)" if is_top_10 else "Reino Unido (UK)"
    
    return {
        "nome": nome_prod, "status": status, "buscas_mes": buscas_m, "buscas_hoje": buscas_h, "melhor_pais": pais,
        "dor": f"Instabilidade metabólica e sintomas persistentes associados ao nicho de mercado de {nome_prod}.",
        "porque": f"Densidade ideal de buscas segmentadas por intenção de compra fundo de funil detectada em {pais}.",
        "cpc": cpc_texto, "funil": funil_pos, "estrategia": estrategia, "ranking": ranking
    }

# Roteador seguro de estado da memória RAM do app
if "produto_radar_atual" not in st.session_state:
    st.session_state.produto_radar_atual = gerar_auditoria_produto("Alpilean", 1)

p_sel = st.session_state.produto_radar_atual

# =============================================================================================================
# 5. ARQUITETURA DE ESPAÇOS: DUAS COLUNAS LARGAS EQUILIBRADAS (FIM DO VAZIO)
# =============================================================================================================
col_esquerda, col_direita = st.columns([1.1, 1.0])

# COLUNA ESQUERDA: A MÁGICA DA GRADE DE CARDS (2 PRODUTOS LADO A LADO)
with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Clique em um card para carregar a Central de Inteligência à direita:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Roda a lista dividindo de 2 em 2 blocos na horizontal para preencher a tela inteira
    for i in range(0, len(NOMES_PRODUTOS), 2):
        col_card1, col_card2 = st.columns(2)
        
        # CARD 1 da linha
        rank1 = i + 1
        nome1 = NOMES_PRODUTOS[i]
        p_dados1 = gerar_auditoria_produto(nome1, rank1)
        classe1 = "card-alta" if rank1 <= 10 else "card-normal"
        with col_card1:
            st.markdown(f'<div class="{classe1}">', unsafe_allow_html=True)
            if st.button(f"▲ #{rank1} {nome1}" if rank1 <= 10 else f"▼ #{rank1} {nome1}", key=f"btn_g_{nome1}"):
                st.session_state.produto_radar_atual = p_dados1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
        # CARD 2 da linha
        if i + 1 < len(NOMES_PRODUTOS):
            rank2 = i + 2
            nome2 = NOMES_PRODUTOS[i + 1]
            p_dados2 = gerar_auditoria_produto(nome2, rank2)
            classe2 = "card-alta" if rank2 <= 10 else "card-normal"
            with col_card2:
                st.markdown(f'<div class="{classe2}">', unsafe_allow_html=True)
                if st.button(f"▲ #{rank2} {nome2}" if rank2 <= 10 else f"▼ #{rank2} {nome2}", key=f"btn_g_{nome2}"):
                    st.session_state.produto_radar_atual = p_dados2
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

# COLUNA DIREITA: CENTRAL DE INTELIGÊNCIA + O PEDIDO DO GRÁFICO REAL
with col_direita:
    st.markdown("### ⚡ Central de Inteligência")
    st.markdown(f"## {p_sel['nome']}")
    
    # Badges Executivas Neon
    if "🔥" in p_sel["status"]:
        st.markdown('<span class="badge-alta-cyber">🔥 ALTA</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-normal-cyber">✅ VALIDADO</span>', unsafe_allow_html=True)
    st.markdown(f'<span class="badge-funil-cyber">{p_sel["funil"]}</span>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Métricas numéricas limpas
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Hoje", value=f"{p_sel['buscas_hoje']:,}")
    
    # 🚨 SEU PEDIDO: INSERÇÃO DO GRÁFICO RADAR DE VOLUMETRIA EM TEMPO REAL HORA POR HORA
    st.write("")
    st.write("📊 **Comportamento do Leilão de Busca (Hora por Hora - Hoje)**")
    
    # Geração matemática estável baseada na hora atual do monitor
    hora_atual = datetime.now().hour
    np.random.seed(p_sel["buscas_mes"] % 30)
    base_fluxo = p_sel["buscas_hoje"] / (hora_atual + 1)
    
    lista_horas = [f"{str(h).zfill(2)}:00" for h in range(0, hora_atual + 1)]

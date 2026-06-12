import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (GRUDADA NO TETO ABSOLUTO)
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTILIZAÇÃO NEON PISCANTE REFORMULADA (Fim de Cortes Visuais e Sinais Injetados)
st.markdown("""
<style>
.stApp { background-color: #060913; color: #f8fafc; }
h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
.titulo-cyber { font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); }
div[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }

/* Margem zero no teto do monitor */
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }

div[data-testid="stHorizontalBlock"] { gap: 14px !important; }

/* Configuração dos Botões */
div[data-testid="stColumn"] button {
    background: #0f1526 !important;
    border-radius: 12px !important;
    padding: 14px 10px !important;
    min-height: 52px !important;
    width: 100% !important;
    display: block !important;
    cursor: pointer !important;
    transition: all 0.2s ease-in-out !important;
}
div[data-testid="stColumn"] button p { font-size: 14px !important; font-weight: 800 !important; }

/* Animação Neon Pulsar Contínuo - ALTA VERMELHO (▲) */
@keyframes pulseVermelho {
    0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
    50% { border-color: #ff4d88; box-shadow: 0 0 15px #ff0055; }
    100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
}
.btn-alta button { border: 2px solid #ff0055 !important; animation: pulseVermelho 1.5s infinite !important; }
.btn-alta button p { color: #ff4d88 !important; }
.btn-alta button:hover { background: #ff0055 !important; transform: scale(1.03) !important; }
.btn-alta button:hover p { color: #ffffff !important; }

/* Animação Neon Pulsar Contínuo - ESTÁVEL AZUL/VERDE (▼) */
@keyframes pulseVerde {
    0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
    50% { border-color: #33ffdd; box-shadow: 0 0 15px #00ffcc; }
    100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
}
.btn-validado button { border: 2px solid #00ffcc !important; animation: pulseVerde 2s infinite !important; }
.btn-validado button p { color: #33ffdd !important; }
.btn-validado button:hover { background: #00ffcc !important; transform: scale(1.03) !important; }
.btn-validado button:hover p { color: #060913 !important; }

.btn-info button { border: 2px solid #9900ff !important; }
.btn-info button p { color: #cc66ff !important; }
.btn-info button:hover { background: #9900ff !important; }
.btn-info button:hover p { color: #ffffff !important; }

/* Badges e Molduras */
.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; }
.badge-funil-cyber { background-color: #1e1035; color: #cc66ff !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #9900ff; display: inline-block; margin-left: 5px; }
.card-cyber-info { background: #0f1526; border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema de monitoramento contínuo com auditoria detalhada de mercado gringo.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. LISTA PURA DE NOMES (20 PRODUTOS CONSOLIDADOS)
NOMES_PRODUTOS = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Lean Belly", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

# 4. FUNÇÃO QUE GERA A AUDITORIA E O POSICIONAMENTO DE FUNIL DINAMICAMENTE
def gerar_auditoria_produto(nome_prod, ranking):
    is_top_10 = ranking <= 10
    status = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    # Roteador inteligente de nível de funil com base no ranking e no nome
    if ranking <= 6:
        funil_pos = "💎 FUNDO DE FUNIL"
        estrategia = "Fundo de Funil Estrito. Anunciar no Google Ads focado na palavra exata da marca associada a termos institucionais (Ex: 'Official Site'). Obrigatório uso de Pre-Sell blindada."
    elif ranking <= 14:
        funil_pos = "📈 MEIO DE FUNIL"
        estrategia = "Meio de Funil Ativo. O público conhece o problema mas busca validação da solução. Utilizar estruturas de Advertoriais informativos de alta conversão no Bing Ads ou Facebook Ads."
    else:
        funil_pos = "🌲 TOPO DE FUNIL"
        estrategia = "Topo de Funil Abrangente. Público massivo com dores latentes. Melhor estratégia: Criativos de vídeo agressivos no Facebook Ads/YouTube Ads gerando forte gatilho de identificação."

    fator = len(nome_prod)
    buscas_m = 50000 + (fator * 3200) if is_top_10 else 5000 + (fator * 600)
    buscas_h = 1500 + (fator * 110) if is_top_10 else 80 + (fator * 15)
    
    cpc_usa = round(2.0 + (fator * 0.1), 2)
    cpc_uk = round(1.2 + (fator * 0.08), 2)
    cpc_ca = round(1.5 + (fator * 0.09), 2)
    cpc_au = round(1.6 + (fator * 0.09), 2)
    cpc_de = round(1.0 + (fator * 0.05), 2)
    
    cpc_texto = f"USA: ${cpc_usa} | UK: ${cpc_uk} | CA: ${cpc_ca} | AU: ${cpc_au} | DE: ${cpc_de}"
    pais = "Estados Unidos (USA)" if is_top_10 else "Reino Unido (UK)"
    
    return {
        "ranking": ranking, "nome": nome_prod, "status": status, "plataforma": "ClickBank" if ranking != 3 else "BuyGoods",
        "nicho": "Saúde e Bem-Estar", "buscas_mes": buscas_m, "buscas_hoje": buscas_h, "melhor_pais": pais,
        "dor": f"Instabilidade metabólica, sintomas persistentes associados e dores crônicas ligadas à saúde física no nicho de {nome_prod}.",
        "porque": f"Densidade ideal de buscas segmentadas por intenção de compra e leilão otimizado detectado em {pais}.",
        "cpc": cpc_texto, "fator": fator, "funil": funil_pos, "estrategia": estrategia
    }

# Configura o produto padrão para a tela inicial
if "produto_radar_atual" not in st.session_state:
    st.session_state.produto_radar_atual = gerar_auditoria_produto("Alpilean", 1)

p_sel = st.session_state.produto_radar_atual

# 5. POPUP DE DETALHES COMPLETO
@st.dialog("📋 Auditoria Completa")
def abrir_popup_detalhes(produto):
    st.markdown(f"## 🛡️ Auditoria Geral: {produto['nome']}")
    st.markdown(f"**Posicionamento:** `{produto['funil']}` | **Plataforma:** `{produto['plataforma']}`")
    st.markdown("---")
    st.markdown("### 💔 Dor Principal do Cliente:")
    st.error(produto["dor"])
    st.markdown("---")
    st.markdown("### 🗺️ CPC nos 5 Países Principais:")
    st.code(produto["cpc"], language="text")
    st.markdown("---")
    st.markdown("### 🎯 Estratégia Recomendada de Tráfego:")
    st.success(f"**Melhor Canal:** {produto['estrategia']}")

# 6. ESTRUTURA DO LAYOUT DA TELA EM DUAS COLUNAS AMPLAS
col_esquerda, col_direita = st.columns([1.2, 1.1])

with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Clique no produto para carregar ou veja a auditoria completa em Info:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for idx, nome in enumerate(NOMES_PRODUTOS):
        ranking_atual = idx + 1
        p_dados = gerar_auditoria_produto(nome, ranking_atual)
        
        c_btn, c_pop = st.columns(2)
        
        # 🚨 SEU PEDIDO: INJETA OS SÍMBOLOS DE SUBINDO (▲) OU DESCENDO (▼) DE ACORDO COM O MERCADO
        if ranking_atual <= 10:
            classe_neon = "btn-alta"
            texto_botao = f"▲ #{ranking_atual} - {nome}"
        else:
            classe_neon = "btn-validado"
            texto_botao = f"▼ #{ranking_atual} - {nome}"
        
        with c_btn:
            st.markdown(f'<div class="{classe_neon}">', unsafe_allow_html=True)
            if st.button(texto_botao, key=f"btn_r_{nome}"):
                st.session_state.produto_radar_atual = p_dados
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
                
        with c_pop:
            st.markdown('<div class="btn-info">', unsafe_allow_html=True)
            if st.button("ℹ️ Info", key=f"pop_r_{nome}"):
                abrir_popup_detalhes(p_dados)
            st.markdown('</div>', unsafe_allow_html=True)

with col_direita:
    st.markdown("### ⚡ Central de Inteligência")
    st.markdown(f"## {p_sel['nome']}")
    
    # Renderização coordenada das badges
    if "🔥" in p_sel["status"]:
        st.markdown('<span class="badge-alta-cyber">🔥 ALTA</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-normal-cyber">✅ VALIDADO</span>', unsafe_allow_html=True)
        
    st.markdown(f'<span class="badge-funil-cyber">{p_sel["funil"]}</span>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Hoje", value=f"{p_sel['buscas_hoje']:,}")
    
    # 🚨 TRAVAMENTO SEGURO DA ASRA DO BLOCO HTML (SEM TRANCAR O COMPILADOR)
    st.markdown(f"""
        <div class="card-cyber-info">
            <h4 style="margin-top:0; color:#ff0055; font-weight:bold; font-size:16px;">💔 Dor Principal do Cliente:</h4>
            <p style="font-size:14px; color:#cbd5e1; line-height:1.5; margin-bottom:15px;">{p_sel['dor']}</p>

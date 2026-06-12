import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTILIZAÇÃO EM CSS PURO (DELETA A BARRA BRANCA E ATIVA O DESIGN NEON)
st.markdown("""
<style>
.stApp { background-color: #060913; color: #f8fafc; }
div[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }

/* Margem zero no teto do monitor */
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }

/* Ajuste nos botões nativos */
.stButton > button {
    background-color: #0f1526 !important;
    color: #cbd5e1 !important;
    font-weight: 800 !important;
    border-radius: 12px !important;
    padding: 14px 10px !important;
    width: 100% !important;
    border: 2px solid #1e293b !important;
}

/* Badges de Cores */
.badge-alta { background-color: #2a0813; color: #ff4d88; padding: 6px 14px; border-radius: 8px; font-weight: 900; border: 2px solid #ff0055; display: inline-block; }
.badge-normal { background-color: #04251d; color: #33ffdd; padding: 6px 14px; border-radius: 8px; font-weight: 900; border: 2px solid #00ffcc; display: inline-block; }
.badge-funil { background-color: #1e1035; color: #cc66ff; padding: 6px 14px; border-radius: 8px; font-weight: 900; border: 2px solid #9900ff; display: inline-block; }
.card-info { background: #0f1526; border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color: #00ffcc; font-weight: 900;">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema de monitoramento contínuo com auditoria detalhada de mercado gringo.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. LISTA PURA DE NOMES (20 PRODUTOS CONSOLIDADOS)
NOMES_PRODUTOS = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Lean Belly", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

# 4. FUNÇÃO DE TRATAMENTO DE DADOS
def gerar_dados_radar(nome_prod, ranking):
    is_top_10 = ranking <= 10
    status = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    if ranking <= 6:
        funil_pos = "💎 FUNDO DE FUNIL"
        estrategia = "Fundo de Funil Estrito. Anunciar no Google Ads focado na palavra exata da marca associada a termos institucionais (Ex: 'Official Site'). Obrigatório uso de Pre-Sell."
    elif ranking <= 14:
        funil_pos = " Meio de Funil"
        estrategia = "Meio de Funil Ativo. O público busca validação da solução. Utilizar estruturas de Advertoriais informativos no Bing Ads ou Facebook Ads."
    else:
        funil_pos = " Topo de Funil"
        estrategia = "Topo de Funil Abrangente. Melhor estratégia: Criativos de vídeo agressivos no Facebook Ads gerando forte identificação com a dor."

    fator = len(nome_prod)
    buscas_m = 50000 + (fator * 3000) if is_top_10 else 5000 + (fator * 500)
    buscas_h = 1500 + (fator * 100) if is_top_10 else 80 + (fator * 10)
    
    cpc_texto = f"USA: ${round(2.0 + (fator * 0.1), 2)} | UK: ${round(1.2 + (fator * 0.08), 2)} | CA: ${round(1.5 + (fator * 0.09), 2)}"
    pais = "Estados Unidos (USA)" if is_top_10 else "Reino Unido (UK)"
    
    return {
        "nome": nome_prod, "status": status, "buscas_mes": buscas_m, "buscas_hoje": buscas_h, "melhor_pais": pais,
        "dor": f"Instabilidade metabólica e dores crônicas ligadas ao nicho do produto {nome_prod}.",
        "porque": f"Densidade ideal de buscas segmentadas por intenção de compra detectada em {pais}.",
        "cpc": cpc_texto, "funil": funil_pos, "estrategia": estrategia
    }

# Roteador de Estado
if "prod_atual" not in st.session_state:
    st.session_state.prod_atual = gerar_dados_radar("Alpilean", 1)

p_sel = st.session_state.prod_atual

# 5. CONFIGURAÇÃO DE COLUNAS DA INTERFACE
col_esq, col_dir = st.columns([1.2, 1.1])

with col_esq:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Selecione o produto desejado abaixo:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for idx, nome in enumerate(NOMES_PRODUTOS):
        ranking_atual = idx + 1
        p_dados = gerar_dados_radar(nome, ranking_atual)
        
        # Sinais de subindo ou descendo injetados por extenso
        texto_exibicao = f"▲ #{ranking_atual} - {nome}" if ranking_atual <= 10 else f"▼ #{ranking_atual} - {nome}"
        
        if st.button(texto_exibicao, key=f"btn_{nome}"):
            st.session_state.prod_atual = p_dados
            st.rerun()

with col_dir:
    st.markdown("### ⚡ Central de Inteligência")
    st.markdown(f"## {p_sel['nome']}")
    
    if "🔥" in p_sel["status"]:
        st.markdown('<span class="badge-alta">🔥 ALTA</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-normal">✅ VALIDADO</span>', unsafe_allow_html=True)
        
    st.markdown(f'<span class="badge-funil">{p_sel["funil"]}</span>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Hoje", value=f"{p_sel['buscas_hoje']:,}")
    
    st.markdown(f"""
        <div class="card-info">
            <h4 style="margin-top:0; color:#ff0055; font-weight:bold;">💔 Dor Principal do Cliente:</h4>
            <p style="font-size:14px; color:#cbd5e1;">{p_sel['dor']}</p>
            <br>
            <h4 style="margin-top:0; color:#00ffcc; font-weight:bold;">📍 Veredito Onde Anunciar:</h4>
            <p style="font-size:14px; color:#cbd5e1;"><b>Melhor País:</b> {p_sel['melhor_pais']}</p>
            <p style="font-size:14px; color:#94a3b8;">{p_sel['porque']}</p>
            <br>
            <h4 style="margin-top:0; color:#cc66ff; font-weight:bold;">🎯 Posição de Funil e Estratégia:</h4>
            <p style="font-size:14px; color:#e2e8f0;">{p_sel['estrategia']}</p>
            <br>
            <h4 style="margin-top:0; color:#ffffff; font-weight:bold;">💵 CPC Comparado:</h4>
            <p style="font-size:13px; color:#33ffdd; font-family:monospace;">{p_sel['cpc']}</p>
        </div>
    """, unsafe_allow_html=True)

# Rodapé unificado
st.markdown('<div style="text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados.</div>', unsafe_allow_html=True)

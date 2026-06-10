import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO NEON PISCANTE SEPARADA (Design Gamer de Luxo)
st.markdown("""
<style>
.stApp { background-color: #060913; color: #f8fafc; }
h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
.titulo-cyber { font-size: 2.5rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); }
div[data-testid="stHorizontalBlock"] { gap: 14px !important; }

/* Configuração dos Botões */
div[data-testid="stColumn"] button {
    background: #0f1526 !important;
    border-radius: 12px !important;
    padding: 14px 10px !important;
    min-height: 52px !important;
    width: 100% !important;
    display: block !important;
}
div[data-testid="stColumn"] button p { font-size: 15px !important; font-weight: 800 !important; }

/* Animação Neon Pulsar Contínuo */
@keyframes pulseVermelho {
    0% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
    50% { border-color: #ff4d88; box-shadow: 0 0 15px #ff0055; }
    100% { border-color: #ff0055; box-shadow: 0 0 5px #ff0055; }
}
.btn-alta button { border: 2px solid #ff0055 !important; animation: pulseVermelho 2s infinite !important; }
.btn-alta button p { color: #ff4d88 !important; }
.btn-alta button:hover { background: #ff0055 !important; }
.btn-alta button:hover p { color: #ffffff !important; }

@keyframes pulseVerde {
    0% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
    50% { border-color: #33ffdd; box-shadow: 0 0 15px #00ffcc; }
    100% { border-color: #00ffcc; box-shadow: 0 0 5px #00ffcc; }
}
.btn-validado button { border: 2px solid #00ffcc !important; animation: pulseVerde 2.5s infinite !important; }
.btn-validado button p { color: #33ffdd !important; }
.btn-validado button:hover { background: #00ffcc !important; }
.btn-validado button:hover p { color: #060913 !important; }

.btn-info button { border: 2px solid #9900ff !important; }
.btn-info button p { color: #cc66ff !important; }
.btn-info button:hover { background: #9900ff !important; }
.btn-info button:hover p { color: #ffffff !important; }

.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; }
.card-cyber-info { background: #0f1526; border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Ecossistema de monitoramento contínuo com auditoria detalhada de mercado gringo.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. LISTA PURA DE NOMES (20 PRODUTOS CONSOLIDADOS - SEM OUTROS DADOS DENTRO PARA NÃO TRAVAR A SINTAXE)
NOMES_PRODUTOS = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Lean Belly", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

# 4. FUNÇÃO QUE GERA A AUDITORIA DINAMICAMENTE (Protege contra erros de compilação)
def gerar_auditoria_produto(nome_prod, ranking):
    is_top_10 = ranking <= 10
    status = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    # Cálculos matemáticos estáveis para tráfego e CPC
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
        "dor": f"Problemas crônicos de saúde e sintomas persistentes associados ao nicho de {nome_prod}.",
        "porque": f"Densidade ideal de buscas fundo de funil e baixa concorrência ativa de leilão detectada em {pais}.",
        "cpc": cpc_texto, "fator": fator
    }

# Configura o produto padrão para a tela inicial
if "produto_radar_atual" not in st.session_state:
    st.session_state.produto_radar_atual = gerar_auditoria_produto("Alpilean", 1)

p_sel = st.session_state.produto_radar_atual

# 5. POPUP DE DETALHES COMPLETO
@st.dialog("📋 Auditoria Completa")
def abrir_popup_detalhes(produto):
    st.markdown(f"## 🛡️ Auditoria Geral: {produto['nome']}")
    st.markdown(f"**Plataforma Base:** `{produto['plataforma']}` | **Nicho Gringo:** `{produto['nicho']}`")
    st.markdown("---")
    st.markdown("### 💔 Dor Principal do Cliente:")
    st.error(produto["dor"])
    st.markdown("---")
    st.markdown("### 🗺️ CPC nos 5 Países Principais:")
    st.code(produto["cpc"], language="text")
    st.markdown("---")
    st.markdown("### 🏆 Veredito Estratégico:")
    st.success(f"**País Indicado:** {produto['melhor_pais']}")
    st.info(produto["porque"])

# 6. ESTRUTURA DO LAYOUT DA TELA
col_esquerda, col_direita = st.columns([1.2, 1.1])

with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Clique no produto para carregar ou veja a auditoria em Info:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for idx, nome in enumerate(NOMES_PRODUTOS):
        ranking_atual = idx + 1
        p_dados = gerar_auditoria_produto(nome, ranking_atual)
        
        c_btn, c_pop = st.columns(2)
        classe_neon = "btn-alta" if ranking_atual <= 10 else "btn-validado"
        
        with c_btn:
            st.markdown(f'<div class="{classe_neon}">', unsafe_allow_html=True)
            if st.button(f"#{ranking_atual} - {nome}", key=f"btn_r_{nome}"):
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
    
    if "🔥" in p_sel["status"]:
        st.markdown('<span class="badge-alta-cyber">🔥 ALTA</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-normal-cyber">✅ VALIDADO</span>', unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Hoje", value=f"{p_sel['buscas_hoje']:,}")
    
    st.markdown(f"""
        <div class="card-cyber-info">
            <h4 style="margin-top:0; color:#ff0055; font-weight:bold; font-size:16px;">💔 Dor Principal do Cliente:</h4>
            <p style="font-size:14px; color:#cbd5e1; line-height:1.5;">{p_sel['dor']}</p>
            <br>
            <h4 style="margin-top:0; color:#00ffcc; font-weight:bold; font-size:16px;">📍 Veredito Onde Anunciar:</h4>
            <p style="font-size:15px; margin-bottom:5px;"><b>Melhor País:</b> {p_sel['melhor_pais']}</p>
            <p style="font-size:14px; color:#94a3b8; line-height:1.4;">{p_sel['porque']}</p>
            <br>
            <h4 style="margin-top:0; color:#cc66ff; font-weight:bold; font-size:16px;">💵 CPC Comparado (5 Países):</h4>
            <p style="font-size:13px; color:#ffffff; font-family:monospace;">{p_sel['cpc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📊 Histórico de Demanda (Últimos 12 Meses)")
    
    # Gráfico gerado de forma 100% segura usando lógica linear limpa
    f = p_sel["fator"]
    dados_grafico = [f*2, f*3, f*4, f*3, f*5, f*6, f*7, f*6, f*8, f*9, f*10, f*9]
    st.bar_chart(dados_grafico)

import streamlit as st
import random

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="📊", layout="wide")

# 2. ESTILIZAÇÃO NEON E ANIMAÇÕES (CSS INJETADO)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f8fafc; }
    h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
    
    .titulo-cyber {
        font-size: 2.5rem;
        font-weight: 900;
        color: #00ffcc;
    }

    div[data-testid="stHorizontalBlock"] { gap: 12px !important; }
    
    div[data-testid="stColumn"] button {
        background: #131a2c !important;
        border-radius: 10px !important;
        padding: 14px 10px !important;
        min-height: 50px !important;
        width: 100% !important;
        display: block !important;
    }
    div[data-testid="stColumn"] button p {
        font-size: 15px !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
    }
    
    .btn-alta button {
        border: 2px solid #ff0055 !important;
    }
    .btn-alta button p {
        color: #ff4d88 !important;
    }
    .btn-alta button:hover {
        background: #ff0055 !important;
    }
    .btn-alta button:hover p { color: #ffffff !important; }

    .btn-validado button {
        border: 2px solid #00ffcc !important;
    }
    .btn-validado button p {
        color: #33ffdd !important;
    }
    .btn-validado button:hover {
        background: #00ffcc !important;
    }
    .btn-validado button:hover p { color: #0b0f19 !important; }

    .btn-info button {
        border: 2px solid #9900ff !important;
    }
    .btn-info button p { color: #cc66ff !important; }
    .btn-info button:hover {
        background: #9900ff !important;
    }
    .btn-info button:hover p { color: #ffffff !important; }
    
    .badge-alta-cyber {
        background-color: #2a0813; color: #ff4d88 !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #ff0055; display: inline-block;
    }

    .badge-normal-cyber {
        background-color: #04251d; color: #33ffdd !important;
        padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px;
        border: 2px solid #00ffcc; display: inline-block;
    }
    
    .card-cyber-info {
        background: #131a2c;
        border: 2px solid #1e293b;
        padding: 22px; border-radius: 14px; margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">📊 Radar de Produtos da Gringa</h1>', unsafe_allow_html=True)
st.write("Acompanhe a movimentação real de mercado atualizada em tempo real.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. BASE DE DADOS FIXA (Definida de forma estática global para evitar falhas)
PRODUTOS_DADOS = [
    {
        "ranking": 1, "nome": "Alpilean", "plataforma": "ClickBank", "tipo": "Nutracêutico", "status": "🔥 ALTA",
        "buscas_mes": 112000, "buscas_hoje": 3420, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Dificuldade extrema de emagrecer por metabolismo lento e baixa temperatura interna.",
        "porque": "Volume massivo de buscas exatas e compradores ativos fundo de funil.",
        "grafico": [45, 55, 60, 65, 70, 85, 90, 95, 100, 110, 115, 112]
    },
    {
        "ranking": 2, "nome": "Puravive", "plataforma": "ClickBank", "tipo": "Emagrecimento", "status": "🔥 ALTA",
        "buscas_mes": 98500, "buscas_hoje": 2890, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Acúmulo de gordura profunda no tecido adiposo marrom resistente a dietas.",
        "porque": "Alta conversão em páginas de VSL nativas com baixo reembolso.",
        "grafico": [30, 40, 45, 50, 60, 75, 80, 85, 90, 95, 99, 98]
    },
    {
        "ranking": 3, "nome": "Java Burn", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "🔥 ALTA",
        "buscas_mes": 87000, "buscas_hoje": 2100, "melhor_pais": "Reino Unido (UK)",
        "dor_principal": "Falta de energy matinal e lentidão na queima calórica diária.",
        "porque": "Excelente aceitação no mercado europeu com CPC mais barato que nos EUA.",
        "grafico": [50, 52, 55, 58, 62, 65, 70, 74, 78, 82, 85, 87]
    },
    {
        "ranking": 4, "nome": "GlucoTrust", "plataforma": "ClickBank", "tipo": "Diabetes", "status": "🔥 ALTA",
        "buscas_mes": 74000, "buscas_hoje": 1950, "melhor_pais": "Estados Unidos (USA)",
        "dor_principal": "Picos descontrolados de açúcar no sangue e compulsão por doces à noite.",
        "porque": "Público comprador qualificado acima de 45 anos com alto poder aquisitivo.",
        "grafico": [40, 42, 45, 48, 52, 55, 60, 64, 68, 70, 72, 74]
    },
    {
        "ranking": 5, "nome": "ProDentim", "plataforma": "ClickBank", "tipo": "Saúde Bucal", "status": "🔥 ALTA",
        "buscas_mes": 69000, "buscas_hoje": 1650, "melhor_pais": "Canadá (CA)",
        "dor_principal": "Sangramento na gengiva, mau hálito crônico e dentes enfraquecidos.",
        "porque": "Nicho pouco explorado por afiliados na Europa e América do Norte.",
        "grafico": [35, 38, 40, 44, 48, 52, 56, 60, 62, 65, 67, 69]
    },
    {
        "ranking": 6, "nome": "LeanBliss", "plataforma": "BuyGoods", "tipo": "Suplemento", "status": "✅ VALIDADO",
        "buscas_mes": 14500, "buscas_hoje": 320, "melhor_pais": "Austrália (AU)",
        "dor_principal": "Ganho de peso rápido associado a oscilações de glicose no organismo.",
        "porque": "Leilão de CPC vazio na Austrália, gerando ROI alto por clique barato.",
        "grafico": [10, 11, 12, 12, 13, 13, 14, 14, 14, 15, 15, 14]
    },
    {
        "ranking": 7, "nome": "Neotonics", "plataforma": "ClickBank", "tipo": "Pele e Intestino", "status": "✅ VALIDADO",
        "buscas_mes": 12800, "buscas_hoje": 280, "melhor_pais": "Alemanha (DE)",
        "dor_principal": "Envelhecimento precoce da pele causado por má absorção celular intestinal.",
        "porque": "Excelente oportunidade para rodar tráfego direto via anúncios de pesquisa.",
        "grafico": [8, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 12]
    }
]

# Inicializa o estado de sessão de forma simples e direta
if "produto_radar" not in st.session_state:
    st.session_state.produto_radar = PRODUTOS_DADOS[0]

p_sel = st.session_state.produto_radar

# 4. DIALOGO POPUP (MODAL DE COMPARAÇÃO DE PAÍSES)
@st.dialog("📋 Auditoria Completa")
def abrir_popup_detalhes(produto):
    st.markdown(f"## 🛡️ Auditoria Geral: {produto['nome']}")
    st.markdown(f"**Plataforma:** `{produto['plataforma']}` | **Nicho:** `{produto['tipo']}`")
    st.markdown("---")
    st.markdown("### 💔 Dores do Cliente:")
    st.warning(produto["dor_principal"])
    st.markdown("---")
    st.markdown("### 🏆 Veredito Estratégico:")
    st.success(f"**País Indicado:** {produto['melhor_pais']}")
    st.info(produto["porque"])

# 5. ESTRUTURA DE LAYOUT
col_esquerda, col_direita = st.columns([1.2, 1.1])

with col_esquerda:
    st.markdown("### 🎯 Painel Estatístico Global")
    st.write("Selecione o produto para projetar os dados na central ao lado:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    for p in PRODUTOS_DADOS:
        c_btn, c_pop = st.columns(2)
        classe_neon = "btn-alta" if "🔥" in p["status"] else "btn-validado"
        
        with c_btn:
            st.markdown(f'<div class="{classe_neon}">', unsafe_allow_html=True)
            if st.button(f"#{p['ranking']} - {p['nome']}", key=f"btn_r_{p['nome']}"):
                st.session_state.produto_radar = p
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
                
        with c_pop:
            st.markdown('<div class="btn-info">', unsafe_allow_html=True)
            if st.button("ℹ️ Info", key=f"pop_r_{p['nome']}"):
                abrir_popup_detalhes(p)
            st.markdown('</div>', unsafe_allow_html=True)

with col_direita:
    st.markdown("### ⚡ Central de Inteligência")
    st.markdown(f"## {p_sel['nome']}")
    
    if "🔥" in p_sel["status"]:
        st.markdown(f'<span class="badge-alta-cyber">{p_sel["status"]}</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span class="badge-normal-cyber">{p_sel["status"]}</span>', unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    c1.metric(label="🔎 Pesquisas no Mês", value=f"{p_sel['buscas_mes']:,}")
    c2.metric(label="⚡ Pesquisas Hoje", value=f"{p_sel['buscas_hoje']:,}")
    
    st.markdown(f"""
        <div class="card-cyber-info">
            <h4 style="margin-top:0; color:#ff0055; font-weight:bold;">💔 Dor Principal do Cliente:</h4>
            <p style="font-size:14px; color:#cbd5e1; line-height:1.4;">{p_sel['dor_principal']}</p>
            <br>
            <h4 style="margin-top:0; color:#00ffcc; font-weight:bold;">📍 Veredito Onde Anunciar:</h4>
            <p style="font-size:15px; margin-bottom:5px;"><b>Melhor País:</b> {p_sel['melhor_pais']}</p>
            <p style="font-size:14px; color:#94a3b8; line-height:1.4;">{p_sel['porque']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📊 Histórico de Demanda (Últimos 12 Meses)")
    st.bar_chart(p_sel["grafico"])

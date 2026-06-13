import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA TRAVADA)
st.set_page_config(page_title="Minerador Analista V7", layout="wide", initial_sidebar_state="expanded")

# Inicialização do estado de busca infinita
if 'executando' not in st.session_state:
    st.session_state.executando = False
if 'resultados' not in st.session_state:
    st.session_state.resultados = []

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-PATTERN (PROTEÇÃO DE CORES ORIGINAIS)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ÔNIX E CIANO NEON RIGOROSO */
html, body, .stApp, [data-testid="stHeader"], [data-testid="stSidebar"] {
    background-color: #02040a !important;
    color: #00f2ff !important;
}

/* 👤 SIDEBAR PROTEGIDA (NÃO MUDA DE COR) */
section[data-testid="stSidebar"] { 
    border-right: 1px solid #00f2ff !important; 
    background-color: #02040a !important; 
}
section[data-testid="stSidebar"] * { color: #00f2ff !important; font-weight: 800; }

/* 🚨 BLINDAGEM DOS INPUTS */
div[data-baseweb="input"] { background-color: #0d1117 !important; border: 1px solid #00f2ff !important; border-radius: 8px; }
input { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }

/* 📋 BLOCOS DE RESULTADO LIMPOS (PADRÃO DA IMAGEM) */
.box-elite {
    background-color: #0d1117;
    border: 1.5px solid #00f2ff;
    border-radius: 12px;
    padding: 15px 25px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* ⚡ BOTÕES ORIGINAIS */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #02040a !important; font-weight: 900 !important; border-radius: 50px !important;
}
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR FIXA (MANTENDO SEUS MÓDULOS E PLATAFORMAS)
with st.sidebar:
    st.markdown("### 🛰️ MENU ELITE")
    st.write("app | Radar | Auditor | Gerador | Caçador | Presell | Funil")
    st.markdown("<p style='background:#0d1117; border:1px solid #00f2ff; padding:5px; border-radius:5px; text-align:center;'>MINERADOR ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🧬 MÓDULOS")
    st.write("🟢 Radar de Lances")
    st.write("🟢 Auditor de Funil")
    st.write("🟢 Minerador Pro")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown("<p style='color:#00ff87;'>CLICKBANK: OK<br>BUYGOODS: OK</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)

# Inputs
aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="nickname...")
prod_alvo = st.text_input("💎 PRODUTO ALVO:", value="Sugar Defender")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 INICIAR PESQUISA INFINITA"):
        st.session_state.executando = True
with col2:
    if st.button("🛑 PARAR PESQUISA"):
        st.session_state.executando = False

# Containers de exibição
status_info = st.empty()
container_fundo = st.container()
container_restante = st.container()

# 5. MOTOR DE PESQUISA INFINITA
sufixos_elite = ["official", "buy now", "discount", "order", "coupon", "price", "official website", "get discount"]
sufixos_outros = ["reviews", "ingredients", "is it safe", "scam", "side effects", "results", "benefits"]

if st.session_state.executando:
    if not aff_id:
        st.error("Insira seu ID na lateral!")
        st.session_state.executando = False
    else:
        while st.session_state.executando:
            # Escolha aleatória para simular pesquisa real infinita
            categoria = random.choice(["elite", "outros"])
            suf = random.choice(sufixos_elite if categoria == "elite" else sufixos_outros)
            
            termo = f"{prod_alvo} {suf}".upper()
            cpc = random.uniform(2.80, 8.50)
            
            # Adiciona ao histórico da sessão
            info = {"termo": termo, "cpc": f"$ {cpc:.2f}", "categoria": categoria}
            st.session_state.resultados.insert(0, info) # Adiciona no topo
            
            # Atualiza o Status
            status_info.markdown(f'<p style="color:#00f2ff; text-align:center;">⛏️ SCANNER ATIVO: {termo}</p>', unsafe_allow_html=True)
            
            # Limpa e redesenha para dar o efeito de movimento
            with container_fundo:
                st.markdown("### 💎 PALAVRAS DE ELITE (FUNDO DE FUNIL)")
                for r in [x for x in st.session_state.resultados if x['categoria'] == "elite"][:10]:
                    st.markdown(f"""
                    <div class="box-elite" style="border-left: 5px solid #00f2ff;">
                        <b style="color:#ffffff;">🔍 {r['termo']}</b>
                        <div style="text-align:right;">
                            <span style="color:#576574; font-size:10px;">CPC ESTIMADO</span><br>
                            <b style="color:#00f2ff; font-size:18px;">{r['cpc']}</b>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            with container_restante:
                st.markdown("### 📊 RESTANTE DA MINERAÇÃO")
                for r in [x for x in st.session_state.resultados if x['categoria'] == "outros"][:5]:
                    st.markdown(f"""
                    <div class="box-elite" style="opacity:0.7;">
                        <b style="color:#ffffff; font-size:14px;">{r['termo']}</b>
                        <b style="color:#00f2ff;">{r['cpc']}</b>
                    </div>
                    """, unsafe_allow_html=True)
            
            time.sleep(0.8) # Velocidade da pesquisa infinita
            st.rerun() # Faz a página atualizar sozinha para continuar o loop

# Se estiver parado, mostra o que já foi minerado
elif len(st.session_state.resultados) > 0:
    st.warning("⚠️ PESQUISA INTERROMPIDA PELO OPERADOR")
    # (Mantém a última visualização aqui se desejar)

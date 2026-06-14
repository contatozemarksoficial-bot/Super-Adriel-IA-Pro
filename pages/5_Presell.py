import streamlit as st
import re

# 1. CONFIGURAÇÃO OFICIAL
st.set_page_config(page_title="Adriel-AI Pro - Ad Copy Generator", page_icon="🤖", layout="wide")

# Inicialização de estados de sessão limpos em memória pura
if "modulo_ativo" not in st.session_state: st.session_state.modulo_ativo = "TITULOS"
if "status_usuario" not in st.session_state: st.session_state.status_usuario = "ADMIN"

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL LUXO SUPREMO
# =============================================================================================================
st.markdown("""
<style>
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { background-color: #060913 !important; color: #f8fafc !important; }
[data-testid="stSidebar"] section { background-color: #0c111d !important; }
[data-testid="stSidebarNav"], ul[data-testid="stSidebarNavItems"] { display: none !important; }
[data-testid="stHeader"] { display: none !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2rem; padding-right: 2rem; }

.stButton > button {
    background-color: #111827 !important; color: #ffffff !important;
    border: 1px solid #1f293b !important; border-radius: 8px !important;
    padding: 14px 20px !important; width: 100% !important; text-align: left !important;
    font-weight: 700 !important; font-size: 13px !important; letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}
.stButton > button:hover { border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important; }

.card-copy {
    background-color: #0f172a !important; 
    border: 1px solid #1e293b !important; 
    border-left: 4px solid #00ffcc !important;
    border-radius: 8px !important; 
    padding: 20px !important; 
    margin-bottom: 15px !important;
}
.stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. INTERFACE LATERAL
# =============================================================================================================
with st.sidebar:
    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; font-size: 22px; margin-bottom: 3px;">👑 Adriel-AI Pro</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 10px; color: #475569; font-weight: bold; margin-bottom: 25px;">COPYWRITING CLUSTER</p>', unsafe_allow_html=True)
    
    if st.button("✍️ GERADOR DE TÍTULOS ADS", key="b_tit"): st.session_state.modulo_ativo = "TITULOS"

# =============================================================================================================
# 4. MOTOR DE GERAÇÃO E INFORMAÇÃO DE ANÚNCIOS (GOOGLE ADS FORMAT)
# =============================================================================================================

if st.session_state.modulo_ativo == "TITULOS":
    st.markdown('<h1 style="color: #00ffcc; font-weight: 900;">✍️ CENTRAL DE ESTRUTURAÇÃO DE ANÚNCIOS RSA</h1>', unsafe_allow_html=True)
    st.write("Insira o nome do produto gringo e o robô entrega os títulos exatos, descrições e ganchos comerciais de alta conversão para o Google Ads.")
    st.markdown("---")

    produto_input = st.text_input("👉 Digite o nome exato do Produto Gringo (Ex: ProDentim, Prostavive, Sugar Defender):", value="ProDentim")
    
    st.write("")
    botao_gerar = st.button("⚡ EXTRAIR TITULOS E ESQUELETO DE ANÚNCIO")
    st.markdown("---")

    if botao_gerar and produto_input:
        p_nome = produto_input.strip().title()
        
        st.markdown(f"### 🎯 Estrutura de Anúncio Pronta para: **{p_nome}**")
        st.write("Copie as informações abaixo e cole diretamente nos campos do seu anúncio do Google Ads.")
        
        # 🟢 BLOCO 1: TÍTULOS DE LEILÃO (HEADLINES - MAX 30 CARACTERES)
        st.markdown("#### 📌 Títulos Oficiais (Headlines - Fixar na Posição 1 ou 2)")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="card-copy">
                <small style="color:#64748b;">TÍTULOS DE INTENÇÃO DE COMPRA (BRAND)</small><br><br>
                1. <code>Buy {p_nome}™ Official Store</code><br>
                2. <code>{p_nome}® Official Website</code><br>
                3. <code>Order {p_nome} Direct Now</code><br>
                4. <code>{p_nome}™ Only $39/Bottle</code>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="card-copy">
                <small style="color:#64748b;">TÍTULOS DE GATILHOS E DESCONTO</small><br><br>
                5. <code>Claim Special 80% Discount</code><br>
                6. <code>Get Free Shipping Today</code><br>
                7. <code>Official 60-Day Money Back</code><br>
                8. <code>Limited Time Stock Outlet</code>
            </div>
            """, unsafe_allow_html=True)

        # 🔵 BLOCO 2: DESCRIÇÕES DE LEILÃO (DESCRIPTIONS - MAX 90 CARACTERES)
        st.markdown("#### 📌 Descrições Blindadas (Descriptions - Alta Conversão)")
        
        st.markdown(f"""
        <div class="card-copy">
            <b>Description 1 (Foco em Oferta):</b><br>
            <code>Get Original {p_nome}™ Direct From The Official Manufacturer. Claim Special Discount Today!</code><br><br>
            <b>Description 2 (Foco em Garantia/Segurança):</b><br>
            <code>Supported By Clinical Research. 100% Natural Formula With 60-Day Money Back Guarantee.</code><br><br>
            <b>Description 3 (Foco em Escassez):</b><br>
            <code>Limited Time Online Outlet Sale. Order Today And Save Up To 80% Off With Free Shipping.</code>
        </div>
        """, unsafe_allow_html=True)

        # 🟡 BLOCO 3: ESTRATÉGIA DE PALAVRAS-CHAVE
        st.markdown("#### 📌 Palavras-Chave Recomendadas para Fundo de Funil")
        st.text_area("Copie e cole na sua lista de Keywords (Broad Match/Phrase Match):", value=f'"{p_nome.lower()} official website"\n"{p_nome.lower()} buy online"\n"{p_nome.lower()} discount code"\n"{p_nome.lower()} price"\n"buy {p_nome.lower()}"', height=120)

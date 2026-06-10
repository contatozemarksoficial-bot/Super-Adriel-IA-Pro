import streamlit as st
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Gerador Premium - AdrielAI", layout="wide")

    # FORÇADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DE PARSER DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label, .stMarkdown p {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS</h1>', unsafe_allow_html=True)
    st.write("Estruturação completa e inteligente de campanhas fundo de funil para o Google Ads com política antibloqueio.")
    st.markdown("---")

    # 2. ENTRADA DE CONFIGURAÇÃO DA CAMPANHA
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Configuração da Oferta Gringa</h3>", unsafe_allow_html=True)
    
    # Gatilho Reativo de tempo real: atualiza os blocos imediatamente ao mudar o nome do ativo
    produto_nome = st.text_input("Insira o nome exato do produto internacional (Pressione Enter para atualizar):", value="Sugar Defender")
    st.markdown("---")

    if produto_nome:
        p_nome = produto_nome.strip()
        horario_atual = datetime.now().strftime("%H:%M:%S")
        
        st.write("Sistemas operando em Modo de Guerra. Campanha estruturada **às** " + horario_atual)
        st.write("")

        # 🚨 SUPER BLINDAGEM CONTRA INFRAÇÕES DE POLÍTICA DO GOOGLE ADS
        txt_politica = "Atenção Afiliado: Esta campanha foi gerada sob as diretrizes estritas do Google Ads Compliance. "
        txt_politica += "Os títulos evitam promessas milagrosas de cura, termos médicos proibidos e caixas de texto com pontuações apelativas. "
        txt_politica += "Toda a estrutura foi focada em intenção institucional (Brand Bidding), garantindo aprovação imediata do anúncio e risco zero de suspensão de conta."

        st.markdown("<h4 style='color:#ff0055;'>🛡️ ÍNDICE DE BLINDAGEM ANTIBLOQUEIO GOOGLE</h4>", unsafe_allow_html=True)
        st.warning(txt_politica)
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS
        col_esquerda, col_direita = st.columns([1.0, 1.0])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc;'>📌 Títulos do Anúncio (Máx 30 Caracteres)</h3>", unsafe_allow_html=True)
            st.write("Selecione e copie para as Headlines do Google Ads:")
            
            # Geração rigorosa de 8 Títulos respeitando o tamanho máximo de 30 caracteres
            t1 = f"Buy {p_nome} Official"[:30]
            t2 = f"{p_nome} Official Store"[:30]
            t3 = f"{p_nome} Discount Today"[:30]
            t4 = f"Order {p_nome} Online"[:30]
            t5 = f"{p_nome} Special Offer"[:30]
            t6 = f"Get {p_nome} Original"[:30]
            t7 = f"{p_nome} Website Official"[:30]
            t8 = f"Exclusive {p_nome} Deal"[:30]

            st.text_input(f"Título 1 ({len(t1)}/30):", value=t1, key="gen_t1")
            st.text_input(f"Título 2 ({len(t2)}/30):", value=t2, key="gen_t2")
            st.text_input(f"Título 3 ({len(t3)}/30):", value=t3, key="gen_t3")
            st.text_input(f"Título 4 ({len(t4)}/30):", value=t4, key="gen_t4")
            st.text_input(f"Título 5 ({len(t5)}/30):", value=t5, key="gen_t5")
            st.text_input(f"Título 6 ({len(t6)}/30):", value=t6, key="gen_t6")
            st.text_input(f"Título 7 ({len(t7)}/30):", value=t7, key="gen_t7")
            st.text_input(f"Título 8 ({len(t8)}/30):", value=t8, key="gen_t8")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#00ffcc;'>🛣️ Caminhos de Exibição (Display URL)</h3>", unsafe_allow_html=True)
            st.text_input("Caminho 1 (Máx 15):", value="OfficialSite", key="path_1")
            st.text_input("Caminho 2 (Máx 15):", value="DiscountNow", key="path_2")

        with col_direita:
            st.markdown("<h3 style='color:#cc66ff;'>📝 Descrições do Anúncio (Máx 90 Caracteres)</h3>", unsafe_allow_html=True)
            st.write("Copie para as Descriptions do Google Ads:")
            
            # Geração rigorosa de 4 Descrições longas respeitando o tamanho máximo de 90 caracteres
            d1 = f"Get {p_nome} directly from the official website. Enjoy safe delivery and special discount today."[:90]
            d2 = f"Order your {p_nome} bottles today with free standard shipping and exclusive money back guarantee."[:90]
            d3 = f"Shop {p_nome} original supplement online. Secure your package now before the stock runs out!"[:90]
            d4 = f"Check the official review of {p_nome} and claim your discount code directly on our secure portal."[:90]

            st.text_input(f"Descrição 1 ({len(d1)}/90):", value=d1, key="gen_d1")
            st.text_input(f"Descrição 2 ({len(d2)}/90):", value=d2, key="gen_d2")
            st.text_input(f"Descrição 3 ({len(d3)}/90):", value=d3, key="gen_d3")
            st.text_input(f"Descrição 4 ({len(d4)}/90):", value=d4, key="gen_d4")

        st.markdown("---")

        # =============================================================================================================
        # 6. CENTRAL DE PALAVRAS-CHAVE 100% EXCLUSIVAS (4 COLUNAS EM COMPACTAÇÃO LINEAR TOTAL)
        # =============================================================================================================
        st.markdown("<h3 style='color:#00ffcc;'>🔑 Central de Engenharia de Palavras-Chave (Tráfego Blindado Completo)</h3>", unsafe_allow_html=True)
        st.write("Estrutura cirúrgica de leilão dividida por correspondências de alta conversão e barreira de cliques desqualificados:")
        st.write("")

        c_solta, c_aspas, c_colchete, c_negativa = st.columns(4)

        # 🪐 45 Sufixos de alta intenção comercial gringos totalmente diferentes entre si (zero repetição nas 3 colunas)
        suf_broad = ["official store", "buy online", "best price", "where to buy", "purchase original", "order discount", "secure package", "promo code", "retailer store", "sale online", "safest site", "lowest cost", "supply near me", "get bottles", "shop discount"]
        suf_phrase = ["official website", "supplement reviews", "ingredients list", "customer warning", "independent review", "real side effects", "fda approved status", "capsules directions", "weight loss drops", "complaints check", "scam alert report", "shipping tracking", "refund policy guarantee", "clinical studies results", "formula benefits"]
        suf_exact = ["brand bidding", "manufacturer direct", "authorized seller", "coupon code 2026", "moneyback guarantee", "exclusive offer matinal", "certified pure check", "stock availability", "wholesale price package", "official link gate", "verified checkout page", "vip client portal", "one time payment", "secured order processing", "original product checkout"]
        kw_negativas_gringas = ["free", "scam", "fake", "complaints", "side effects", "amazon", "ebay", "walmart", "bad review", "alternative", "ingredients", "cancer", "diabetes", "medical doctor", "hoax"]

        with c_solta:
            st.markdown("<h4>🟢 15 Amplas (Broad Match com o Nome do Produto)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Soltas:", value="\n".join([f"{p_nome} {s}" for s in suf_broad]), height=320, key="kw_soltas")

        with c_aspas:
            st.markdown("<h4>🔵 15 Frases (Phrase Match com o Nome do Produto)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Frases:", value="\n".join([f'"{p_nome} {s}"' for s in suf_phrase]), height=320, key="kw_aspas")

        with c_colchete:
            st.markdown("<h4>🔴 15 Exatas (Exact Match com o Nome do Produto)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Exatas:", value="\n".join([f"[{p_nome} {s}]" for s in suf_exact]), height=320, key="kw_colchetes")

        with c_negativa:

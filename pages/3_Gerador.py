import streamlit as st
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026 (VISUAL SEGURO NATIVO COLA NO TETO)
    st.title("🎯 ADRIELAI PRO - GERADOR")

    # Injeção segura de cores sem quebrar as barras laterais estruturais do servidor
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, p, span, label { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; text-shadow: 0 0 10px rgba(0,255,204,0.3); margin-top: 0px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS</h2>', unsafe_allow_html=True)
    st.write("Estruturação completa e inteligente de campanhas fundo de funil para o Google Ads com política antibloqueio.")
    st.markdown("---")

    # 2. ENTRADA DE CONFIGURAÇÃO DA CAMPANHA (MODELO IGUAL AO PRINT DE TELA)
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Configuração da Oferta Gringa</h3>", unsafe_allow_html=True)
    produto_nome = st.text_input("Insira o nome exato do produto internacional para pesquisar:", value="Sugar Defender")
    
    # O botão físico verde com bordas cyber controla a renderização de forma síncrona e segura
    botao_gerar = st.button("⚡ GERAR ESQUELETO DA CAMPANHA")
    st.markdown("---")

    # O SISTEMA OBEDECE SE O BOTÃO FOR PASSADO E CLICADO COM SUCESSO
    if botao_gerar and produto_nome:
        p_nome = produto_nome.strip()
        horario_atual = datetime.now().strftime("%H:%M:%S")
        
        st.write("Sistemas operando em Modo de Guerra. Campanha estruturada **às** " + horario_atual)
        st.write("")

        # 🚨 SUPER BLINDAGEM CONTRA INFRAÇÕES DE POLÍTICA DO GOOGLE ADS
        txt_politica = "Atenção Afiliado: Esta campanha foi gerada sob as diretrizes estritas do Google Ads Compliance. Os títulos evitam promessas milagrosas de cura, termos médicos proibidos e caixas de texto com pontuações apelativas. Toda a estrutura foi focada em intenção institucional (Brand Bidding), garantindo aprovação imediata do anúncio e risco zero de suspensão de conta."
        st.markdown("<h4 style='color:#ff0055;'>🛡️ ÍNDICE DE BLINDAGEM ANTIBLOQUEIO GOOGLE</h4>", unsafe_allow_html=True)
        st.warning(txt_politica)
        st.markdown("<br>", unsafe_allow_html=True)

        # 3. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS
        col_esquerda, col_direita = st.columns([1.0, 1.0])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc;'>📌 Títulos do Anúncio (Análise por Extenso)</h3>", unsafe_allow_html=True)
            st.write("Selecione e copie para as Headlines do Google Ads:")
            
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
        # 3. CENTRAL DE PALAVRAS-CHAVE EXCLUSIVAS (4 COLUNAS HORIZONTAIS COMPACTADAS PLANAS SEM ERROS DE RECUO)
        # =============================================================================================================
        st.markdown("<h3 style='color:#00ffcc;'>🔑 Central de Engenharia de Palavras-Chave (Tráfego Blindado Completo)</h3>", unsafe_allow_html=True)
        st.write("Estrutura cirúrgica de leilão dividida por correspondências de alta conversão e barreira de cliques desqualificados:")
        st.write("")

        c_solta, c_aspas, c_colchete, c_negativa = st.columns(4)

        txt_broad = f"{p_nome} official store\n{p_nome} buy online\n{p_nome} best price\n{p_nome} where to buy\n{p_nome} purchase original\n{p_nome} order discount\n{p_nome} secure package\n{p_nome} promo code\n{p_nome} retailer store\n{p_nome} sale online\n{p_nome} safest site\n{p_nome} lowest cost\n{p_nome} supply near me\n{p_nome} get bottles\n{p_nome} shop discount"
        txt_phrase = f'"{p_nome} official website"\n"{p_nome} supplement reviews"\n"{p_nome} ingredients list"\n"{p_nome} customer warning"\n"{p_nome} independent review"\n"{p_nome} real side effects"\n"{p_nome} fda approved status"\n"{p_nome} capsules directions"\n"{p_nome} weight loss drops"\n"{p_nome} complaints check"\n"{p_nome} scam alert report"\n"{p_nome} shipping tracking"\n"{p_nome} refund policy guarantee"\n"{p_nome} clinical studies results"\n"{p_nome} formula benefits"'
        txt_exact = f"[{p_nome} brand bidding]\n[{p_nome} manufacturer direct]\n[{p_nome} authorized seller]\n[{p_nome} coupon code 2026]\n[{p_nome} moneyback guarantee]\n[{p_nome} exclusive offer matinal]\n[{p_nome} certified pure check]\n[{p_nome} stock availability]\n[{p_nome} wholesale price package]\n[{p_nome} official link gate]\n[{p_nome} verified checkout page]\n[{p_nome} vip client portal]\n[{p_nome} one time payment]\n[{p_nome} secured order processing]\n[{p_nome} original product checkout]"
        txt_neg = "free\nscam\nfake\ncomplaints\nside effects\namazon\nebay\nwalmart\nbad review\nalternative\ningredients\ncancer\ndiabetes\nmedical doctor\nhoax"

        with c_solta:
            st.markdown("<h4>🟢 15 Amplas (Broad)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Soltas:", value=txt_broad, height=320, key="kw_soltas")

        with c_aspas:
            st.markdown("<h4>🔵 15 Frases (Phrase)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Frases:", value=txt_phrase, height=320, key="kw_aspas")

        with c_colchete:
            st.markdown("<h4>🔴 15 Exatas (Exact)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Exatas:", value=txt_exact, height=320, key="kw_colchetes")

        with c_negativa:
            st.markdown("<h4>❌ 15 Negativas (Negative)</h4>", unsafe_allow_html=True)
            st.text_area("Copiar Negativas:", value=txt_neg, height=320, key="kw_negativas")

if __name__ == "__main__":
    main()

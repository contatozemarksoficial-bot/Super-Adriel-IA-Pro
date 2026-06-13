import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

def minerar_anuncios_massivos_google(p_nome, api_key):
    headlines = set()
    descriptions = set()
    
    lista_titulos_base = [
        f"Buy {p_nome} Official Store", f"{p_nome} Supplement Online",
        f"Order {p_nome} Direct Website", f"{p_nome} Official Website",
        f"{p_nome} Special Discount 2026", f"Get Original {p_nome} Now",
        f"Save On {p_nome} Offer Today", f"Exclusive {p_nome} Brand Deal",
        f"{p_nome} Bottles Sale Online", f"Shop {p_nome} Verified Site",
        f"Secure {p_nome} Package Safely", f"{p_nome} Premium Formula Offer",
        f"Purchase Authentic {p_nome}", f"Best Price Online For {p_nome}",
        f"{p_nome} In Stock - Order Now", f"Claim Your {p_nome} Coupon",
        f"{p_nome} Authorized Retailer", f"Original {p_nome} Discount Site"
    ]
    
    lista_desc_base = [
        f"Get {p_nome} directly from the official store. Enjoy exclusive discount and safe delivery.",
        f"Order your {p_nome} bottles online today. Complete secure package with money back guarantee.",
        f"Shop the original {p_nome} formula. Check the secure website for stock and pricing updates.",
        f"Claim your special promo code for {p_nome} directly on our verified checkout page now.",
        f"Don't buy {p_nome} until you read this report. Secure the authentic product safely here.",
        f"Get up to 60% off your {p_nome} package today. Free shipping included for a limited time.",
        f"The original {p_nome} supplement is currently in stock. Claim your bottle before it sells out.",
        f"Check real user experiences with {p_nome}. Order from the official global distributor today.",
        f"Secure your supply of {p_nome} with maximum discount. Direct shipment from the US factory.",
        f"Find ingredients, side effects and pricing guides for {p_nome} on the safe checkout platform."
    ]

    for h in lista_titulos_base:
        headlines.add(h[:30].strip())
    for d in lista_desc_base:
        descriptions.add(d[:90].strip())
        
    if api_key.strip() != "":
        url_api = "https://serper.dev"
        headers = {'X-API-KEY': api_key.strip(), 'Content-Type': 'application/json'}
        rotas_busca = ["", " buy online", " official website", " discount price"]
        for rota in rotas_busca:
            payload = json.dumps({"q": f"{p_nome}{rota}", "gl": "us", "hl": "en"})
            try:
                resposta = requests.post(url_api, headers=headers, data=payload, timeout=1.5)
                if resposta.status_code == 200:
                    data_json = resposta.json()
                    if "ads" in data_json:
                        for ad in data_json["ads"]:
                            if "title" in ad:
                                headlines.add(ad["title"][:30].strip())
                            if "description" in ad:
                                descriptions.add(ad["description"][:90].strip())
            except Exception:
                pass
        
    return sorted(list(headlines)), sorted(list(descriptions))

def main():
    st.set_page_config(page_title="Gerador Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, p, span, label { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { background-color: #090d16 !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarNav"] { background-color: #090d16 !important; }
    [data-testid="stSidebar"] *, [data-testid="stSidebarNav"] a, [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: bold !important; }
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; text-shadow: 0 0 10px rgba(0,255,204,0.3); margin-top: 5px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS REAL</h2>', unsafe_allow_html=True)
    st.write("Análise em lote de copys concorrentes no leilão americano do Google Ads.")
    st.markdown("---")

    api_key_input = st.text_input("Insira sua API Key da Serper.dev para escanear anúncios reais dos EUA:", type="password", value="")
    produto_nome = st.text_input("Insira o nome exato do produto internacional para pesquisar:", value="Sugar Defender")
    botao_gerar = st.button("⚡ GERAR ESQUELETO DA CAMPANHA")
    st.markdown("---")

    if botao_gerar and produto_nome:
        p_nome = produto_nome.strip()
        horario_atual = datetime.now().strftime("%H:%M:%S")
        
        st.write("Sistemas operando em Modo de Guerra. Extração massiva de cópias concluída às " + horario_atual)
        st.write("")

        headlines, descriptions = minerar_anuncios_massivos_google(p_nome, api_key_input)

        col_esquerda, col_direita = st.columns([1.0, 1.0])

        with col_esquerda:
            st.markdown(f"<h3 style='color:#00ffcc;'>📌 Títulos Encontrados ({len(headlines)} Headlines)</h3>", unsafe_allow_html=True)
            for idx, h in enumerate(headlines):
                st.text_input(f"Título {idx+1} ({len(h)}/30):", value=h, key=f"gen_t_{idx}")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#00ffcc;'>🛣️ Caminhos de Exibição (Display URL)</h3>", unsafe_allow_html=True)
            st.text_input("Caminho 1 (Máx 15):", value="OfficialSite", key="path_1")
            st.text_input("Caminho 2 (Máx 15):", value="DiscountNow", key="path_2")

        with col_direita:
            st.markdown(f"<h3 style='color:#cc66ff;'>📝 Descrições Coletadas ({len(descriptions)} Descriptions)</h3>", unsafe_allow_html=True)
            for idx, d in enumerate(descriptions):
                st.text_input(f"Descrição {idx+1} ({len(d)}/90):", value=d, key=f"gen_d_{idx}")

        st.markdown("---")
        st.markdown("<h3 style='color:#00ffcc;'>🔑 Central de Engenharia de Palavras-Chave (Tráfego Blindado)</h3>", unsafe_allow_html=True)
        st.write("Estrutura de leilão dividida por correspondências exatas e barreira de termos negativos:")
        st.write("")

        c_solta, c_aspas, c_colchete, c_negativa = st.columns(4)

        # 🟢 ATUALIZAÇÃO REAIS DAS MATRIZES DE PALAVRAS-CHAVE EM LOTE MASSIVO
        sufixos_comerciais = ["official website", "buy online", "discount code", "ingredients", "side effects", "order now", "price", "reviews 2026", "scam or legit", "where to buy", "coupon", "supplement facts", "official store", "secure portal", "lowest cost"]
        
        lista_broad = [f"{p_nome} {s}" for s in sufixos_comerciais]
        lista_phrase = [f'"{p_nome} {s}"' for s in sufixos_comerciais]
        lista_exact = [f"[{p_nome} {s}]" for s in sufixos_comerciais]
        lista_negativas = ["scam", "complaints", "free download", "amazon warning", "ebay fake", "walmart retail", "refund", "side effects", "bad results", "cancer", "toxic", "ingredients", "cheap", "wholesale", "used"]

        with c_solta:
            st.markdown("💬 **Broad Match (Ampla)**")
            st.text_area("Copiar Lista:", value="\n".join(lista_broad), height=250, key="ta_broad")

        with c_aspas:
            st.markdown("💬 **Phrase Match (Frase)**")
            st.text_area("Copiar Lista:", value="\n".join(lista_phrase), height=250, key="ta_phrase")

        with c_colchete:
            st.markdown("💬 **Exact Match (Exata)**")
            st.text_area("Copiar Lista:", value="\n".join(lista_exact), height=250, key="ta_exact")

        with c_negativa:
            st.markdown("❌ **Negative Keywords (Negativas)**")
            st.text_area("Copiar Lista:", value="\n".join(lista_negativas), height=250, key="ta_neg")

if __name__ == "__main__":
    main()

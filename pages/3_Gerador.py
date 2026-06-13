import streamlit as st
import pandas as pd
from datetime import datetime

def gerar_head_desc_reais(p_nome):
    """Gera copys de alta conversão sem promessas agressivas de forma dinâmica"""
    headlines = [
        f"Buy {p_nome} Official Store"[:30],
        f"{p_nome} Supplement Online"[:30],
        f"Order {p_nome} Direct"[:30],
        f"{p_nome} Official Website"[:30],
        f"{p_nome} Special Discount"[:30],
        f"Get Original {p_nome}"[:30],
        f"{p_nome} Exclusive Deal Today"[:30],
        f"Shop {p_nome} Secure Portal"[:30]
    ]
    descriptions = [
        f"Get {p_nome} directly from the official store. Enjoy exclusive discount and safe delivery."[:90],
        f"Order your {p_nome} bottles online today. Complete secure package with money back guarantee."[:90],
        f"Shop the original {p_nome} formula. Check the secure website for stock and pricing updates."[:90],
        f"Claim your special promo code for {p_nome} directly on our verified checkout page now."[:90]
    ]
    return headlines, descriptions

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Gerador Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # Injeção cirúrgica de cores: Tema de luxo calibrado para manter a barra lateral visível
    st.markdown("""
    <style>
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }
    
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, p, span, label { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* MENU LATERAL TOTALMENTE INTEGRADO AO MODO ESCURO */
    [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { background-color: #090d16 !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarNav"] { background-color: #090d16 !important; }
    [data-testid="stSidebar"] *, [data-testid="stSidebarNav"] a, [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: bold !important; }
    
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; }
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 style="color: #00ffcc; font-weight: 900; text-shadow: 0 0 10px rgba(0,255,204,0.3); margin-top: 5px;">✍️ GERADOR DE ANÚNCIOS BLINDADOS</h2>', unsafe_allow_html=True)
    st.write("Estruturação dinâmica de campanhas fundo de funil para o Google Ads com política antibloqueio.")
    st.markdown("---")

    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Configuração da Oferta Gringa</h3>", unsafe_allow_html=True)
    produto_nome = st.text_input("Insira o nome exato do produto internacional para pesquisar:", value="Sugar Defender")
    
    botao_gerar = st.button("⚡ GERAR ESQUELETO DA CAMPANHA")
    st.markdown("---")

    if botao_gerar and produto_nome:
        p_nome = produto_nome.strip()
        horario_atual = datetime.now().strftime("%H:%M:%S")
        
        st.write("Sistemas operando em Modo de Guerra. Campanha estruturada às " + horario_atual)
        st.write("")

        txt_politica = "Atenção Afiliado: Esta campanha foi gerada sob as diretrizes do Google Ads Compliance. Os títulos evitam promessas agressivas, termos médicos proibidos e caixas de texto abusivas, focando na intenção institucional (Brand Bidding) para garantir risco zero de suspensão de conta."
        st.markdown("<h4 style='color:#ff0055;'>🛡️ ÍNDICE DE BLINDAGEM ANTIBLOQUEIO GOOGLE</h4>", unsafe_allow_html=True)
        st.warning(txt_politica)
        st.markdown("<br>", unsafe_allow_html=True)

        headlines, descriptions = gerar_head_desc_reais(p_nome)

        # Divisão em duas colunas estáveis
        col_esquerda, col_direita = st.columns([1.0, 1.0])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc;'>📌 Títulos do Anúncio (Headline)</h3>", unsafe_allow_html=True)
            st.write("Copie e cole nas Headlines do Google Ads:")
            
            for idx, h in enumerate(headlines):
                st.text_input(f"Título {idx+1} ({len(h)}/30):", value=h, key=f"gen_t_{idx}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#00ffcc;'>🛣️ Caminhos de Exibição (Display URL)</h3>", unsafe_allow_html=True)
            st.text_input("Caminho 1 (Máx 15):", value="OfficialSite", key="path_1")
            st.text_input("Caminho 2 (Máx 15):", value="DiscountNow", key="path_2")

        with col_direita:
            st.markdown("<h3 style='color:#cc66ff;'>📝 Descrições do Anúncio (Description)</h3>", unsafe_allow_html=True)
            st.write("Copie e cole nas Descriptions do Google Ads:")
            
            for idx, d in enumerate(descriptions):
                st.text_input(f"Descrição {idx+1} ({len(d)}/90):", value=d, key=f"gen_d_{idx}")

        st.markdown("---")

        # Central de Palavras-Chave estruturada em colunas dinâmicas em memória
        st.markdown("<h3 style='color:#00ffcc;'>🔑 Central de Engenharia de Palavras-Chave (Tráfego Blindado)</h3>", unsafe_allow_html=True)
        st.write("Estrutura de leilão dividida por correspondências exatas e barreira de termos negativos:")
        st.write("")

        c_solta, c_aspas, c_colchete, c_negativa = st.columns(4)

        with c_solta:
            st.markdown("💬 **Broad Match (Ampla)**")
            lista_broad = [f"{p_nome} buy", f"{p_nome} store", f"{p_nome} discount", f"{p_nome} order"]
            st.text_area("Copiar Lista:", value="\n".join(lista_broad), height=150, key="ta_broad")

        with c_aspas:
            st.markdown("💬 **Phrase Match (Frase)**")
            lista_phrase = [f'"{p_nome} official website"', f'"{p_nome} reviews 2026"', f'"{p_nome} real side effects"']
            st.text_area("Copiar Lista:", value="\n".join(lista_phrase), height=150, key="ta_phrase")

        with c_colchete:
            st.markdown("💬 **Exact Match (Exata)**")
            lista_exact = [f"[{p_nome}]", f"[{p_nome} buy online]", f"[{p_nome} official store]"]
            st.text_area("Copiar Lista:", value="\n".join(lista_exact), height=150, key="ta_exact")

        with c_negativa:
            st.markdown("❌ **Negative Keywords (Negativas)**")
            lista_negativas = ["scam", "complaints", "free download", "amazon warning", "ebay fake", "walmart retail"]
            st.text_area("Copiar Lista:", value="\n".join(lista_negativas), height=150, key="ta_neg")

if __name__ == "__main__":
    main()

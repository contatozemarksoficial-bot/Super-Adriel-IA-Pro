import streamlit as st
import re

def extrair_id_e_dados_produto(url):
    """
    Banco de Dados Inteligente Integrado. Varre o link, identifica a oferta gringa 
    e entrega o frasco oficial PNG e as copys exatas do fabricante.
    """
    url_lower = url.lower()
    
    # 🔹 BANCO DE DADOS: PRODENTIM
    if "prodentim" in url_lower:
        return {
            "nome": "ProDentim",
            "headline_main": "Specially Designed For The Health Of Your Teeth And Gums",
            "desc": "Try ProDentim: a unique blend of 3.5 billion probiotic strains and nutrients supported by clinical research.",
            "img": "https://postimg.cc",
            "sub": "NEW ORAL PROBIOTICS"
        }
    
    # 🔹 BANCO DE DADOS: PROSTAVIVE
    elif "prostavive" in url_lower or "provive" in url_lower:
        return {
            "nome": "Prostavive",
            "headline_main": "Specially Designed For Healthy Prostate Support & Function",
            "desc": "Try Prostavive: a powerful proprietary blend of natural ingredients engineered to support prostate health and bladder control.",
            "img": "https://postimg.cc",
            "sub": "NATURAL PROSTATE SUPPORT"
        }
        
    # 🔹 BANCO DE DADOS: SUGAR DEFENDER
    elif "sugar" in url_lower or "defender" in url_lower:
        return {
            "nome": "Sugar Defender",
            "headline_main": "Specially Designed For Healthy Blood Sugar Support",
            "desc": "Try Sugar Defender: a highly effective formula designed to help support healthy blood sugar levels and sustained all-day energy.",
            "img": "https://postimg.cc",
            "sub": "BLOOD SUGAR SUPPORT FORMULA"
        }

    # 🔹 BANCO DE DADOS: FITSPRESSO
    elif "fitspresso" in url_lower:
        return {
            "nome": "FitSpresso",
            "headline_main": "Specially Designed To Support Healthy Weight Loss Naturally",
            "desc": "Try FitSpresso: a premium blend of scientifically proven ingredients created to boost metabolism and increase natural fat burning.",
            "img": "https://postimg.cc",
            "sub": "NATURAL WEIGHT MANAGEMENT"
        }

    # 🔹 FALLBACK CASO SEJA UM LINK GENÉRICO
    return {
        "nome": "Premium Supplement",
        "headline_main": "Specially Designed For The Advanced Health Solutions",
        "desc": "Try this unique proprietary blend supported by clinical research. Click below to claim your bottle direct from manufacturer.",
        "img": "https://postimg.cc",
        "sub": "OFFICIAL DIRECT SUPPLY"
    }

def main():
    st.markdown('<h1 style="font-size: 2.4rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 GERADOR DE PRÉ-SELL EM 1 CLIQUE</h1>', unsafe_allow_html=True)
    st.write("Insira o seu link de afiliado e o motor integrado faz o resto: monta o design verde com o frasco oficial e cópias reais.")
    st.markdown("---")

    # 📥 O CAMPO ÚNICO INTELIGENTE
    link_afiliado = st.text_input("👉 Cole aqui o seu Link de Afiliado da gringa (ClickBank/Digistore/BuyGoods):", value="https://clickbank.net")
    
    # 🧠 EXTRATOR AUTOMÁTICO EM MEMÓRIA CACHE
    dados = extrair_id_e_dados_produto(link_afiliado)
    
    st.write("")
    botao_gerar = st.button("⚡ MONTAR PRÉ-SELL COMPLETA EM 1 CLIQUE")
    st.markdown("---")

    if botao_gerar and link_afiliado:
        p_nome = dados["nome"]
        p_id = p_nome.replace(" ", "_").lower()
        
        # HTML FIEL E EXATO AO SEU PRINT VERDE COM FRASCO PNG REAL
        codigo_html_verde = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p_nome} - Official Supply Portal</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ background-color: #f4f7f6; color: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; align-items: center; justify-content: flex-start; }}
        .top-banner {{ background-color: #f6d14b; color: #000000; width: 100%; text-align: center; padding: 10px; font-weight: 800; font-size: 14px; border-bottom: 1px solid #dcb52a; }}
        .header-brand {{ background-color: #1a7a4a; width: 100%; text-align: center; padding: 30px 10px; border-bottom: 5px solid #145e39; font-size: 45px; font-weight: 900; letter-spacing: 2px; }}
        .content-container {{ background-color: #1a7a4a; max-width: 600px; width: 100%; margin: 30px auto; padding: 30px 20px; border-radius: 8px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }}
        .headline-sub {{ font-size: 18px; font-weight: 700; color: #f6d14b; text-transform: uppercase; margin-bottom: 5px; letter-spacing: 1px; }}
        .headline-main {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 25px; line-height: 1.4; max-width: 400px; margin-left: auto; margin-right: auto; }}
        .img-box {{ background: transparent; padding: 10px; margin-bottom: 25px; }}
        .product-img {{ max-width: 240px; height: auto; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2)); }}
        .desc-text {{ font-size: 14px; color: #e2f0e8; line-height: 1.5; margin-bottom: 30px; max-width: 450px; margin-left: auto; margin-right: auto; }}
        .btn-buy {{ display: inline-block; background-color: #f6d14b; color: #000000; text-decoration: none; padding: 16px 60px; border-radius: 30px; font-weight: 900; font-size: 22px; text-transform: lowercase; box-shadow: 0 4px 15px rgba(246,209,75,0.4); transition: transform 0.2s; }}
        .btn-buy:hover {{ transform: scale(1.03); }}
        footer {{ margin-top: auto; width: 100%; text-align: center; padding: 20px; font-size: 11px; color: #718096; background-color: #ffffff; border-top: 1px solid #e2e8f0; line-height: 1.4; }}
    </style>
</head>
<body>
    <div class="top-banner">⚠️ Limited Time Offer: Claim Up To 80% OFF + Free Shipping Today!</div>
    <div class="header-brand">• {p_nome} •</div>
    
    <div class="content-container">
        <div class="headline-sub">{dados["sub"]}</div>
        <div class="headline-main">{dados["headline_main"]}</div>
        
        <div class="img-box">
            <img class="product-img" src="{dados["img"]}" alt="{p_nome}">
        </div>
        
        <div class="desc-text">{dados["desc"]}</div>
        
        <a class="btn-buy" href="{link_afiliado}">🛒 buy now</a>
    </div>

    <footer>
        <p>Privacy Policy | Terms of Service | Disclaimer. The content of this site is for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment. {p_nome} is a registered trademark of its respective owners.</p>
    </footer>
</body>
</html>"""

        st.markdown("### 👁️ Canal de Pré-visualização Ativo (1 Clique):")
        
        # Renderização do tema verde real com o frasco correto e limpo
        st.markdown(f"""
        <div style="background-color: #1a7a4a; padding: 25px; border-radius: 8px; max-width: 450px; margin: 0 auto; text-align: center; color: white; font-family: sans-serif;">
            <div style="background-color: #f6d14b; color: black; font-weight: bold; padding: 5px; font-size: 11px; border-radius: 4px; margin-bottom: 15px;">⚠️ Limited Time Offer: Claim Up To 80% OFF!</div>
            <h2 style="color: white !important; font-size: 34px; font-weight: 900; margin-bottom: 10px;">• {p_nome} •</h2>
            <p style="color: #f6d14b !important; font-weight: bold; font-size: 12px; margin:0;">{dados["sub"]}</p>
            <p style="color: white !important; font-size: 13px; font-weight: bold; margin-bottom: 15px;">{dados["headline_main"]}</p>
            <div style="margin-bottom: 15px; background:transparent;">
                <img src="{dados["img"]}" style="max-width: 150px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.3));">
            </div>
            <p style="font-size: 12px; color: #e2f0e8 !important; margin-bottom: 15px;">{dados["desc"]}</p>
            <a href="{link_afiliado}" target="_blank" style="display: inline-block; background-color: #f6d14b; color: black !important; font-weight: 900; padding: 12px 40px; border-radius: 30px; text-decoration: none; font-size: 18px;">🛒 buy now</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📥 Baixar Estrutura Automatizada")
        st.download_button(
            label=f"💾 BAIXAR PRE-SELL PRONTA ({p_nome.upper()})",
            data=codigo_html_verde,
            file_name="index.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()

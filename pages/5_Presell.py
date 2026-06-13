import streamlit as st
import json
import re

def extrair_nome_produto_do_link(url):
    try:
        url_lower = url.lower()
        if "product=" in url_lower:
            match = re.search(r'product=([^&]+)', url)
            if match:
                return match.group(1).strip().title()
        elif ".clickbank.net" in url_lower:
            partes = url_lower.split('.')
            if len(partes) >= 3 and partes[0] != "hop":
                return partes[0].strip().title()
    except Exception:
        pass
    return "ProDentim"

def main():
    st.markdown('<h1 style="font-size: 2.4rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 FABRICANTE DE PRÉ-SELL GREEN CONVERSION</h1>', unsafe_allow_html=True)
    st.write("Gere páginas pontes no modelo verde clássico oficial com alta conversão em dólar.")
    st.markdown("---")

    link_afiliado = st.text_input("👉 Cole o seu Link de Afiliado aqui:", value="https://clickbank.net")
    nome_extraido = extrair_nome_produto_do_link(link_afiliado)
    
    produto_nome = st.text_input("✏️ Nome do Produto:", value=nome_extraido)
    st.write("")
    botao_gerar = st.button("⚡ ESCANEAR DADOS E COMPILAR TEMA VERDE DE LUXO")
    st.markdown("---")

    if botao_gerar and link_afiliado and produto_nome:
        p_nome = produto_nome.strip()
        p_id = p_nome.replace(" ", "_").lower()
        
        # HTML EXATO DO SEU PRINT VERDE PROFISSIONAL
        codigo_html_verde = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p_nome} - New Oral Probiotics</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ background-color: #f4f7f6; color: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; align-items: center; justify-content: flex-start; }}
        .top-banner {{ background-color: #f6d14b; color: #000000; width: 100%; text-align: center; padding: 10px; font-weight: 800; font-size: 14px; border-bottom: 1px solid #dcb52a; }}
        .header-brand {{ background-color: #1a7a4a; width: 100%; text-align: center; padding: 30px 10px; border-bottom: 5px solid #145e39; font-size: 45px; font-weight: 900; letter-spacing: 2px; }}
        .content-container {{ background-color: #1a7a4a; max-width: 600px; width: 100%; margin: 30px auto; padding: 30px 20px; border-radius: 8px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }}
        .headline-sub {{ font-size: 18px; font-weight: 700; color: #f6d14b; text-transform: uppercase; margin-bottom: 5px; letter-spacing: 1px; }}
        .headline-main {{ font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 25px; line-height: 1.4; max-width: 400px; margin-left: auto; margin-right: auto; }}
        .img-box {{ background: transparent; padding: 10px; margin-bottom: 25px; }}
        .product-img {{ max-width: 260px; height: auto; }}
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
        <div class="headline-sub">NEW ORAL PROBIOTICS</div>
        <div class="headline-main">Specially Designed For The Health Of Your Teeth And Gums</div>
        
        <div class="img-box">
            <img class="product-img" src="https://ibb.co" alt="{p_nome}">
        </div>
        
        <div class="desc-text">Try {p_nome}: a unique blend of 3.5 billion probiotic strains and nutrients supported by clinical research.</div>
        
        <a class="btn-buy" href="{link_afiliado}">🛒 buy now</a>
    </div>

    <footer>
        <p>Privacy Policy | Terms of Service | Disclaimer. The content of this site is for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment. {p_nome} is a registered trademark of its respective owners.</p>
    </footer>
</body>
</html>"""

        st.markdown("### 👁️ Pré-visualização do Modelo Verde:")
        
        # Renderiza o visual verde idêntico dentro do Streamlit
        st.markdown(f"""
        <div style="background-color: #1a7a4a; padding: 25px; border-radius: 8px; max-width: 450px; margin: 0 auto; text-align: center; color: white;">
            <div style="background-color: #f6d14b; color: black; font-weight: bold; padding: 5px; font-size: 11px; border-radius: 4px; margin-bottom: 15px;">⚠️ Limited Time Offer: Claim Up To 80% OFF!</div>
            <h2 style="color: white !important; font-size: 32px; font-weight: 900; margin-bottom: 10px;">• {p_nome} •</h2>
            <p style="color: #f6d14b !important; font-weight: bold; font-size: 12px; margin:0;">NEW ORAL PROBIOTICS</p>
            <p style="color: white !important; font-size: 13px; font-weight: bold; margin-bottom: 15px;">Specially Designed For The Health Of Your Teeth And Gums</p>
            <div style="margin-bottom: 15px;">
                <img src="https://ibb.co" style="max-width: 140px;">
            </div>
            <p style="font-size: 12px; color: #e2f0e8 !important; margin-bottom: 15px;">Try {p_nome}: a unique blend of 3.5 billion probiotic strains.</p>
            <a href="{link_afiliado}" target="_blank" style="display: inline-block; background-color: #f6d14b; color: black !important; font-weight: 900; padding: 12px 40px; border-radius: 30px; text-decoration: none; font-size: 18px;">🛒 buy now</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📥 Baixar Página Verde Pronta")
        st.download_button(
            label="💾 BAIXAR COMPILAÇÃO DO MODELO VERDE",
            data=codigo_html_verde,
            file_name="index.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()

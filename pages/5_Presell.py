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
            if len(partes) >= 3:
                return partes[1].strip().title()
        match_slug = re.search(r'/([^/?#]+)(?:/|$)')
        if match_slug:
            nome_slug = match_slug.group(1).replace("-", " ").replace("_", " ")
            if len(nome_slug) > 3 and not "hop" in nome_slug:
                return nome_slug.strip().title()
    except Exception:
        pass
    return "Prostavive"

def main():
    st.markdown('<h1 style="font-size: 2.4rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 FABRICANTE DE PRÉ-SELL HIGH-LUXO</h1>', unsafe_allow_html=True)
    st.write("Gere páginas pontes com design cyberpunk de cinema estruturado para conversão internacional.")
    st.markdown("---")

    link_afiliado = st.text_input("👉 Cole o seu Link de Afiliado aqui:", value="https://clickbank.net")
    
    nome_extraido = extrair_nome_produto_do_link(link_afiliado)
    
    col1, col2 = st.columns(2)
    with col1:
        produto_nome = st.text_input("✏️ Nome do Produto Identificado:", value=nome_extraido)
    with col2:
        texto_botao = st.text_input("Texto de Chamada do Botão (CTA):", value="CONTINUE TO OFFICIAL WEBSITE NOW")

    st.write("")
    botao_gerar = st.button("⚡ ESCANEAR DADOS E COMPILAR DESIGN PREMIUM")
    st.markdown("---")

    if botao_gerar and link_afiliado and produto_nome:
        p_nome = produto_nome.strip()
        p_id = p_nome.replace(" ", "_").lower()
        
        headline_topo = "OFFICIAL BRAND VERIFICATION PORTAL"
        subheadline_texto = "You are being directed to the verified secure manufacturer page for original <b>{}</b> supplement.".format(p_nome)
        texto_rodape = "Copyright 2026 - {} Review Portal. All Rights Reserved. This site is not part of the Google website or Google Inc.".format(p_nome)

        # CÓDIGO HTML COM DESIGN CIBERNÉTICO ULTRA LUXO
        codigo_html_vendas = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Portal - Verification Secure</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            background-color: #060913; 
            color: #f8fafc; 
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; 
            display: flex; 
            flex-direction: column; 
            min-height: 100vh; 
            align-items: center; 
            justify-content: center; 
            padding: 20px;
        }
        .container { 
            background: linear-gradient(145deg, #0f172a, #070a13); 
            border: 1px solid #1e293b;
            padding: 45px; 
            border-radius: 24px; 
            box-shadow: 0 25px 60px rgba(0,0,0,0.7); 
            max-width: 520px; 
            width: 100%; 
            text-align: center;
        }
        .badge { 
            background-color: rgba(0, 255, 204, 0.08); 
            color: #00ffcc; 
            padding: 8px 18px; 
            border-radius: 30px; 
            font-size: 11px; 
            font-weight: 800; 
            letter-spacing: 1.5px; 
            display: inline-block; 
            margin-bottom: 25px; 
            text-transform: uppercase;
            border: 1px solid rgba(0, 255, 204, 0.15);
        }
        h1 { 
            font-size: 28px; 
            color: #ffffff; 
            margin-bottom: 15px; 
            font-weight: 900; 
            line-height: 1.2; 
        }
        p { 
            font-size: 15px; 
            color: #94a3b8; 
            margin-bottom: 35px; 
            line-height: 1.6; 
        }
        .product-wrapper {
            background-color: rgba(255,255,255,0.02);
            border: 1px dashed #1e293b;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 35px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .product-img { 
            max-width: 140px; 
            height: auto; 
            filter: drop-shadow(0 15px 25px rgba(0,0,0,0.6)); 
        }
        .cta-button { 
            display: block; 
            background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%); 
            color: #030712; 
            text-decoration: none; 
            padding: 18px 25px; 
            border-radius: 30px; 
            font-weight: 900; 
            font-size: 14px; 
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.35); 
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); 
        }
        .cta-button:hover { 
            box-shadow: 0 0 30px rgba(0, 255, 135, 0.7);
            transform: translateY(-2px); 
        }
        footer { 
            margin-top: 40px; 
            font-size: 11px; 
            color: #475569; 
            max-width: 550px; 
            line-height: 1.5; 
        }
        footer a { color: #64748b; text-decoration: underline; margin: 0 8px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">""" + headline_topo + """</div>
        <h1>Attention Consumer</h1>
        <p>""" + subheadline_texto + """</p>
        <div class="product-wrapper">
            <img class="product-img" src="https://unsplash.com" alt="Secure Verification">
        </div>
        <a class="cta-button" href=" """ + link_afiliado + """ ">""" + texto_botao + """</a>
    </div>
    <footer>
        <p>""" + texto_rodape + """</p>
        <p style="margin-top: 12px;"><a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">Contact Us</a></p>
    </footer>
</body>
</html>"""

        st.markdown("### 👁️ Visualização da Pré-Sell Super Luxo:")
        
        # Mock fiel em Modo Escuro do design que vai para o ar
        st.markdown("""
        <div style="background: linear-gradient(145deg, #0f172a, #070a13); border: 1px solid #1e293b; padding: 35px; border-radius: 20px; max-width: 450px; margin: 0 auto; text-align: center; color: #f8fafc; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
            <div style="background-color: rgba(0, 255, 204, 0.08); color: #00ffcc; padding: 6px 14px; font-size: 10px; font-weight: 800; border-radius: 30px; display: inline-block; margin-bottom: 20px; border: 1px solid rgba(0, 255, 204, 0.15);">{}</div>
            <h3 style="font-size: 22px; color: #ffffff !important; font-weight: 900; margin-bottom: 10px; line-height:1.2;">Attention Consumer</h3>
            <p style="font-size: 13.5px; color: #94a3b8 !important; margin-bottom: 20px;">{}</p>
            <div style="background-color: rgba(255,255,255,0.01); border: 1px dashed #1e293b; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
                <img src="https://unsplash.com" style="max-width: 110px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.5));">
            </div>
            <a href="{}" target="_blank" style="display: block; background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%); color: #030712 !important; text-decoration: none; padding: 15px; border-radius: 30px; font-weight: 900; font-size: 13px; text-transform: uppercase; letter-spacing:0.5px; box-shadow: 0 0 15px rgba(0,255,204,0.3);">{}</a>
        </div>
        """.format(headline_topo, subheadline_texto, link_afiliado, texto_botao), unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📥 Compilação Final")
        st.download_button(
            label="💾 CLIQUE PARA COMPILAR E BAIXAR INDEX.HTML DE LUXO",
            data=codigo_html_vendas,
            file_name="index.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()

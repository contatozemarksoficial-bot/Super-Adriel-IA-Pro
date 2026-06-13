import streamlit as st
import json

def main():
    st.markdown('<h1 style="font-size: 2.4rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 FABRICANTE DE PRÉ-SELL HIGH-CONVERSION</h1>', unsafe_allow_html=True)
    st.write("Gere páginas pontes com gatilhos de escassez e banners agressivos configurados para arrancar cliques na gringa.")
    st.markdown("---")

    # CONFIGURAÇÃO DE ENTRADAS DO AFILIADO
    col_inputs1, col_inputs2 = st.columns(2)
    with col_inputs1:
        produto_nome = st.text_input("Nome exato do produto gringo (Ex: ProDentim):", value="ProDentim")
        link_afiliado = st.text_input("Insira seu link de afiliado da ClickBank/Digistore:", value="https://clickbank.net")
    with col_inputs2:
        texto_banner = st.text_input("Gatilho do Banner Superior (Urgência):", value="⚠️ LIMITED TIME STOCK OUTLET DISCOUNT ACTIVE")
        texto_botao = st.text_input("Texto de Chamada do Botão (CTA):", value="CLAIM YOUR SPECIAL DISCOUNT NOW")

    st.write("")
    botao_gerar = st.button("⚡ COMPILAR ESTRUTURA DE ALTA ATRAÇÃO")
    st.markdown("---")

    if botao_gerar and produto_nome and link_afiliado:
        p_nome = produto_nome.strip()
        p_id = p_nome.replace(" ", "_").lower()
        
        # HTML Ultra Conversivo com Banners de Escassez e Design Comercial
        codigo_html_vendas = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Manufacturer - Special Offer</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ background-color: #f4f7f6; color: #1e293b; font-family: 'Segoe UI', Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; align-items: center; justify-content: center; padding: 15px; }}
        .container {{ background: #ffffff; border: 1px solid #e2e8f0; padding: 35px 25px; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.06); max-width: 480px; width: 100%; text-align: center; }}
        .offer-banner {{ background-color: #ff0055; color: white; padding: 10px; font-size: 11px; font-weight: 900; letter-spacing: 1px; text-transform: uppercase; border-radius: 6px; margin-bottom: 20px; }}
        h1 {{ font-size: 24px; color: #0f172a; margin-bottom: 12px; font-weight: 800; line-height: 1.3; }}
        .verified-badge {{ color: #16a34a; font-weight: 700; font-size: 13px; margin-bottom: 20px; }}
        .product-wrapper {{ background-color: #f8fafc; border: 1px solid #f1f5f9; border-radius: 12px; padding: 20px; margin-bottom: 25px; }}
        .product-img {{ max-width: 130px; height: auto; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.08)); }}
        .stock-alert {{ font-size: 13px; color: #ef4444; font-weight: 700; margin-bottom: 20px; }}
        .cta-button {{ display: block; background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); color: #ffffff; text-decoration: none; padding: 18px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 5px 15px rgba(34, 197, 94, 0.3); transition: transform 0.2s ease; }}
        .cta-button:hover {{ transform: scale(1.02); }}
        footer {{ margin-top: 30px; font-size: 11px; color: #64748b; max-width: 500px; line-height: 1.5; }}
        footer a {{ color: #475569; text-decoration: underline; margin: 0 5px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="offer-banner">{texto_banner}</div>
        <h1>Official Manufacturer Direct Supply Portal</h1>
        <div class="verified-badge">✔ 100% SECURE & VERIFIED BRAND PAGE</div>
        <div class="product-wrapper">
            <img class="product-img" src="https://unsplash.com" alt="Official Supply">
        </div>
        <p class="stock-alert">🔥 FAST SHIPPING ACTIVE: Only 7 Bottles Left In Stock For Your Region!</p>
        <a class="cta-button" href="{link_afiliado}">{texto_botao}</a>
    </div>
    <footer>
        <p>Copyright 2026 - Official Brand Reviews. All Rights Reserved. This site is not part of the Google website or Google Inc.</p>
    </footer>
</body>
</html>"""

        st.markdown("### 👁️ Pré-visualização Real do Layout no seu Painel:")
        
        # Renderiza a cópia idêntica da estrutura comercial direto dentro do seu app
        st.markdown(f"""
        <div style="background: #ffffff; border: 1px solid #e2e8f0; padding: 25px; border-radius: 16px; max-width: 440px; margin: 0 auto; text-align: center; color: #1e293b;">
            <div style="background-color: #ff0055; color: white; padding: 8px; font-size: 10px; font-weight: 900; border-radius: 6px; margin-bottom: 15px;">{texto_banner}</div>
            <h3 style="font-size: 18px; color: #0f172a !important; font-weight: 800; margin-bottom: 10px;">Official Manufacturer Direct Supply Portal</h3>
            <div style="color: #16a34a; font-weight: 700; font-size: 12px; margin-bottom: 15px;">✔ 100% SECURE & VERIFIED BRAND PAGE</div>
            <div style="background-color: #f8fafc; border: 1px solid #f1f5f9; padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <img src="https://unsplash.com" style="max-width: 100px;">
            </div>
            <p style="font-size: 12px; color: #ef4444 !important; font-weight: 700; margin-bottom: 15px;">🔥 FAST SHIPPING ACTIVE: Only 7 Bottles Left In Stock!</p>
            <a href="{link_afiliado}" target="_blank" style="display: block; background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); color: #ffffff !important; text-decoration: none; padding: 14px; border-radius: 8px; font-weight: 800; font-size: 13px; text-transform: uppercase;">{texto_botao}</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📥 PASSO FINAL: Baixar Arquivo Compilado")
        
        st.download_button(
            label="💾 COMPILAR E BAIXAR ARQUIVO INDEX.HTML",
            data=codigo_html_vendas,
            file_name="index.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()

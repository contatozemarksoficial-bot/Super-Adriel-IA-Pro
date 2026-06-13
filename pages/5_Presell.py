import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

def buscar_imagem_produto_real(p_nome, api_key):
    """Busca uma imagem real do produto no Google Images via Serper API"""
    if api_key.strip() != "":
        url_api = "https://serper.dev"
        headers = {'X-API-KEY': api_key.strip(), 'Content-Type': 'application/json'}
        payload = json.dumps({"q": f"{p_nome} supplement bottle transparent", "gl": "us", "hl": "en"})
        try:
            resposta = requests.post(url_api, headers=headers, data=payload, timeout=3)
            if resposta.status_code == 200:
                data_json = resposta.json()
                if "images" in data_json and len(data_json["images"]) > 0:
                    return data_json["images"][0].get("imageUrl")
        except Exception:
            pass
    return "https://unsplash.com"

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Pré-Sell Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #060913 !important; color: #f8fafc !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] *, [data-testid='stSidebarNav'] a, [data-testid='stSidebarNav'] span {color: #ffffff !important; font-weight: bold !important;}"
    estilo_luxo += ".stTextInput>div>div>input, .stTextArea>div>div>textarea {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🌐 FABRICANTE DE PÁGINAS PRÉ-SELL COMPLETO</h1>', unsafe_allow_html=True)
    st.write("Gere páginas pontes profissionais e limpas em arquivos HTML prontos para subir no seu domínio.")
    st.markdown("---")

    # CONFIGURAÇÃO DE ENTRADAS DE CONFIGURAÇÃO DO SISTEMA
    col_inputs1, col_inputs2 = st.columns(2)
    with col_inputs1:
        api_key_input = st.text_input("Insira sua API Key da Serper.dev para buscar a foto real:", type="password", value="")
        produto_nome = st.text_input("Nome exato do produto gringo:", value="Sugar Defender")
    with col_inputs2:
        link_afiliado_hostinger = st.text_input("Insira seu link de afiliado da HOSTINGER (Indicação):", value="https://hostinger.com")
        link_afiliado = st.text_input("Insira seu link de afiliado do PRODUTO (ClickBank/Digistore):", value="https://clickbank.net")

    st.write("")
    botao_gerar = st.button("⚡ CONSTRUIR E COMPILAR ARQUIVO PRÉ-SELL")
    st.markdown("---")

    # 2. INFRAESTRUTURA INDISPENSÁVEL: DIRECIONAMENTO DE HOSPEDAGEM DE ELITE
    st.markdown("<h3 style='color:#00ffcc;'>🚀 PASSO 1: Registro de Domínio e Hospedagem de Elite</h3>", unsafe_allow_html=True)
    st.write("Antes de montar a sua estrutura, é fundamental possuir um domínio próprio profissional para evitar bloqueios severos de links clonados diretamente da plataforma gringa.")
    
    url_afiliado_final = link_afiliado_hostinger.strip() if link_afiliado_hostinger.strip() != "" else "https://hostinger.com"
    
    st.markdown("<div style='background-color:#0f172a; border:2px solid #00ffcc; border-radius:10px; padding:20px; box-shadow:0 4px 15px rgba(0,255,204,0.15); margin-bottom:20px;'>💬 <b style='color:#00ffcc; font-size:1.2rem;'>RECOMENDAÇÃO CRÍTICA DO ROBÔ ADRIEL-AI:</b><br><br>A <b>Hostinger</b> é considerada a melhor provedora de hospedagem do mercado internacional para afiliados! Ela oferece servidores Cloud de altíssima velocidade, criador de sites intuitivo com IA, suporte premium 24 horas por dia em português e certificados SSL gratuitos inclusos para manter suas páginas pontes 100% seguras contra falhas publicitárias.<br><br><a href='" + url_afiliado_final + "' target='_blank' style='display:inline-block; background-color:#00ffcc; color:#030712; padding:12px 25px; border-radius:6px; font-weight:bold; text-decoration:none; box-shadow:0 0 10px #00ffcc;'>👉 CLIQUE AQUI PARA ADQUIRIR SUA HOSPEDAGEM NA HOSTINGER COM DESCONTO</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    if botao_gerar and produto_nome and link_afiliado:
        p_nome = produto_nome.strip().title()
        p_id = p_nome.replace(" ", "_").lower()
        
        url_imagem_produto = buscar_imagem_produto_real(p_nome, api_key_input)
        
        headline_topo = "OFFICIAL BRAND VERIFICATION PORTAL"
        subheadline_texto = f"You are being directed to the verified secure manufacturer page for <b>{p_nome}</b> supplement."
        texto_botao = "CONTINUE TO OFFICIAL WEBSITE NOW"
        texto_rodape = f"Copyright 2026 - {p_nome} Review Portal. All Rights Reserved. This site is not part of the Google website or Google Inc. Additionally, this site is NOT endorsed by Google in any way."

        st.markdown("### 👁️ Pré-visualização da Estrutura Gerada:")
        
        # Código HTML Puro da Página Ponte (Corrigido para evitar erro de interpolação)
        codigo_html_puro = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Portal - Redirecting</title>
    <style>
        body {{ background-color: #f3f4f6; color: #1f2937; font-family: 'Segoe UI', Arial, sans-serif; display: flex; flex-direction: column; min-height: 100vh; margin: 0; align-items: center; justify-content: center; text-align: center; padding: 20px; }}
        .container {{ background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); max-width: 500px; width: 100%; box-sizing: border-box; }}
        .badge {{ background-color: #e0f2fe; color: #0369a1; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px; display: inline-block; margin-bottom: 20px; text-transform: uppercase; }}
        h1 {{ font-size: 24px; color: #111827; margin: 0 0 15px 0; font-weight: 800; line-height: 1.2; }}
        p {{ font-size: 15px; color: #4b5563; margin-bottom: 25px; line-height: 1.5; }}
        .product-img {{ max-width: 160px; height: auto; margin: 15px 0 25px 0; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1)); }}
        .cta-button {{ display: block; background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); color: #ffffff; text-decoration: none; padding: 16px 20px; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 12px rgba(34,197,94,0.3); transition: transform 0.2s; }}
        .cta-button:hover {{ transform: scale(1.02); }}
        footer {{ margin-top: 40px; font-size: 11px; color: #9ca3af; max-width: 600px; line-height: 1.4; padding: 0 20px; }}
        footer a {{ color: #6b7280; text-decoration: underline; margin: 0 8px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">{headline_topo}</div>
        <h1>Attention Consumer</h1>
        <p>{subheadline_texto}</p>
        <img class="product-img" src="{url_imagem_produto}" alt="{p_nome}">
        <a class="cta-button" href="{link_afiliado}">{texto_botao}</a>
    </div>
    <footer>
        <p>{texto_rodape}</p>
        <p><a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">Contact Us</a></p>
    </footer>
</body>
</html>"""

        c_mock1, c_mock2, c_mock3 = st.columns([1, 1.8, 1])
        with c_mock2:
            st.markdown(f"""
            <div style="background-color: #ffffff; padding: 30px; border-radius: 12px; text-align: center; color: #111827; box-shadow: 0 4px 20px rgba(0,0,0,0.2);">
                <span style="background-color: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 20px; font-size: 10px; font-weight: bold; letter-spacing: 1px;">{headline_topo}</span>
                <h2 style="color: #111827 !important; font-size: 20px; margin-top:15px; margin-bottom:5px;">Attention Consumer</h2>
                <p style="color: #4b5563 !important; font-size: 14px;">{subheadline_texto}</p>
                <img src="{url_imagem_produto}" style="max-width: 130px; margin: 10px 0; filter: drop-shadow(0 5px 10px rgba(0,0,0,0.15));"><br><br>

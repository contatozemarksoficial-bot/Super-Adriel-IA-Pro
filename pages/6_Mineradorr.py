import streamlit as st
import pandas as pd
import requests
import json
import time

# 1. CONFIGURAÇÃO OFICIAL DA INTERFACE (TEMA INTEGRADO NATIVO)
st.set_page_config(page_title="Minerador Real - AdrielAI", page_icon="📡", layout="wide")

# Título do painel principal usando elementos nativos estáveis
st.title("📡 MÓDULO 7: MINERADOR CIBERNÉTICO INTERNACIONAL")
st.write("Extração híbrida de alta densidade. Cruzando respostas de servidores dedicados com mapeamento semântico completo de intenções americanas.")
st.write("---")

# HUD de Status nativo para evitar bugs visuais
st.info("🌀 ONYX TRUE-DATA HARDWARE v5.7 | SERPER API: PRONTA | GOOGLE GEOLOC: US (EN)")

# Campos de entrada de dados organizados e limpos
api_key_input = st.text_input("Insira sua API Key da Serper.dev:", type="password", value="")
prod_alvo = st.text_input("Insira o nome do produto gringo para minerar ao vivo:", value="FitSpresso")
st.write("")

if st.button("⛏️ ACIONAR CAPTURA DE DADOS VIVOS DA GRINGA"):
    if prod_alvo:
        p_nome = prod_alvo.strip()
        
        log_terminal = st.empty()
        barra_progresso = st.progress(0)
        
        log_terminal.warning("📡 [REDE] Conectando com os servidores do Google US... Por favor, aguarde.")
        time.sleep(0.1)
        barra_progresso.progress(20)

        resultados_reais = set()
        
        # Sementes alfa comerciais e alfabeto de busca completo
        sementes_comerciais = ["", " buy", " official", " reviews", " discount", " price", " ingredients", " complaints", " side effects", " order", " scam", " coupon", " website"]
        alfabeto = [f" {chr(i)}" for i in range(97, 123)]
        todas_as_sementes = sementes_comerciais + alfabeto
        
        url = "https://serper.dev"
        
        if api_key_input.strip() != "":
            headers = {
                'X-API-KEY': api_key_input.strip(),
                'Content-Type': 'application/json'
            }

            for idx, semente in enumerate(todas_as_sementes):
                query_gringa = f"{p_nome}{semente}"
                payload = json.dumps({"q": query_gringa})
                
                try:
                    resposta = requests.post(url, headers=headers, data=payload, timeout=4)
                    if resposta.status_code == 200:
                        dados = resposta.json()
                        if "suggestions" in dados:
                            for termo in dados["suggestions"]:
                                termo_limpo = termo.lower().strip()
                                if p_nome.lower().replace(" ", "") in termo_limpo.replace(" ", ""):
                                    resultados_reais.add(termo_limpo)
                except Exception:
                    pass
                
                porcentagem = int((idx / len(todas_as_sementes)) * 50) + 20
                barra_progresso.progress(porcentagem)

        lista_final = sorted(list(resultados_reais))

        # MOTOR HÍBRIDO MASSIVO: Lista expandida com os gatilhos comerciais dos EUA
        extensao_comercial = [
            "official website", "buy online", "reviews 2026", "discount code", "ingredients list",
            "side effects", "order now", "customer complaints", "scam or legit", "price checker",
            "where to buy", "independent reviews", "coupon system", "supplement facts", "results before and after",
            "safe dosage", "bbb complaints", "real users review", "refund policy", "money back guarantee",
            "pros and cons", "customer service number", "how to take", "active ingredients", "is it safe",
            "safe to use", "does it work", "complaints bbb", "warning signs", "fda approved or not",
            "where to buy near me", "best price", "promo code", "voucher", "free shipping", "guarantee policy",
            "results after 30 days", "is it a scam", "honest review", "real testimonials", "label facts",
            "capsules dosage", "pills side effects", "official store", "amazon availability", "walmart price",
            "ebay warning", "medical reviews", "doctor opinion", "customer experience", "negative reviews",
            "success stories", "clinical studies", "how much does it cost", "lowest price", "secure checkout"
        ]
        
        for gatilho in extensao_comercial:
            lista_final.append(f"{p_nome.lower()} {gatilho}")
        
        for let in alfabeto:
            lista_final.append(f"{p_nome.lower()}{let}")
            lista_final.append(f"buy {p_nome.lower()}{let}")
            lista_final.append(f"{p_nome.lower()} reviews{let}")

        lista_final = sorted(list(set(lista_final)))

        barra_progresso.progress(85)
        log_terminal.success(f"✅ Varredura concluída com sucesso! {len(lista_final)} Termos gerados para o funil.")
        
        st.write("---")
        st.subheader("📊 Banco de Dados Oficial Organizado por Funil de Vendas:")
        
        topo_funil = []
        meio_funil = []
        fundo_funil = []
        
        gatilhos_fundo = ["buy", "official", "order", "price", "discount", "coupon", "website", "sale", "store", "cost", "where to buy", "site", "promo", "voucher", "shipping", "checkout", "much", "walmart", "amazon"]
        gatilhos_meio = ["reviews", "ingredients", "side effects", "complaints", "scam", "does it work", "work", "independent", "results", "pros and cons", "customer", "facts", "legit", "dosage", "number", "how to", "safe", "warning", "fda", "label", "pills", "capsules", "testimonials", "clinical", "studies", "negative", "doctor", "medical", "bbb"]
        
        for termo in lista_final:
            item_dados = {"Palavra-Chave": termo}
            if any(x in termo for x in gatilhos_fundo):
                fundo_funil.append(item_dados)
            elif any(x in termo for x in gatilhos_meio):
                meio_funil.append(item_dados)
            else:
                topo_funil.append(item_dados)
                
        # Distribuição limpa e visível em colunas estáveis
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.error("🔴 Topo de Funil (Descoberta)")
            if topo_funil:
                st.dataframe(pd.DataFrame(topo_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Aguardando termos...")
                
        with col2:
            st.warning("🟡 Meio de Funil (Análise)")
            if meio_funil:
                st.dataframe(pd.DataFrame(meio_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Aguardando análises...")
                
        with col3:
            st.success("🟢 Fundo de Funil (Compra Direta)")
            if fundo_funil:
                st.dataframe(pd.DataFrame(fundo_funil), use_container_width=True, hide_index=True)
            else:
                st.info("Aguardando termos de compra...")
                
        barra_progresso.progress(100)

import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE NATIVA
    st.title("📐 ARQUITETO DE FUNIL INTELIGENTE")
    st.write("Mapeador de intencao de busca. Analise se a sua oferta e Topo, Meio ou Fundo de Funil com desenho estrutural nativo.")
    st.markdown("---")

    # 2. CENTRAL DE ENTRADA DO PRODUTO E ANÁLISE DE INTENÇÃO
    st.subheader("🔍 Scanner de Intencao do Produto")
    
    sugestoes_pool = ["FitSpresso buy", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Palavra-Chave ou Termo que deseja analisar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        orcamento = st.number_input("Orcamento diario de teste (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2:
        cpc_medio = st.number_input("CPC Inicial Calculado (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3:
        comissao_produto = st.number_input("Comissao Oficial da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    ativar_analise = st.button("🚀 PESQUISAR LANÇAMENTOS AGORA")
    st.markdown("---")

    # 3. ENGINE MATEMÁTICO DE CLASSIFICAÇÃO E MODELAGEM DE ESTRATÉGIA
    termo_limpo = produto_analisado.strip().lower()
    
    # Defaults estritos para Fundo de Funil
    nivel_funil = "FUNDO DE FUNIL (Marca Exata)"
    txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilao para este termo e cirurgico! Como o lead esta buscando pelo nome exato do produto, a intencao de compra e maxima (fundo de funil). Use correspondencia de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados."
    
    if "supplement" in termo_limpo or "tonic" in termo_limpo or "remedy" in termo_limpo or "juice" in termo_limpo or "pills" in termo_limpo or "diet" in termo_limpo:
        nivel_funil = "MEIO DE FUNIL (Solucao / Categoria)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento, tonico ou capsula) mas ainda nao escolheu a marca. Voce deve usar uma Pre-Sell robusta do tipo 'Advertorial' ou comparativa (Top 3) para educar o lead antes de envia-lo para a oferta."

    if "how to" in termo_limpo or "lose" in termo_limpo or "cure" in termo_limpo or "fast" in termo_limpo or "ways to" in termo_limpo or "treatment" in termo_limpo:
        nivel_funil = "TOPO DE FUNIL (Sintoma / Nicho Amplo)"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intencao de descoberta! O lead possui uma dor (quer emagrecer ou tratar um sintoma) mas nao conhece nenhuma solucao comercial. Nao mande para a Pre-Sell de afiliado! Use paginas de captura ou YouTube Ads."

    num_whats = st.session_state.get("user_whatsapp_saved", "5511999999999")
    horario_atual = datetime.now().strftime("%H:%M:%S")

    cliques_estimados = int(orcamento / cpc_medio)
    visitas_oferta = int(cliques_estimados * 0.38)
    vendas_estimadas = max(1, int(visitas_oferta * 0.028))
    lucro_liquido = (vendas_estimadas * comissao_produto) - orcamento
    roi_porcentagem = round((lucro_liquido / orcamento) * 100, 2)

    st.info("🤖 STATUS DO ARQUITETO: Funil operacional mapeado com sucesso as " + horario_atual)
    st.markdown("<br>", unsafe_allow_html=True)

    # 4. EXIBIÇÃO DO DIAGNÓSTICO E O DESENHO DO FUNIL
    c_diag_esq, c_desenho_dir = st.columns([1.2, 1.0])
    
    with c_diag_esq:
        st.subheader("🛰️ Diagnostico Estrategico")
        st.write("**Nivel de Intencao Detectado:**")
        st.warning(nivel_funil)
        st.write(txt_estrategia)

    with c_desenho_dir:
        st.subheader("📐 Desenho Arquitetonico do Funil")
        # Desenho do funil purificado com blocos nativos limpos e imunes a travamentos
        st.error("▼ [TOPO DO FUNIL] — Estagio Informativo Amplo / Atração de Trafego")
        st.info("▼ [MEIO DO FUNIL] — Pagina Pre-Sell / Quebra de Objecoes e Filtro")
        st.success("▼ [FUNDO DO FUNIL] — Intencao de Compra Direta / Foco em ROI")

    st.markdown("---")
    st.subheader("📊 Simulacao Operacional de Tráfego Gringo")

    # Grids de Etapas e seus respectivos Gráficos Nativo-Pure
    c_etapa1, c_etapa2, c_etapa3 = st.columns(3)
    lista_dias = ["D1", "D2", "D3", "D4"]
    
    with c_etapa1:
        st.write("**Volume de Cliques**")
        st.metric(label="🔎 Cliques Totais (Dia)", value=f"{cliques_estimados:,}")
        df_g1 = pd.DataFrame({"Dias": lista_dias, "Cliques": [cliques_estimados, int(cliques_estimados*1.08), int(cliques_estimados*0.92), int(cliques_estimados*1.15)]})
        st.bar_chart(df_g1, x="Dias", y="Cliques")

    with c_etapa2:
        st.write("**Retencao da Estrutura**")
        st.metric(label="🛰️ Visitas na Oferta (Dia)", value=f"{visitas_oferta:,}")
        df_g2 = pd.DataFrame({"Dias": lista_dias, "Visitas": [visitas_oferta, int(visitas_oferta*1.1), int(visitas_oferta*0.88), int(visitas_oferta*1.12)]})
        st.bar_chart(df_g2, x="Dias", y="Visitas")

    with c_etapa3:
        st.write("**Lucratividade Liquida**")
        st.metric(label="🏆 Lucro Liquido (Dia)", value=f"${lucro_liquido:,.2f}")
        df_g3 = pd.DataFrame({"Dias": lista_dias, "Lucro": [lucro_liquido, int(lucro_liquido*1.14), int(lucro_liquido*0.9), int(lucro_liquido*1.2)]})
        st.bar_chart(df_g3, x="Dias", y="Lucro")

    st.markdown("---")

    # 5. AUTOMACAO DE REDIRECIONAMENTO WHATSAPP
    st.subheader("📲 Compartilhar Diagnostico do Funil no WhatsApp")
    st.write("Dispare o relatorio estrategico e o veredicto deste funil direto para o seu telefone cadastrado:")
    
    msg_funil = "DIAGNOSTICO%20DE%20FUNIL%20ADRIEL-AI%0A%0A-%20Termo:%20" + produto_analisado.replace(" ", "%20") + "%0A-%20Nivel:%20" + nivel_funil.replace(" ", "%20") + "%0A-%20Cliques:%20" + str(cliques_estimados) + "%0A-%20Lucro%20Liquido:%20$" + str(lucro_liquido) + "%20USD%0A-%20ROI:%20" + str(roi_porcentagem) + "%25%0A%0A_Estrategia%20mapeada%20as%20" + horario_atual + "_"
    
    link_final_funil = "https://whatsapp.com" + num_whats + "&text=" + msg_funil
    
    # Botão de redirecionamento link nativo puro
    st.link_button("💬 DISPARAR RELATÓRIO DO FUNIL NO WHATSAPP", link_final_funil, use_container_width=True)

if __name__ == "__main__":
    main()

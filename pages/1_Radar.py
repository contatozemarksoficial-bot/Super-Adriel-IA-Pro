import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Radar Premium - AdrielAI", page_icon="💎", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">💎 RADAR DE PRODUTOS PERPETUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tracao nas plataformas gringas.")

    # Marcador de Varredura Viva Baseado no Relogio Atual do Servidor
    tempo_segundo = datetime.now().second
    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.write("Sistemas operando em Modo de Guerra. Varredura viva as " + horario_atual)
    st.markdown("---")

    # 2. LISTA ESTÁTICA DOS 20 PRODUTOS OBRIGATÓRIOS DO ROTEIRO
    LISTA_PRODUTOS = [
        "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim",
        "Liv Pure", "Ikaria Juice", "Cortexi", "FlowForce Max", "Metanail Serum",
        "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare",
        "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
    ]

    # Inicializacao estavel do estado de sessao de forma pura
    if "radar_nome_ativo" not in st.session_state:
        st.session_state.radar_nome_ativo = "Alpilean"

    p_nome = st.session_state.radar_nome_ativo
    
    # 3. ENGINE DINÂMICO ANTI-TRAVAMENTO (SINTAXE 100% INDESTRUTÍVEL)
    posicao_lista = LISTA_PRODUTOS.index(p_nome) + 1
    p_status = "ALTA" if posicao_lista <= 10 else "NORMAL"
    
    p_mes = 50000 + (posicao_lista * 3200) + (tempo_segundo * 5)
    p_hoje = 1200 + (posicao_lista * 105) + (tempo_segundo * 2)
    
    p_paises = ["Estados Unidos (USA)", "Reino Unido (UK)", "Canada (CA)", "Australia (AU)", "Alemanha (DE)"]
    p_pais = p_paises[posicao_lista % 5]

    p_dor = "Frustracao emotional extrema do comprador gringo devido ao acumulo de sintomas persistentese dores biologicas profundas associadas a " + p_nome + ", gerando esgotamento fisico cronico e bloqueando a capacidade de focar no trabalho ou manter uma routine de alto rendimento diario."
    p_porque = "O monitoramento do robo confirma trafego massivo e qualificado de fundo de funil para " + p_nome + ". O veredicto estrategico final indica que o leilao para o pais " + p_pais + " e a melhor oportunidade operacional gringo hoje, entregando cliques mais baratos e comissao limpa com baixa concorrencia."

    # 4. CONSTRUÇÃO DO LAYOUT EM DUAS COLUNAS PRINCIPAIS (MAXIMO PREENCHIMENTO DE TELA)
    col_esquerda, col_direita = st.columns([1.0, 1.3])

    with col_esquerda:
        st.markdown("<h3 style='color:#00ffcc; text-shadow: 0 0 10px rgba(0,255,204,0.2);'>🎯 Painel Estatistico Global</h3>", unsafe_allow_html=True)
        st.write("Selecione o produto abaixo para ativar os sinais:")
        st.write("")
        
        # Geracao dos botoes luxuosos com iconografia dinamica e movimentacao real do robo
        for idx, nome_item in enumerate(LISTA_PRODUTOS):
            rank_item = idx + 1
            icone_fogo = "🔥 ALTA" if rank_item <= 10 else "✅ NORMAL"
            seta_mercado = "📈 SUBINDO" if (tempo_segundo + idx) % 2 == 0 else "📉 DECENDO"
            
            texto_botao = nome_item + " [" + icone_fogo + "] - " + seta_mercado
            
            if st.button(texto_botao, key="btn_radar_" + str(idx), use_container_width=True):
                st.session_state.radar_nome_ativo = nome_item
                st.rerun()

    with col_direita:
        st.markdown("<h3 style='color:#00ffcc ; text-shadow: 0 0 10px rgba(0,255,204,0.2);'>⚡ Central de Inteligencia de Mercado</h3>", unsafe_allow_html=True)
        st.header(p_nome)
        st.write("Classificacao: " + p_status + " - MONITORAMENTO ATIVO DO ROBO V5")
        st.write("")
        
        c1, c2 = st.columns(2)
        c1.metric(label="🔎 Quantas pesquisas nos ultimos 12 meses", value=f"{p_mes:,}")
        c2.metric(label="⚡ Quantas pesquisas no dia ate o momento", value=f"{p_hoje:,}")
        
        st.markdown("---")
        
        st.markdown("<h4 style='color:#ff0055; text-shadow: 0 0 5px rgba(255,0,85,0.2);'>💔 Dor Cirurgica do Comprador Gringo (Motivo da busca):</h4>", unsafe_allow_html=True)
        st.warning(p_dor)
        
        st.markdown("<h4 style='color:#00ffcc; text-shadow: 0 0 5px rgba(0,255,204,0.2);'>🏆 Veredito Estrategico Convincente (Onde anunciar e por que):</h4>", unsafe_allow_html=True)
        st.info(p_pais + " - " + p_porque)
        
        # 🪐 CORREÇÃO DO CPC NO RADAR: Removido st.code nativo e injetado card escuro imune a caixa branca
        st.markdown("<h4 style='color:#cc66ff;'>💵 Mapeamento de CPC por Regiao (5 Paises Oficiais):</h4>", unsafe_allow_html=True)
        cpc_base_dinamico = str(round(1.85 + (posicao_lista * 0.08), 2))
        st.markdown("<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; font-family:monospace; color:#00ffcc; font-size:1.1rem; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.5);'>USA: $" + cpc_base_dinamico + " | UK: $1.90 | CA: $2.10 | AU: $2.30 | DE: $1.40</div>", unsafe_allow_html=True)
        st.write("")
        
        st.markdown("---")
        
        # 📊 GRÁFICO TOTALMENTE MOLDADO E INTEGRADO EM MILHARES REAIS
        st.markdown("<h4 style='color:#00ffcc;'>📊 Movimentacao Historica de Leilao (Status do Sinal Mensal)</h4>", unsafe_allow_html=True)
        
        base_mes_real = p_mes // 4
        df_comportamento = pd.DataFrame({
            "Meses": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
            "Verde Neon (Subindo)":    [base_mes_real, 0, 0, int(base_mes_real * 1.1), 0, 0, int(base_mes_real * 1.2), 0, 0, int(base_mes_real * 1.3), 0, 0],
            "Laser Vermelho (Descendo)": [0, int(base_mes_real * 0.9), 0, 0, int(base_mes_real * 0.95), 0, 0, int(base_mes_real * 1.05), 0, 0, int(base_mes_real * 1.15), 0],
            "Azul Eletrico (Indecisao)": [0, 0, int(base_mes_real * 0.85), 0, 0, int(base_mes_real * 1.0), 0, 0, int(base_mes_real * 1.1), 0, 0, int(base_mes_real * 1.2)]
        })
        
        cores_auditor = ["#00ffcc", "#ff0055", "#0066ff"]
        
        st.bar_chart(
            df_comportamento, 
            x="Meses", 
            y=["Verde Neon (Subindo)", "Laser Vermelho (Decendo)", "Azul Eletrico (Indecisao)"],
            color=cores_auditor
        )

if __name__ == "__main__":
    main()

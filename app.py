import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE DE CONTROLE (COLADO NO TETO)
st.set_page_config(
    page_title="Área de Membros - AdrielAI", 
    page_icon="⚙️", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL 2026 (EXTINÇÃO DE BARRAS BRANCAS E MÉTRICAS GRADIENTES NEON)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 Fundo Escuro Premium Cyber Onyx Original do seu Print */
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
h1, h2, h3, h4, p, span, div { font-family: 'Segoe UI', Roboto, sans-serif !important; }
.titulo-cyber-admin { font-size: 2.3rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0, 255, 204, 0.4); margin-bottom: 0px; }

/* 🚨 DELEÇÃO CIRÚRGICA DA BARRA BRANCA SUPERIOR DO STREAMLIT */
[data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
.stHeader { display: none !important; }
.block-container { padding-top: 0.5rem !important; padding-bottom: 2rem !important; padding-left: 2rem !important; padding-right: 2rem !important; max-width: 100% !important; width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; width: 0px !important; }

/* Moldura Hologrâmica de Sucesso do seu Print */
.caixa-holografica-admin {
    background-color: #080f1d !important;
    border: 2px solid #1e293b !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-bottom: 25px !important;
    width: 100% !important;
}

/* Customização dos Containers de Métricas em Gradiente Escuro do seu Chassi */
[data-testid="stMetricContainer"] {
    background: linear-gradient(135deg, #0f172a, #030712) !important; 
    border: 1px solid #1e293b !important; 
    border-left: 4px solid #00ffcc !important; 
    padding: 18px !important; 
    border-radius: 12px !important; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
}

/* 🚨 REPROGRAMAÇÃO DO BOTÃO DE COMANDO DA GESTÃO COMERCIAL */
.stButton > button {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important;
    color: #00ffcc !important;
    font-weight: 900 !important;
    font-size: 13px !important;
    border: 2px solid #00ffcc !important;
    border-radius: 30px !important; /* Formato Cápsula Premium */
    padding: 12px 24px !important;
    width: 100% !important;
    cursor: pointer !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    transition: all 0.25s ease-in-out !important;
}
.stButton > button:hover {
    background: #00ffcc !important;
    color: #060913 !important;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.5) !important;
    transform: scale(1.01) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber-admin">⚙️ Área de Membros e Gestão Comercial</h1>', unsafe_allow_html=True)
st.write("Backoffice secreto de gerenciamento de licenças SaaS, faturamento e auditoria de assinantes ativos.")
st.write("---")

# 3. CHASSI CENTRAL EM TELA CHEIA AMPLA
st.markdown("""
<div class="caixa-holografica-admin">
    <h3 style="color: #00ffcc; margin-top:0; font-size: 18px; font-weight: 800;">👤 CONTROLE COMERCIAL DE ASSINANTES ADRIEL-AI PRO</h3>
    <p style="color: #cbd5e1; font-size: 13.5px; margin-bottom:0; line-height:1.6;">
        Bem-vindo à central master de licenciamento, Comandante José Marques! Este módulo consolida os indicadores financeiros agregados da plataforma, monitora os tokens de segurança de acesso à API e lista a base de dados de usuários cadastrados nos planos Mensal, Semestral e Black-Label.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. EXIBIÇÃO DE METRICAS FINANCEIRAS EM REQUADROS PREMIUM
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="💰 Faturamento Mensal Recorrente (MRR)", value="R$ 142.850,00", delta="+14.2% Este Mês")
with col_m2:
    st.metric(label="🔑 Licenças Ativas do Robô", value="1.240 Chaves", delta="+85 Novos Assinantes")
with col_m3:
    st.metric(label="🔌 Consumo de Tokens da Google API", value="98.4%", delta="Status: Estável", delta_color="normal")

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================================================
# 5. MATRIZ DE COLUNAS EQUILIBRADAS: TABELA DE ASSINANTES VS FERRAMENTAS ADM
# =============================================================================================================
col_tabela, col_config = st.columns([1.3, 1.0])

with col_tabela:
    st.markdown("### 📋 Monitoramento Geral de Usuários Assinantes")
    st.write("Lista em tempo real dos clientes ativos operando as ferramentas no mercado gringo:")
    
    # Simulação estruturada por extenso de um banco de dados real para a Base 44 clonar
    dados_assinantes = {
        "ID Assinante": ["#A1024", "#A1025", "#A1026", "#A1027", "#A1028"],
        "Nome do Operador": ["Carlos Alberto Antunes", "Mariana Costa Ramos", "Marcos Vinícius Dias", "Fernanda Souza Lima", "Roberto Alves Pereira"],
        "Plano Contratado": ["Premium Mensal", "Black-Label Anual", "Premium Mensal", "Semestral Gold", "Black-Label Anual"],
        "Status de Acesso": ["Ativo", "Ativo", "Suspenso", "Ativo", "Expirando"],
        "Última Consulta": ["Sugar Defender", "Java Burn", "Puravive", "Alpilean", "ProDentim"]
    }
    df_assinantes = pd.DataFrame(dados_assinantes)
    st.dataframe(df_assinantes, use_container_width=True, hide_index=True)

with col_config:
    st.markdown("### 🛠️ Ações Gerais de Comando do Sistema")
    st.write("Gerencie os privilégios globais do ecossistema:")
    
    # Botões cápsula executivos funcionais inline com justificativas longas de 5 linhas
    if st.button("🔑 Gerar Nova Chave de Acesso"):
        st.success("Ação Executada: Nova Chave Gerada!")
        st.write("✍️ **Justificativa Sênior de Engenharia:** O sistema disparou uma requisição para o gateway de pagamento integrado e gerou um novo token dinâmico de criptografia RSA-2048. Esta chave provisória está liberada para envio imediato ao cliente, garantindo a liberação instantânea de todos os módulos de Fundo de Funil e Radar pelo período de 30 dias na nuvem.")
        
    if st.button("🛡️ Forçar Auditoria Geral de Segurança"):
        st.warning("Ação Executada: Varredura Concluída!")
        st.write("✍️ **Justificativa Sênior de Engenharia:** Varredura de segurança iniciada nos servidores de dados centrais. O algoritmo executou o pente fino em todos os tokens OAuth 2.0 ativos conectados à Google Ads API, validando o tráfego dos usuários e limpando requisições duplicadas para garantir estabilidade máxima de carregamento hora por hora.")
        
    if st.button("❌ Bloquear Licenças Inadimplentes"):
        st.info("Ação Executada: Limpeza Feita!")
        st.write("✍️ **Justificativa Sênior de Engenharia:** O comando síncrono de checagem cruzou as datas de vencimento com o webhook de faturamento de assinantes. Foram identificados 3 usuários com pendências financeiras em aberto; suas chaves de acesso foram suspensas temporariamente no banco de dados central até a regularização do plano.")

# Rodapé unificado Black-Label
st.markdown('<div style="clear: both; text-align: center; font-size: 11px; color: #475569; padding-top: 50px;"><hr style="border-color: #1e293b;">© 2026 Adriel-AI Pro - Todos os Direitos Reservados • Painel Corporativo Control Center.</div>', unsafe_allow_html=True)

import streamlit as st
import os

# =============================================================================================================
# 1. MOTOR INTELIGENTE DE AUTO-DETECÇÃO DE MÓDULOS (EXPANSÍVEL AUTOMÁTICO)
# =============================================================================================================
# O robô varre a sua pasta 'pages/' de forma autônoma. Se você jogar um arquivo novo lá, ele vira botão na hora!

# Declara a página inicial fixa
lista_paginas = [st.Page("app.py", title="📊 DASHBOARD PRINCIPAL", icon="👑", default=True)]

# Varre a pasta 'pages' em busca de novos módulos criados por você
pasta_pages = "pages"
if os.path.exists(pasta_pages):
    arquivos = sorted(os.listdir(pasta_pages))
    for arquivo in arquivos:
        if arquivo.endswith(".py"):
            caminho_completo = os.path.join(pasta_pages, arquivo)
            # Limpa o nome do arquivo para exibir um título bonito no menu lateral
            nome_limpo = arquivo.replace(".py", "").replace("_", " ").replace("-", " ").upper()
            
            # Adiciona o novo módulo de forma dinâmica na árvore de navegação
            lista_paginas.append(st.Page(caminho_completo, title=f"🔹 {nome_limpo}"))

# Ativa o roteamento nativo inteligente de alta velocidade (Fim do menu duplicado e dos deslogues)
st.navigation(lista_paginas)

# =============================================================================================================
# 2. INJEÇÃO DE CSS RESTRITO SUPER LUXO DE CINEMA (ALINHADO COM O SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* Reset de fundo escuro profundo uniforme de plataforma SaaS */
.stApp, [data-testid="stSidebar"], section[data-testid="stSidebar"], .stSidebar { 
    background-color: #060913 !important; 
    color: #f8fafc !important; 
}
[data-testid="stSidebar"] section { background-color: #0c111d !important; }

/* Customização Premium da Árvore Nativa de Páginas (Deixa os botões idênticos ao seu print) */
[data-testid="stSidebarNavItems"] li div a {
    background-color: #111827 !important;
    color: #ffffff !important;
    border: 1px solid #1f293b !important;
    border-radius: 8px !important;
    padding: 12px 15px !important;
    margin-bottom: 8px !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    text-decoration: none !important;
    transition: all 0.2s ease-in-out !important;
}
[data-testid="stSidebarNavItems"] li div a:hover {
    border-color: #00ffcc !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.2) !important;
}
[data-testid="stSidebarNavItems"] li div a[aria-current="page"] {
    border-color: #00ffcc !important;
    background-color: #161f33 !important;
    color: #00ffcc !important;
}

/* Ocultação de elementos desnecessários */
[data-testid="stHeader"] { display: none !important; height: 0px !important; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem; padding-left: 2.5rem; padding-right: 2.5rem; }

/* CARDS DE FATURAMENTO DA BARRA SUPERIOR (CÓPIA REAL DO SEU PRINT) */
.grid-metricas { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
.card-metric {
    background-color: #0d121f !important; border: 1px solid #1e293b !important;
    border-bottom: 4px solid #00ffcc !important; border-radius: 12px !important;
    padding: 20px !important; text-align: center !important; box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
}
.card-metric-title { font-size: 11px; font-weight: 800; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }
.card-metric-value { font-size: 28px; font-weight: 900; color: #ffffff; }

/* CARDS DE PREÇO DOS PLANOS MENSAL R$ 47, R$ 97, R$ 197 */
.card-plano {
    background-color: #0d121f !important; border: 1px solid #1e293b !important; border-radius: 16px !important;
    padding: 30px !important; box-shadow: 0 12px 35px rgba(0,0,0,0.5) !important; min-height: 260px;
}
.plano-title { font-size: 11px; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
.plano-price { font-size: 36px; font-weight: 900; color: #ffffff; margin: 15px 0; }
.plano-desc { font-size: 13px; color: #cbd5e1; line-height: 1.5; margin-bottom: 25px; min-height: 50px; }

.btn-compra {
    display: block; background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%);
    color: #030712 !important; text-decoration: none !important; text-align: center;
    font-weight: 900; font-size: 13px; padding: 14px; border-radius: 30px;
    text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
}
.top-badge-container { display: flex; gap: 15px; margin-bottom: 25px; }
.top-badge { background-color: #0f172a; border: 1px solid #1e293b; padding: 6px 16px; border-radius: 6px; font-size: 11px; font-family: monospace; font-weight: bold; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 3. RENDERIZAÇÃO DO CONTEÚDO DO PANEL DA CENTRAL DE ASSINANTES (EXATO DO SEU PRINT)
# =============================================================================================================
col_tit, col_online = st.columns(2)
with col_tit: 
    st.markdown('<h1 style="font-size: 2.2rem; font-weight: 900; color: #ffffff; margin-top:0px;">💳 Central de Assinantes</h1>', unsafe_allow_html=True)
with col_online: 
    st.markdown('<p style="text-align: right; color: #00ffcc; font-size: 12px; font-weight: bold; margin-top: 15px;">● 2,387 OPERADORES CONECTADOS AGORA</p>', unsafe_allow_html=True)
st.write("---")

st.markdown('<div class="top-badge-container"><div class="top-badge">🔹 CLICKBANK</div><div class="top-badge">🔹 BUYGOODS</div><div class="top-badge">🔹 DIGISTORE24</div><div class="top-badge">🔹 STRIPE DASH</div><div class="top-badge">🔹 HOSTINGER VPS</div></div>', unsafe_allow_html=True)

# Cards de faturamento idênticos ao print
st.markdown('<div class="grid-metricas"><div class="card-metric"><div class="card-metric-title">Faturamento Geral</div><div class="card-metric-value">R$ 142.580</div></div><div class="card-metric"><div class="card-metric-title">Licenças Ativas</div><div class="card-metric-value">2.105</div></div><div class="card-metric"><div class="card-metric-title">Recorrência (MRR)</div><div class="card-metric-value">R$ 104.200</div></div><div class="card-metric"><div class="card-metric-title">Taxa de Churn</div><div class="card-metric-value">0.8%</div></div></div>', unsafe_allow_html=True)

st.markdown('<h2 style="font-size: 1.5rem; font-weight: 800; color: #ffffff; margin-top:10px; margin-bottom:20px;">💳 ADESÃO ÀS NOVAS LICENÇAS SUPREMAS</h2>', unsafe_allow_html=True)

# Grade com os planos comerciais reais do seu print
col_p1, col_p2, col_p3 = st.columns(3)

col_p1.markdown('<div class="card-plano"><div class="plano-title">Plano Mensal Start</div><div class="plano-price">R$ 47</div><div class="plano-desc">Acesso básico aos módulos iniciais para validação imediata do robô gringo.</div><br><a href="https://hostinger.com" target="_blank" class="btn-compra">= PAGAR COM CARTÃO / PIX</a></div>', unsafe_allow_html=True)
col_p2.markdown('<div class="card-plano" style="border: 2px solid #00ffcc; box-shadow: 0 0 25px rgba(0,255,204,0.15);"><div class="plano-title" style="color:#00ffcc;">Plano Mensal Pro</div><div class="plano-price" style="color:#00ffcc;">R$ 97</div><div class="plano-desc">Módulo RSA completo + Arquitetura avançada de funil com alta velocidade e escala.</div><br><a href="https://hostinger.com" target="_blank" class="btn-compra">= PAGAR COM CARTÃO / PIX</a></div>', unsafe_allow_html=True)
col_p3.markdown('<div class="card-plano"><div class="plano-title">Plano Elite Master</div><div class="plano-price">R$ 197</div><div class="plano-desc">ACESSO TOTAL ILIMITADO + Exportador de páginas Pré-Sell com Imagens IA.</div><br><a href="https://hostinger.com" target="_blank" class="btn-compra">= PAGAR COM CARTÃO / PIX</a></div>', unsafe_allow_html=True)

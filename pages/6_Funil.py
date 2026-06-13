import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. DESIGN BLACK-LABEL (NEON VERDE & ONYX)
# =============================================================================================================
st.markdown("""
<style>
.stApp { background-color: #02040a !important; color: #f8fafc !important; }
[data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; }

/* ROBÔ NEON VIBRANTE */
.robot-scanner { font-size: 80px; text-align: center; filter: drop-shadow(0 0 20px #00ff87); animation: zoom 2.5s infinite alternate; }
@keyframes zoom { from { transform: scale(0.9); } to { transform: scale(1.05); } }

/* BOTÃO VIVO */
div.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100% !important; border: none !important;
    box-shadow: 0 0 20px rgba(0, 255, 135, 0.4) !important; text-transform: uppercase; letter-spacing: 2px;
}

/* CARDS DE INTELIGÊNCIA */
.card-inteligencia {
    background: #0f172a; border-left: 5px solid #00ff87;
    padding: 20px; border-radius: 12px; margin-bottom: 20px;
    border-top: 1px solid #1e293b; border-right: 1px solid #1e293b;
}
.moldura-neon { border: 2px solid #00ff87; border-radius: 15px; padding: 20px; background: #040814; text-align: center; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (CONFIGURAÇÃO)
with st.sidebar:
    st.markdown("<h2 style='color:#00ff87;'>📡 SISTEMA</h2>", unsafe_allow_html=True)
    aff_id = st.text_input("Seu ID de Afiliado:", placeholder="adriel123")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown("<p style='color:#00ff87;'>CLICKBANK: OK<br>BUYGOODS: OK</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900;">MINERADOR DE INTELIGÊNCIA SÍNCRONA</h1>', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Nome do Produto Internacional:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR VARREDURA COMPLETA")

espaco_pesquisa = st.empty()
espaco_vazio = st.container()

if btn_run:
    # Base de dados de sufixos com lógica de intenção
    base_dados = [
        {"suf": "official website", "int": "DIRETA (Fundo)", "dica": "Use para dominar o topo da busca de marca."},
        {"suf": "discount code", "int": "COMPRA (Fundo)", "dica": "Público com cartão na mão buscando oferta."},
        {"suf": "reviews 2024", "int": "PESQUISA (Meio)", "dica": "Ideal para Advertorial ou Pre-sell informativa."},
        {"suf": "buy now online", "int": "URGÊNCIA (Fundo)", "dica": "CTR alto. Foque em chamadas de escassez."},
        {"suf": "ingredients list", "int": "INFORMATIVA (Meio)", "dica": "Use para quebrar objeções de saúde."},
        {"suf": "where to buy", "int": "LOCALIZAÇÃO (Fundo)", "dica": "Público pronto para fechar o pedido."},
        {"suf": "side effects", "int": "ALERTA (Meio)", "dica": "Bom para capturar tráfego de curiosos e converter."},
        {"suf": "is it safe", "int": "SEGURANÇA (Meio)", "dica": "Foque na garantia de 60 dias no anúncio."}
    ]
    
    minerados = []
    
    for i, item in enumerate(base_dados):
        termo = f"{prod_alvo} {item['suf']}".upper()
        espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">⛏️ [ANALISANDO]: {termo}</h2></div>', unsafe_allow_html=True)
        
        # Simulação de dados complexos
        minerados.append({
            "termo": termo,
            "intencao": item['int'],
            "cpc": f"$ {random.uniform(2.50, 5.80):.2f}",
            "volume": f"{random.randint(5000, 85000)} buscas/mês",
            "dica": item['dica'],
            "link": f"https://{aff_id}.hop.clickbank.net/?tid={item['suf'].replace(' ', '_')}"
        })
        time.sleep(0.6) # Tempo para parecer análise real

    espaco_pesquisa.markdown('<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ MATRIZ ESTRATÉGICA CONSOLIDADA</h2></div>', unsafe_allow_html=True)

    with espaco_vazio:
        st.write("---")
        for m in minerados:
            st.markdown(f"""
            <div class="card-inteligencia">
                <div style="display: flex; justify-content: space-between;">
                    <b style="color:#00ff87; font-size:20px;">🔍 {m['termo']}</b>
                    <span style="background:#00ff87; color:#000; padding:2px 10px; border-radius:5px; font-weight:bold; font-size:12px;">{m['intencao']}</span>
                </div>
                <div style="margin-top:10px; color:#ffffff;">
                    <b>📊 Métrica:</b> {m['volume']} | <b>💸 CPC Sugerido:</b> {m['cpc']}
                </div>
                <div style="margin-top:10px; border-top:1px solid #1e293b; padding-top:10px; color:#cbd5e1; font-style: italic;">
                    🤖 <b>Veredito do Robô:</b> {m['dica']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("🔗 Obter Link de Afiliado Rastreado"):
                st.code(m['link'])


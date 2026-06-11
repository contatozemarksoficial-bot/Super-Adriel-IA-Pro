import streamlit as st
import pandas as pd
import time
import random

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark em Tela Cheia)
    st.set_page_config(page_title="Adriel-AI Pro | Gestão de Assinantes", layout="wide", initial_sidebar_state="expanded")

    # CSS MASTER LUXO - PROTOCOLO GATEWAY DE PAGAMENTOS
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp { background-color: #010409 !important; }
    
    /* Métrica Executiva com Gradiente de Faturamento */
    [data-testid="stMetricValue"] { color: #00ffcc !important; font-size: 2.2rem !important; font-weight: 900 !important; }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; text-transform: uppercase; letter-spacing: 1px; }

    /* Estilo dos Cards de Pagamento */
    .payment-card {
        border: 1px solid #1e293b; padding: 25px; border-radius: 16px;
        background: linear-gradient(145deg, #0d1117, #010409);
        margin-bottom: 20px; border-top: 4px solid #00ffcc;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .neon-text { color: #00ffcc !important; font-weight: bold; }
    
    /* Botões Executivos de Checkout */
    .btn-checkout {
        display: block; width: 100%; padding: 12px;
        background: transparent; color: #00ffcc !important;
        border: 2px solid #00ffcc; border-radius: 8px;
        text-align: center; text-decoration: none !important;
        font-weight: 800; font-size: 0.85rem; text-transform: uppercase;
        transition: 0.4s; margin-top: 10px;
    }
    .btn-checkout:hover { background: #00ffcc; color: #010409 !important; box-shadow: 0 0 20px #00ffcc; }

    /* Badge de Status de Assinatura */
    .status-active { color: #00ffcc; background: rgba(0, 255, 204, 0.1); padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

    # --- CABEÇALHO EXCLUSIVO ---
    st.markdown('<h1 style="color: #ffffff; font-size: 2.5rem; font-weight: 900; letter-spacing: -2px;">💎 ÁREA DE <span style="color: #00ffcc;">MEMBROS & PAGAMENTOS</span></h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; font-weight: 600;">Monitoramento de Licenças Ativas e Faturamento Automático</p>', unsafe_allow_html=True)

    # --- DASHBOARD DE FATURAMENTO (MÉTRICAS) ---
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("FATURAMENTO TOTAL", "R$ 142.840,00", "+12%")
    c2.metric("LICENÇAS ATIVAS", "1.584", "85% Cap.")
    c3.metric("CHURN RATE", "1.2%", "-0.5%")
    c4.metric("MRR (MENSAL)", "R$ 48.200,00", "+R$ 4.2k")

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- BLOCO 1: GATEWAY DE PAGAMENTO (VENDA DE ACESSO) ---
    st.markdown('<h3 style="color:white; margin-bottom:20px;">💳 GATEWAY DE ACESSO IMEDIATO</h3>', unsafe_allow_html=True)
    cp1, cp2, cp3 = st.columns(3)

    planos = [
        {"nome": "PLANO MENSAL", "preco": "R$ 297,00", "vant": "Acesso ao Caçador Pro + Radar"},
        {"nome": "PLANO ANUAL", "preco": "R$ 1.997,00", "vant": "Acesso VIP + Funil Clone + IA Extra"},
        {"nome": "PLANO LIFETIME", "preco": "R$ 4.997,00", "vant": "Acesso Vitalício + Todas as 6 Telas"}
    ]

    cols = [cp1, cp2, cp3]
    for i, p in enumerate(planos):
        with cols[i]:
            st.markdown(f"""
            <div class="payment-card">
                <span class="status-active">OPORTUNIDADE</span>
                <h2 style="color:white; margin:10px 0;">{p['nome']}</h2>
                <div style="font-size:2rem; color:#00ffcc; font-weight:900; margin-bottom:10px;">{p['preco']}</div>
                <p style="color:#94a3b8; font-size:0.85rem;">{p['vant']}</p>
                <a href="#" class="btn-checkout">💳 COMPRAR LICENÇA VIA CARTÃO / PIX</a>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- BLOCO 2: GESTÃO DE ASSINANTES (TABELA EXECUTIVA) ---
    st.markdown('<h3 style="color:white; margin-bottom:20px;">👥 GESTÃO DE LICENÇAS E SEGURANÇA</h3>', unsafe_allow_html=True)
    
    # Simulação de Banco de Dados de Assinantes
    dados_membros = {
        "Usuário": ["Jose Marques", "Ana Silva", "Carlos Gringo", "Elite Traffic", "Base 44 Clone", "Robo King"],
        "Plano": ["LIFETIME", "ANUAL", "MENSAL", "LIFETIME", "ANUAL", "ANUAL"],
        "Status": ["✓ ATIVO", "✓ ATIVO", "✓ ATIVO", "✓ ATIVO", "⚠ PENDENTE", "✓ ATIVO"],
        "Último Acesso": ["Agora", "2h atrás", "5h atrás", "Ontem", "3 dias", "12min"],
        "Faturamento": ["R$ 4.997", "R$ 1.997", "R$ 297", "R$ 4.997", "R$ 0", "R$ 1.997"]
    }
    df = pd.DataFrame(dados_membros)
    st.dataframe(df, use_container_width=True)

    # BOTÕES EXECUTIVOS DE COMANDO
    st.markdown("<br>", unsafe_allow_html=True)
    cb1, cb2, cb3 = st.columns([1, 1, 1])
    with cb1:
        if st.button("🔓 LIBERAR ACESSO MANUAL"):
            st.toast("Comando de Criptografia enviado para a Base 44!", icon="🟢")
    with cb2:
        if st.button("🔒 BLOQUEAR LICENÇA"):
            st.toast("Acesso trancado nos servidores globais.", icon="🔴")
    with cb3:
        if st.button("📑 GERAR RELATÓRIO DE MRR"):
            st.success("Dossiê de faturamento gerado com sucesso!")

if __name__ == "__main__":
    main()

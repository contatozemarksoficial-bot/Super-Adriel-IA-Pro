import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Gestão Suprema", layout="wide", initial_sidebar_state="expanded")

    if "sessao_ativa" not in st.session_state: st.session_state.sessao_ativa = True

    # 2. CSS MASTER LUXO - PROTOCOLO TRIPLE BLACK & NEON
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp { background-color: #010409 !important; }
        
        /* Logo e Contador Live */
        .main-logo {
            color: #ffffff; font-size: 2.8rem; font-weight: 900; letter-spacing: -2px;
            display: flex; align-items: center; gap: 15px;
            text-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
        }
        .badge-pro {
            background: linear-gradient(90deg, #00ffcc, #0088ff);
            color: #010409; padding: 4px 15px; border-radius: 6px;
            font-size: 0.9rem; font-weight: 900; box-shadow: 0 0 20px #00ffcc88;
        }
        .live-counter {
            background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc22;
            padding: 10px 20px; border-radius: 50px; color: #00ffcc; font-weight: 800;
            display: inline-flex; align-items: center; gap: 10px; font-size: 0.8rem;
        }
        .blink { height: 8px; width: 8px; background-color: #00ffcc; border-radius: 50%; animation: pulse 1.2s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

        /* Métrica Executiva */
        .metric-box {
            background: rgba(13, 17, 23, 0.9); border: 1px solid #1e293b;
            padding: 20px; border-radius: 15px; border-bottom: 4px solid #00ffcc;
            text-align: center;
        }
        .metric-label { color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; font-weight: 700; letter-spacing: 1px; }
        .metric-value { color: #ffffff; font-size: 1.6rem; font-weight: 900; margin-top: 5px; }

        /* Cards de Planos e Checkout */
        .plan-card {
            border: 1px solid #1e293b; padding: 30px; border-radius: 20px;
            background: linear-gradient(145deg, #0d1117, #010409);
            margin-bottom: 20px; transition: 0.4s; text-align: center;
        }
        .plan-card:hover { border-color: #00ffcc66; transform: translateY(-5px); }
        .btn-pay {
            display: block; width: 100%; padding: 12px; margin-top: 15px;
            background: transparent; color: #00ffcc !important;
            border: 2px solid #00ffcc; border-radius: 8px;
            text-align: center; text-decoration: none !important;
            font-weight: 900; font-size: 0.8rem; text-transform: uppercase;
        }
        .btn-pay:hover { background: #00ffcc; color: #010409 !important; box-shadow: 0 0 20px #00ffcc; }

        /* Tabela Suprema */
        .sub-table { width: 100%; border-collapse: collapse; color: #f9fafb; margin-top: 20px; }
        .sub-table th { background: #0d1117; color: #00ffcc; padding: 15px; text-align: left; border-bottom: 2px solid #1e293b; font-size: 0.7rem; text-transform: uppercase; }
        .sub-table td { padding: 15px; border-bottom: 1px solid #1e293b; font-size: 0.85rem; vertical-align: top; }
    </style>
    """, unsafe_allow_html=True)

    # --- TOP BAR (LOGO + LIVE) ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8; margin-top:-10px; margin-left:65px; font-weight:600;">Comando Geral de Assinantes e Faturamento Síncrono</p>', unsafe_allow_html=True)
    with c_live:
        st.markdown(f'<div style="text-align:right; padding-top:10px;"><div class="live-counter"><div class="blink"></div> {random.randint(1420, 1680):,} OPERADORES CONECTADOS AGORA</div></div>', unsafe_allow_html=True)

    # --- DASHBOARD FINANCEIRO ---
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-box"><div class="metric-label">Faturamento Total</div><div class="metric-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-box"><div class="metric-label">Assinantes Ativos</div><div class="metric-value">1.842</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-box"><div class="metric-label">Recorrência (MRR)</div><div class="metric-value">R$ 98.400</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-box" style="border-bottom-color:#ff0055;"><div class="metric-label">Churn Rate</div><div class="metric-value">1.2%</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- PLANOS DE ACESSO (GATEWAY) ---
    st.markdown('<h3 style="color:white; margin-bottom:25px; letter-spacing:1px;">💳 ADESÃO À LICENÇA ADRIEL-AI PRO</h3>', unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    planos = [
        {"n": "PLANO MENSAL", "v": "R$ 297", "desc": "Acesso ao Caçador de Produtos + Radar de Elite."},
        {"n": "PLANO ANUAL", "v": "R$ 1.997", "desc": "Acesso Premium + Gerador de Pre-sell + Auditor IA."},
        {"n": "PLANO LIFETIME", "v": "R$ 4.997", "desc": "Acesso Vitalício + Todas as 6 Telas + Base 44."}
    ]

    cols = [p1, p2, p3]
    for i, plan in enumerate(planos):
        with cols[i]:
            st.markdown(f"""
            <div class="plan-card">
                <div class="metric-label">{plan['n']}</div>
                <div style="font-size:2.5rem; color:#ffffff; font-weight:900; margin:10px 0;">{plan['v']}</div>
                <p style="color:#94a3b8; font-size:0.8rem;">{plan['desc']}</p>
                <a href="#" class="btn-pay">💳 LIBERAR ACESSO AGORA</a>
            </div>
            """, unsafe_allow_html=True)

    # --- TABELA DE GESTÃO (BASE 44) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h3 style="color:#00ffcc; margin-bottom:20px; letter-spacing:1px;">🛡️ MONITORAMENTO DE OPERADORES (BASE 44)</h3>', unsafe_allow_html=True)
    
    membros = [
        {"u": "Marcos Oliveira", "p": "Diamond", "s": "ATIVO", "j": "Operador de elite focado em escala agressiva no mercado americano via BuyGoods. Utiliza a infraestrutura do Adriel-AI para antecipar lançamentos com ROI de 315%. Sua licença permite acesso total aos servidores de tráfego frio sem limitações geográficas, garantindo o domínio das ofertas rastreadas."},
        {"u": "Ana Júlia Sampaio", "p": "Platinum", "s": "ATIVO", "j": "Especialista em Brand Bidding e fundo de funil gringo. Ana opera com blindagem de cookies através do nosso sistema síncrono, protegendo suas comissões em cada clique gerado no Google Ads. Este membro mantém taxa de conversão 4x superior devido ao uso das métricas de gravidade."}
    ]

    t_html = """<table class="sub-table"><thead><tr><th>Operador / Plano</th><th>Justificativa Estratégica Adriel-AI</th><th>Status / Comando</th></tr></thead><tbody>"""
    for m in membros:
        t_html += f"""
        <tr>
            <td><b style='color:white;'>{m['u']}</b><br><span style='color:#00ffcc; font-size:0.7rem;'>PLANO: {m['p']}</span></td>
            <td style='color:#94a3b8; font-style:italic; line-height:1.5;'>"{m['j']}"</td>
            <td><span style='color:#00ffcc; font-weight:800;'>● {m['s']}</span><br><br>
                <div style='display:flex; gap:5px;'>
                    <div style='padding:5px 10px; border:1px solid #ff0055; color:#ff0055; border-radius:4px; font-size:0.6rem; font-weight:800; cursor:pointer;'>BLOQUEAR</div>
                </div>
            </td>
        </tr>"""
    t_html += "</tbody></table>"
    st.markdown(t_html, unsafe_allow_html=True)

    # --- FOOTER LINCADO ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-size:0.7rem; text-align:center;">PLATAFORMAS LINCADAS: CLICKBANK | BUYGOODS | DIGISTORE24 | STRIPE GATEWAY</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

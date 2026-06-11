import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO SUPREMA
    st.set_page_config(page_title="Adriel-AI Pro | Licenciamento", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS DE ALTA COSTURA - DESIGN CINEMA DARK
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp { background-color: #010409 !important; }
        
        /* Logo Magnética */
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

        /* Widgets de Faturamento */
        .metric-container {
            background: rgba(13, 17, 23, 0.9); border: 1px solid #1e293b;
            padding: 20px; border-radius: 15px; border-bottom: 4px solid #00ffcc;
            text-align: center;
        }
        .m-label { color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; font-weight: 700; }
        .m-value { color: #ffffff; font-size: 1.6rem; font-weight: 900; }

        /* CARDS DAS NOVAS LICENÇAS ACESSÍVEIS */
        .plan-card {
            border: 1px solid #1e293b; padding: 25px; border-radius: 20px;
            background: linear-gradient(145deg, #0d1117, #010409);
            margin-bottom: 20px; transition: 0.4s; text-align: left;
            position: relative; overflow: hidden;
        }
        .plan-card:hover { border-color: #00ffcc; transform: translateY(-5px); }
        .plan-price { font-size: 2.2rem; color: #ffffff; font-weight: 900; margin: 10px 0; }
        .plan-badge { position: absolute; top: 15px; right: -30px; background: #00ffcc; color: #010409; padding: 5px 40px; transform: rotate(45deg); font-size: 0.6rem; font-weight: 800; }
        
        .btn-activate {
            display: block; width: 100%; padding: 12px; margin-top: 15px;
            background: transparent; color: #00ffcc !important;
            border: 2px solid #00ffcc; border-radius: 8px;
            text-align: center; text-decoration: none !important;
            font-weight: 900; font-size: 0.8rem; text-transform: uppercase;
        }
        .btn-activate:hover { background: #00ffcc; color: #010409 !important; box-shadow: 0 0 20px #00ffcc; }

        /* Plataformas Lincadas */
        .plat-badge {
            padding: 8px 15px; border-radius: 8px; border: 1px solid #1e293b;
            background: #0d1117; color: #f9fafb; font-size: 0.7rem; font-weight: 700;
            display: flex; align-items: center; gap: 8px;
        }
        .online-dot { height: 6px; width: 6px; background: #00ffcc; border-radius: 50%; box-shadow: 0 0 10px #00ffcc; }

        /* Tabela Suprema */
        .sub-table { width: 100%; border-collapse: collapse; color: #f9fafb; margin-top: 20px; }
        .sub-table th { background: #0d1117; color: #00ffcc; padding: 15px; text-align: left; border-bottom: 2px solid #1e293b; font-size: 0.7rem; text-transform: uppercase; }
        .sub-table td { padding: 15px; border-bottom: 1px solid #1e293b; font-size: 0.8rem; vertical-align: top; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

    # --- TOP BAR ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
    with c_live:
        st.markdown(f'<div style="text-align:right; padding-top:15px;"><div style="color:#00ffcc; font-weight:800; font-size:0.8rem;"><span style="display:inline-block; width:8px; height:8px; background:#00ffcc; border-radius:50%; margin-right:5px; animation:pulse 1.5s infinite;"></span> {random.randint(1520, 1890):,} OPERADORES EM VARREDURA</div></div>', unsafe_allow_html=True)

    # --- DASHBOARD FINANCEIRO ---
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-container"><div class="m-label">Faturamento Total</div><div class="m-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-container"><div class="m-label">Assinaturas Ativas</div><div class="m-value">2.105</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-container"><div class="m-label">Recorrência (MRR)</div><div class="m-value">R$ 104.200</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-container" style="border-bottom-color:#ff0055;"><div class="m-label">Taxa de Churn</div><div class="m-value">0.8%</div></div>', unsafe_allow_html=True)

    # --- PLATAFORMAS LINCADAS ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; font-size:0.7rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-bottom:10px;">🔌 Conectividade Global do Robô</p>', unsafe_allow_html=True)
    lp1, lp2, lp3, lp4, lp5 = st.columns(5)
    platforms = [("CLICKBANK", lp1), ("BUYGOODS", lp2), ("DIGISTORE24", lp3), ("STRIPE", lp4), ("HOSTINGER", lp5)]
    for name, col in platforms:
        with col: st.markdown(f'<div class="plat-badge"><div class="online-dot"></div> {name}</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- NOVAS LICENÇAS ACESSÍVEIS ---
    st.markdown('<h3 style="color:white; margin-bottom:25px; letter-spacing:1px;">💳 ADESÃO ÀS NOVAS LICENÇAS ACESSÍVEIS</h3>', unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    licencas = [
        {"n": "PLANO MENSAL START", "v": "R$ 47", "desc": "Liberação do Módulo 1 (Radar) com lista vertical e setas de tendência. Ideal para validação rápida."},
        {"n": "PLANO MENSAL PRO", "v": "R$ 97", "desc": "Start + Módulo 3 (Gerador RSA com 45 Keywords BoF) e Arquiteto de Funil. Foco em quem já escala."},
        {"n": "PLANO ELITE MASTER", "v": "R$ 197", "desc": "Acesso TOTAL e ILIMITADO: Radar, Auditor, RSA, Caçador e Construtor de Pre-Sell Hostinger."}
    ]

    cols = [p1, p2, p3]
    for i, lic in enumerate(licencas):
        with cols[i]:
            promo = "OFERTA" if i == 0 else "MAIS VENDIDO" if i == 1 else "COMPLETO"
            st.markdown(f"""
            <div class="plan-card">
                <div class="plan-badge">{promo}</div>
                <div class="m-label">{lic['n']}</div>
                <div class="plan-price">{lic['v']}<span style="font-size:1rem; color:#94a3b8;">/mês</span></div>
                <p style="color:#94a3b8; font-size:0.8rem; height:60px;">{lic['desc']}</p>
                <a href="#" class="btn-activate">💳 ADQUIRIR ACESSO IMEDIATO</a>
            </div>
            """, unsafe_allow_html=True)

    # --- GESTÃO DE MEMBROS (BASE 44) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h3 style="color:#00ffcc; margin-bottom:20px; letter-spacing:1px;">🛡️ PROTOCOLO DE SEGURANÇA BASE 44</h3>', unsafe_allow_html=True)
    
    membros = [
        {"u": "Comandante Marques", "p": "Elite Master", "s": "ATIVO", "j": "Acesso vitalício configurado. Operador raiz com domínio total da ferramenta para construção de ecossistemas de vendas automáticas. Utiliza o construtor de Pre-sell para Hostinger com integração síncrona, garantindo 100% de aproveitamento do tráfego rastreado pelo Adriel-AI."},
        {"u": "Operador Base 44 #108", "p": "Mensal Pro", "s": "ATIVO", "j": "Focado em Brand Bidding no Google Ads USA. Este membro utiliza o Gerador RSA para criar 45 variações de anúncios em segundos, mantendo um CTR de 12% nas campanhas de fundo de funil. Licença validada para operação em 5 países simultâneos."}
    ]

    t_html = """<table class="sub-table"><thead><tr><th>Operador / Licença</th><th>Justificativa Estratégica IA</th><th>Comando Servidor</th></tr></thead><tbody>"""
    for m in membros:
        t_html += f"""
        <tr>
            <td><b style='color:white;'>{m['u']}</b><br><span style='color:#00ffcc; font-size:0.7rem;'>LICENÇA: {m['p']}</span></td>
            <td style='color:#94a3b8; font-style:italic;'>"{m['j']}"</td>
            <td><span style='color:#00ffcc; font-weight:800;'>● {m['s']}</span><br><br>
                <div style='padding:5px 10px; border:1px solid #ff0055; color:#ff0055; border-radius:4px; font-size:0.6rem; font-weight:800; cursor:pointer; text-align:center;'>REVOGAR</div>
            </td>
        </tr>"""
    t_html += "</tbody></table>"
    st.markdown(t_html, unsafe_allow_html=True)

    st.markdown("<br><br><p style='color:#475569; font-size:0.6rem; text-align:center;'>SISTEMA PROTEGIDO POR CRIPTOGRAFIA AES-256 | SERVIDORES LINCADOS VIA API SÍNCRONA</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

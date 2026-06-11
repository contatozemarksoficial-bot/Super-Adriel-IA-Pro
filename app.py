import streamlit as st
import pandas as pd
import random
import time

def main():
    # 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
    st.set_page_config(page_title="Adriel-AI Pro | Central de Comando", layout="wide", initial_sidebar_state="expanded")

    # 2. CSS DE ALTA PERFORMANCE - PROTOCOLO CONEXÃO TOTAL
    st.markdown("""
    <style>
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp { background-color: #010409 !important; }
        
        /* Logo e Header */
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

        /* PLATAFORMAS LINCADAS (Badges Clicáveis) */
        .plat-link { text-decoration: none !important; color: inherit !important; }
        .plat-badge {
            padding: 12px 15px; border-radius: 8px; border: 1px solid #1e293b;
            background: #0d1117; color: #f9fafb; font-size: 0.7rem; font-weight: 800;
            display: flex; align-items: center; gap: 8px; transition: 0.3s;
            cursor: pointer; justify-content: center;
        }
        .plat-badge:hover { border-color: #00ffcc; background: #010409; box-shadow: 0 0 15px #00ffcc33; }
        .online-dot { height: 7px; width: 7px; background: #00ffcc; border-radius: 50%; box-shadow: 0 0 10px #00ffcc; }

        /* Widgets de Faturamento */
        .metric-container {
            background: rgba(13, 17, 23, 0.9); border: 1px solid #1e293b;
            padding: 20px; border-radius: 15px; border-bottom: 4px solid #00ffcc;
            text-align: center;
        }
        .m-label { color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; font-weight: 700; }
        .m-value { color: #ffffff; font-size: 1.6rem; font-weight: 900; }

        /* CARDS DE LICENÇA (CHECKOUT REAL) */
        .plan-card {
            border: 1px solid #1e293b; padding: 30px; border-radius: 20px;
            background: linear-gradient(145deg, #0d1117, #010409);
            margin-bottom: 20px; transition: 0.4s; position: relative; overflow: hidden;
        }
        .plan-card:hover { border-color: #00ffcc; transform: translateY(-5px); }
        .plan-price { font-size: 2.5rem; color: #ffffff; font-weight: 900; margin: 10px 0; }
        
        .btn-checkout-real {
            display: block; width: 100%; padding: 15px; margin-top: 20px;
            background: #00ffcc; color: #010409 !important;
            border-radius: 10px; text-align: center; text-decoration: none !important;
            font-weight: 900; font-size: 0.9rem; text-transform: uppercase;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.4); transition: 0.3s;
        }
        .btn-checkout-real:hover { background: #ffffff; box-shadow: 0 0 40px #00ffcc; transform: scale(1.02); }

        /* Tabela Base 44 */
        .sub-table { width: 100%; border-collapse: collapse; color: #f9fafb; margin-top: 20px; }
        .sub-table th { background: #0d1117; color: #00ffcc; padding: 15px; text-align: left; border-bottom: 2px solid #1e293b; font-size: 0.7rem; text-transform: uppercase; }
        .sub-table td { padding: 15px; border-bottom: 1px solid #1e293b; font-size: 0.8rem; vertical-align: top; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    c_logo, c_live = st.columns([1.5, 1])
    with c_logo:
        st.markdown('<div class="main-logo">🤖 Adriel-AI <span class="badge-pro">PRO</span></div>', unsafe_allow_html=True)
    with c_live:
        st.markdown(f'<div style="text-align:right; padding-top:15px;"><div style="color:#00ffcc; font-weight:800; font-size:0.8rem;"><span style="display:inline-block; width:8px; height:8px; background:#00ffcc; border-radius:50%; margin-right:5px; animation:pulse 1.5s infinite;"></span> {random.randint(1840, 2350):,} MEMBROS ATIVOS NA ÁREA</div></div>', unsafe_allow_html=True)

    # --- PLATAFORMAS LINCADAS (FUNCIONANDO AGORA) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; font-size:0.7rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-bottom:10px;">🔌 Gateway de Conexão Síncrona (Clique para Acessar)</p>', unsafe_allow_html=True)
    lp1, lp2, lp3, lp4, lp5 = st.columns(5)
    
    # Links reais das plataformas
    platas = [
        ("CLICKBANK", "https://clickbank.com", lp1),
        ("BUYGOODS", "https://buygoods.com", lp2),
        ("DIGISTORE24", "https://digistore24.com", lp3),
        ("STRIPE DASH", "https://stripe.com", lp4),
        ("HOSTINGER VPS", "https://hostinger.com", lp5)
    ]
    
    for name, link, col in platas:
        with col:
            st.markdown(f'<a href="{link}" target="_blank" class="plat-link"><div class="plat-badge"><div class="online-dot"></div> {name}</div></a>', unsafe_allow_html=True)

    # --- DASHBOARD FINANCEIRO ---
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-container"><div class="m-label">Faturamento Geral</div><div class="m-value">R$ 142.580</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-container"><div class="m-label">Licenças Ativas</div><div class="m-value">2.105</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-container"><div class="m-label">MRR (Recorrência)</div><div class="m-value">R$ 104.200</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-container" style="border-bottom-color:#ff0055;"><div class="m-label">Taxa de Churn</div><div class="m-value">0.8%</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:1px; background:linear-gradient(90deg, transparent, #1e293b, transparent); margin:40px 0;"></div>', unsafe_allow_html=True)

    # --- NOVAS LICENÇAS (BOTOES COM LINKS REAIS) ---
    st.markdown('<h3 style="color:white; margin-bottom:25px; letter-spacing:1px;">💳 ADESÃO ÀS NOVAS LICENÇAS ACESSÍVEIS</h3>', unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    # Substitua pelos seus links reais de checkout
    licencas = [
        {"n": "PLANO MENSAL START", "v": "R$ 47", "desc": "Acesso ao Módulo 1 (Radar) + Tendências. Validação imediata.", "link": "https://seu-link-de-pagamento.com"},
        {"n": "PLANO MENSAL PRO", "v": "R$ 97", "desc": "Start + Módulo RSA (45 Keywords) + Arquiteto de Funil.", "link": "https://seu-link-de-pagamento.com"},
        {"n": "PLANO ELITE MASTER", "v": "R$ 197", "desc": "ACESSO TOTAL ILIMITADO + Construtor Pre-Sell Hostinger.", "link": "https://seu-link-de-pagamento.com"}
    ]

    cols = [p1, p2, p3]
    for i, lic in enumerate(licencas):
        with cols[i]:
            st.markdown(f"""
            <div class="plan-card">
                <div class="m-label">{lic['n']}</div>
                <div class="plan-price">{lic['v']}</div>
                <p style="color:#94a3b8; font-size:0.8rem; height:50px;">{lic['desc']}</p>
                <a href="{lic['link']}" target="_blank" class="btn-checkout-real">💳 PAGAR COM CARTÃO / PIX</a>
            </div>
            """, unsafe_allow_html=True)

    # --- GESTÃO DE MEMBROS (BASE 44) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h3 style="color:#00ffcc; margin-bottom:20px; letter-spacing:1px;">🛡️ CONTROLE DE ACESSO BASE 44</h3>', unsafe_allow_html=True)
    
    membros = [
        {"u": "Comandante Marques", "p": "Elite Master", "s": "ATIVO", "j": "Proprietário do sistema. Acesso total aos servidores de tráfego frio e integração síncrona com Hostinger. O robô opera com 100% de prioridade para este terminal."},
        {"u": "Operador Base 44 #108", "p": "Mensal Pro", "s": "ATIVO", "j": "Especialista em Brand Bidding USA. Utiliza a inteligência do Adriel-AI para dominar o fundo de funil com CTR de 12% nas redes gringas."}
    ]

    t_html = """<table class="sub-table"><thead><tr><th>Operador / Licença</th><th>Justificativa Estratégica IA</th><th>Controle Servidor</th></tr></thead><tbody>"""
    for m in membros:
        t_html += f"""
        <tr>
            <td><b style='color:white;'>{m['u']}</b><br><span style='color:#00ffcc; font-size:0.7rem;'>PLANO: {m['p']}</span></td>
            <td style='color:#94a3b8; font-style:italic;'>"{m['j']}"</td>
            <td>
                <span style='color:#00ffcc; font-weight:800;'>● {m['s']}</span><br><br>
                <button style='background:transparent; border:1px solid #ff0055; color:#ff0055; padding:5px 10px; border-radius:4px; font-size:0.6rem; font-weight:800; cursor:pointer;'>BLOQUEAR ACESSO</button>
            </td>
        </tr>"""
    t_html += "</tbody></table>"
    st.markdown(t_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

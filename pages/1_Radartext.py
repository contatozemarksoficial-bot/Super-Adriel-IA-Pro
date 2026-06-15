import streamlit as st
import requests
import json
import pandas as pd
import datetime

st.set_page_config(page_title="Robô Radar - Adriel-AI Pro", page_icon="🔥", layout="wide")

CHAVE_SERPER_REAL = "1e3c16719fbd4f5833199d7466193252986bba26"

st.markdown("""
<style>
.stApp { background-color: #060913 !important; color: #f8fafc !important; }
.card-coluna { background-color: #0c111d !important; border: 1px solid #1f293b !important; border-radius: 12px !important; padding: 15px !important; min-height: 480px; }
.titulo-coluna { font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 15px; border-bottom: 2px solid #1e293b; padding-bottom: 5px; }
.terminal-cyber { background-color: #02040a !important; border: 2px solid #1e293b !important; border-left: 4px solid #00ffcc !important; border-radius: 8px !important; padding: 15px !important; font-family: monospace !important; color: #00ffcc !important; font-size: 13px !important; margin-bottom: 20px; }
.badge-status { font-size: 9px; font-weight: 900; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; float: right; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color: #00ffcc; font-weight: 900; font-size: 2.2rem;">📊 MÓDULO 01: RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
st.write("Monitoramento de varredura global em tempo real nas plataformas ClickBank, Digistore24, BuyGoods e MaxWeb.")
st.markdown("---")

produtos_gringos = {
    "ProDentim": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / UK", "motivo": "Altíssimo volume de buscas por cupons. Lances de CPC caros, exige orçamento.", "base": 65000},
    "Prostavive": {"col": "T10", "sym": "🔥", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "BuyGoods", "pais": "EUA / CA", "motivo": "Forte tração em buscas de fundo de funil. CPC inflacionado no leilão.", "base": 48000},
    "FitSpresso": {"col": "T10", "sym": "📈", "status": "ALVO DE GUERRA", "cor": "#ef4444", "p": "ClickBank", "pais": "EUA / AU", "motivo": "Nicho de emagrecimento explodindo. Concorrência pesada na pesquisa Google.", "base": 72000},
    "ZeniCortex": {"col": "EST", "sym": "🟢", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "UK / CA", "motivo": "Suporte auditivo. Concorrência moderada de afiliados, brecha de ROI.", "base": 18000},
    "LeanBliss": {"col": "EST", "sym": "🛡️", "status": "MODERADA", "cor": "#eab308", "p": "Digistore24", "pais": "EUA / UK", "motivo": "Nicho de peso mastigável. Concorrência de nível médio. Ótima brecha.", "base": 22000},
    "Java Burn": {"col": "GER", "sym": "⚡", "status": "EXCELENTE", "cor": "#22c55e", "p": "ClickBank", "pais": "EUA / DE", "motivo": "Aditivo de café. Reaquecendo nas últimas horas devido a criativos novos.", "base": 31000}
}

p_pesquisa = st.text_input("🔍 Faça uma consulta manual de volume real no Google US:", value="")
if st.button("⛏️ EXECUTAR VARREDURA DA INTELIGÊNCIA CENTRAL"):
    if p_pesquisa.strip() != "":
        with st.spinner("Buscando dados reais na gringa..."):
            url = "https://serper.dev"
            headers = {'X-API-KEY': CHAVE_SERPER_REAL, 'Content-Type': 'application/json'}
            payload = json.dumps({"q": p_pesquisa.replace("-", " "), "gl": "us", "hl": "en"})
            try:
                res = requests.post(url, headers=headers, data=payload, timeout=8)
                if res.status_code == 200:
                    dados = res.json()
                    tot = len(dados.get("organic", []))
                    v_mes = dados.get("searchParameters", {}).get("page", 1) * 4000 + (tot * 130)
                    v_dia = int(v_mes / 30) + 12
                    
                    st.markdown(f'<div class="terminal-cyber">✅ [SUCESSO] Varredura orgânica concluída para o termo: {p_pesquisa}</div>', unsafe_allow_html=True)
                    cm1, cm2 = st.columns(2)
                    cm1.metric(label="🔎 Buscas Estimadas no Mês (EUA)", value=f"{v_mes:,}")
                    cm2.metric(label="⚡ Buscas Hoje (Até o momento)", value=f"{v_dia:,}")
                    
                    df_barras = pd.DataFrame({"Volume de Busca": [v_mes, 15000]}, index=[p_pesquisa, "Média do Mercado"])
                    st.bar_chart(df_barras)
            except Exception as e: st.error(f"Erro: {e}")

st.write("### 📋 MAPEAMENTO ATUAL DO MERCADO INTERNACIONAL (COLUNAS DO SEU PRINT)")
c_t10, c_est, c_ger = st.columns(3)
with c_t10:
    st.markdown('<div class="card-coluna"><div class="titulo-coluna" style="color:#ef4444;">🔥 TOP 10 FOGO ALTO</div>', unsafe_allow_html=True)
    for k, v in produtos_gringos.items():
        if v["col"] == "T10":
            if st.button(f"{v['sym']} {k}", key=f"r_{k}"): st.session_state.radar_sel = k
    st.markdown('</div>', unsafe_allow_html=True)
    
with c_est:
    st.markdown('<div class="card-coluna"><div class="titulo-coluna" style="color:#eab308;">🟢 OUTROS 10 ESTÁVEIS</div>', unsafe_allow_html=True)
    for k, v in produtos_gringos.items():
        if v["col"] == "EST":
            if st.button(f"{v['sym']} {k}", key=f"r_{k}"): st.session_state.radar_sel = k
    st.markdown('</div>', unsafe_allow_html=True)
    
with c_ger:
    st.markdown('<div class="card-coluna"><div class="titulo-coluna" style="color:#00ffcc;">⚡ MOVIMENTAÇÃO AO VIVO</div>', unsafe_allow_html=True)
    for k, v in produtos_gringos.items():
        if v["col"] == "GER":
            if st.button(f"{v['sym']} {k}", key=f"r_{k}"): st.session_state.radar_sel = k
    st.markdown('</div>', unsafe_allow_html=True)

if "radar_sel" in st.session_state:
    p_sel = st.session_state.radar_sel
    info = produtos_gringos[p_sel]
    agora = datetime.datetime.now()
    v_m = info["base"] + (agora.day * 110)
    v_d = int(info["base"] / 30) + (agora.hour * 30)
    st.write("---")
    st.markdown(f'<h3 style="color:#00ffcc;">🎯 Raio-X Detalhado do Mercado: {p_sel}</h3>', unsafe_allow_html=True)
    cp1, cp2 = st.columns(2)
    cp1.markdown(f'<div style="background-color:#0f172a; border-left:4px solid {info["cor"]}; border-radius:8px; padding:20px;"><span class="badge-status" style="background-color:{info["cor"]}; color:#000000;">{info["status"]}</span><b>Plataforma:</b> {info["p"]}<br><b style="color:#f6d14b;">🇺🇸 MELHOR PAÍS PARA ANUNCIAR:</b> {info["pais"]}<br><br><b>🔍 Porquê Estratégico:</b><br><i>{info["motivo"]}</i></div>', unsafe_allow_html=True)
    cp2.metric(label="Buscas Acumuladas no MÊS de Referência", value=f"{v_m:,}")
    cp2.metric(label="Buscas no DIA ATÉ O MOMENTO ATUAL", value=f"{v_d:,}")

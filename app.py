import streamlit as st

def menu_lateral_executivo():
    # 1. CSS PARA TRANSFORMAR A LATERAL EM BOTÕES DE LUXO
    st.markdown("""
    <style>
        /* Esconde a navegação padrão feia */
        [data-testid="stSidebarNav"] { display: none; }
        
        /* Fundo Total Preto na Lateral */
        [data-testid="stSidebar"] {
            background-color: #010409 !important;
            border-right: 1px solid #1e293b !important;
        }

        /* Estilo dos Botões de Menu */
        .sidebar-btn {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px;
            margin: 8px 15px;
            background: #0d1117;
            border: 1px solid #1e293b;
            border-radius: 10px;
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s all;
        }

        .sidebar-btn:hover {
            border-color: #00ffcc;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
            background: #010409;
            transform: translateX(5px);
        }

        .btn-active {
            border-left: 4px solid #00ffcc !important;
            background: linear-gradient(90deg, #00ffcc11, transparent) !important;
        }

        .icon-neon {
            color: #00ffcc;
            font-size: 1.1rem;
            text-shadow: 0 0 10px #00ffcc;
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. CONSTRUÇÃO VISUAL NA SIDEBAR
    with st.sidebar:
        # Logo Adriel-AI Pro
        st.markdown('<div style="padding: 20px 15px;"><span style="color:white; font-size:1.6rem; font-weight:900;">🤖 ADRIEL-AI <span style="color:#00ffcc;">PRO</span></span></div>', unsafe_allow_html=True)
        
        st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:20px; margin-bottom:15px;">Módulos de Comando</p>', unsafe_allow_html=True)
        
        # Lista de Botões (Links para as páginas)
        # Importante: O href deve ser o nome da página no seu GitHub (ex: "Radar")
        st.markdown("""
        <div style="display: flex; flex-direction: column;">
            <a href="/" class="sidebar-btn"><span class="icon-neon">🏠</span> Dashboard</a>
            <a href="Radar" class="sidebar-btn"><span class="icon-neon">📡</span> 1. Radar Elite</a>
            <a href="Auditor" class="sidebar-btn"><span class="icon-neon">🔍</span> 2. Auditor IA</a>
            <a href="Gerador" class="sidebar-btn"><span class="icon-neon">✍️</span> 3. Gerador RSA</a>
            <a href="Cacador" class="sidebar-btn"><span class="icon-neon">🎯</span> 4. Caçador V10</a>
            <a href="Presell" class="sidebar-btn"><span class="icon-neon">📄</span> 5. Pre-Sell</a>
            <a href="Funil" class="sidebar-btn"><span class="icon-neon">📐</span> 6. Funil</a>
            <a href="Assinantes" class="sidebar-btn"><span class="icon-neon">💎</span> Área Membros</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<p style="color:#1e293b; font-size:0.6rem; text-align:center;">PROTOCOL SINC V16.2</p>', unsafe_allow_html=True)

# Basta chamar essa função no início do seu código principal
menu_lateral_executivo()

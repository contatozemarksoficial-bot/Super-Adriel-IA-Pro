import streamlit as st

def aplicar_layout_supremo():
    # 1. CSS PARA TRANSFORMAR A LATERAL EM PAINEL DE BOTÕES DE LUXO
    st.markdown("""
    <style>
        /* RESET E FUNDO TOTAL */
        header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
        .stApp, [data-testid="stSidebar"] { background-color: #010409 !important; }

        /* ESCONDE O MENU PADRÃO CINZA */
        [data-testid="stSidebarNav"] { display: none; }
        
        /* BORDA FINA DE SEPARAÇÃO */
        [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }

        /* CONTAINER DOS NOVOS BOTÕES */
        .sidebar-menu {
            display: flex;
            flex-direction: column;
            gap: 12px;
            padding: 20px 15px;
        }

        /* BOTÃO DE COMANDO NEON */
        .menu-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px;
            background: #0d1117;
            border: 1px solid #1e293b;
            border-radius: 10px;
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s all ease-in-out;
        }

        .menu-item:hover {
            border-color: #00ffcc;
            box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
            background: #010409;
            transform: translateX(5px);
        }

        /* DESTAQUE PARA PÁGINA ATIVA */
        .active-page {
            border-left: 4px solid #00ffcc !important;
            background: linear-gradient(90deg, #00ffcc11, transparent) !important;
        }

        .icon-neon {
            color: #00ffcc;
            font-size: 1.1rem;
            text-shadow: 0 0 8px #00ffcc;
        }
    </style>
    """, unsafe_allow_html=True)

    # 2. CONSTRUÇÃO DO MENU NA SIDEBAR
    with st.sidebar:
        # Logo no topo da lateral
        st.markdown('<div style="text-align:center; padding: 20px 0;"><span style="color:white; font-size:1.5rem; font-weight:900;">🤖 ADRIEL-AI <span style="color:#00ffcc;">PRO</span></span></div>', unsafe_allow_html=True)
        
        st.markdown('<p style="color:#475569; font-size:0.65rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:15px;">Módulos de Comando</p>', unsafe_allow_html=True)
        
        # Div com os botões (Links para as páginas)
        # Importante: O href deve ser o nome exato da página que aparece na URL
        st.markdown("""
        <div class="sidebar-menu">
            <a href="/" class="menu-item">
                <span class="icon-neon">🏠</span> Dashboard
            </a>
            <a href="Radar" class="menu-item">
                <span class="icon-neon">📡</span> 1. Radar
            </a>
            <a href="Auditor" class="menu-item">
                <span class="icon-neon">🕵️</span> 2. Auditor
            </a>
            <a href="Gerador" class="menu-item">
                <span class="icon-neon">✍️</span> 3. Gerador RSA
            </a>
            <a href="Cacador" class="menu-item">
                <span class="icon-neon">🛰️</span> 4. Caçador V10
            </a>
            <a href="Presell" class="menu-item">
                <span class="icon-neon">📄</span> 5. Pre-Sell
            </a>
            <a href="Funil" class="menu-item">
                <span class="icon-neon">📐</span> 6. Funil
            </a>
            <a href="Assinantes" class="menu-item">
                <span class="icon-neon">💎</span> Área Membros
            </a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<p style="color:#1e293b; font-size:0.6rem; text-align:center;">SISTEMA ADRIEL V15.8</p>', unsafe_allow_html=True)

# Chamar a função
aplicar_layout_supremo()

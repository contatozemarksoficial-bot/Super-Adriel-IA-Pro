# --- CÓDIGO DO MENU CORRIGIDO (NAVEGAÇÃO NA MESMA ABA) ---
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label">MÓDULOS DE COMANDO</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-menu">
        <a href="/" target="_self" class="menu-btn">🏠 DASHBOARD</a>
        <a href="Radar" target="_self" class="menu-btn">📡 1. RADAR ELITE</a>
        <a href="Auditor" target="_self" class="menu-btn">🕵️ 2. AUDITOR IA</a>
        <a href="RSA" target="_self" class="menu-btn">✍️ 3. GERADOR RSA</a>
        <a href="Cacador" target="_self" class="menu-btn">🎯 4. CAÇADOR V10</a>
        <a href="Presell" target="_self" class="menu-btn">📄 5. PRE-SELL</a>
        <a href="Funil" target="_self" class="menu-btn">📐 6. FUNIL</a>
        <a href="Assinantes" target="_self" class="menu-btn">💎 ASSINANTES</a>
    </div>
    """, unsafe_allow_html=True)

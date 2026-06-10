import streamlit as st
from ftplib import FTP
import io
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026 (VISUAL SEGURO COLA NO TETO)
    st.set_page_config(page_title="Pré-Sell Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # INJEÇÃO CIRÚRGICA ESTILO LUXO CYBER-NEON COMPILADO (IMUNE A TELA BRANCA NO PYTHON 3.14)
    st.markdown("""
    <style>
    /* Forçador escuro premium do chassi principal e fontes sem mexer no body global */
    .stApp, [data-testid="stAppViewContainer"] { background-color: #030712 !important; color: #f9fafb !important; }
    h1, h2, h3, h4, p, span, label, .stMarkdown p { color: #f3f4f6 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* Remove o cabeçalho branco nativo para colar o conteúdo no teto do monitor */
    [data-testid="stHeader"] { display: none !important; height: 0px !important; background: transparent !important; }
    .block-container { padding-top: 0px !important; padding-bottom: 2rem !important; }
    
    /* Elementos de entrada de dados personalizados */
    .stTextInput>div>div>input { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important; }
    .stTextInput>div>div>input:focus { border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important; }
    
    /* Botões originais com borda cyber verde e hover ativo do seu design */
    .stButton>button { background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; width: 100% !important; height: 45px !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; }
    .stButton>button:hover { background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01); }
    
    /* Customização dos contêineres nativos para integrar ao modo escuro */
    [data-testid="stVerticalBlockBorderWrapper"] { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important; }
    [data-testid="stNotification"] { background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🏭 FÁBRICA DE PÁGINAS PRÉ-SELL</h1>', unsafe_allow_html=True)
    st.write("Geração e publicação automatizada de páginas de alta conversão diretamente no servidor Hostinger.")
    st.markdown("---")

    # 💾 MEMÓRIA DE SESSÃO PERMANENTE INTERNA (PREVINE RESETS DE FORMULÁRIO)
    if "ftp_host" not in st.session_state: st.session_state.ftp_host = "://seu-dominio.com"
    if "ftp_user" not in st.session_state: st.session_state.ftp_user = "usuario_ftp"
    if "ftp_pass" not in st.session_state: st.session_state.ftp_pass = "sua_senha_ftp"

    # 2. SEÇÃO DE LAYOUT EM DUAS COLUNAS PRINCIPAIS
    col_esquerda, col_direita = st.columns([1.0, 1.0])

    with col_esquerda:
        st.markdown("<h3 style='color:#00ffcc;'>🖥️ Configuração do Servidor Hostinger</h3>", unsafe_allow_html=True)
        h_input = st.text_input("Host FTP da Hostinger:", value=st.session_state.ftp_host)
        u_input = st.text_input("Usuário FTP Criado no hPanel:", value=st.session_state.ftp_user)
        p_input = st.text_input("Senha do Usuário FTP:", value=st.session_state.ftp_pass, type="password")
        
        if st.button("🔒 SALVAR CREDENCIAIS COMPLIANCE"):
            st.session_state.ftp_host = h_input.strip()
            st.session_state.ftp_user = u_input.strip()
            st.session_state.ftp_pass = p_input.strip()
            st.success("Credenciais de hospedagem salvas em cache de segurança com sucesso!")

    with col_direita:
        st.markdown("<h3 style='color:#cc66ff;'>📐 Estrutura do Clone Pré-Sell</h3>", unsafe_allow_html=True)
        p_nome = st.text_input("Nome Comercial do Ativo Gringo (Ex: Sugar Defender):", value="Sugar Defender")
        p_slug = st.text_input("Diretório / Pasta da URL (Ex: sugardefender-site):", value="sugardefender-site")
        p_link = st.text_input("Seu Link de Afiliado Internacional (ClickBank/BuyGoods):", value="https://clickbank.net")

    st.markdown("---")

    # 3. TERMINAL DE DISPARO SÍNCRONO DA COMPILAÇÃO FTP
    st.markdown("<h3 style='color:#00ffcc;'>🚀 Painel de Transmissão e Deploy na Web</h3>", unsafe_allow_html=True)
    botao_publicar = st.button("⚡ PUBLICAR PÁGINA DIRETORIO NA HOSTINGER")
    st.markdown("---")

    horario_atual = datetime.now().strftime("%H:%M:%S")
    st.info("🤖 STATUS DA FÁBRICA: Motor de deploy pronto para empacotar HTML **às** " + horario_atual)

    # 🪐 MAQUINÁRIO DE CLONAGEM E DISPARO REALTIME VIA PROTOCOLO FTP
    if botao_publicar:
        if not p_nome or not p_slug or not p_link:
            st.error("Erro Técnico: Todos os campos do clone pré-sell precisam estar preenchidos!")
        else:
            with st.spinner("Fabricando código-fonte estrutural e injetando link de afiliado..."):
                
                # 📝 CONSTRUTOR HTML PLANO PURE - Anatomia Blindada Antivírus e Antibloqueio Google Ads
                html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p_nome} - Official Website</title>
    <style>
        body {{ background-color: #030712; color: #f3f4f6; font-family: sans-serif; text-align: center; padding: 50px 20px; }}
        .card {{ max-width: 600px; margin: 0 auto; background: #0f172a; padding: 30px; border-radius: 12px; border: 1px solid #1e293b; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        h1 {{ color: #00ffcc; font-size: 2.2rem; }}
        p {{ font-size: 1.1rem; line-height: 1.6; color: #94a3b8; }}
        .btn {{ display: inline-block; background: linear-gradient(135deg, #00ff66 0%, #009933 100%); color: #030712; padding: 15px 40px; font-weight: bold; text-decoration: none; border-radius: 8px; font-size: 1.2rem; margin-top: 25px; box-shadow: 0 0 15px rgba(0,255,102,0.4); }}
        .btn:hover {{ transform: scale(1.02); box-shadow: 0 0 25px #00ff66; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>⚠️ REDIRECTION PROTOCOL ACTIVE</h1>
        <p>You are being safely routed to the official manufacturer portal of <strong>{p_nome}</strong> to claim your exclusive discount package with secure checkout mapping.</p>
        <p><em>Click the button below if you are not redirected within 3 seconds.</em></p>
        <a href="{p_link}" class="btn">PROCEED TO OFFICIAL SITE</a>
    </div>
</body>
</html>"""

                # Converte a string HTML plana em bytes legíveis para transmissão de rede
                html_bytes = io.BytesIO(html_code.encode('utf-8'))
                
                try:
                    # 🚀 EXECUÇÃO DE CONEXÃO E PUBLICAÇÃO MILITAR VIA PORTA 21
                    ftp = FTP()
                    ftp.connect(st.session_state.ftp_host, 21, timeout=15)
                    ftp.login(st.session_state.ftp_user, st.session_state.ftp_pass)
                    
                    # Tenta acessar ou criar a pasta slug do produto na raiz pública da Hostinger
                    try:
                        ftp.cwd(f"public_html/{p_slug}")
                    except:
                        try:
                            ftp.mkd(f"public_html/{p_slug}")
                            ftp.cwd(f"public_html/{p_slug}")
                        except:
                            ftp.mkd(p_slug)
                            ftp.cwd(p_slug)
                    
                    # Efetua o upload real do index.html para dentro da pasta criada
                    ftp.storbinary("STOR index.html", html_bytes)
                    ftp.quit()
                    
                    # EXIBIÇÃO DE SUCESSO COMPLIANCE COM PORTUGUÊS IMPECÁVEL
                    st.balloons()
                    st.success(f"🔥 SUCESSO TOTAL! Página clonada com Veredito operacional estável!")
                    st.info(f"🌐 Link Ativo na Web: http://{st.session_state.ftp_host.replace('ftp.', '')}/{p_slug}/index.html")
                    
                except Exception as erro_ftp:
                    st.error(f"Falha na Transmissão FTP: {str(erro_ftp)}")
                    st.warning("Dica de Leilão: Verifique se o Host, Usuário e Senha FTP estão corretos e se a pasta public_html existe no seu domínio.")

if __name__ == "__main__":
    main()

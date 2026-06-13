# ... (mantenha o seu CSS e o robô ASCII acima)

# =============================================================================================================
# 🚨 MOTOR CORRIGIDO: ESTEIRA DE DADOS EM LINHAS (FLUIDO)
# =============================================================================================================
if st.button("⛏️ DISPARAR INTEGRAÇÃO E INICIAR MINERAÇÃO"):
    st.write("---")
    
    # 1. Status do Terminal
    log_terminal = st.empty()
    log_terminal.markdown('<div class="terminal-hacker">📡 [CONEXÃO] Portão de dados aberto! Descarregando fluxo...</div>', unsafe_allow_html=True)
    
    st.markdown("### 📊 Esteira de Dados Ativa:")
    
    # 2. O PULO DO GATO: Criar um container vazio para a tabela
    tabela_viva = st.empty()
    
    # Lista de termos para minerar
    sufixos = ["official site", "buy now", "discount", "order online", "customer reviews", "price", "ingredients", "is it safe", "where to buy", "best price"]
    
    lista_movimento = []
    
    for suf in sufixos:
        # Adiciona a nova linha
        nova_linha = {
            "Keyword": f"{prod_alvo} {suf}".lower(),
            "Volume/Mês": f"{10000 // (len(lista_movimento)+1)}", # Simulação de volume
            "CPC Médio": f"$ {2.10 + (len(lista_movimento)/10):.2f}",
            "Funil": "💎 FUNDO"
        }
        lista_movimento.append(nova_linha)
        
        # 3. ATUALIZA APENAS O CONTAINER DA TABELA (Cria o efeito de 'linhas crescendo')
        df_atual = pd.DataFrame(lista_movimento)
        tabela_viva.dataframe(df_atual, use_container_width=True, hide_index=True)
        
        # Velocidade da esteira (ajuste aqui)
        time.sleep(0.3)
    
    log_terminal.markdown('<div class="terminal-hacker" style="border-color:#00ffcc;">✅ [CONCLUÍDO] 10/10 Termos de Elite extraídos com sucesso.</div>', unsafe_allow_html=True)

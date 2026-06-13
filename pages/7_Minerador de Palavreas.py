    # =====================================================================
    # 🎯 GERAÇÃO DE ANÚNCIOS AUTOMÁTICA (PÓS-MINERAÇÃO)
    # =====================================================================
    st.write("---")
    st.markdown(f"### 📣 Anúncios Sugeridos para: **{prod_alvo}**")
    
    col_ads1, col_ads2 = st.columns(2)
    
    with col_ads1:
        st.markdown("""
        <div class="terminal-hacker" style="border-color: #ff0055; color: #fff;">
            <b style="color: #ff0055;">[G-ADS TITLES]</b><br>
            1. {prod} Official Site - Only $49<br>
            2. Buy {prod} Original Today<br>
            3. {prod}® | Special Discount
        </div>
        """.format(prod=prod_alvo), unsafe_allow_html=True)
        
    with col_ads2:
        st.markdown("""
        <div class="terminal-hacker" style="border-color: #00ffcc; color: #fff;">
            <b style="color: #00ffcc;">[DESCRIPTIONS]</b><br>
            - Get the real {prod} from the official store. Limited time offer and free shipping.<br>
            - Support your health with {prod}. 100% natural ingredients. Order now and save!
        </div>
        """.format(prod=prod_alvo), unsafe_allow_html=True)

    st.info("💡 Esses anúncios foram otimizados para o CTR da Gringa.")

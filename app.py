import streamlit as st


def main():
    st.title('Income Manager')

    st.sidebar.button("Dashboard", key="expandir_minimizar", use_container_width=True )

    # Adiciona o conteúdo da barra lateral
    st.sidebar.button("Transações", use_container_width=True)
    




if __name__ == '__main__':
    main()
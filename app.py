import streamlit as st
from transactions.page import show_transactions
from dashboard.page import show_dashboard


def main():
    st.title('Income Manager')

    st.sidebar.button("Dashboard", key="expandir_minimizar", use_container_width=True, on_click=show_dashboard())

    # Adiciona o conteúdo da barra lateral
    st.sidebar.button("Transações", use_container_width=True, on_click=show_transactions())
        

if __name__ == '__main__':
    main()
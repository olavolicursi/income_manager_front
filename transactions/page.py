import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

transactions = [
    {
        'id': 1,
        'value': 1200,
        'type': 'C'
    },
    {
        'id': 2,
        'value': 1000,
        'type': 'C'
    },
    {
        'id': 3,
        'value': 500,
        'type': 'D'
    },
]

def show_transactions():
    st.selectbox('', ('Despesas', 'Receitas'))

    AgGrid(
        data=pd.DataFrame(transactions),
        reload_data=True,
        key='transactions_grid',
    )


    
    
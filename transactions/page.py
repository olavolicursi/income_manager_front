import streamlit as st

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
    
    
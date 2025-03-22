import streamlit as st 
import numpy as np
import pandas as pd

# crear title de la app web
st.title("Streamlit con Sidebar")

sidebar = st.sidebar
sidebar.title("Titulo de barra lateral")

sidebar.write("Informacion de mi sidebar")

st.header("Te amo mucho mi vida preciosa")
st.write("Eres lo mejor que me ha pasado")

if sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randint(1,10, size=(20, 3)),
       columns=['col 1', 'col 2', 'col 3'])

    st.dataframe(chart_data)
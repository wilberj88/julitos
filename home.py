import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Julitos", page_icon="🚬 ")

st.title('Julitos 🚬 ')
st.header("Gánate tu primer Julito")

st.write("Bienvenidos a la tienda más parchada de todas")

st.write("Cuéntanos:")

st.slider('Mensualmente: ¿cuál es tu presupuesto Julitos 🚬')

st.slider('¿Cuánto gramos consumes a la semana?', 0, 1000000, key="presupuesto")

st.radio('Indícanos tus cepas preferidas:', ['Orange', 'Gorila Kush', 'Gorila Og', 'PuntoRojo', 'IRE', 'Amazonas'])

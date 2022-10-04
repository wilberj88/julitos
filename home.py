import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Julitos", page_icon="☘️")

st.title('Julitos ☘️')
st.write("Bienvenidos a la tienda más parchada de todas")

st.header("Gánate tu primer Julito")

st.write("Formulario de Registro✍")
    

d = st.text_input('Nombre')

e = st.text_input('Apellido')

a = st.text_input('1. Correo electrónico')

b = st.text_input('2. Ciudad ')

c = st.text_input('3. Dirección?')

f = st.write("Adicionalmente, cuéntanos:")

g = st.slider('Mensualmente: ¿cuál es tu presupuesto Julitos 🚬')

h = st.slider('¿Cuánto gramos consumes a la semana?', 0, 1000000, key="presupuesto")

i = st.radio('Indícanos tus cepas preferidas:', ['Orange', 'Gorila Kush', 'Gorila Og', 'PuntoRojo', 'IRE', 'Amazonas'])

if a and b and c:
  st.write('Muchas gracias, ', d, e, 'Enviamos un correo de confirmación a  <<',a, '>>. Estamos preparando el envío de tu Julito hacia la ciudad de <<', b, '>> a la dirección: <<', c, '>>. REPORTE DE USUARIO: consumo mensual en gramos es de <<',h, '>>, en presupuesto es de <<',g, '>> y su cepa preferida es <<',i, '>>')


picture = st.camera_input("Sonríe para nuestro registro")

if picture:
    st.image(picture)
    st.write('Bienvenido a la comunidad de Julitos☘️. Ya eres parte de nuestro parche')

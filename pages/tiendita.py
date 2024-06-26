
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os

import streamlit as st

# Inicializar el estado del carrito si no existe
if 'carrito' not in st.session_state:
    st.session_state['carrito'] = []

# Función para agregar producto al carrito
def agregar_al_carrito(producto):
    st.session_state.carrito.append(producto)
    st.session_state["carrito_updated"] = True

# Función para mostrar la sección de producto
def mostrar_producto(imagen, titulo, descripcion, precio):
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(imagen, use_column_width=True)
    
    with col2:
        st.header(titulo)
        st.write(descripcion)
        st.subheader(f"Precio: {precio}")
        if st.button(f'Agregar {titulo} al carrito', on_click=agregar_al_carrito, args=({"titulo": titulo, "precio": precio},)):
            st.experimental_rerun()

# Función para mostrar el carrito
def mostrar_carrito():
    st.sidebar.header("Carrito de Compras")
    if st.session_state.carrito:
        for i, producto in enumerate(st.session_state.carrito):
            st.sidebar.write(f"{i+1}. {producto['titulo']} - {producto['precio']}")
        if st.sidebar.button('Vaciar Carrito'):
            st.session_state.carrito = []
            st.session_state["carrito_updated"] = True
            st.experimental_rerun()
    else:
        st.sidebar.write("El carrito está vacío")

# Título de la página
st.title("Tienda de Zapatillas")

# Mostrar el carrito en la barra lateral
mostrar_carrito()

# Datos de los productos
productos = [
    {
        "imagen": "https://livesport-ott-images.ssl.cdn.cra.cz/r900xfq60/8d3a916a-38a5-4d15-87c4-8063a8371507.jpeg",
        "titulo": "Air Forces",
        "descripcion": "Las Nike Air Force 1 son un ícono de la moda urbana desde su lanzamiento en 1982. "
                       "Originalmente diseñadas como zapatillas de baloncesto, han evolucionado para convertirse en una pieza esencial del streetwear.",
        "precio": "$100"
    },
    {
        "imagen": "https://livesport-ott-images.ssl.cdn.cra.cz/r900xfq60/8d3a916a-38a5-4d15-87c4-8063a8371507.jpeg",
        "titulo": "Air Maxes",
        "descripcion": "Las Nike Air Max son famosas por su unidad de aire visible en la suela, introducida por primera vez en 1987. "
                       "Han evolucionado con diferentes modelos y tecnologías a lo largo de los años.",
        "precio": "$120"
    }
]

# Mostrar productos
for producto in productos:
    mostrar_producto(producto["imagen"], producto["titulo"], producto["descripcion"], producto["precio"])
    st.markdown("---")  # Separador entre productos


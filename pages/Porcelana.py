from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os


# Datos de los productos
products = [
     {
        "name": "Maquillaje Porcelana",
        "description": "Base de maquillaje ideal para pieles muy claras, ofrece una cobertura impecable y ligera que ilumina y realza el tono natural de la piel sin dejar sensación pesada.",
        "price": 820,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    }
]

# Título de la página
st.title('Tienda E-commerce')

# Mostrar los productos
for product in products:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(product['image'], width=150)
    with col2:
        st.subheader(product['name'])
        st.write(f"**Descripción:** {product['description']}")
        st.write(f"**Precio:** ${product['price']}")
        st.number_input('Cantidad', min_value=1, max_value=10, value=1, key=product['name'])
        st.button('Agregar al pedido', key=product['name'] + '_button')

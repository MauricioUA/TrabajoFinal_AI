from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os

import streamlit as st

# Datos de los productos
products = [
     {
        "name": "Maquillaje Porcelana",
        "description": "Base de maquillaje ideal para pieles muy claras, ofrece una cobertura impecable y ligera que ilumina y realza el tono natural de la piel sin dejar sensación pesada.",
        "price": 820,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Marfil",
        "description": "Base de maquillaje perfecta para pieles claras, proporciona un acabado suave y natural con una fórmula ligera y de larga duración, logrando una cobertura uniforme y luminosa.",
        "price": 830,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Beige",
        "description": "Base de maquillaje adecuada para pieles claras a medias, con una textura sedosa que se funde perfectamente y proporciona una cobertura natural que resalta el resplandor de la piel.",
        "price": 840,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Arena",
        "description": "Base de maquillaje diseñada para pieles medio claras, ofrece una cobertura uniforme que disimula imperfecciones y realza el tono natural de la piel con una fórmula hidratante.",
        "price": 850,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Beige Dorado",
        "description": "Base de maquillaje ideal para pieles medias, con una fórmula ligera y de alta cobertura que se adapta perfectamente al tono de la piel, ofreciendo un acabado radiante y uniforme.",
        "price": 860,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Caramelo",
        "description": "Base de maquillaje adecuada para pieles medio oscuras, proporciona una cobertura impecable mientras hidrata y unifica la piel, dejándola con un aspecto naturalmente bello y luminoso.",
        "price": 870,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Almendra",
        "description": "Base de maquillaje perfecta para pieles oscuras, con una fórmula rica en hidratación que proporciona un acabado suave y luminoso, destacando la belleza natural de la piel.",
        "price": 880,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Cacao",
        "description": "Base de maquillaje ideal para pieles muy oscuras, ofrece una cobertura impecable que unifica el tono de la piel mientras la hidrata profundamente, con un acabado mate natural.",
        "price": 890,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Espresso",
        "description": "Base de maquillaje adecuada para pieles profundas, con una fórmula de alta cobertura que se adapta perfectamente al tono de la piel, ofreciendo un acabado impecable y duradero.",
        "price": 900,
        "image": "https://www.paris.cl/dw/image/v2/BCHW_PRD/on/demandware.static/-/Sites-cencosud-master-catalog/default/dw788b7129/images/imagenes-productos/626/601443-0000-001.jpg"
    },
    {
        "name": "Maquillaje Ébano",
        "description": "Base de maquillaje ideal para pieles muy profundas, ofrece una cobertura completa y un acabado mate que unifica y resalta el tono de la piel de manera natural, hidratando y protegiendo.",
        "price": 910,
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



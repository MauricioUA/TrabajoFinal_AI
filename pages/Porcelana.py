from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os

# Título de la página
st.title('Maquillaje Porcelana')

# Layout en columnas
col1, col2 = st.columns([1, 2])

with col1:
    # Carusel de imágenes del producto
    st.subheader('Galería de Imágenes')
    images = [
        {
            "url": "https://www.uomax.com.ar/11209-large_default/base-de-maquillaje-loreal-infalible-130.jpg",
            "caption": "Maquillaje Porcelana - Vista Frontal"
        },
        {
            "url": "https://romanamx.com/cdn/shop/files/LorealInfalliblepromatte_4.jpg?v=1684437947&width=1080",
            "caption": "Maquillaje Porcelana - Vista Posterior"
        }
    ]
    
    # Mostrar imágenes como una galería
    selected_image = st.radio("Selecciona una imagen", [img['caption'] for img in images])
    image_url = next(img['url'] for img in images if img['caption'] == selected_image)
    st.image(image_url, caption=selected_image, width=300)

with col2:
    # Descripción del producto
    st.subheader('Descripción del Producto')
    st.write("""
    La base de maquillaje Porcelana es ideal para pieles muy claras, ofreciendo una cobertura impecable y ligera que ilumina y realza el tono natural de la piel sin dejar sensación pesada. Con su fórmula avanzada, esta base asegura un acabado uniforme y natural que dura todo el día. Es perfecta para quienes buscan resaltar su belleza natural sin comprometer la comodidad. ¡Siente la diferencia con cada aplicación!
    """)

    # Precio del producto
    st.subheader('Precio')
    st.write("**$820**")

    # Selección de cantidad
    st.subheader('Selecciona la cantidad')
    quantity = st.number_input('Cantidad', min_value=1, max_value=10, value=1)

    # Botón de Agregar al Carrito
    if st.button('Agregar al Carrito'):
        st.success(f"¡Gracias por tu compra! {quantity} unidad(es) de Maquillaje Porcelana han sido añadidas a tu carrito.")

    # Enlace de regreso a la tienda
    st.markdown("[Regresar a la Tienda](Tienda.py)")
    
    # Divider para separación visual
    st.markdown("---")

    # Información adicional o preguntas frecuentes
    st.subheader('Preguntas Frecuentes')
    st.write("""
    **¿Es esta base adecuada para pieles sensibles?**
    Sí, nuestra base de maquillaje Porcelana está formulada para ser suave y segura para todo tipo de piel, incluyendo pieles sensibles.

    **¿Es resistente al agua?**
    Sí, esta base de maquillaje ofrece resistencia al agua, asegurando que tu look permanezca intacto durante todo el día.
    """)

# Espacio para mejorar la disposición visual
st.markdown("<br><br>", unsafe_allow_html=True)


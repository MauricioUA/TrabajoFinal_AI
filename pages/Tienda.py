from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os
from st_pages import show_pages_from_config, add_page_title
import streamlit_shadcn_ui as ui
from streamlit_card import card
import base64

show_pages_from_config()

# Inicializar el estado del carrito si no existe
if 'carrito' not in st.session_state:
    st.session_state['carrito'] = []

# Función para agregar producto al carrito
def agregar_al_carrito(producto):
    st.session_state.carrito.append(producto)
    st.session_state["carrito_updated"] = True

# Función para mostrar la sección de producto
def mostrar_producto(imagen, titulo, descripcion, precio, index):
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(imagen, use_column_width=True)
    
    with col2:
        st.header(titulo)
        st.write(descripcion)
        st.subheader(f"Precio: {precio}")
        # Proporciona una clave única para cada botón usando el índice
        if st.button(f'Agregar {titulo} al carrito', on_click=agregar_al_carrito, args=({"titulo": titulo, "precio": precio},), key=f"btn_{index}"):
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
st.header("Selecciona tu tono:")

# Mostrar el carrito en la barra lateral
mostrar_carrito()

choice = ui.select(options=["Todos los tonos", "Muy Claro", "Claro", "Medio", "Oscuro", "Muy Oscuro"])

index = 0

productos = {
    "Muy Claro": [
        {
            "imagen": "Fotos/BASE_MUY_CLARA.png",
            "titulo": "Base Muy Clara",
            "descripcion": "Logra un acabado impecable con nuestra Base Muy Clara, ideal para tonos de piel porcelana, ofreciendo cobertura total y un acabado natural.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_MUY_CLARO.png",
            "titulo": "Corrector Muy Claro",
            "descripcion": "Oculta imperfecciones y ojeras con nuestro Corrector Muy Claro, perfecto para tonos de piel porcelana, dejando un acabado impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MUY_CLARO.png",
            "titulo": "Polvo Muy Claro",
            "descripcion": "Fija tu maquillaje con nuestro Polvo Muy Claro, diseñado para tonos de piel porcelana, ofreciendo un acabado mate y suave.",
            "precio": "$150"
        }
    ],
    "Claro": [
        {
            "imagen": "Fotos/BASE_CLARA.png",
            "titulo": "Base Clara",
            "descripcion": "Nuestra Base Clara proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_CLARO.png",
            "titulo": "Corrector Claro",
            "descripcion": "Nuestro Corrector Claro cubre ojeras y manchas en pieles claras, ofreciendo un resultado natural y de larga duración.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_CLARO.png",
            "titulo": "Polvo Claro",
            "descripcion": "El Polvo Claro proporciona una fijación perfecta y un acabado natural para pieles claras, manteniendo el maquillaje intacto todo el día.",
            "precio": "$150"
        }
    ],
    "Medio": [
        {
            "imagen": "Fotos/BASE_MEDIA.png",
            "titulo": "Base Media",
            "descripcion": "Descubre la perfección con nuestra Base Media, diseñada para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_MEDIO.png",
            "titulo": "Corrector Medio",
            "descripcion": "Nuestro Corrector Medio proporciona una cobertura perfecta para imperfecciones en tonos de piel medios, asegurando un look fresco y luminoso.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MEDIO.png",
            "titulo": "Polvo Medio",
            "descripcion": "Nuestro Polvo Medio es ideal para tonos de piel medios, ofreciendo un acabado mate y control de brillo durante horas.",
            "precio": "$150"
        }
    ],
    "Oscuro": [
        {
            "imagen": "Fotos/BASE_OSCURA.png",
            "titulo": "Base Oscura",
            "descripcion": "La Base Oscura se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_OSCURO.png",
            "titulo": "Corrector Oscuro",
            "descripcion": "El Corrector Oscuro se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_OSCURO.png",
            "titulo": "Polvo Oscuro",
            "descripcion": "Controla el brillo y fija tu maquillaje con nuestro Polvo Oscuro, perfecto para tonos de piel oscuros, proporcionando un acabado suave y uniforme.",
            "precio": "$150"
        }
    ],
    "Muy Oscuro": [
        {
            "imagen": "Fotos/BASE_MUY_OSCURA.png",
            "titulo": "Base Muy Oscura",
            "descripcion": "Nuestra Base Muy Oscura ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_MUY_OSCURO.png",
            "titulo": "Corrector Muy Oscuro",
            "descripcion": "Nuestro Corrector Muy Oscuro ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MUY_OSCURO.png",
            "titulo": "Polvo Muy Oscuro",
            "descripcion": "El Polvo Muy Oscuro fija el maquillaje y controla el brillo en tonos de piel muy oscuros, asegurando un look impecable y natural.",
            "precio": "$150"
        }
    ]
}

videos = {
    "Muy Claro": "https://www.youtube.com/watch?v=7PR1FxrrEhU&pp=ygUZZmFpciBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D",
    "Claro": "https://www.youtube.com/watch?v=XRNnWbaPv9Q&pp=ygUZZmFpciBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D",
    "Medio": "https://www.youtube.com/watch?v=W0Wcaqrt94I&pp=ygUabWVkaXVtc2tpbiBtYWtldXAgdHV0b3JpYWw%3D",
    "Oscuro": "https://www.youtube.com/watch?v=3ASGtEc5un0&pp=ygUZZGFyayBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D",
    "Muy Oscuro": "https://www.youtube.com/watch?v=pgcrU-V2oTg&pp=ygUgcmVhbGx5IGRhcmsgc2tpbiBtYWtldXAgdHV0b3JpYWw%3D"
}

if choice == "Todos los tonos":
    # Código para mostrar todos los tonos
    st.header('Bases')
    bases = productos["Muy Claro"] + productos["Claro"] + productos["Medio"] + productos["Oscuro"] + productos["Muy Oscuro"]

    for base in bases:
        mostrar_producto(base["imagen"], base["titulo"], base["descripcion"], base["precio"], index)
        st.markdown("---")  # Separador entre productos
        index += 1
    
    st.header('Correctores')
    correctores = productos["Muy Claro"] + productos["Claro"] + productos["Medio"] + productos["Oscuro"] + productos["Muy Oscuro"]

    for corrector in correctores:
        mostrar_producto(corrector["imagen"], corrector["titulo"], corrector["descripcion"], corrector["precio"], index)
        st.markdown("---")  # Separador entre productos
       

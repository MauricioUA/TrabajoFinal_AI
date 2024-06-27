from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os
from st_pages import show_pages_from_config, add_page_title
import streamlit as st
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

if choice == "Todos los tonos":
    #st.header('Bases')



    with open('Fotos\Portada.jpeg', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")


    res = card(
    title="SKINLY",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )

    # Datos de los Bases
    bases = [
        {
            "imagen": "Fotos\BASE_MUY_CLARA.png.crdownload",
            "titulo": "Base Muy Clara",
            "descripcion": "Logra un acabado impecable con nuestra Base Muy Clara, ideal para tonos de piel porcelana, ofreciendo cobertura total y un acabado natural.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\BASE_CLARA.png.crdownload",
            "titulo": "Base Clara",
            "descripcion": "Nuestra Base Clara proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\BASE_MEDIA.png.crdownload",
            "titulo": "Base Media",
            "descripcion": "Descubre la perfección con nuestra Base Media, diseñada para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\BASE_OSCURA.png.crdownload",
            "titulo": "Base Oscura",
            "descripcion": "La Base Oscura se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\BASE_MUY_OSCURA.png.crdownload",
            "titulo": "Base Muy Oscura",
            "descripcion": "Nuestra Base Muy Oscura ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$100"
        }
    ]

# Mostrar productos

    for base in bases:
        mostrar_producto(base["imagen"], base["titulo"], base["descripcion"], base["precio"], index)
        st.markdown("---")  # Separador entre productos
        index += 1
    
    st.header('Correctores')

    # Datos de los Correctores
    correctores = [
        {
            "imagen": "Fotos\CORRECTOR_MUY_CLARO.png.crdownload",
            "titulo": "Corrector Muy Claro",
            "descripcion": "Oculta imperfecciones y ojeras con nuestro Corrector Muy Claro, perfecto para tonos de piel porcelana, dejando un acabado impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\CORRECTOR_CLARO.png.crdownload",
            "titulo": "Corrector Claro",
            "descripcion": "Nuestro Corrector Claro proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\CORRECTOR_MEDIO.png.crdownload",
            "titulo": "Corrector Medio",
            "descripcion": "Descubre la perfección con nuestro Corrector Medio, diseñado para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\CORRECTOR_OSCURO.png.crdownload",
            "titulo": "Corrector Oscuro",
            "descripcion": "El Corrector Oscuro se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\CORRECTOR_MUY_OSCURO.png.crdownload",
            "titulo": "Corrector Muy Oscuro",
            "descripcion": "Nuestro Corrector Muy Oscuro ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for corrector in correctores:
        mostrar_producto(corrector["imagen"], corrector["titulo"], corrector["descripcion"], corrector["precio"], index)
        st.markdown("---")  # Separador entre productos
        index += 1
    

    st.header('Polvos')


    # Datos de los Polvos
    polvos = [
        {
            "imagen": "Fotos\POLVO_MUY_CLARO.png.crdownload",
            "titulo": "Polvo Muy Claro",
            "descripcion": "Fija tu maquillaje con nuestro Polvo Muy Claro, diseñado para tonos de piel porcelana, ofreciendo un acabado mate y suave.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_CLARO.png.crdownload",
            "titulo": "Polvo Claro",
            "descripcion": "El Polvo Claro proporciona una fijación perfecta y un acabado natural para pieles claras, manteniendo el maquillaje intacto todo el día.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_MEDIO.png.crdownload",
            "titulo": "Polvo Medio",
            "descripcion": "Nuestro Polvo Medio es ideal para tonos de piel medios, ofreciendo un acabado mate y control de brillo durante horas.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_OSCURO.png.crdownload",
            "titulo": "Polvo Oscuro",
            "descripcion": "Controla el brillo y fija tu maquillaje con nuestro Polvo Oscuro, perfecto para tonos de piel oscuros, proporcionando un acabado suave y uniforme.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_MUY_OSCURO.png.crdownload",
            "titulo": "Polvo Muy Oscuro",
            "descripcion": "El Polvo Muy Oscuro fija el maquillaje y controla el brillo en tonos de piel muy oscuros, asegurando un look impecable y natural.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for polvo in polvos:
        mostrar_producto(polvo["imagen"], polvo["titulo"], polvo["descripcion"], polvo["precio"], index)
        st.markdown("---")  # Separador entre productos
        index += 1





if choice == "Muy Claro":


    #st.header('Muy Claro')

    import base64

    with open('Fotos\MUY_CLARO.png.crdownload', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    from streamlit_card import card

    res = card(
    title="Muy Claro",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )


    # Datos de los Correctores
    muyclaros = [
        {
            "imagen": "Fotos\BASE_MUY_CLARA.png.crdownload",
            "titulo": "Base Muy Clara",
            "descripcion": "Logra un acabado impecable con nuestra Base Muy Clara, ideal para tonos de piel porcelana, ofreciendo cobertura total y un acabado natural.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\CORRECTOR_MUY_CLARO.png.crdownload",
            "titulo": "Corrector Muy Claro",
            "descripcion": "Oculta imperfecciones y ojeras con nuestro Corrector Muy Claro, perfecto para tonos de piel porcelana, dejando un acabado impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_MUY_CLARO.png.crdownload",
            "titulo": "Polvo Muy Claro",
            "descripcion": "Fija tu maquillaje con nuestro Polvo Muy Claro, diseñado para tonos de piel porcelana, ofreciendo un acabado mate y suave.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for muyclaro in muyclaros:
        mostrar_producto(muyclaro["imagen"], muyclaro["titulo"], muyclaro["descripcion"], muyclaro["precio"], index)
        st.markdown("---")  # Separador entre productos
        index += 1

    VIDEO_URL = "https://www.youtube.com/watch?v=7PR1FxrrEhU&pp=ygUZZmFpciBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D"
    
    st.video(VIDEO_URL, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=True)



if choice == "Claro":


    #st.header('Claro')

    import base64

    with open('Fotos\CLARO.png.crdownload', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    from streamlit_card import card

    res = card(
    title="Claro",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )

    # Datos de los Correctores
    claros = [
        {
            "imagen": "Fotos\BASE_CLARA.png.crdownload",
            "titulo": "Base Clara",
            "descripcion": "Nuestra Base Clara proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",            
            "precio": "$100"
        },
        {
            "imagen": "Fotos\CORRECTOR_CLARO.png.crdownload",
            "titulo": "Corrector Claro",
            "descripcion": "El Corrector Claro cubre ojeras y manchas en pieles claras, ofreciendo un resultado natural y de larga duración.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_CLARO.png.crdownload",
            "titulo": "Polvo Claro",
            "descripcion": "El Polvo Claro proporciona una fijación perfecta y un acabado natural para pieles claras, manteniendo el maquillaje intacto todo el día.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for claro in claros:
        mostrar_producto(claro["imagen"], claro["titulo"], claro["descripcion"], claro["precio"], claro)
        st.markdown("---")  # Separador entre productos
        index += 1

    VIDEO_URL = "https://www.youtube.com/watch?v=XRNnWbaPv9Q&pp=ygUZZmFpciBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D"
    
    st.video(VIDEO_URL, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=True)





if choice == "Medio":


    #st.header('Medio')

    import base64

    with open('Fotos\MEDIO.png.crdownload', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    from streamlit_card import card

    res = card(
    title="Medio",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )

    # Datos de los Correctores
    medios = [
        {
            "imagen": "Fotos\BASE_MEDIA.png.crdownload",
            "titulo": "Base Media",
            "descripcion": "Descubre la perfección con nuestra Base Media, diseñada para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\CORRECTOR_MEDIO.png.crdownload",
            "titulo": "Corrector Medio",
            "descripcion": "Nuestro Corrector Medio proporciona una cobertura perfecta para imperfecciones en tonos de piel medios, asegurando un look fresco y luminoso.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_MEDIO.png.crdownload",
            "titulo": "Polvo Medio",
            "descripcion": "Nuestro Polvo Medio es ideal para tonos de piel medios, ofreciendo un acabado mate y control de brillo durante horas",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for medio in medios:
        mostrar_producto(medio["imagen"], medio["titulo"], medio["descripcion"], medio["precio"], medio)
        st.markdown("---")  # Separador entre productos
        index += 1

    VIDEO_URL = "https://www.youtube.com/watch?v=W0Wcaqrt94I&pp=ygUabWVkaXVtc2tpbiBtYWtldXAgdHV0b3JpYWw%3D"
    
    st.video(VIDEO_URL, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=True)





if choice == "Oscuro":


    #st.header('Oscuro')

    #st.header('Muy Claro')

    import base64

    with open('Fotos\OSCURO.png.crdownload', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    from streamlit_card import card

    res = card(
    title="Oscuro",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )

    # Datos de los Correctores
    oscuros = [
        {
            "imagen": "Fotos\BASE_OSCURA.png.crdownload",
            "titulo": "Base Oscura",
            "descripcion": "La Base Oscura se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\CORRECTOR_OSCURO.png.crdownload",
            "titulo": "Corrector Oscuro",
            "descripcion": "Disimula imperfecciones con nuestro Corrector Oscuro, ideal para tonos de piel oscuros, ofreciendo una cobertura suave y natural.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_OSCURO.png.crdownload",
            "titulo": "Polvo Oscuro",
            "descripcion": "Controla el brillo y fija tu maquillaje con nuestro Polvo Oscuro, perfecto para tonos de piel oscuros, proporcionando un acabado suave y uniforme.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for oscuro in oscuros:
        mostrar_producto(oscuro["imagen"], oscuro["titulo"], oscuro["descripcion"], oscuro["precio"], oscuro)
        st.markdown("---")  # Separador entre productos
        index += 1
    
    VIDEO_URL = "https://www.youtube.com/watch?v=3ASGtEc5un0&pp=ygUZZGFyayBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D"
    
    st.video(VIDEO_URL, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=True)


if choice == "Muy Oscuro":


    #st.header('Muy Oscuro')

    import base64

    with open('Fotos\MUY_OSCURO.png.crdownload', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    from streamlit_card import card

    res = card(
    title="Muy Oscuro",
    text="",
    image=data,
    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "150px" # <- if you want to set the card height to 300px
                }
            }
    )

    # Datos de los Correctores
    muyoscuros = [
        {
            "imagen": "Fotos\BASE_MUY_OSCURA.png.crdownload",
            "titulo": "Base Muy Oscura",
            "descripcion": "Nuestra Base Muy Oscura ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos\CORRECTOR_MUY_OSCURO.png.crdownload",
            "titulo": "Corrector Muy Oscuro",
            "descripcion": "El Corrector Muy Oscuro es perfecto para ocultar ojeras y manchas en tonos de piel muy oscuros, proporcionando un acabado impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos\POLVO_MUY_OSCURO.png.crdownload",
            "titulo": "Polvo Muy Oscuro",
            "descripcion": "El Polvo Muy Oscuro fija el maquillaje y controla el brillo en tonos de piel muy oscuros, asegurando un look impecable y natural.",
            "precio": "$150"
        }
    ]

    # Mostrar productos
    for muyoscuro in muyoscuros:
        mostrar_producto(muyoscuro["imagen"], muyoscuro["titulo"], muyoscuro["descripcion"], muyoscuro["precio"], muyoscuro)
        st.markdown("---")  # Separador entre productos
        index += 1

    import streamlit as st

    VIDEO_URL = "https://www.youtube.com/watch?v=pgcrU-V2oTg&pp=ygUgcmVhbGx5IGRhcmsgc2tpbiBtYWtldXAgdHV0b3JpYWw%3D"
    
    st.video(VIDEO_URL, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=True)
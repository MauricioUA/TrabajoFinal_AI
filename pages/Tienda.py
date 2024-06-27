import base64
import streamlit as st
from streamlit_card import card

def mostrar_producto(imagen, titulo, descripcion, precio, index):
    with open(imagen, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title=titulo,
        text=descripcion + "\nPrecio: " + precio,
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

choice = st.selectbox("Selecciona un tono", ["Todos los tonos", "Muy Claro", "Claro", "Medio", "Oscuro", "Muy Oscuro"])

index = 0

if choice == "Todos los tonos":
    with open('Fotos/Portada.jpeg', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title="SKINLY",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    bases = [
        {
            "imagen": "Fotos/BASE_MUY_CLARA.png",
            "titulo": "Base Muy Clara",
            "descripcion": "Logra un acabado impecable con nuestra Base Muy Clara, ideal para tonos de piel porcelana, ofreciendo cobertura total y un acabado natural.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/BASE_CLARA.png",
            "titulo": "Base Clara",
            "descripcion": "Nuestra Base Clara proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/BASE_MEDIA.png",
            "titulo": "Base Media",
            "descripcion": "Descubre la perfección con nuestra Base Media, diseñada para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/BASE_OSCURA.png",
            "titulo": "Base Oscura",
            "descripcion": "La Base Oscura se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/BASE_MUY_OSCURA.png",
            "titulo": "Base Muy Oscura",
            "descripcion": "Nuestra Base Muy Oscura ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$100"
        }
    ]

    for base in bases:
        mostrar_producto(base["imagen"], base["titulo"], base["descripcion"], base["precio"], index)
        st.markdown("---")
        index += 1
    
    st.header('Correctores')

    correctores = [
        {
            "imagen": "Fotos/CORRECTOR_MUY_CLARO.png",
            "titulo": "Corrector Muy Claro",
            "descripcion": "Oculta imperfecciones y ojeras con nuestro Corrector Muy Claro, perfecto para tonos de piel porcelana, dejando un acabado impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/CORRECTOR_CLARO.png",
            "titulo": "Corrector Claro",
            "descripcion": "Nuestro Corrector Claro proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/CORRECTOR_MEDIO.png",
            "titulo": "Corrector Medio",
            "descripcion": "Descubre la perfección con nuestro Corrector Medio, diseñado para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/CORRECTOR_OSCURO.png",
            "titulo": "Corrector Oscuro",
            "descripcion": "El Corrector Oscuro se adapta perfectamente a tonos de piel oscuros, proporcionando una cobertura sin igual y un acabado mate impecable.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/CORRECTOR_MUY_OSCURO.png",
            "titulo": "Corrector Muy Oscuro",
            "descripcion": "Nuestro Corrector Muy Oscuro ofrece una cobertura completa para tonos de piel muy oscuros, asegurando un look natural y radiante.",
            "precio": "$150"
        }
    ]

    for corrector in correctores:
        mostrar_producto(corrector["imagen"], corrector["titulo"], corrector["descripcion"], corrector["precio"], index)
        st.markdown("---")
        index += 1

    st.header('Polvos')

    polvos = [
        {
            "imagen": "Fotos/POLVO_MUY_CLARO.png",
            "titulo": "Polvo Muy Claro",
            "descripcion": "Fija tu maquillaje con nuestro Polvo Muy Claro, diseñado para tonos de piel porcelana, ofreciendo un acabado mate y suave.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_CLARO.png",
            "titulo": "Polvo Claro",
            "descripcion": "El Polvo Claro proporciona una fijación perfecta y un acabado natural para pieles claras, manteniendo el maquillaje intacto todo el día.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MEDIO.png",
            "titulo": "Polvo Medio",
            "descripcion": "Nuestro Polvo Medio es ideal para tonos de piel medios, ofreciendo un acabado mate y control de brillo durante horas.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_OSCURO.png",
            "titulo": "Polvo Oscuro",
            "descripcion": "Controla el brillo y fija tu maquillaje con nuestro Polvo Oscuro, perfecto para tonos de piel oscuros, proporcionando un acabado suave y uniforme.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MUY_OSCURO.png",
            "titulo": "Polvo Muy Oscuro",
            "descripcion": "El Polvo Muy Oscuro fija el maquillaje y controla el brillo en tonos de piel muy oscuros, asegurando un look impecable y natural.",
            "precio": "$150"
        }
    ]

    for polvo in polvos:
        mostrar_producto(polvo["imagen"], polvo["titulo"], polvo["descripcion"], polvo["precio"], index)
        st.markdown("---")
        index += 1

if choice == "Muy Claro":
    with open('Fotos/MUY_CLARO.png', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/jpeg;base64," + encoded.decode("utf-8")

    res = card(
        title="Muy Claro",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    muyclaros = [
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
    ]

    for muyclaro in muyclaros:
        mostrar_producto(muyclaro["imagen"], muyclaro["titulo"], muyclaro["descripcion"], muyclaro["precio"], index)
        st.markdown("---")
        index += 1

    VIDEO_URL = "https://www.youtube.com/watch?v=7PR1FxrrEhU&pp=ygUZZmFpciBza2luIG1ha2V1cCB0dXRvcmlhbA%3D%3D"
    st.video(VIDEO_URL, format="video/mp4", start_time=0, loop=False, autoplay=True, muted=True)

if choice == "Claro":
    with open('Fotos/CLARO.png', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title="Claro",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    claros = [
        {
            "imagen": "Fotos/BASE_CLARA.png",
            "titulo": "Base Clara",
            "descripcion": "Nuestra Base Clara proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_CLARO.png",
            "titulo": "Corrector Claro",
            "descripcion": "Nuestro Corrector Claro proporciona una cobertura uniforme y un acabado radiante para pieles claras, manteniendo la frescura durante todo el día.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_CLARO.png",
            "titulo": "Polvo Claro",
            "descripcion": "El Polvo Claro proporciona una fijación perfecta y un acabado natural para pieles claras, manteniendo el maquillaje intacto todo el día.",
            "precio": "$150"
        }
    ]

    for claro in claros:
        mostrar_producto(claro["imagen"], claro["titulo"], claro["descripcion"], claro["precio"], index)
        st.markdown("---")
        index += 1

if choice == "Medio":
    with open('Fotos/MEDIO.png', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title="Medio",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    medios = [
        {
            "imagen": "Fotos/BASE_MEDIA.png",
            "titulo": "Base Media",
            "descripcion": "Descubre la perfección con nuestra Base Media, diseñada para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$100"
        },
        {
            "imagen": "Fotos/CORRECTOR_MEDIO.png",
            "titulo": "Corrector Medio",
            "descripcion": "Descubre la perfección con nuestro Corrector Medio, diseñado para tonos de piel medios, ofreciendo una textura suave y cobertura duradera.",
            "precio": "$150"
        },
        {
            "imagen": "Fotos/POLVO_MEDIO.png",
            "titulo": "Polvo Medio",
            "descripcion": "Nuestro Polvo Medio es ideal para tonos de piel medios, ofreciendo un acabado mate y control de brillo durante horas.",
            "precio": "$150"
        }
    ]

    for medio in medios:
        mostrar_producto(medio["imagen"], medio["titulo"], medio["descripcion"], medio["precio"], index)
        st.markdown("---")
        index += 1

if choice == "Oscuro":
    with open('Fotos/OSCURO.png', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title="Oscuro",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    oscuros = [
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
    ]

    for oscuro in oscuros:
        mostrar_producto(oscuro["imagen"], oscuro["titulo"], oscuro["descripcion"], oscuro["precio"], index)
        st.markdown("---")
        index += 1

if choice == "Muy Oscuro":
    with open('Fotos/MUY_OSCURO.png', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    res = card(
        title="Muy Oscuro",
        text="",
        image=data,
        styles={
            "card": {
                "width": "100%",
                "height": "150px"
            }
        }
    )

    muyoscuros = [
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

    for muyoscuro in muyoscuros:
        mostrar_producto(muyoscuro["imagen"], muyoscuro["titulo"], muyoscuro["descripcion"], muyoscuro["precio"], index)
        st.markdown("---")
        index += 1

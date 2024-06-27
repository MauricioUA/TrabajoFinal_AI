import streamlit as st
from PIL import Image
from image_analysis import predict_image
import random
from st_pages import show_pages_from_config, add_page_title
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
from streamlit_extras.stoggle import stoggle
from streamlit_card import card
import base64
import os

show_pages_from_config()

st.set_page_config(page_title="Skinly - Tu maquillaje ideal")

# Estilo CSS para el fondo negro y otros estilos personalizados
st.markdown(
    """
    <style>
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
        .stFileUploader, .stCameraInput {
            text-align: center;
            font-size: 16px;
            color: #ffb3da;
        }
        .stFileUploader div, .stCameraInput div {
            font-size: 16px;
            color: #ffb3da;
        }
        .st-success {
            background-color: #000000 !important;
            color: #ffffff !important;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .myCard {
            background-color: #0e1117;
            padding: 10px;
            border-radius: 10px;
            margin: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Leer y codificar la imagen
image_path = 'Fotos/Portada.jpeg'
if os.path.exists(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/jpeg;base64," + encoded.decode("utf-8")
else:
    st.error("El archivo de imagen no se encuentra en la ruta especificada. Por favor, asegúrate de que el archivo 'Portada.jpeg' esté en la carpeta 'Fotos'.")

# Crear una tarjeta con la imagen codificada
res = card(
    title="SKINLY",
    text="Encuentra tu maquillaje ideal",
    image=data,
    styles={
        "card": {
            "width": "100%",  # La tarjeta usará el ancho de su contenedor
            "height": "150px"  # Altura de la tarjeta
        }
    }
)

# Initialize session state for disabling camera
if "disable_camera" not in st.session_state:
    st.session_state.disable_camera = False

# Card con la información
st.markdown("""
    <div class='myCard'>
       <p>Usar Skinly es muy simple, solo sigue los siguientes pasos para obtener la mejor recomendación sobre tu maquillaje perfecto:</p>
            <ol>
                <li>Posa sin anteojos y sin maquillaje</li>
                <li>Asegúrate que el pelo no tape tu cara</li>
                <li>Comprueba tener buena iluminación</li>
                <li>Toma la foto con una expresión neutra</li>
            </ol>
    </div>
    """, unsafe_allow_html=True)

input_img = st.file_uploader("", type=["jpeg", "jpg", "png"])
if input_img is not None:
    st.session_state.disable_camera = True
else:
    st.session_state.disable_camera = False

if not st.session_state.disable_camera:
    camera_img = st.camera_input("")

# Process the image when uploaded or captured
def process_image(image_file):
    with st.spinner('Analizando imagen...'):
        result = predict_image(image_file)
        label = result["Class"]
        confidence_score = result["Confidence Score"]

        # Frases para solicitar una nueva foto
        frases_nueva_foto = [
            "Por favor, intenta tomar otra foto.",
            "La calidad de la imagen no es suficiente. Por favor, toma otra foto.",
            "Inténtalo de nuevo con una mejor iluminación.",
            "La foto no es clara. Por favor, vuelve a intentarlo.",
            "Necesitamos una foto más nítida. Intenta de nuevo.",
            "La imagen no se pudo procesar correctamente. Intenta otra vez.",
            "Por favor, asegúrate de que la cámara esté enfocada y toma otra foto.",
            "La foto no es lo suficientemente clara. Intenta tomar otra.",
            "Intenta capturar una imagen con mejor ángulo.",
            "No se pudo analizar la imagen. Inténtalo de nuevo."
        ]

        # Mostrar mensaje aleatorio si la confianza es baja
        if confidence_score < 0.9:
            st.warning(random.choice(frases_nueva_foto))
            return

        # Create a dictionary for recommendations
        recommendations = {
            "0 Muy Claro": ("Muy Clara", "Ideal para pieles muy claras, esta base ofrece una cobertura impecable que ilumina y realza tu belleza natural sin dejar sensación pesada. ¡Estoy seguro de que te quedará muy bien!", "Tienda"),
            "1 Claro": ("Clara", "Es perfecta para lograr un acabado suave y natural. Con una fórmula ligera y de larga duración, proporciona una cobertura uniforme que dejará tu piel con un aspecto luminoso. ¡Te verás increíble!", "Tienda"),
            "2 Medio": ("Media", "Su textura sedosa se funde perfectamente, proporcionando una cobertura natural que resalta tu resplandor. ¡Seguro que notarás la diferencia!", "Tienda"),
            "3 Oscuro": ("Oscura", "Ofrece una cobertura uniforme que disimula imperfecciones y realza tu tono natural. Con una fórmula hidratante, tu piel lucirá fresca y radiante todo el día. ¡Destacarás tu belleza natural!", "Tienda"),
            "4 Muy Oscuro": ("Muy Oscura", "Su fórmula ligera y de alta cobertura se adapta perfectamente a tu piel, ofreciendo un acabado radiante y uniforme. ¡Luce una piel perfecta sin esfuerzo!", "Tienda"),
        }

        if label in recommendations:
            product, description, link = recommendations[label]
            st.markdown(
                f"<div class='st-success'>En base a tu tono de piel, te recomiendo utilizar nuestra base de maquillaje <b>{product}</b>. {description}</div>",
                unsafe_allow_html=True
            )
            if link:
                st.markdown(f"[Ver Producto]({link})")
        else:
            st.warning("No se ha reconocido la etiqueta proporcionada.")

# Automatically process the image once it's uploaded or captured
if input_img is not None:
    process_image(Image.open(input_img))
elif 'camera_img' in locals() and camera_img is not None:
    process_image(Image.open(camera_img))

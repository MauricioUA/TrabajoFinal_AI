import streamlit as st
from PIL import Image
from image_analysis import predict_image
import random
from st_pages import show_pages_from_config, add_page_title
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Skinly - Tu maquillaje ideal")




# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be

show_pages_from_config()



# Hide the sidebar toggle button
st.markdown(
    """
<style>
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
</style>
""",
    unsafe_allow_html=True,
)

# Add a custom header
st.markdown("<h1 style='text-align: center; color: #ff66b2;'>Bienvenido a Skinly!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffa3d7;'>Encuentra el maquillaje perfecto para tu tono de piel</h3>", unsafe_allow_html=True)

# Initialize session state for disabling camera
if "disable_camera" not in st.session_state:
    st.session_state.disable_camera = False

# Add an image uploader and camera input
st.markdown("<h4 style='text-align: center; color: #ffb3da;'>Sube una imagen o toma una foto para empezar</h4>", unsafe_allow_html=True)

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
            st.success(confidence_score)
            st.warning(random.choice(frases_nueva_foto))
            return

        # Create a dictionary for recommendations
        recommendations = {
            "0 Muy Claro": ("Porcelana", "Ideal para pieles muy claras, esta base ofrece una cobertura impecable que ilumina y realza tu belleza natural sin dejar sensación pesada. ¡Estoy seguro de que te quedará muy bien!", "Porcelana"),
            "1 Claro": ("Marfil", "Es perfecta para lograr un acabado suave y natural. Con una fórmula ligera y de larga duración, proporciona una cobertura uniforme que dejará tu piel con un aspecto luminoso. ¡Te verás increíble!", "Marfil"),
            "2 Medio": ("Beige", "Su textura sedosa se funde perfectamente, proporcionando una cobertura natural que resalta tu resplandor. ¡Seguro que notarás la diferencia!", "Tienda"),
            "3 Oscuro": ("Arena", "Ofrece una cobertura uniforme que disimula imperfecciones y realza tu tono natural. Con una fórmula hidratante, tu piel lucirá fresca y radiante todo el día. ¡Destacarás tu belleza natural!", "Tienda"),
            "4 Muy Oscuro": ("Beige Dorado", "Su fórmula ligera y de alta cobertura se adapta perfectamente a tu piel, ofreciendo un acabado radiante y uniforme. ¡Luce una piel perfecta sin esfuerzo!", "Tienda"),
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

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the directory containing the script
directory_files = os.listdir(script_dir)
# st.text("Files in directory: " + ", ".join(directory_files))

def predict_image(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model_path = os.path.join(script_dir, "modelo_caras", "keras_model.h5")
    model = load_model(model_path, compile=False)

    # Load the labels
    labels_path = os.path.join(script_dir, "modelo_caras", "labels.txt")
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Convert the image to RGB
    image = img.convert("RGB")

    # Resize and crop the image to 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Turn the image into a numpy array and normalize it
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict with the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # Return prediction and confidence score
    return {
        "Class": class_name,
        "Confidence Score": confidence_score,
    }

# Streamlit App
st.set_page_config(layout="wide")  # Permite que la App no sea centrada, sino en pantalla completa

st.title("Bienvenido a Skinly! El lugar donde te recomendamos el maquillaje perfecto para tu tono de piel!")

input_img = st.file_uploader("Ingresa una imagen para que podamos analizarla", type=["jpeg", "jpg", "png"])
camera_img = st.camera_input("O toma una foto con tu cámara")

if input_img is not None or camera_img is not None:
    if st.button("Encontrar Maquillaje"):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.info("Imagen Cargada:")
            if input_img is not None:
                st.image(input_img, use_column_width=True)
                image_file = Image.open(input_img)
            else:
                st.image(camera_img, use_column_width=True)
                image_file = Image.open(camera_img)

        with col2:
            st.info("Recomendación")
            with st.spinner('Analizando imagen...'):
                result = predict_image(image_file)
                label = result["Class"]
                confidence_score = result["Confidence Score"]

                # Mostrar la etiqueta y el puntaje de confianza
                #st.success(f"Etiqueta: {label}")
                #st.success(f"Puntaje de confianza: {confidence_score:.2f}")

                if label == "0 MST-E 1":
                    st.success("En base a tu tono de piel, te recomiendo utilizar nuestra base de maquillaje Porcelana. Ideal para pieles muy claras, esta base ofrece una cobertura impecable que ilumina y realza tu belleza natural sin dejar sensación pesada. ¡Estoy seguro de que te quedará muy bien!")
                    st.markdown("[Ver Producto](Porcelana)")
                elif label == "1 MST-E 2":
                    st.success("Para tu tono de piel claro, te sugiero probar nuestra base de maquillaje Marfil. Es perfecta para lograr un acabado suave y natural. Con una fórmula ligera y de larga duración, proporciona una cobertura uniforme que dejará tu piel con un aspecto luminoso. ¡Te verás increíble!")
                    st.markdown("[Ver Producto](Marfil)")
                elif label == "2 MST-E 3":
                    st.success("Con tu tono de piel claro a medio, nuestra base de maquillaje Beige es una excelente elección. Su textura sedosa se funde perfectamente, proporcionando una cobertura natural que resalta tu resplandor. ¡Seguro que notarás la diferencia!")
                    st.markdown("[Ir a Tienda](Tienda)")                
                elif label == "3 MST-E 4":
                    st.success("Para tu tono de piel medio claro, te recomiendo nuestra base de maquillaje Arena. Ofrece una cobertura uniforme que disimula imperfecciones y realza tu tono natural. Con una fórmula hidratante, tu piel lucirá fresca y radiante todo el día. ¡Destacarás tu belleza natural!")
                    st.markdown("[Ir a Tienda](Tienda)")
                elif label == "4 MST-E 5":
                    st.success("Tu tono de piel medio se verá espectacular con nuestra base de maquillaje Beige Dorado. Su fórmula ligera y de alta cobertura se adapta perfectamente a tu piel, ofreciendo un acabado radiante y uniforme. ¡Luce una piel perfecta sin esfuerzo!")
                    st.markdown("[Ir a Tienda](Tienda)")
                elif label == "5 MST-E 6":
                    st.success("Para tu tono de piel medio oscuro, te sugiero nuestra base de maquillaje Caramelo. Diseñada para proporcionar una cobertura impecable, esta base hidrata y unifica tu piel, dejándola con un aspecto naturalmente bello y luminoso. ¡Te sentirás increíble cada día!")
                    st.markdown("[Ir a Tienda](Tienda)")
                elif label == "6 MST-E 7":
                    st.success("Con tu tono de piel oscuro, nuestra base de maquillaje Almendra es la solución perfecta. Con una fórmula rica en hidratación, esta base proporciona un acabado suave y luminoso, destacando tu belleza única. ¡Sé la mejor versión de ti mismo!")
                elif label == "7 MST-E 8":
                    st.success("Para tu tono de piel muy oscuro, te recomiendo nuestra base de maquillaje Cacao. Ofrece una cobertura impecable que unifica el tono de la piel mientras la hidrata profundamente. Con un acabado mate natural, tu piel lucirá radiante y sin imperfecciones. ¡Te verás espectacular!")
                    st.markdown("[Ir a Tienda](Tienda)")
                elif label == "8 MST-E 9":
                    st.success("Tu tono de piel profundo se verá magnífico con nuestra base de maquillaje Espresso. Su fórmula de alta cobertura se adapta perfectamente a tu piel, ofreciendo un acabado impecable y duradero. ¡Realza tu belleza con un tono que complementa tu piel perfectamente!")
                    st.markdown("[Ir a Tienda](Tienda)")
                elif label == "9 MST-E 10":
                    st.success("Para tu tono de piel muy profundo, te sugiero nuestra base de maquillaje Ébano. Con una cobertura completa y un acabado mate, esta base unifica y resalta tu tono de piel de manera natural. Hidrata y protege, dejando tu piel con un aspecto saludable y radiante. ¡Siente la diferencia!")
                    st.markdown("[Ir a Tienda](Tienda)")
                else:
                    st.warning("No se ha reconocido la etiqueta proporcionada.")
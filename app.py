from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
from openai import OpenAI



def predict_image(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("modelo_caras\keras_model.h5", compile=False)

    # Load the labels
    class_names = open("modelo_caras\labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Open the image and convert it to RGB
    #image = Image.open(image_path).convert("RGB") #orignial
    image = img.convert("RGB") #video campus clase 6, minuto 37

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

# Usage example:
#result = predict_image("your_image_path_here.jpg")
#print("Class:", result["Class"])
#print("Confidence Score:", result["Confidence Score"])





# def generate_recipe(label):


   # client = OpenAI(api_key="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")

    

    #response = client.completions.create(
    #model="gpt-3.5-turbo-instruct",
    #prompt= f"Sos un asistente experto en cocina con frutas y tenes que recomendar solo 3 ideas de comida para hacer con {label}. Puede ser algo comestible o bebible, considerando si la fruta está buena o mala. No hace falta que expliques las recetas, solo una lista con 3 ideas",
    #temperature=0.5,
    #max_tokens=300,
    #top_p=1,
    #frequency_penalty=0,
    #presence_penalty=0
    #)

    #return response.choices[0].text



# Streamlit App
#st.set_page_config(layout="wide") #Permite que la App no sea centrada, sino en pantalla completa

st.title("Clasificador de Caras: Humanas vs AI")

input_img = st.file_uploader("Ingresa la cara que quieres analizas", type=["jpeg", "jpg", "png"])


if input_img is not None:
    if st.button("Clasificar Cara"):
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.info("Cara cargada:")
            st.image(input_img, use_column_width=True)
        
        with col2:
            st.info("Resultado")
            image_file = Image.open(input_img)
            with st.spinner('Analizando imagen...'):
                result = predict_image(image_file)
                label = result["Class"]
                confidence_score = result["Confidence Score"]

                # Mostrar la etiqueta y el puntaje de confianza
                st.success(f"Etiqueta: {label}")
                st.success(f"Puntaje de confianza: {confidence_score:.2f}")
        
        with col3:
            st.info("ChatGPT")
    



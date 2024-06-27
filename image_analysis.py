from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

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

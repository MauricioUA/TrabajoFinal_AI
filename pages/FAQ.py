from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import os

# Título de la aplicación
st.title('Preguntas Frecuentes sobre Skinly')

# Pregunta 1
with st.expander("¿Cómo funciona la aplicación Skinly para recomendar productos de maquillaje?"):
    st.write("""
        Skinly utiliza tecnología de inteligencia artificial para analizar una foto de tu rostro y determinar tu tono de piel. 
        Basándose en esta información, la aplicación recomienda productos de maquillaje que mejor se adapten a tu tono y tipo de piel. 
        Además, Skinly ofrece tutoriales y consejos personalizados para ayudarte a aplicar el maquillaje de manera efectiva.
    """)

# Pregunta 2
with st.expander("¿Es seguro subir mi foto a la aplicación?"):
    st.write("""
        Sí, la seguridad y privacidad de nuestros usuarios son nuestras principales prioridades. 
        Todas las fotos subidas a Skinly se procesan de manera segura y se almacenan con estrictas medidas de seguridad. 
        No compartimos tus fotos ni datos personales con terceros sin tu consentimiento explícito.
    """)

# Pregunta 3
with st.expander("¿La aplicación es gratuita?"):
    st.write("""
        Sí, Skinly es gratuita para descargar y usar. 
        Puedes explorar recomendaciones de productos y tutoriales sin costo. 
        Sin embargo, la compra de productos de maquillaje recomendados a través de la aplicación está sujeta a precios de los productos y posibles costos de envío.
    """)

# Pregunta 4
with st.expander("¿Qué marcas de maquillaje están disponibles en Skinly?"):
    st.write("""
        Skinly colabora con una amplia variedad de marcas de maquillaje reconocidas, incluyendo L'Oréal, Maybelline, Sephora, y muchas más. 
        Constantemente ampliamos nuestra base de datos para incluir nuevas marcas y productos que puedan interesar a nuestros usuarios.
    """)

# Pregunta 5
with st.expander("¿Puedo devolver productos comprados a través de Skinly si no me gustan?"):
    st.write("""
        Las políticas de devolución de productos comprados a través de Skinly están sujetas a las políticas de las marcas y tiendas de cosméticos asociadas. 
        Al realizar una compra, te proporcionaremos información sobre las políticas de devolución y cambio específicas de cada proveedor. 
        En caso de cualquier problema, nuestro equipo de soporte al cliente está disponible para asistirte.
    """)

# Ejecuta el siguiente comando en tu terminal para ver la aplicación: streamlit run nombre_del_archivo.py

import streamlit as st
from wordcloud import WordCloud
from io import BytesIO
from pydub import AudioSegment
import speech_recognition as sr

def main():
    st.title("Contador de palabras en audio y nube de palabras")

    # Paso 1: Cargar el archivo de audio
    st.sidebar.title("Cargar archivo de audio")
    uploaded_file = st.sidebar.file_uploader("Cargar archivo de audio", type=["mp3", "wav"])

    if uploaded_file:
        # Paso 2: Interpretar las palabras del audio
        st.sidebar.title("Procesamiento de audio")
        audio = AudioSegment.from_file(BytesIO(uploaded_file.read()))
        r = sr.Recognizer()
        with sr.AudioFile(BytesIO(uploaded_file.read())) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="es-ES")
            st.sidebar.subheader("Texto extraído del audio:")
            st.sidebar.write(text)

        # Paso 3: Contabilizar las palabras y mostrar la nube de palabras
        st.sidebar.title("Nube de palabras")
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        st.image(wordcloud.to_array(), use_column_width=True)

        # Mostrar el contador de palabras
        words = text.split()
        word_count = len(words)
        st.subheader("Contador de palabras:")
        st.write(f"El audio contiene {word_count} palabras.")

if __name__ == "__main__":
    main()

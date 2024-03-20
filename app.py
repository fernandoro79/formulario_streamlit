import streamlit as st

def main():
    st.title("Aplicación para cargar datos personales")
    
    # Entradas de datos
    name = st.text_input("Nombre")
    age = st.number_input("Edad", min_value=0, max_value=150, step=1)
    email = st.text_input("Correo electrónico")
    
    # Botón para enviar los datos
    if st.button("Enviar"):
        # Validación de datos
        if not name or not email:
            st.warning("Por favor, ingrese su nombre y correo electrónico.")
        else:
            # Mostrar los datos ingresados
            st.success("Datos enviados con éxito:")
            st.write("Nombre:", name)
            st.write("Edad:", age)
            st.write("Correo electrónico:", email)

if __name__ == "__main__":
    main()
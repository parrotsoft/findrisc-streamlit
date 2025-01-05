import streamlit as st
from helpers.Helpers import imc

st.title("Escala de Findrisc")

col1, col2 = st.columns(2)

with col1:
    st.radio("Género", ("Masculino", "Femenino"), key="sex", horizontal=True)
    st.number_input("Peso en Kg", key="weight")
    st.markdown(f"### **IMC:** {imc()}")

with col2:
    st.date_input("Fecha de Nacimiento", key="birth")
    st.number_input("Altura en m2", key="height")
    st.number_input("Perimetro abdominal (medido a nivel del ombligo) :", key="perimeter")

with st.container(border=True):
    col3, col4 = st.columns(2)

    with col3:
        st.radio("¿Realiza al menos 30 minutos diarios de actividad física?", ("Si", "No"), key="ask1")
        st.radio("¿Le ha recetado alguna vez medicamentos contra HTA?", ("Si", "No"), key="ask2")
        st.radio("¿Ha habilitado algún diagnóstico de DM en su familia?", (
        "No", "Si: Abuelos, tíos o primos hermanos (pero no padres, hermanos o hijos)", "Si: Padres, hermano o hijos"),
                 key="ask3")

    with col4:
        st.radio("¿Con qué frecuencia come frutas, verduras y hortalizas?", ("A diario", "No a diario"), key="ask4")
        st.radio("¿Le ha detectado alguna vez niveles altos de glucosa en sangre?", ("Si", "No"), key="ask5")
        st.markdown("## PUNTUACIÓN TOTAL: 0")


def calculate():
    st.write("La")


st.button("Calcular", key="calculate", on_click=calculate, type="primary", icon="🔥", use_container_width=True)

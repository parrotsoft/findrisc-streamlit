import streamlit as st
from helpers.Helpers import imc
from core.Data import df
from core.AskCalc import *

st.set_page_config(
    page_title="Escala de Findrisc",
    page_icon="🧊",
)

st.title("Escala de Findrisc")

col1, col2 = st.columns(2)

with col1:
    st.radio("Género", ("Masculino", "Femenino"), key="sex", horizontal=True)
    st.number_input("Edad", key="age")
    st.number_input("Perimetro abdominal (medido a nivel del ombligo) :", key="perimeter")

with col2:
    st.number_input("Peso en Kg", key="weight")
    st.number_input("Altura en m2", key="height")
    st.markdown(f"### **IMC:** {imc(st.session_state.get('weight'), st.session_state.get('height'))}")


with st.container(border=True):
    col3, col4 = st.columns(2)

    with col3:
        st.radio("¿Realiza al menos 30 minutos diarios de actividad física?", ("Si", "No"), key="ask1")
        st.radio("¿Le ha recetado alguna vez medicamentos contra HTA?", ("Si", "No"), key="ask3")
        st.radio("¿Ha habilitado algún diagnóstico de DM en su familia?", (
            "No", "Si: Abuelos, tíos o primos hermanos (pero no padres, hermanos o hijos)",
            "Si: Padres, hermano o hijos"),
                 key="ask5")

    with col4:
        st.radio("¿Con qué frecuencia come frutas, verduras y hortalizas?", ("A diario", "No a diario"), key="ask2")
        st.radio("¿Le ha detectado alguna vez niveles altos de glucosa en sangre?", ("Si", "No"), key="ask4")
        st.text_input("Puntuación Total", disabled=True, key="total_point")


def calculate():
    total = 0
    imc_total = imc(st.session_state.get('weight'), st.session_state.get('height'));

    total += by_age(int(st.session_state.get('age')))
    total += by_imc(int(imc_total))
    total += by_abdominal_perimeter(st.session_state.get('perimeter'), st.session_state.get('sex'))
    total += by_ask_one(st.session_state.get('ask1'))
    total += by_ask_two(st.session_state.get('ask2'))
    total += by_ask_three(st.session_state.get('ask3'))
    total += by_ask_four(st.session_state.get('ask4'))
    total += by_ask_five(st.session_state.get('ask5'))

    st.session_state['total_point'] = f"{total}"
    validate_general(total)
    st.toast('Cálculo realizado!', icon='🎉')


st.button("Calcular", key="calculate", on_click=calculate, type="primary", icon="🔥", use_container_width=True)

st.html("<h1 style='margin-top: 1em;'>Tabla de referencia</h1>")
st.dataframe(
    df,
    column_config={
        "total_points": "Puntuación total",
        "risk_diabetes": "Riesgo de desarrollar diabetes en los próximos 10 años",
        "interpretation": "Interpretación"
    },
    hide_index=True,
    use_container_width=True,
)

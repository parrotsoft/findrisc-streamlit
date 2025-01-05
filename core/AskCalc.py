import streamlit as st


def by_age(age):
    if age < 45:
        return 0
    elif 45 <= age <= 54:
        return 2
    elif 55 <= age <= 64:
        return 3
    elif age > 64:
        return 4
    else:
        return 0


def by_imc(imc):
    if imc < 25:
        return 0
    elif 25 < imc <= 30:
        return 1
    elif imc > 30:
        return 3
    else:
        return 0


def by_abdominal_perimeter(abdominal_perimeter, sex):
    if sex == 'Masculino':
        if abdominal_perimeter < 94:
            return 0
        elif 94 <= abdominal_perimeter <= 102:
            return 3
        elif abdominal_perimeter > 102:
            return 4
        else:
            return 0
    elif sex == 'Femenino':
        if abdominal_perimeter < 80:
            return 0
        elif 80 <= abdominal_perimeter <= 88:
            return 3
        elif abdominal_perimeter > 88:
            return 4
        else:
            return 0
    else:
        return 0


def by_ask_one(ask):
    if ask == 'Si':
        return 0
    elif ask == 'No':
        return 2
    else:
        return 0


def by_ask_two(ask):
    if ask == 'A diario':
        return 0
    elif ask == 'No a diario':
        return 1
    else:
        return 0


def by_ask_three(ask):
    if ask == 'Si':
        return 2
    elif ask == 'No':
        return 0
    else:
        return 0


def by_ask_four(ask):
    if ask == 'Si':
        return 5
    elif ask == 'No':
        return 0
    else:
        return 0


def by_ask_five(ask):
    if ask == 'Si: Padres, hermano o hijos':
        return 5
    elif ask == 'No':
        return 0
    else:
        return 3


def validate_general(total):
    if total <= 7:
        st.toast('Nivel de riesgo bajo', icon='😊')
    elif total > 7 and total <= 11:
        st.toast('Nivel de riesgo ligeramente elevado', icon='🙂')
    elif total >= 12 and total <= 14:
        st.toast('Nivel de riesgo moderado', icon='😐')
    elif total >= 15 and total <= 20:
        st.toast('Nivel de riesgo alto', icon='😕')
    elif total > 20:
        st.toast('Nivel de riesgo muy alto', icon='☹')

import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

st.title("👑 Trivia de Villanas Disney")
st.write("Responde las 5 preguntas. ¡Suerte!")

# Banco de preguntas
questions_bank = [
    {
        "question": "¿Cómo se llama la villana de La Sirenita?",
        "options": ["Úrsula", "Maléfica", "Cruella", "Jafar"],
        "answer": "Úrsula"
    },
    {
        "question": "¿Qué villana odia a los dálmatas?",
        "options": ["Maléfica", "Cruella", "Yzma", "Gothel"],
        "answer": "Cruella"
    },
    {
        "question": "¿Quién es la villana de Enredados?",
        "options": ["Úrsula", "Madre Gothel", "Evil Queen", "Yzma"],
        "answer": "Madre Gothel"
    },
    {
        "question": "¿Qué villana se convierte en dragón?",
        "options": ["Maléfica", "Cruella", "Yzma", "Gothel"],
        "answer": "Maléfica"
    },
    {
        "question": "¿Quién es la villana de El emperador y sus locuras?",
        "options": ["Yzma", "Cruella", "Úrsula", "Maléfica"],
        "answer": "Yzma"
    }
]

# 🔥 Inicializar estado (SOLO UNA VEZ)
if "questions" not in st.session_state:
    st.session_state.questions = questions_bank.copy()
    random.shuffle(st.session_state.questions)

    # Mezclar opciones también UNA sola vez
    for q in st.session_state.questions:
        random.shuffle(q["options"])

if "answers" not in st.session_state:
    st.session_state.answers = {}

# Mostrar preguntas
for i, q in enumerate(st.session_state.questions):
    st.subheader(f"Pregunta {i+1}")
    
    selected = st.radio(
        q["question"],
        q["options"],
        key=f"q_{i}"
    )

    st.session_state.answers[i] = selected

# Botón de resultado
if st.button("Ver resultados"):
    score = 0

    for i, q in enumerate(st.session_state.questions):
        if st.session_state.answers.get(i) == q["answer"]:
            score += 1

    st.write(f"Tu puntaje: {score}/5")

    if score == 5:
        st.success("¡Perfecto! 🎉 Eres experta en villanas Disney 👑")
        st.balloons()
    else:
        st.info("Sigue intentando 💪")

# Botón para reiniciar juego
if st.button("Jugar otra vez"):
    st.session_state.clear()
    st.rerun()

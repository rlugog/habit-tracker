import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Seguimiento de Hábitos", page_icon="📈")

# Título
st.title("Seguimiento de Hábitos 📈")

# Descripción
st.write("""
Bienvenido a tu aplicación de seguimiento de hábitos. 
Aquí puedes registrar tus hábitos diarios y visualizar tu progreso a lo largo del tiempo.
""")

# Inicializamos una lista de hábitos
if "habits" not in st.session_state:
    st.session_state["habits"] = []

# Formulario para registrar hábitos
st.subheader("Registrar un hábito")
habit_name = st.text_input("Nombre del hábito")
habit_date = st.date_input("Fecha")
habit_status = st.selectbox("Estado", ["Completado", "No completado"])

if st.button("Añadir hábito"):
    st.session_state["habits"].append({"Hábito": habit_name, "Fecha": habit_date, "Estado": habit_status})
    st.success("¡Hábito registrado exitosamente!")

# Mostrar los hábitos registrados
st.subheader("Hábitos registrados")
if len(st.session_state["habits"]) > 0:
    df = pd.DataFrame(st.session_state["habits"])
    st.dataframe(df)

    # Gráficos del progreso
    st.subheader("Progreso de hábitos")
    progress = df.groupby("Estado")["Hábito"].count()
    fig, ax = plt.subplots()
    progress.plot(kind="bar", color=["green", "red"], ax=ax)
    ax.set_ylabel("Número de hábitos")
    st.pyplot(fig)
else:
    st.write("No hay hábitos registrados aún.")

# Footer
st.write("Desarrollado por Rodrigo Lugo")

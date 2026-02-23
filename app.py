import streamlit as st

# ---------------------------------------------------
# 🎨 CONFIGURACIÓN GENERAL DE LA PÁGINA
# ---------------------------------------------------
# Aquí definimos el título, ícono y estructura básica
# de la aplicación antes de que se renderice cualquier contenido.

st.set_page_config(
    page_title="Proyecto Módulo 1 – Fundamentos de Python",
    page_icon="📊",
    layout="centered"
)

# ---------------------------------------------------
# 🎨 ESTILOS PERSONALIZADOS (CSS)
# ---------------------------------------------------
# Fondo celeste y texto negro para mejor contraste visual
# Aquí hemos personalizado nuestra aplicación 

st.markdown("""
    <style>
        .stApp {
            background-color: #87CEEB; /* Celeste */
            color: black;
        }

        .stMarkdown, .stText, .stTitle, .stSubheader, 
        .stHeader, .stMetric, label, p, span {
            color: black !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #5DADE2; /* Azul un poco más fuerte para sidebar */
        }

        .stSidebar label {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 🧠 INICIALIZACIÓN DE SESSION STATE
# ---------------------------------------------------
# Creamos una variable persistente para almacenar
# las actividades financieras registradas por el usuario.

if "actividades" not in st.session_state:
    st.session_state.actividades = []

# ---------------------------------------------------
# 🏗 CLASE ACTIVIDAD (POO)
# ---------------------------------------------------
# Esta clase modela una actividad financiera.
# Incluye atributos y métodos propios.

class Actividad:
    """
    Clase que representa una actividad financiera.
    Aplica Programación Orientada a Objetos (POO).
    """

    # Constructor: inicializa los atributos del objeto
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    # Método que evalúa si la actividad está dentro del presupuesto
    def esta_en_presupuesto(self):
        return self.gasto_real <= self.presupuesto

    # Método que devuelve la información resumida de la actividad
    def mostrar_info(self):
        diferencia = self.presupuesto - self.gasto_real
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "presupuesto": self.presupuesto,
            "gasto_real": self.gasto_real,
            "diferencia": diferencia
        }

# ---------------------------------------------------
# 🏠 FUNCIÓN HOME
# DEFINICIÓN DE FUNCIONES AUXILIARES
# ---------------------------------------------------

def mostrar_home():
    st.title("📊 Proyecto Módulo 1 – Fundamentos de Python 🚀")

    st.markdown("### 👨‍💻 Información del Proyecto 📘")
    st.write("📌 Nombre del estudiante: Williams Michael Rupailla Ruiz 👤")
    st.write("📌 Curso: Especialización en Python for Analytics 📚 – Módulo 1 - Edición 55 🐍")
    st.write("📌 Año: 2026 📅")

    st.markdown("---")

    st.markdown("### 🎯 Objetivo del Proyecto 💡")
    st.write("Este proyecto integra conceptos fundamentales de programación en Python 🐍 mediante una aplicación interactiva desarrollada con Streamlit 📊.")

    st.markdown("---")
    st.markdown("### 🛠 Tecnologías Utilizadas 💻")
    st.write("🐍 Python")
    st.write("📊 Streamlit")
    st.write("🧠 Programación Funcional 🧩")
    st.write("🏗 Programación Orientada a Objetos (POO) 🏗️")
    st.write("📦 Variables")
    st.write("🚦 Condicionales")
    st.write("🗂️ Estructuras de datos")
    st.write("⚙️ Funciones")




# ---------------------------------------------------
# 💰 EJERCICIO 1 – VARIABLES Y CONDICIONALES
# ---------------------------------------------------

def ejercicio_1():
    st.title("💰 Ejercicio 1 – Control de Presupuesto 📊")
    
    st.markdown("### 💰 Evaluador Financiero 💰🔎📈")
    st.write("Ingrese los valores para analizar si el gasto se mantiene dentro del presupuesto.")

    # -------------------------------
    # INPUTS
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        presupuesto = st.number_input(
            "💵 Presupuesto asignado:",
            min_value=0.0,
            format="%.2f"
        )

    with col2:
        gasto = st.number_input(
            "💸 Gasto realizado:",
            min_value=0.0,
            format="%.2f"
        )

    # -------------------------------
    # BOTÓN DE EVALUACIÓN
    # -------------------------------
    if st.button("🔎 Evaluar situación financiera 📈"):

        diferencia = presupuesto - gasto

        st.markdown("---")
        st.markdown("### 📊 Resultado del Análisis")

        # Métricas visuales
        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Presupuesto", f"{presupuesto:.2f}")
        col2.metric("💸 Gasto", f"{gasto:.2f}")
        col3.metric("📊 Diferencia", f"{diferencia:.2f}")

        # Barra de progreso (porcentaje ejecutado)
        if presupuesto > 0:
            porcentaje = min(gasto / presupuesto, 1.0)
            st.progress(porcentaje)

        # -------------------------------
        # CONDICIONAL
        # -------------------------------
        if gasto <= presupuesto:
            st.success("✅ El gasto está dentro del presupuesto. 🎉")
            st.write(f"Te quedan **{diferencia:.2f}** disponibles.")
        else:
            st.error("🚨 El presupuesto ha sido excedido. ⚠️")
            st.write(f"Te excediste por **{abs(diferencia):.2f}**.")


# ---------------------------------------------------
# 📋 EJERCICIO 2 – LISTAS Y DICCIONARIOS
# ---------------------------------------------------

def ejercicio_2():
    st.title("📋 Ejercicio 2 – Registro de Actividades Financieras 📊")

    st.markdown("### 📝 Registrar nueva actividad")

    # -------------------------------
    # INPUTS
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:
        nombre = st.text_input("📝 Nombre de la actividad")
        tipo = st.selectbox("Tipo de actividad", ["Inversión", "Operativo", "Marketing", "Otro"])

    with col2:
        presupuesto = st.number_input("💰 Presupuesto asignado", min_value=0.0, format="%.2f")
        gasto_real = st.number_input("💸 Gasto real", min_value=0.0, format="%.2f")

    # -------------------------------
    # BOTÓN AGREGAR
    # -------------------------------

    if st.button("➕ Agregar actividad 📌"):

        if nombre.strip() == "":
            st.warning("El nombre de la actividad no puede estar vacío.")
        else:
            actividad = {
                "nombre": nombre,
                "tipo": tipo,
                "presupuesto": presupuesto,
                "gasto_real": gasto_real
            }

            st.session_state.actividades.append(actividad)
            st.success("✅ Actividad agregada correctamente. 🎉")

    st.markdown("---")

    # -------------------------------
    # MOSTRAR ACTIVIDADES
    # -------------------------------

    if len(st.session_state.actividades) > 0:

        st.markdown("### 📊 Actividades registradas 📈")

        total_presupuesto = 0
        total_gasto = 0

        # Recorremos con índice para poder eliminar
        for i, act in enumerate(st.session_state.actividades):

            diferencia = act["presupuesto"] - act["gasto_real"]
            total_presupuesto += act["presupuesto"]
            total_gasto += act["gasto_real"]

            with st.container():
                col1, col2, col3 = st.columns([3, 2, 1])

                with col1:
                    st.subheader(f"{act['nombre']} ({act['tipo']})")

                    st.write(f"Presupuesto: {act['presupuesto']:.2f}")
                    st.write(f"Gasto Real: {act['gasto_real']:.2f}")

                with col2:
                    if act["gasto_real"] <= act["presupuesto"]:
                        st.success("✅ Dentro del presupuesto")
                        st.write(f"Disponible: {diferencia:.2f}")
                    else:
                        st.error("🚨 PRESUPUESTO EXCEDIDO")
                        st.write(f"Exceso: {abs(diferencia):.2f}")

                with col3:
                    if st.button("❌ Eliminar", key=f"eliminar_{i}"):
                        st.session_state.actividades.pop(i)
                        st.rerun()

            st.markdown("---")

        # -------------------------------
        # RESUMEN GENERAL
        # -------------------------------

        diferencia_total = total_presupuesto - total_gasto

        st.markdown("### 📈 Resumen General")

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Presupuesto Total", f"{total_presupuesto:.2f}")
        col2.metric("💸 Gasto Total", f"{total_gasto:.2f}")
        col3.metric("📈 Diferencia Total", f"{diferencia_total:.2f}")

        if total_presupuesto > 0:
            porcentaje_total = min(total_gasto / total_presupuesto, 1.0)
            st.progress(porcentaje_total)

        # -------------------------------
        # BOTÓN LIMPIAR TODO
        # -------------------------------

        if st.button("🗑️ Limpiar todas las actividades 🚨"):
            st.session_state.actividades.clear()
            st.rerun()

    else:
        st.info("Aún no se han registrado actividades.")


# ---------------------------------------------------
# 📈 EJERCICIO 3 – PROGRAMACIÓN FUNCIONAL
# ---------------------------------------------------
def ejercicio_3():
    st.title("📈 Ejercicio 3 – Funciones y Programación Funcional 📊")

    st.markdown("### 📈 Cálculo de Retorno Esperado")
    st.write("Se calculará el retorno esperado de cada actividad registrada.")

    # Verificamos si hay actividades
    if len(st.session_state.actividades) == 0:
        st.warning("⚠️ Primero debes registrar actividades en el Ejercicio 2. 📋")
        return

    # -------------------------------
    # INPUTS
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:
        tasa = st.slider("📊 Tasa de retorno (%)", 0.0, 100.0, 10.0) / 100

    with col2:
        meses = st.number_input("📅 Cantidad de meses", min_value=1, value=12)

    # -------------------------------
    # FUNCIÓN REQUERIDA
    # -------------------------------

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    # -------------------------------
    # BOTÓN DE CÁLCULO
    # -------------------------------

    if st.button("🔎 Calcular retorno esperado 💰"):

        st.markdown("---")
        st.markdown("### 📊 Resultados por Actividad")

        # Aplicamos programación funcional
        retornos = list(
            map(
                lambda act: {
                    "nombre": act["nombre"],
                    "retorno": calcular_retorno(act, tasa, meses)
                },
                st.session_state.actividades
            )
        )

        total_retorno = 0

        # Mostrar resultados
        for r in retornos:
            total_retorno += r["retorno"]

            with st.container():
                col1, col2 = st.columns([3, 2])

                with col1:
                    st.subheader(r["nombre"])

                with col2:
                    st.metric("Retorno Esperado", f"{r['retorno']:.2f}")

            st.markdown("---")

        # -------------------------------
        # MÉTRICA GENERAL
        # -------------------------------

        st.markdown("### 💰 Retorno Total Proyectado")

        st.metric("📌 Retorno Total", f"{total_retorno:.2f}")

# ---------------------------------------------------
# 🏗 EJERCICIO 4 – POO
# ---------------------------------------------------
def ejercicio_4():
    st.title("🏗 Ejercicio 4 – Programación Orientada a Objetos (POO) 📚")

    st.markdown("### 🏗 Modelado con Clase Actividad")
    st.write("Se convertirán las actividades registradas en objetos de la clase Actividad.")

    if len(st.session_state.actividades) == 0:
        st.warning("⚠️ Primero debes registrar actividades en el Ejercicio 2. 📋")
        return

    st.markdown("---")
    st.markdown("### 📦 Objetos creados")

    objetos_actividades = []

    # Convertimos diccionarios en objetos
    for act in st.session_state.actividades:
        obj = Actividad(
            act["nombre"],
            act["tipo"],
            act["presupuesto"],
            act["gasto_real"]
        )
        objetos_actividades.append(obj)

    total_presupuesto = 0
    total_gasto = 0

    # Mostrar información usando métodos
    for obj in objetos_actividades:

        info = obj.mostrar_info()

        total_presupuesto += info["presupuesto"]
        total_gasto += info["gasto_real"]

        with st.container():
            col1, col2 = st.columns([3, 2])

            with col1:
                st.subheader(f"{info['nombre']} ({info['tipo']})")
                st.write(f"Presupuesto: {info['presupuesto']:.2f}")
                st.write(f"Gasto Real: {info['gasto_real']:.2f}")

            with col2:
                if obj.esta_en_presupuesto():
                    st.success("✅ Dentro del presupuesto")
                    st.write(f"Disponible: {info['diferencia']:.2f}")
                else:
                    st.error("🚨 PRESUPUESTO EXCEDIDO")
                    st.write(f"Exceso: {abs(info['diferencia']):.2f}")

        st.markdown("---")

    # -------------------------------
    # RESUMEN GENERAL
    # -------------------------------

    st.markdown("### 📊 Resumen General (POO)")

    diferencia_total = total_presupuesto - total_gasto

    col1, col2, col3 = st.columns(3)

    col1.metric("Presupuesto Total", f"{total_presupuesto:.2f}")
    col2.metric("Gasto Total", f"{total_gasto:.2f}")
    col3.metric("Diferencia Total", f"{diferencia_total:.2f}")

    if total_presupuesto > 0:
        porcentaje = min(total_gasto / total_presupuesto, 1.0)
        st.progress(porcentaje)

# ---------------------------------------------------
# MENÚ LATERAL
# ---------------------------------------------------

menu = st.sidebar.selectbox(
    "📂 Navegación 📌",
    ["🏠 Home 🚀", "💰 Ejercicio 1 📊", "📋 Ejercicio 2 📈", "📈 Ejercicio 3 💰", "🏗 Ejercicio 4 📚"]
)

# ---------------------------------------------------
# 🔄 CONTROL DE FLUJO PRINCIPAL
# ---------------------------------------------------

if menu == "🏠 Home 🚀":
    mostrar_home()

elif menu == "💰 Ejercicio 1 📊":
    ejercicio_1()

elif menu == "📋 Ejercicio 2 📈":
    ejercicio_2()

elif menu == "📈 Ejercicio 3 💰":
    ejercicio_3()

elif menu == "🏗 Ejercicio 4 📚":
    ejercicio_4()
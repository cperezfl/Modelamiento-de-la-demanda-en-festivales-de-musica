import streamlit as st
import pandas as pd
import os

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Soporte Visual - Unidad 3",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS COMPACTOS DE ALTO CONTRASTE ---
st.markdown("""
    <style>
    .main-title { font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 15px; }
    .section-header { font-size: 18px; font-weight: bold; color: #1E3A8A; margin-top: 15px; margin-bottom: 10px; border-bottom: 1px solid #E5E7EB; padding-bottom: 3px; }
    .subsection-header { font-size: 15px; font-weight: bold; color: #2563EB; margin-top: 10px; margin-bottom: 5px; }
    
    /* Contenedor del Banner Principal para controlar la altura de forma estricta */
    .banner-container {
        width: 100%;
        max-height: 400px; /* Altura máxima reducida para no saturar la pantalla */
        overflow: hidden;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    .banner-container img {
        width: 100%;
        height: 400px;
        object-fit: cover; /* Recorta la imagen proporcionalmente manteniendo el ancho */
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER EN LA PANTALLA PRINCIPAL (ALTURA CONTROLADA) ---
# Se busca el archivo header.jpg en la carpeta images/
header_path = os.path.join("images", "header.jpg")
if os.path.exists(header_path):
    # Usamos HTML para inyectar la imagen dentro del contenedor estilizado con CSS
    import base64
    with open(header_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f'<div class="banner-container"><img src="data:image/jpeg;base64,{encoded_image}"></div>', 
        unsafe_allow_html=True
    )

# --- BARRA LATERAL (LOGOTIPO Y NAVEGACIÓN) ---
logo_path = os.path.join("images", "logo_utem.jpg")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_column_width=True)

st.sidebar.markdown("### Estructura del Informe")
menu = st.sidebar.radio(
    "Seleccione el módulo:",
    [
        "Portada",
        "Problema de Investigación",
        "Estado del Arte",
        "Pregunta e Hipótesis",
        "Objetivos",
        "Evidencia Bibliográfica",
        "Coherencia del Planteamiento",
        "Declaración de Uso de IA"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Asignatura: Metodología de Investigación\nUTEM — 2026")

# --- MÓDULOS DE LA PRESENTACIÓN ---

if menu == "Portada":
    st.markdown('<div class="main-title">Modelamiento de la dema en festivales de música: Integración de minería de textos y modelos de grafos para la evaluación competitiva de lineups</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-header">Identificación del Estudiante</div>', unsafe_allow_html=True)
        st.write("**Estudiante:** Christian Elías Isaías Pérez Flores")
        st.write("**Correo electrónico:** cperezfl@utem.cl")
        st.write("**Carrera:** Ingeniería Civil en Ciencia de Datos")
        st.write("**Institución:** Universidad Tecnológica Metropolitana")
    
    with col2:
        st.markdown('<div class="section-header">Clasificación del Proyecto</div>', unsafe_allow_html=True)
        st.write("**Asignatura:** Metodología de Investigación en Ciencia de Datos")
        st.write("**Área OCDE:**  Ciencias Sociales (Economía y Negocios) / Ciencias de la Computación e Información")
        st.write("**Objetivos de Desarrollo Sostenible (ODS):**")
        
        ods_col1, ods_col2 = st.columns(2)
        with ods_col1:
            ods8_path = os.path.join("images", "ods8.jpg")
            if os.path.exists(ods8_path):
                st.image(ods8_path, width=300)
            else:
                st.caption("• ODS 8: Trabajo Decente")
        with ods_col2:
            ods9_path = os.path.join("images", "ods9.jpg")
            if os.path.exists(ods9_path):
                st.image(ods9_path, width=300)
            else:
                st.caption("• ODS 9: Industria, Innovación y Infraestructura")

    st.markdown('<div class="section-header">Documentación Oficial</div>', unsafe_allow_html=True)
    informe_path = os.path.join("anexos", "Modelamiento_de_la_dema_en_festivales.pdf")
    if os.path.exists(informe_path):
        with open(informe_path, "rb") as f:
            pdf_data = f.read()
        st.download_button(
            label="Descargar Informe Escrito Completo (PDF)",
            data=pdf_data,
            file_name="Modelamiento_de_la_dema_en_festivales.pdf",
            mime="application/pdf"
        )

elif menu == "Problema de Investigación":
    st.markdown('<div class="main-title">Problema de Investigación</div>', unsafe_allow_html=True)
    
    st.markdown("**Definición Central:**")
    st.write("En la industria musical actual, los eventos en vivo representan la principal fuente de ingresos. Sin embargo, las productoras enfrentan el dilema de optimizar la composición de sus lineups bajo alta incertidumbre. Tradicionalmente, la gestión se enfoca de forma exclusiva en asegurar la contratación de headliners (cabezas de cartel), asumiendo erróneamente que esto garantiza el éxito total y subestimando el impacto predictivo de la parrilla artística secundaria.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="subsection-header">Contexto y Afectados</div>', unsafe_allow_html=True)
        st.write("Afecta de manera directa a los promotores de festivales y recintos de música en vivo, quienes asumen un riesgo financiero crítico al fundamentar decisiones estratégicas de alta inversión en la intuición empírica y en marcadas asimetrías de información de mercado.")
    with col2:
        st.markdown('<div class="subsection-header">Relevancia en Ciencia de Datos</div>', unsafe_allow_html=True)
        st.write("El comportamiento digital de los consumidores genera un flujo constante de datos no estructurados (búsquedas web, redes sociales, reseñas). La Ciencia de Datos permite procesar esta información no estructurada para descubrir los verdaderos motores de la demanda comercial, mitigando la incertidumbre del promotor al reemplazar la dependencia empírica por modelos predictivos basados en datos objetivos.")

elif menu == "Estado del Arte":
    st.markdown('<div class="main-title">Estado del Arte: Síntesis Visual</div>', unsafe_allow_html=True)
    st.write("Estructura conceptual derivada de la Revisión Sistemática de la Literatura (SLR):")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Fundamentos y Conceptos**")
        st.write("""
        * Composición estructural del lineup.
        * Intención de compra del consumidor.
        * Modelamiento de redes culturales.
        * Análisis de sentimiento contextual.
        """)
    with col2:
        st.markdown("**Avances Actuales**")
        st.write("""
        * Modelos LDA para identificar el atributo 'Performance' como prioridad.
        * Aplicación de arquitecturas BERT-BiLSTM para satisfacción en recintos.
        * Modelos ERGM basados en Google Trends para flujos turísticos.
        """)
    with col3:
        st.markdown("**Brecha Identificada**")
        st.write("""
        * Falta de un marco analítico unificado que integre simultáneamente el Procesamiento de Lenguaje Natural (NLP) y los Modelos de Grafos para evaluar el cartel de forma global (densidad y conectividad) en lugar de medir solo variables aisladas.
        """)

elif menu == "Pregunta e Hipótesis":
    st.markdown('<div class="main-title">Pregunta de Investigación e Hipótesis</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Pregunta Principal</div>', unsafe_allow_html=True)
    st.warning("¿En qué medida un modelo predictivo integrado por técnicas de minería de textos y variables estructurales de grafos incrementa la exactitud en la estimación de la intención de compra de entradas para festivales de música, en comparación con los enfoques analíticos tradicionales basados únicamente en la popularidad de los artistas principales?")
    
    st.markdown('<div class="section-header">Hipótesis de Trabajo</div>', unsafe_allow_html=True)
    st.write("**H₁:** El modelo predictivo integrado por minería de textos y variables de estructura de grafos posee una exactitud de estimación estadísticamente superior (medida a través de RMSE y R²) para determinar la intención de compra de entradas, en comparación con los modelos de regresión tradicionales basados únicamente en la popularidad aislada de los artistas principales (headliners).")
    
    st.markdown('<div class="subsection-header">Justificación Breve</div>', unsafe_allow_html=True)
    st.write("La literatura técnica demuestra que el atributo de calidad percibida y las relaciones de co-ocurrencia entre artistas capturan dinámicas de consumo complejas que los modelos lineales simples omiten. Por ende, la integración de ambas dimensiones reduce el sesgo del modelo y captura de mejor forma la varianza de la demanda.")

elif menu == "Objetivos":
    st.markdown('<div class="main-title">Estructura de Objetivos</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Objetivo General</div>', unsafe_allow_html=True)
    st.info("**Evaluar el desempeño predictivo de la integración de minería de textos y modelos de grafos** para de esta forma estimar la intención de compra de entradas asociada a la composición estructural del lineup (diversidad de géneros y sentimiento de calidad), utilizando datos generados por usuarios en el contexto de festivales de música en vivo.")
    
    st.markdown('<div class="section-header">Objetivos Específicos</div>', unsafe_allow_html=True)
    st.write("""
    1. **Identificar** las variables de composición estructural del lineup (diversidad de géneros y atributos de los artistas) mediante la extracción y estructuración de datos generados por usuarios (texto y búsquedas) en plataformas digitales.
    2. **Implementar** técnicas de minería de textos para la extracción de sentimientos y modelos de grafos para medir la centralidad y densidad de géneros, consolidando un modelo analítico integrado.
    3. **Contrastar** la exactitud predictiva del modelo integrado en la estimación de la intención de compra frente a enfoques tradicionales que evalúan únicamente la popularidad aislada de los headliners.
    4. **Interpretar** los patrones y resultados obtenidos para determinar el impacto real de la percepción de calidad y la diversidad del cartel en la demanda competitiva de los festivales de música en vivo.
    """)

elif menu == "Evidencia Bibliográfica":
    st.markdown('<div class="main-title">Evidencia Bibliográfica</div>', unsafe_allow_html=True)
    st.write("Artículos técnico-científicos principales seleccionados para dar fundamento metodológico al planteamiento:")
    
    articulos_data = {
        "Autor y Año": [
            "Hiller (2016)",
            "Montoro-Pons & Cuadrado-García (2021)",
            "de Lira et al. (2019)",
            "Quan et al. (2025)"
        ],
        "Revista / Origen": [
            "Journal of Cultural Economics",
            "Tourism Economics",
            "Information Processing & Management",
            "Entertainment Computing"
        ],
        "Aporte Metodológico Clave": [
            "Modelamiento de negociación bilateral y optimización de contratación bajo criterios de calidad vertical y horizontal.",
            "Uso de datos de Google Trends para la construcción de grafos y estimación de modelos de grafos aleatorios exponenciales (ERGM).",
            "Clasificación cuantitativa de la intención de asistencia a festivales masivos utilizando contenido de publicaciones en redes sociales.",
            "Integración de modelos BERT-BiLSTM para extracción de sentimiento a partir de revisiones online aplicados a la competitividad."
        ]
    }
    
    df_articulos = pd.DataFrame(articulos_data)
    st.dataframe(df_articulos, use_container_width=True)

elif menu == "Coherencia del Planteamiento":
    st.markdown('<div class="main-title">Coherencia Metodológica del Planteamiento</div>', unsafe_allow_html=True)
    st.write("Representación de la trazabilidad y consistencia lógica de la investigación:")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("**1. Problema**")
        st.caption("Dependencia exclusiva de headliners y subestimación empírica del resto del lineup.")
    with col2:
        st.markdown("**2. Brecha**")
        st.caption("Inexistencia de un enfoque que unifique minería de textos y grafos en un modelo de demanda.")
    with col3:
        st.markdown("**3. Pregunta**")
        st.caption("¿En qué medida el enfoque integrado supera la medición analítica tradicional?")
    with col4:
        st.markdown("**4. Hipótesis**")
        st.caption("El modelo integrado posee una exactitud predictiva (RMSE, R²) superior.")
    with col5:
        st.markdown("**5. Objetivo**")
        st.caption("Evaluar y contrastar el desempeño predictivo del modelo analítico propuesto.")
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("Nota: Cada fase metodológica se vincula en secuencia estricta para asegurar la coherencia interna requerida por la rúbrica.")

elif menu == "Declaración de Uso de IA":
    st.markdown('<div class="main-title">Declaración de Uso de Inteligencia Artificial</div>', unsafe_allow_html=True)
    st.write("En cumplimiento con los lineamientos académicos del curso, se explicita el alcance técnico asistencial de las herramientas utilizadas:")
    
    st.markdown("""
    * **Herramientas Utilizadas:** Modelos de lenguaje de gran escala (LLM).
    * **Propósito y Alcance:** 
        * Apoyo en la optimización sintáctica y cohesión de la redacción académica formal.
        * Soporte estructurado en el formateo y diseño técnico de la interfaz gráfica a través de código compatible con Streamlit.
        * Automatización del ordenamiento tipográfico del apartado de referencias bibliográficas.
    * **Verificación Humana (Control de Calidad):** La formulación teórica del problema, la hipótesis de trabajo, el diseño analítico de grafos y el desarrollo de los objetivos de investigación corresponden a un producto intelectual propio, validado manualmente por el autor para asegurar consistencia estricta frente al corpus de literatura técnica real.
    """)

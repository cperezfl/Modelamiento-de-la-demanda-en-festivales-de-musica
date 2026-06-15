# Soporte Visual Interactivo - Unidad 3

Este repositorio contiene la aplicación web interactiva desarrollada en **Streamlit** que sirve como soporte visual y defensa para la evaluación de la Unidad 3 de la asignatura **Metodología de Investigación en Ciencia de Datos**.

## Autoría y Contexto Academicó
* **Estudiante:** Christian Elías Isaías Pérez Flores
* **Carrera:** Ingeniería Civil en Ciencia de Datos
* **Institución:** Universidad Tecnológica Metropolitana (UTEM), Chile
* **Fecha:** Junio, 2026

## Resumen del Proyecto
La aplicación sistematiza y expone de forma lógica el planteamiento de la investigación titulada:  
*«Modelamiento de la demanda en festivales de música: Integración de minería de textos y modelos de grafos para la evaluación competitiva de lineups»*.

A través de una interfaz limpia y estructurada, el software despliega la trazabilidad completa del diseño de investigación: desde la definición del problema estocástico e industrial en la composición de carteles artísticos, pasando por la hipótesis multidimensional ($RMSE$ y $R^2$), los objetivos secuenciales, hasta la evidencia bibliográfica indexada y la declaración explícita del uso ético de Inteligencia Artificial.

---

## Estructura del Proyecto

El directorio de trabajo debe mantener estrictamente la siguiente organización para su correcto despliegue:

```
├── app.py
├── requirements.txt
├── images/
│   ├── logo_UTEM.jpg
│   ├── header.jpg
│   ├── ods8.jpg
│   └── ods9.jpg
└── anexos/
    └── Modelamiento_de_la_demanda_en_festivales.pdf
```

## Instrucciones de Instalación y Ejecución

Para ejecutar la aplicación localmente, asegúrese de contar con Python 3.8 o superior instalado y siga estos breves pasos:

1. Abra su terminal o consola de comandos.
2. Clonar o posicionarse en el directorio del proyecto:
   ```
   cd "ruta/hacia/esta/carpeta"
3. Instalar las dependencias requeridas, ejecutando el siguiente comando:
   ```
   pip install -r requirements.txt
5. Iniciar la aplicación, despliegue el servidor local de Streamlit mediante el comando:
   ```
   streamlit run app.py

La plataforma se abrirá de manera automática en su navegador web predeterminado (por defecto en la dirección local http://localhost:8501).
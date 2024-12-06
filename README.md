```markdown
# Análisis de Variables en Documentos Académicos

Este proyecto analiza documentos académicos relacionados con nutrición y su impacto en la ganancia de masa muscular, pérdida de peso y mejora de la composición corporal. A través de técnicas de análisis y visualización de datos, identificamos las variables más recurrentes en los documentos.

## 1. Carga de los Datos

### Extracción del texto de los PDFs

Se utiliza la librería `PyPDF2` para extraer el texto de los archivos PDF. Se define una función `extract_text_from_pdf` que extrae el texto de cada página del PDF y lo trunca si supera un límite de caracteres especificado.

```python
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path, max_length):
    """
    Extrae texto de un archivo PDF y lo trunca si supera el límite especificado.
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    # Truncar si el texto excede el límite
    if len(text) > max_length:
        print(f"El texto extraído de {pdf_path} excede el límite de {max_length} caracteres. Será truncado.")
        # Buscar el último espacio antes del límite para truncar limpiamente
        cut_index = text.rfind(" ", 0, max_length)
        if cut_index == -1:  # Si no encuentra un espacio, corta directamente
            cut_index = max_length
        text = text[:cut_index]
    
    return text

pdf_files = [
    'pdf/pdf_1.pdf',
    'pdf/pdf_2.pdf',
    'pdf/pdf_3.pdf',
    'pdf/pdf_4.pdf',
    'pdf/pdf_5.pdf',
]

# Define el límite de caracteres
limite_caracteres = 800000

# Lista para guardar los textos extraídos
texto = [None] * len(pdf_files)

# Extraer texto con truncamiento
for i, pdf in enumerate(pdf_files):
    texto[i] = extract_text_from_pdf(pdf, limite_caracteres)

# Imprimir un resumen de los textos
for idx, txt in enumerate(texto):
    print(f"\n--- Texto del archivo {pdf_files[idx]} ---\n")
    print(f"Longitud: {len(txt)} caracteres")
    print(txt[:500])  # Muestra los primeros 500 caracteres para verificar
```

## 2. ETL con IA

### Resumen de los textos con IA

Se utiliza la API de OpenAI para resumir los textos extraídos de los PDFs. Esto ayuda a reducir la longitud del texto y a evitar exceder el límite de tokens permitidos por OpenAI al crear el DataFrame.

```python
import dotenv
from openai import OpenAI
import os

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_KEY")

# Configurar el cliente de OpenAI
client = OpenAI(api_key=api_key)

def summarize_text_with_openai(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant who summarizes academic texts. There is a summary but in the above countries possible relevant information from the study, we want to eliminate some information but not important things."},
                {"role": "user", "content": f"Por favor, resume este texto: {text}"}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error al procesar el texto con la API: {e}")
        return None

for item in texto:
    item = summarize_text_with_openai(item)
```

### Búsqueda de las variables en cada PDF

Se define una lista de variables importantes relacionadas con la nutrición y el ejercicio. Se utiliza la API de OpenAI para analizar cada texto y determinar si las variables están presentes. 

```python
import pandas as pd

# List of important variables in English
variables_importantes = [
    "Protein Intake",                 # Ingesta de proteínas
    "Protein Distribution",           # Distribución de proteínas
    "Sources of Protein",             # Fuentes de proteínas
    "Muscle Protein Synthesis (MPS)", # Síntesis de proteínas musculares
    "Effect of Resistance Training",  # Efecto del entrenamiento de resistencia
    "Supplementation Strategies",     # Estrategias de suplementación
    "Anabolic Window",                # Ventana anabólica
    "Macronutrient Distribution",     # Distribución de macronutrientes
    "Target Population",              # Población objetivo
    "Study Methodology",              # Metodología del estudio
    "Key Results",                    # Resultados clave
    "Conclusions and Recommendations",# Conclusiones y recomendaciones
    "Weight Loss",                    # Pérdida de peso
    "Weight Gain",                    # Ganancia de peso
    "Muscle Gain",                    # Ganancia de músculo
    "Muscle Loss",                    # Pérdida de músculo
    "Body Composition Improvement",   # Mejora de la composición corporal
    "Caloric Intake",                 # Ingesta calórica
    "Energy Expenditure",             # Gasto energético
    "Fat Loss",                       # Pérdida de grasa
    "Fat Gain"                        # Ganancia de grasa
]

def generate_prompt(text, variables):
    # Generar una lista de las variables en el formato del prompt
    variables_list = "\n".join([f"- {var}" for var in variables])
    
    # Estructura del prompt
    prompt = f"""You are an assistant analyzing academic papers. Your task is to check whether the following variables are present in the provided text. For each variable, return `True` if it is present and `False` if it is not. The output must be a single line in CSV format, with the variable names as headers.
    Variables:{variables_list}
    Text:{text}
    Output format:
    Variable1,Variable2,Variable3,...
    True/False,True/False,True/False,...    """
    return prompt

def analyze_text_with_openai(text, variables):
    prompt = generate_prompt(text, variables)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant for academic paper analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        # Extraer la respuesta en CSV
        csv_line = response.choices[0].message.content
        return csv_line
    except Exception as e:
        print(f"Error: {e}")
        return None

respuestas = []
for text in texto:
    csv_line = analyze_text_with_openai(text, variables_importantes)
    if csv_line:
        respuestas.append(csv_line)

columns = respuestas[0].split("\n")[0].split(",")  # Cabecera de la primera respuesta
data = []

# Procesar cada respuesta
for response in respuestas:
    row_values = response.split("\n")[1].split(",")
    # Asegurarse de que la fila tenga la misma longitud que las columnas
    if len(row_values) < len(columns):
        row_values += ["False"] * (len(columns) - len(row_values))  # Rellenar faltantes con False
    elif len(row_values) > len(columns):
        row_values = row_values[:len(columns)]  # Truncar si hay valores extra
    data.append(row_values)

# Crear el DataFrame
df = pd.DataFrame(data, columns=columns)
df.head()
```

## 3. Visualización de Resultados

Se utiliza la librería `seaborn` para visualizar la frecuencia de las variables en los documentos.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Convertir valores True/False a 1/0 para análisis
df_numeric = df.replace({"True": 1, "False": 0})

# Sumar menciones de cada variable
mention_counts = df_numeric.sum().reset_index()
mention_counts.columns = ['Variable', 'Mentions']

# Crear el gráfico de barras con seaborn
plt.figure(figsize=(14, 7))
sns.barplot(data=mention_counts, x='Variable', y='Mentions', palette='viridis', edgecolor='black')

# Configurar estilo del gráfico
plt.title("Variables mencionadas en los PDFs", fontsize=20)
plt.ylabel("Número de Menciones", fontsize=14)
plt.xlabel("Variables", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine()
plt.tight_layout()
plt.show()
```

## Observaciones

* El código incluye la funcionalidad para truncar el texto extraído de los PDFs si excede un límite de caracteres. Esto ayuda a evitar problemas con el límite de tokens de la API de OpenAI.
* Se utiliza la API de OpenAI para resumir los textos y para analizar la presencia de variables. 
* Se visualiza la frecuencia de las variables utilizando un gráfico de barras.


Este README.md proporciona una descripción clara del proyecto, incluyendo el código, las librerías utilizadas y la visualización de los resultados.

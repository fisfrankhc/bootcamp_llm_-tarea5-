# RUTA GITHUB
https://github.com/fisfrankhc/bootcamp_llm_-tarea5-


# Proyecto de Generación de Texto

Este proyecto utiliza el modelo `gpt-4o-mini` de OpenAI para tareas de generación de texto. El modelo se seleccionó debido a su alta calidad de generación y eficiencia en el uso de recursos.

## Tabla de Contenidos
- [RUTA GITHUB](#ruta-github)
- [Proyecto de Generación de Texto](#proyecto-de-generación-de-texto)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Instalación de Dependencias](#instalación-de-dependencias)
  - [Configuración](#configuración)
  - [Uso](#uso)
    - [Opción 1:](#opción-1)
    - [Opción 2:](#opción-2)
    - [Opción 3(adicional):](#opción-3adicional)
  - [Motivo de la Elección del Modelo](#motivo-de-la-elección-del-modelo)
    - [Motivo de la Elección del Modelo](#motivo-de-la-elección-del-modelo-1)
      - [Comparación de Modelos](#comparación-de-modelos)
  - [Documentación del Código](#documentación-del-código)
  - [Reproducción del Entorno](#reproducción-del-entorno)

## Instalación de Dependencias

Para instalar las dependencias necesarias, ejecute:

```sh
%pip install openai python-dotenv pandas
```


## Configuración

Guarde su API Key de OpenAI en un archivo .env en el siguiente formato:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Uso

### Opción 1:

Ejecute el script principal para iniciar la interacción con el modelo:

```sh
python main.py
```

### Opción 2:

   1. Abre el archivo `main.ipynb`
   2. Crea un fichero `.env` y guarda tu variable de forma siguiente

         ```env
         OPENAI_API_KEY=
         ```
      
   3. Ejecuta cada línea en forma ordenada de arriba hacia abajo y listo!!


### Opción 3(adicional):

   Se creo un notebook donde se probó con el modelo de `llama3.1:8b`
   1. Abre el archivo `main(llama3.1:8b).ipynb`
   2. Ejecuta cada línea en forma ordenada de arriba hacia abajo y listo!!


## Motivo de la Elección del Modelo

El modelo gpt-4o-mini fue seleccionado debido a su equilibrio entre calidad de generación y eficiencia de recursos. Comparado con otros modelos como BART y T5, gpt-4o-mini ofrece una generación de texto de muy alta calidad con requerimientos de recursos moderados, lo que lo hace adecuado para este proyecto.

### Motivo de la Elección del Modelo

| Modelo       | Parámetros | Calidad de Generación | Recursos Necesarios | Flexibilidad | Facilidad de Integración |
|--------------|------------|-----------------------|---------------------|--------------|--------------------------|
| GPT-4o-mini  | 175B       | Muy Alta              | Alto                | Alta         | Alta                     |
| BART         | 400M       | Alta                  | Alto                | Muy Alta     | Alta                     |
| T5           | 11B        | Alta                  | Alto                | Muy Alta     | Alta                     |
| Llama 3.1: 8B| 8B         | Muy Alta              | Alto                | Alta         | Alta                     |

#### Comparación de Modelos

1. **GPT-4o-mini**:
   - **Calidad de Generación**: GPT-4o-mini destaca por su capacidad para generar textos de alta calidad y coherencia, superando a muchos otros modelos en términos de precisión y relevancia.
   - **Recursos Necesarios**: Aunque requiere recursos computacionales significativos, su rendimiento justifica la inversión, especialmente para proyectos que demandan alta calidad en la generación de textos.
   - **Flexibilidad**: Ofrece una gran flexibilidad para adaptarse a diversas tareas de procesamiento del lenguaje natural, lo que lo hace adecuado para una amplia gama de aplicaciones.
   - **Facilidad de Integración**: Su integración es relativamente sencilla debido a la disponibilidad de amplias bibliotecas y soporte de la comunidad.

2. **BART**:
   - **Calidad de Generación**: BART también proporciona una alta calidad de generación de texto, especialmente en tareas de resumen y traducción.
   - **Recursos Necesarios**: Similar a GPT-4o-mini, BART requiere recursos computacionales considerables, pero menos que los modelos más grandes.
   - **Flexibilidad**: Muy flexible, adecuado para una variedad de tareas de NLP.
   - **Facilidad de Integración**: Buena, con soporte robusto y documentación clara.

3. **T5**:
   - **Calidad de Generación**: T5 es conocido por su rendimiento sólido en múltiples tareas de NLP, ofreciendo una alta calidad de generación de texto.
   - **Recursos Necesarios**: Requiere recursos significativos, pero es menos intensivo que GPT-4o-mini.
   - **Flexibilidad**: Extremadamente flexible, diseñado para resolver múltiples tareas simplemente cambiando el "prompt".
   - **Facilidad de Integración**: Alta, con excelente soporte de la comunidad y documentación.

4. **Llama 3.1: 8B**:
   - **Calidad de Generación**: Ofrece una calidad de generación muy alta, compitiendo con los mejores modelos del mercado.
   - **Recursos Necesarios**: Requiere altos recursos, similar a otros modelos grandes.
   - **Flexibilidad**: Alta, capaz de adaptarse a diferentes tareas de generación de texto.
   - **Facilidad de Integración**: Alta, con una integración sencilla gracias a un buen soporte técnico y comunidad.

En conclusión, se eligió **GPT-4o-mini** debido a su excepcional calidad de generación de texto, flexibilidad y facilidad de integración, lo que lo hace ideal para las necesidades específicas de nuestro proyecto.


## Documentación del Código

Los docstrings se han agregado a todas las funciones para proporcionar información clara sobre su propósito y uso. A continuación se muestra un ejemplo:

```python
def generar_texto_OPENAI(prompt: str, context: str) -> str:
   """
    Genera un texto a partir de un prompt y un contexto, utilizando streaming para mostrar el texto generado en tiempo real.

    Args:
        prompt (str): Prompt para el modelo.
        context (str): Contexto para el modelo.

    Returns:
        str: Texto generado por el modelo.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Modelo de lenguaje GPT-4o-mini de OpenAI (versión más pequeña)
        messages=[
            {"role": "system", "content": context}, # Contexto del chat (mensajes previos) para el modelo de lenguaje de OpenAI 
            {"role": "user", "content": prompt} # Prompt del usuario para el modelo de lenguaje de OpenAI y pueda responder
        ],
    )
   return response.choices[0].message.content  # Retornar el texto generado por el modelo de lenguaje de OpenAI (respuesta) 
```

## Reproducción del Entorno

Para reproducir el entorno, siga estos pasos:

	1.	Instalación de Dependencias: Ejecute pip install -r requirements.txt para instalar todas las dependencias necesarias.
	2.	Configuración: Guarde su API Key de OpenAI en un archivo .env.
	3.	Ejecución: Ejecute python main.py para iniciar la interacción con el modelo.
from typing import List
import pandas as pd

# Cargar datos consolidados de ventas y productos desde archivo CSV a DataFrame de Pandas
file_path = 'databd/datos_procesados.csv'
data = pd.read_csv(file_path) #leer archivo csv y lo guardamos en la variable data

def preparar_textos(df: pd.DataFrame) -> List[str]:
    """
    Prepara una lista de textos a partir de un DataFrame consolidado.

    Args:
        df (pd.DataFrame): DataFrame consolidado.

    Returns:
        List[str]: Lista de textos preparados para el modelo.
    """
    #textos = df.apply(lambda row: f"IDVenta: {row['venta_id']}, Fecha de Venta: {row['venta_fecha']}, Proceso: {row['venta_proceso']}, IDproducto: {row['prod_id']}, Producto: {row['prod_nombre']}, Cantidad Vendida: {row['cantidad_venta']}, Precio Venta: {row['precio_venta_x']}, Sucursal: {row['suc_nombre']}, Vendedor: {row['user_name']}",axis=1)
    textos = df.apply(lambda row: (
        f"ID Venta: {row['venta_id']}, "
        f"Fecha de Venta: {row['venta_fecha']}, "
        f"Proceso: {row['venta_proceso']}, "
        f"ID Producto: {row['prod_id']}, "
        f"Producto: {row['prod_nombre']}, "
        f"Cantidad Vendida: {row['cantidad_venta']}, "
        f"Precio Venta: {row['precio_venta_x']}, "
        f"Sucursal: {row['suc_nombre']}, "
        f"Vendedor: {row['user_name']}"
    ), axis=1)
    return textos.tolist()  # Convertir a lista de Python y retornar los textos preparados en una lista

# Preparar textos
textos_preparados = preparar_textos(data) # llamamos a la funcion preparar_textos y le pasamos el dataframe data y lo guardamos en la variable textos_preparados
context_str = "\n".join(textos_preparados) # unimos los textos preparados en un solo string y lo guardamos en la variable context_str



#CARGAMOS EL MODELO
from openai import OpenAI  # Importamos la clase OpenAI desde el módulo openai
from dotenv import load_dotenv # Importarmos la función load_dotenv desde el módulo dotenv

# Cargar las variables de entorno desde el archivo .env (LA API KEY)
load_dotenv()

# Creamos el cliente de OpenAI
client = OpenAI()

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

def main():
    while True:
        prompt = input("Ingrese su pregunta: ")
        if prompt.lower() in ['exit', 'salir', 'quit']:
            break
        print(f"🅿️ PREGUNTA: {prompt}\n")
        generated_text = generar_texto_OPENAI(prompt, context_str)
        print(f"▶️ Respuesta: \n{generated_text}\n")

if __name__ == "__main__":
    main()
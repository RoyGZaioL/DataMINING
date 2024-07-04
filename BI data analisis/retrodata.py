import pandas as pd
def data_2024():
    # Cargar el archivo CSV
    file = 'consolidado2024.csv'
    df = pd.read_csv(file, sep=";", encoding='latin-1')

    # Obtener las fechas únicas en la columna "Fecha Asignacion"
    fechas_unicas = df["Fecha Asignacion"].unique()

    # Iterar sobre cada fecha única
    for fecha in fechas_unicas:
        # Filtrar el DataFrame original por la fecha actual
        df_fecha = df[df["Fecha Asignacion"] == fecha]
        
        # Guardar el DataFrame filtrado en un archivo CSV separado
        nombre_archivo = f"{fecha}_data.csv"
        df_fecha.to_csv(nombre_archivo, sep=";", index=False, encoding='utf-8')
def data_2023():
    file="consolidado2023_2.csv"
    df = pd.read_csv(file, sep=";", encoding='latin-1')

    # Obtener las fechas únicas en la columna "Fecha Asignacion"
    fechas_unicas = df["Fecha Asignacion"].unique()

    # Iterar sobre cada fecha única
    for fecha in fechas_unicas:
        # Filtrar el DataFrame original por la fecha actual
        df_fecha = df[df["Fecha Asignacion"] == fecha]
        
        # Guardar el DataFrame filtrado en un archivo CSV separado
        nombre_archivo = f"{fecha}_data.csv"
        df_fecha.to_csv(nombre_archivo, sep=";", index=False, encoding='utf-8')

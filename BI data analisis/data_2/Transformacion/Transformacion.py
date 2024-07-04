import pandas as pd
def First():
    # Ruta al archivo CSV
    file_path = r'C:\Users\royza\OneDrive\Escritorio\Trabajo\Transformacion\GESTIONES_MULTICOB_202405.csv'

    # Leer el archivo CSV con manejo de errores, especificando la fila de cabecera
    df = pd.read_csv(file_path, header=0,sep=';', on_bad_lines='warn')  # Ajusta 'header' según sea necesario

    # Limpiar los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Imprimir los nombres de las columnas
    print(df.columns)

    # Obtener una lista única de clientes
    clientes = df['Cliente'].unique()

    # Filtrar los datos por cliente y guardarlos en archivos CSV separados
    for cliente in clientes:
        # Filtrar los datos para el cliente actual
        df_cliente = df[df['Cliente'] == cliente]
        
        # Crear un nombre de archivo para el cliente actual
        nombre_archivo = f'{cliente}.csv'
        
        # Guardar los datos filtrados en un nuevo archivo CSV
        df_cliente.to_csv(nombre_archivo, index=False)

    print("Archivos CSV creados para cada cliente.")

import pandas as pd

# Función para reemplazar caracteres especiales
def replace_special_characters(text):
    replacements = {
        '¥': 'N',
        '¢': 'o',
        '¡': 'i',
        '': 'e'
        
        # Agrega más reemplazos según sea necesario
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
def replace_special_characters2(text):
    replacements = {
        'Ñ': 'N',
        'ó': 'o',
        'í': 'i',
        'é': 'e',
        '°': '',
        'ü':'u',
        'ķ':'i'
        
        # Agrega más reemplazos según sea necesario
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
def replace_special_characters3(text):
    replacements = {
        'Ñ': 'N',
        'ó': 'o',
        'í': 'i',
        'é': 'e',
        '°': '',
        'ü':'u',
        'ķ':'i',
        '$-':'0'
        
        
        # Agrega más reemplazos según sea necesario
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
def main():
    # Cargar el archivo de Excel
    file_path = 'consolidado2024_2.csv'

    # Leer el archivo de Excel
    df = pd.read_csv(file_path,sep=';',encoding='latin-1')

    column_to_replace = ["Sociedad","Region","Zonal","Localidad","Porcion","N referencia","Cuenta contrato","N Servicio","Nombre o Razon Social","Direccion","Telefono","Celular","Email","Tramo Antiguedad","Antiguedad en dias","Deuda No Vencida","Deuda Vencida","Deuda Total","RUT","DV","Fecha Vencimiento Documento","Fecha Asignacion","Fecha Termino","N Servicio2","Fecha Gestion Contact " ,"Tipo de Contacto","Estado","Observacion","PAGO","Fecha de Pago","% Comision","Hon. Multicob","Periodo","Deuda Real","Q Clientes","Q Pagos"]  # Cambia esto al nombre de tu columna
    # Imprimir los primeros valores antes del reemplazo
    print("Nombres de las columnas antes del reemplazo:")
    print(df.columns)
    df.columns = [replace_special_characters(col) for col in df.columns]

    # Aplicar la función de reemplazo a la columna
    for column in column_to_replace:
        if column in df.columns:
            df[column] = df[column].astype(str).apply(replace_special_characters)
        else:
            print(f"La columna '{column}' no existe en el DataFrame.")
    print("Nombres de las columnas después del reemplazo:")
    print(df.columns)

    print("Valores después del reemplazo:")
    print(df[column_to_replace].head())
    #Guardar el resultado en un nuevo archivo de Excel
    new_file_path = 'consolidado2024.csv'
    df.to_csv(new_file_path, index=False,sep=';')
def main_2():
    file="consolidado2023.csv"


    # Leer el archivo de Excel
    df = pd.read_csv(file,sep=';',encoding='ISO 8859-13')

    column_to_replace = ["Sociedad","Region","Zonal","Localidad","Porcion","N referencia","Cuenta contrato","N Servicio","Nombre o Razon Social","Direccion","Telefono","Celular","Email","Tramo Antiguedad","Antiguedad en dias","Deuda No Vencida","Deuda Vencida","Deuda Total","RUT","DV","Fecha Vencimiento Documento","Fecha Asignacion","Fecha Termino","N Servicio2","Fecha Gestion Contact " ,"Tipo de Contacto","Estado","Observacion","PAGO","Fecha de Pago","% Comision","Hon. Multicob","Periodo","Deuda Real","Q Clientes","Q Pagos"]  # Cambia esto al nombre de tu columna
    # Imprimir los primeros valores antes del reemplazo
    print("Nombres de las columnas antes del reemplazo:")
    print(df.columns)
    df.columns = [replace_special_characters2(col) for col in df.columns]

    # Aplicar la función de reemplazo a la columna
    for column in column_to_replace:
        if column in df.columns:
            df[column] = df[column].astype(str).apply(replace_special_characters2)
        else:
            print(f"La columna '{column}' no existe en el DataFrame.")
    print("Nombres de las columnas después del reemplazo:")
    print(df.columns)

    print("Valores después del reemplazo:")
    print(df[column_to_replace].head())
    #Guardar el resultado en un nuevo archivo de Excel
    new_file_path = 'consolidado2023_2.csv'
    df.to_csv(new_file_path, index=False,sep=';')
def main3():
    df=pd.read_csv("datos junio.csv",sep=";",encoding="ISO 8859-13")
    column_to_replace = ["Sociedad","Region","Zonal","Localidad","Porcion","N referencia","Cuenta contrato","N Servicio","Nombre o Razon Social","Direccion","Telefono","Celular","Email","Tramo Antiguedad","Antiguedad en dias","Deuda No Vencida","Deuda Vencida","Deuda Total","RUT","DV","Fecha Vencimiento Documento","Fecha Asignacion","Fecha Termino","N Servicio2","Fecha Gestion Contact " ,"Tipo de Contacto","Estado","Observacion","PAGO","Fecha de Pago","% Comision","Hon. Multicob","Periodo","Deuda Real","Q Clientes","Q Pagos"]  # Cambia esto al nombre de tu columna
    print("Nombres de las columnas antes del reemplazo:")
    print(df.columns)
        
        # Aplicar la función de reemplazo a los nombres de las columnas
    df.columns = [replace_special_characters3(col) for col in df.columns]
        
        # Filtrar las columnas que existen en el DataFrame después del reemplazo
    
    columns_to_process = [col for col in column_to_replace if col in df.columns]
        
        # Aplicar la función de reemplazo a cada columna especificada en columns_to_process
    for column in columns_to_process:
        df[column] = df[column].astype(str).apply(replace_special_characters3)
        
        # Imprimir nombres de las columnas después del reemplazo
    print("Nombres de las columnas después del reemplazo:")
    print(df.columns)
        
        # Imprimir los primeros valores de las columnas seleccionadas después del reemplazo
    print("Valores después del reemplazo:")
    print(df[columns_to_process].head())
        
        # Guardar el resultado en un nuevo archivo CSV
    new_file_path = 'datos junio_2.csv'
    df.to_csv(new_file_path, index=False, sep=';')
main3()
    

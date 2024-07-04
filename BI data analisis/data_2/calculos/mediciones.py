import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = r'06. Gestiones Diarias Junio 2024\GESTIONES_MULTICOB_20240619.csv'
DF=pd.read_csv(file_path, header=0,sep=';', on_bad_lines="warn")
Clientes=DF['Cliente'].unique()
Operarios=DF['Operador'].unique()
Fecha=DF['Fecha']
Telefono=DF['Telefono'].unique()
Correo=DF['Correo'].unique()
rut=DF['Rut']
digitoVerificador=DF['Dv']
lista1=[]
lista2=[]
lista3=[]
lista4=[]
Arreglo1={}
def RutDigitoVerificador():
    x=0
    for i in rut:
        lista1.append(i)
    for j in digitoVerificador:
        lista2.append(j)   
    if len(lista1) != len(lista2):
        raise ValueError("Las listas de RUT y dígitos verificadores no tienen la misma longitud")
        
    for k in range(len(lista1)):
        RUT = lista1[k]
        DV = lista2[k]
        A=(f"{RUT}-{DV}")
        lista3.append(A)
        x += 1
    print(lista3)
def Count_Operarios():
    y=0
    for i in Operarios:
        y += 1
        lista4.append(i)
    print(y)
    print(lista4)
def operaciones_por_operario():
    for i in Operarios:
        x=0
        fechas_trabajadas = set()
        for j in DF['Operador'].values:
            if i == j:
                x += 1
                fechas_trabajadas.update(DF[DF['Operador'] == i]['Fecha'].unique())
        lista4.append({
            'Operador': i,
            'Dias_trabajados': len(fechas_trabajadas),
            'Cantidad_operaciones': x
        })
    
    # Crear DataFrame a partir de la lista de resultados
    df_resultados = pd.DataFrame(lista4)
    
    # Exportar el DataFrame a CSV
    df_resultados.to_csv('resultados_operaciones.csv', index=False)
    
    # Exportar el DataFrame a JSON
    df_resultados.to_json('resultados_operaciones.json', orient='records')
      
    print(lista4)


operaciones_por_operario()   
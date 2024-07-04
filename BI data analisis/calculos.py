import pandas as pd
from collections import defaultdict
files=[r"operaciones junio\GESTIONES_MULTICOB_20240619.csv",r"operaciones junio\GESTIONES_MULTICOB_20240618.csv",r"operaciones junio\GESTIONES_MULTICOB_20240617.csv",r"operaciones junio\GESTIONES_MULTICOB_20240615.csv",r"operaciones junio\GESTIONES_MULTICOB_20240614.csv",r"operaciones junio\GESTIONES_MULTICOB_20240613.csv",r"operaciones junio\GESTIONES_MULTICOB_20240612.csv",r"operaciones junio\GESTIONES_MULTICOB_20240611.csv",r"operaciones junio\GESTIONES_MULTICOB_20240610.csv",r"operaciones junio\GESTIONES_MULTICOB_20240608.csv",r"operaciones junio\GESTIONES_MULTICOB_20240607.csv",r"operaciones junio\GESTIONES_MULTICOB_20240606.csv",r"operaciones junio\GESTIONES_MULTICOB_20240605.csv",r"operaciones junio\GESTIONES_MULTICOB_20240604.csv",r"operaciones junio\GESTIONES_MULTICOB_20240603.csv",r"operaciones junio\GESTIONES_MULTICOB_20240601.csv"]
files2=[r"2023\01-12-2023_data.csv",r"2023\15-12-2023_data.csv",r"C:\Users\royza\OneDrive\Escritorio\BI data analisis\2023\18-12-2023_data.csv",r"2024\01-04-2024_data.csv",r"2024\02-01-2024_data.csv",r"2024\02-05-2024_data.csv",r"2024\04-03-2024_data.csv",r"2024\05-02-2024_data.csv",r"2024\10-01-2024_data.csv",r"2024\10-04-2024_data.csv",r"2024\15-03-2024_data.csv",r"2024\15-04-2024_data.csv",r"2024\26-01-2024_data.csv"]
files3="datos junio_2.csv"
files4=[r"C:\Users\royza\OneDrive\Escritorio\BI data analisis\2024\15-03-2024_data.csv",r"C:\Users\royza\OneDrive\Escritorio\BI data analisis\2024\15-04-2024_data.csv",r"C:\Users\royza\OneDrive\Escritorio\BI data analisis\2024\02-05-2024_data.csv",r"datos junio_2.csv"]
A=["PAGOS"]
B=["Q PAGOS"]
C=["PAGOS"]
D=["Q PAGOS"]
DF2=pd.read_csv(files3,sep=";",encoding="Latin-1")
for i in files2:
    df = pd.read_csv(i, sep=";")
    a = 0
    b = 0
    for j in df["PAGO"]:
        a = a + j
        if j > 0:
            b = b + 1
    A.append(a)
    B.append(b)

def junio():
    c = 0
    d = 0
    for i in DF2["PAGO"]:
        c = c + i
        if i > 0:
            d = d + 1
    C.append(c)
    D.append(d)

junio()

pagosJUN = C[1]
QpagosJUN = D[1]

pagosD = int(A[3])
QpagosD = int(B[3])

pagosE = int(A[13])
QpagosE = int(B[13])

pagosF = int(A[8])
QpagosF = int(B[8])

pagosMR = int(A[11])
QpagosMR = int(B[11])
pagosMA=int(A[6])
QpagosMA=int(B[6])

pagosA = int(A[12])
QpagosA = int(B[12])

# Listas de pagos y cantidad de pagos por mes
lista_P = [pagosD, pagosE, pagosF, pagosMR, pagosA, pagosMA]
lista_QP = [QpagosD, QpagosE, QpagosF, QpagosMR, QpagosA, QpagosMA]

# Función para calcular porcentajes
porcentaje_P = ["% pagos vs Meses Anteriores"]
porcentaje_QP = ["% Qpagos vs Meses Anteriores"]

def calculo_p():
    for i in lista_P:
        porcentaje_p = (pagosJUN / i) * 100
        porcentaje_P.append(f"{porcentaje_p}%")
    for k in lista_QP:
        porcentaje_qp = (QpagosJUN / k) * 100
        porcentaje_QP.append(f"{porcentaje_qp}%")

calculo_p()

# Crear DataFrames para porcentajes
df_porcentaje_P = pd.DataFrame({
    "Mes": ["Dic 2023", "Ene 2024", "Feb 2024", "Mar 2024", "Abr 2024", "May 2024"],
    "Porcentaje_Pagos_vs_Junio": porcentaje_P[1:]  # Excluimos el primer elemento que es un encabezado
})

df_porcentaje_QP = pd.DataFrame({
    "Mes": ["Dic 2023", "Ene 2024", "Feb 2024", "Mar 2024", "Abr 2024", "May 2024"],
    "Porcentaje_QPagos_vs_Junio": porcentaje_QP[1:]  # Excluimos el primer elemento que es un encabezado
})

# Guardar DataFrames en archivos CSV
df_porcentaje_P.to_csv("porcentaje_pagos_vs_junio.csv", sep=";", index=False, encoding="utf-8")
df_porcentaje_QP.to_csv("porcentaje_qpagos_vs_junio.csv", sep=";", index=False, encoding="utf-8")


# Mostrar nombres de archivos guardados
print("Archivo guardado: porcentaje_pagos_vs_mayo_anterior.csv")
print("Archivo guardado: porcentaje_qpagos_vs_mayo_anterior.csv")

operaciones = ["Cantidad de operaciones"]
CONTACTABILIDAD = ["contactavilidad"]
Por_contactavilidad = ["% Contactivilidad"]

for i in files4:
    count = 0
    contactavilidad = 0
    df = pd.read_csv(i, sep=";")
    for j in df["Tipo de Contacto"]:
        count = count + 1
        if j != "Sin Contacto" and j != "Inubicable":
            contactavilidad = contactavilidad + 1
    CONTACTABILIDAD.append(contactavilidad)
    operaciones.append(count)
    porcentaje_contactabilidad = (contactavilidad / count) * 100
    Por_contactavilidad.append(f"{porcentaje_contactabilidad}%")

fecha = 0

# Listas y datos de contacto por mes
contacto_data = []

for i in files4:
    df = pd.read_csv(i, sep=";")
    T_con = df["Tipo de Contacto"]
    Sin_Contacto = 0
    Medios_Masivos = 0
    Inubicable = 0
    Contacto_Directo = 0
    Contacto_Indirecto = 0
    Contacto_Tercero = 0
    Total = 0
    for k in T_con:
        if k == "Sin Contacto":
            Sin_Contacto = Sin_Contacto + 1
        elif k == "Inubicable":
            Inubicable = Inubicable + 1
        elif k == "Contacto Directo":
            Contacto_Directo = Contacto_Directo + 1
        elif k == "Contacto Indirecto":
            Contacto_Indirecto = Contacto_Indirecto + 1
        elif k == "Contacto con Tercero":
            Contacto_Tercero = Contacto_Tercero + 1
        Total = Total + 1

    if fecha == 0:
        datos = pd.DataFrame({
            "Mes": ["MARZO"],
            "Sin Contacto": [Sin_Contacto],
            "Inubicable": [Inubicable],
            "Contacto Directo": [Contacto_Directo],
            "Contacto Indirecto": [Contacto_Indirecto],
            "Contacto con Tercero": [Contacto_Tercero]
        })
        contacto_data.append(datos)

    elif fecha == 1:
        datos = pd.DataFrame({
            "Mes": ["ABRIL"],
            "Sin Contacto": [Sin_Contacto],
            "Inubicable": [Inubicable],
            "Contacto Directo": [Contacto_Directo],
            "Contacto Indirecto": [Contacto_Indirecto],
            "Contacto con Tercero": [Contacto_Tercero]
        })
        contacto_data.append(datos)

    elif fecha == 2:
        datos = pd.DataFrame({
            "Mes": ["MAYO"],
            "Sin Contacto": [Sin_Contacto],
            "Inubicable": [Inubicable],
            "Contacto Directo": [Contacto_Directo],
            "Contacto Indirecto": [Contacto_Indirecto],
            "Contacto con Tercero": [Contacto_Tercero]
        })
        contacto_data.append(datos)

    elif fecha == 3:
        datos = pd.DataFrame({
            "Mes": ["JUNIO"],
            "Sin Contacto": [Sin_Contacto],
            "Inubicable": [Inubicable],
            "Contacto Directo": [Contacto_Directo],
            "Contacto Indirecto": [Contacto_Indirecto],
            "Contacto con Tercero": [Contacto_Tercero]
        })
        contacto_data.append(datos)

    fecha = fecha + 1

# Guardar cada DataFrame en un archivo CSV
for idx, df in enumerate(contacto_data):
    mes = df["Mes"].iloc[0]
    nombre_archivo = f"datos_contacto_{mes}.csv"
    df.to_csv(nombre_archivo, sep=";", index=False, encoding="utf-8")

# Mostrar los nombres de los archivos guardados (opcional)
for idx, df in enumerate(contacto_data):
    mes = df["Mes"].iloc[0]
    print(f"Archivo guardado: datos_contacto_{mes}.csv")
impacto_gestion = {
    "Volver a llamar":0,
    "Corta Llamado":0,
    "Telefono no corresponde":0,
    "Sin Gestión":0,
    "No contesta":0,
    "Buzon de Voz":0,
    "Se envia Mail":0,
    "Recado":0,
    "Se envia SMS":0,
    "Ocupado":0,
    "Agendamiento":0,
    "Compromiso de Pago":0,
    "Convenio":0,
    "Informa que pago":0,
    "Expone Requerimiento":0,
    "Nuevo telefono":0,
    "Fallecido":0,
    "Pagando convenio":0,
    "Telefono Inexistente":0,
    "No puede pagar":0,
    "Reclamo pendiente":0,
    "Contesta menor de Edad":0,
    "Desconoce la deuda":0,
    "Se recibe Mail":0
}

df3 = pd.read_csv(files3, sep=";")
tipo_gestion = df3["Gestion"]
recupero = df3["PAGO"]


for idx, gestion in enumerate(tipo_gestion):
    if gestion in impacto_gestion:
        impacto_gestion[gestion] += recupero[idx]

# Calcular porcentaje de impacto por gestión

total_recupero = sum(impacto_gestion.values())
porcentaje_impacto_gestion = {k: (v / total_recupero) * 100 for k, v in impacto_gestion.items()}


# Crear DataFrame
df_impacto = pd.DataFrame(list(porcentaje_impacto_gestion.items()), columns=["Tipo de Gestión", "Porcentaje de Impacto"])

# Ordenar por porcentaje de impacto
df_impacto = df_impacto.sort_values(by="Porcentaje de Impacto", ascending=False)

# Imprimir DataFrame
print(df_impacto.to_string(index=False))
df_impacto.to_csv("Impacto_gestiones.csv",sep=";",encoding="UTF-8")

operadores = defaultdict(int)

# Iterar sobre cada archivo
for file in files:
    try:
        # Leer el archivo CSV
        df = pd.read_csv(file, sep=";", encoding="Latin-1")

        # Filtrar los clientes que contienen "ESSBIO" en su nombre
        df_essbio = df[df['Cliente'].str.contains('ESSBIO', case=False, na=False)]

        # Contar la cantidad de operaciones por operador en el DataFrame filtrado
        counts = df_essbio["Operador"].value_counts()

        # Sumar al diccionario
        for operador, count in counts.items():
            operadores[operador] += count

    except pd.errors.ParserError as e:
        print(f"Error al procesar {file}: {e}")

# Crear DataFrame
df_operaciones = pd.DataFrame({
    "Operador": list(operadores.keys()),
    "Total de Operaciones": list(operadores.values())
})

# Ordenar DataFrame por operador (opcional)
df_operaciones = df_operaciones.sort_values(by="Operador")

# Exportar a CSV
df_operaciones.to_csv("total_operaciones_por_operador_filtrado.csv", sep=";", index=False, encoding="utf-8")

# Mostrar el DataFrame (opcional)
print(df_operaciones)
recuperacionMR = (pagosMR / operaciones[1]) * (100/2935669451)
recuperacionA = (pagosA / operaciones[2]) * (100/579970)
recuperacionMA = (pagosMA / operaciones[3]) * (100/22559883098)
recuperacionJUN= (pagosJUN/ operaciones[4])*(100/21587438559)
lista_recupero=[f"{recuperacionMR}%",f"{recuperacionA}%",f"{recuperacionMA}%",f"{recuperacionJUN}%"]
df_recuperacion = pd.DataFrame({
    "Mes": [ "Mar 2024", "Abr 2024", "May 2024","Jun 2024"],
    "Tasa_Recuperacion": lista_recupero
})

# Guardar DataFrame en archivo CSV
df_recuperacion.to_csv("tasa_recuperacion.csv", sep=";", index=False, encoding="utf-8")


import pandas as pd
from Transformacion.Transformacion import First
from calculos.mediciones import operaciones_por_operario

def main():
    # Ruta al archivo CSV  
    file=[r'Aguas Andinas.csv',r'ANDESAP - Administradora de activo financiero.csv',r'AUTOPISTA RUTAPASS.csv',r'BELCORP.csv',r'Colmena Golden Cross S.A.csv',r'Compañía De Asistencia Al Viajero De Chile Limitada.csv',r'Corona Preventiva.csv',r'CORREOS DE CHILE.csv',r'COSMETICOS AVON S.A.csv',r'DIRECTV.csv',r'ENEL.csv',r'ESSBIO - NO REGULADOS.csv',r'ESSBIO S.A..csv',r'FRUTAROM CHILE SA.csv',r'HITES CASTIGO.csv',r'INSTITUTO PROFESIONAL DE CHILE S A.csv',r'LARA Y COMPAÑIA SPA.csv',r'MACROTEL.csv',r'NATURA COSMETICOS SA.csv',r'Operalia.csv',r'SACYR AGUA S.A.csv',r'Universidad de Concepción.csv']
    X=[]
    for i in file:
        df = pd.read_csv(i, header=0,sep=',', on_bad_lines='warn')  # Ajusta 'header' según sea necesario
        df.columns = df.columns.str.strip()
        print(df.columns)

        operador=df['Operador'].unique()
        for k in operador:
            x=0        
            df_Operador=df[df['Operador']==k]
            nombre_archivo = f'{k} + {i}'
            df_Operador.to_csv(nombre_archivo, index=False)
            
        
        

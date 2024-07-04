import pandas as pd
file="consolidado2024.csv"
df=pd.read_csv(file,header=0,sep=';',encoding='Latin',on_bad_lines='warn')
region = df['Región']
files=[r'Region Del Biobio.csv',r'Region Del Maule.csv',r"Region Libertador Bernardo O'Higgins.csv"]
def main():
        
    for i in region:
        df_region=df[df['Región']==i]
        nombre_region=""
        
        if i==6:
            nombre_region="Region Libertador Bernardo O'Higgins.csv"
        elif i==7:
            nombre_region="Region Del Maule.csv"
        elif i==8:
            nombre_region="Region Del Biobio.csv"
        else:
            print("Not Found")
        df_region.to_csv(nombre_region,index=False)

def secondary():
    for i in files:
        DF=pd.read_csv(i,header=0,sep=',',on_bad_lines='warn')
        df.columns=df.columns.str.strip()
        comuna=DF['Localidad'].unique()
        for k in comuna:
            df_comuna=df[df['Localidad']==k]
            df_comuna.to_csv(f"{k}.csv",index=False)



def Third():
    for i in files:
        DF=pd.read_csv(i,header=0,sep=',',on_bad_lines='warn')
        df2=DF[['Sociedad','Región','Localidad','Tramo Antigüedad','Antigüedad en días','Deuda Total','PAGO','Deuda Real','Q Pagos']]
        
        df2.to_csv(f"{i}_resumido.csv",sep=',',index=False)
Third()
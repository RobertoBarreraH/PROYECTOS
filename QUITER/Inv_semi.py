import pandas as pd 
import datetime

def seminuevos ():
    fecha=datetime.datetime.now().strftime("%Y-%m-%d")
    df=pd.read_excel('C:/Quiter/reportes/U22902-'+fecha+'.xls')
    df=pd.DataFrame(df)
    elementos= df.shape
    elemento1= elementos[0]-2
    elemento2= elementos[0]-1
    df=df.drop(df.index[[elemento1,elemento2]])
    df.to_excel("INV_SEMINUEVOS-"+fecha+".xlsx", index=False)
    print(fecha)  
seminuevos()
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    df = df.applymap(lambda s : s.lower().replace('_', ' ').replace('-', ' ') if type(s) == str else s)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\$[\s*]", "").str.replace(",", "").str.replace("\.00", "")
    df = df.astype({ "monto_del_credito": int, "comuna_ciudadano": float})

    #
    # Inserte su código aquí
    #

    return df

clean_data()

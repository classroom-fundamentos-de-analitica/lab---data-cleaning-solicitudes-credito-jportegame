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

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)

    df.dropna(axis = 0, inplace = True)

    df = df.applymap(lambda s : s.lower().replace('_', ' ').replace('-', ' ') if type(s) == str else s)
    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\$[\s*]", "").str.replace(",", "").str.replace("\.00", "")
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda f: datetime.strptime(f, "%Y/%m/%d") if (len(re.findall("^\d+/", f)[0]) - 1) == 4 else datetime.strptime(f, "%d/%m/%Y"))
    df = df.astype({ "monto_del_credito": int, "comuna_ciudadano": float})

    df.drop_duplicates(inplace = True)

    #
    # Inserte su código aquí
    #

    return df

clean_data()

#[6617, 3589]
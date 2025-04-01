import pandas as pd

df = pd.read_csv("diciembre_2024.csv")

indices_utiles = []
for index in df.index:
    valor = df["fecha"].iloc[index]
    try:
        if (valor[:7] == "2024-12" or valor[:7] == "2024-11"):
            print(valor)
            indices_utiles.append(index)
    except:
        continue

df = df.iloc[indices_utiles]

print(df)

df.to_excel("base_de_datos_diciembre_2024.xlsx")
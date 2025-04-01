import pandas as pd

df = pd.read_csv('coes db/coes.csv')

columna_conflicto_ambiental = "p19a1"
tipo_conflicto_ambiental = [400, 407]
df = df.loc[df[columna_conflicto_ambiental] >= tipo_conflicto_ambiental[0]]
df = df.loc[df[columna_conflicto_ambiental] <= tipo_conflicto_ambiental[1]]

# columna_region = "p6"
# region_coquimbo = 4
# df = df.loc[df[columna_region] == region_coquimbo]

print(df)

df.to_excel("coquimbo_coes.xlsx")

# print(df["p19a1"])
# print(len(df["p19a1"]))

# columna_comuna = "p8"
# print(df[columna_comuna])

# columna_estrategias_manifestacion = "p29a"
# print(df[columna_estrategias_manifestacion])

# columna_medio = "medio"
# print(df[columna_medio])

# columna_actores = "p18a"
# print(df[columna_actores])

# print(df.columns)
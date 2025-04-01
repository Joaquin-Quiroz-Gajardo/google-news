import pandas as pd

columns = [
    "id_noticia",
    "id_accion_contenciosa",
    "id_conflicto",
    "fecha",
    "link",
    "medio",
    "tipo_medio",
    "region",
    "columna",
    "localidad_accion",
    "periodo",
    "tipo_energia",
    "subtipo_renovable",
    "tipo_conflicto",
    "tipo_accion",
    "tipo_actor_demandante",
    "actor_demandante",
    "tipo_actor_demandado",
    "actor_demandado",
    "bajada"
]

df = pd.DataFrame([], columns=columns)
print(df)

news = pd.read_csv("all_news.csv")

for index, row in news.iterrows():
    data_row = [
        "",
        "",
        "",
        row["fecha"],
        row["link"],
        row["medio"],
        "",
        row["region"],
        row["comuna"],
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        row["bajada"]
    ]
    row = pd.DataFrame([data_row], columns=columns)
    df = pd.concat([df, row], ignore_index=True)

df.to_csv("entrega_4_12.csv", index=False)
df.to_excel("entrega_4_12.xlsx", index=False)
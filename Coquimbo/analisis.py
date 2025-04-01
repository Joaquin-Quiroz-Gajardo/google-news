import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_news.csv")

print(len(df))

print(len(df.link.unique()))

print(df.region.value_counts())

# barlist = plt.bar(df.region.value_counts().index, df.region.value_counts(), color="#7fb0b8")
# plt.xticks(rotation=80, fontsize=8)
# plt.title("Frecuencia de noticias por región")
# plt.xlabel("Regiónes")
# plt.ylabel("Número de noticias")
# # centro
# barlist[0].set_color('#f44336')
# barlist[1].set_color('#f44336')
# barlist[2].set_color('#f44336')
# barlist[9].set_color('#f44336')
# barlist[12].set_color('#f44336')
# # norte
# barlist[5].set_color('#6aa84f')
# barlist[7].set_color('#6aa84f')
# barlist[8].set_color('#6aa84f')
# barlist[13].set_color('#6aa84f')
# barlist[14].set_color('#6aa84f')
# plt.show()





# print(df.medio.value_counts()[:20])

# plt.bar(
#     df.medio.value_counts().index[:13], 
#     df.medio.value_counts()[:13],
#     hatch="/",
#     edgecolor="black",
#     color="white"
# )
# plt.title("Medios más frecuentes")
# plt.xlabel("Medios")
# plt.ylabel("Frecuencia")
# plt.xticks(rotation=45, fontsize=8)
# plt.show()


print(df.comuna.value_counts()[:20])






# dates
for index, row in df.iterrows():
    # print(row["fecha"][:4])
    try:
        df.at[index, "fecha"] = row["fecha"][:4]
    except:
        df.at[index, "fecha"] = "2024"

plt.plot(
    df['fecha'].value_counts().index, 
    df['fecha'].value_counts(),
    marker='o',
    color="black",
    linestyle="--",
    markerfacecolor='white',
    )

plt.xticks(df['fecha'].value_counts().index, labels=[
    "2024",
    "2023",
    "2022",
    "2021",
    "2020",
    "2019",
    "2018",
    "2017",
    "2016",
    "2015",
    "2014",
    "2013",
    "2012",
    "2011",
    "2010",
    "2009",
    "2008",
    "2007",  
])

plt.title("Fechas de las noticias")
plt.xlabel("Años")
plt.ylabel("Frecuencia")
plt.show()


# df.to_excel("data_news_20_nov.xlsx", index=False)

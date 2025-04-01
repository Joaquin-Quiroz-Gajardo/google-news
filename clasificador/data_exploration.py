import pandas as pd

# df = pd.read_csv("clasification.csv")
# print("clasification", df.label.value_counts())

df = pd.read_csv("clasification conflicto.csv")
print("clasification conflicto", df.label.value_counts())

df = df.loc[df['label'] == "conflicto"]

df.to_csv("entrega_2025_conflicto_score.csv", index=False)
df.to_excel("entrega_2025_conflicto_score.xlsx", index=False)









# df = pd.read_csv("clasification conflicto categorias.csv")
# print("clasification", df.label.value_counts())

# df_1 = df.loc[df['label'] == "conflicto minero"]
# df_2 = df.loc[df['label'] == "conflicto energias renovables"]

# df = pd.concat([df_1, df_2], ignore_index=True)
# print(len(df))
# # for i in df.titulo[90:95]:
# #     print(i)

# df.to_csv("entrega_2025.csv", index=False)








# df = pd.read_csv("clasification conflicto ambiental.csv")
# print("clasification", df.label.value_counts())

# df_1 = df.loc[df['label'] == "conflicto ambiental"]

# # df = pd.concat([df_1, df_2], ignore_index=True)
# print(len(df))
# # for i in df.titulo[90:95]:
# #     print(i)

# df.to_csv("entrega_2025_conflicto.csv", index=False)







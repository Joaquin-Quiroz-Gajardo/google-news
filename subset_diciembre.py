import pandas as pd

diciembre = pd.read_csv("datos_diciembre_2025.csv")
old_dataset = pd.read_csv("all_news.csv")

diciembre = diciembre.drop_duplicates(subset=['link'], keep='first')

print(diciembre)

diciembre = diciembre[~diciembre.link.isin(old_dataset['link'])]

print(diciembre)

diciembre.to_csv("diciembre_2024.csv", index=False)
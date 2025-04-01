import json
import readFromFile
import pandas as pd

file = open("regiones_y_comunas.json", encoding="utf-8")
data=json.load(file)
# df = pd.DataFrame({'region': [], 'comuna': [], 'titulo': [], 'fecha': [], 'bajada': [], 'link': [], 'medio': []})
df = pd.read_csv("all_news.csv")

content_query = "conflictos+ambientales"

for region in data["regions"]:
    for comuna in region["communes"]:
        query = f'{content_query}+{region["name"].replace(" ", "+")}+"{comuna["name"].replace(" ", "+")}"'
        info = readFromFile.get_data(query, region['name'], comuna['name'])
        print(info)
        new_df = pd.DataFrame(info)
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv("all_news.csv", index=False)

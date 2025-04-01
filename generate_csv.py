import pandas as pd

df = pd.read_excel("data_news_20_nov.xlsx")

df.to_csv("all_news.csv", index=False)
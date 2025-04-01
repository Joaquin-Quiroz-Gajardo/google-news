from transformers import pipeline
import pandas as pd

clasiffier = pipeline("zero-shot-classification", model="Recognai/bert-base-spanish-wwm-cased-xnli")

df = pd.read_csv("all_news.csv")

label = [] 
score = []
for i, row in df.iterrows():
    title = row["titulo"]
    response = clasiffier(title, candidate_labels=["conflicto ambiental", "otros"])
    # print(response)
    label.append(response["labels"][0])
    score.append(response["scores"][0])

df["label"] = label
df["score"] = score

print(df)

df.to_csv("clasification conflicto ambiental.csv", index = False)
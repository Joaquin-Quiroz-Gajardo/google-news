queries = [
    "protesta ambiental", 
    "manifestacion ambiental", 
    "manifestacion minera", 
    "protestas agua",
    ]

comunas_coquimbo = [
    "andacollo",
    "canela",
    "combarbala",
    "coquimbo",
    "illapel",
    "la higuera",
    "la serena",
    "los vilos",
    "monte patria",
    "ovalle",
    "paihuano",
    "punitaqui",
    "rio hurtado",
    "salamanca",
    "vicuña",
]

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.DataFrame([], columns=["title", "link", "date"])

for comuna in comunas_coquimbo:
    for query in queries:
        try:
            created_query = f'{query.replace(" ", "+")}+"{comuna.replace(" ", "+")}"'
            root = "https://www.google.com"
            link = f'https://www.google.com/search?q={created_query}&client=opera-gx&sca_esv=ab93c7b204ecfff7&biw=1377&bih=668&tbm=nws&sxsrf=ADLYWIK1bmE-4CS97fGuuGaO3y--_EaDww%3A1729556765451&ei=HfEWZ_edG8yz1sQPju2TgAw&ved=0ahUKEwi3oP6E3aCJAxXMmZUCHY72BMAQ4dUDCA0&oq={created_query}&gs_lp=Egxnd3Mtd2l6LW5ld3MiHHByb3Rlc3RhcyBhZ3VhICJyaW8gaHVydGFkbyJIAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEMyAEAmAIAoAIAmAMAkgcAoAcA&sclient=gws-wiz-news'

            req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
            webpage = urlopen(req).read()
            
            with requests.Session() as c:
                soup = BeautifulSoup(webpage, "html.parser")
                for item in soup.find_all("div", attrs={"class": "Gx5Zad"}): #kCrYT
                    raw_link=item.find("a", href=True)["href"]
                    if "/search?q=" in raw_link:
                        continue
                    link = (raw_link.split("/url?q=")[1]).split("&sa=U&")[0]
                    print(link)

                    title, date=(item.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).get_text()).split("...")
                    
                    print(title)
                    print(date)
                    row = pd.DataFrame([[title, link, date]], columns=["title", "link", "date"])
                    df = pd.concat([df, row], ignore_index=True)
                    print("------------------------------------------")
        except:
            continue

print(df)
df.to_csv("datos_coquimbo.csv", index=False)
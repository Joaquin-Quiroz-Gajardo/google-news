import json
from bs4 import BeautifulSoup
import requests

print("que paSa".lower())

# data=json.load()

query = 'conflictos+ambientales+conflictos+ambientales+Biobío+"Talcahuano"'#conflictos+ambientales+"la+florida"+chile'

# print(soup)

# all_span = soup.find_all(
#     "a", 
#     # class_ = "f1"
#     )
    
# for index, i in enumerate(all_span):
#     print(i)

def get_data(query, region, comuna):

    data_noticias = {
        "region": [],
        "comuna": [],
        "titulo": [],
        "fecha": [],
        "bajada": [],
        "link": [],
        "medio": [],
    }

    more_news = True
    start = 0

    while more_news == True:
        print("iteration")
        
        url_base = f'https://www.google.com/search?q={query}&client=opera-gx&sca_esv=7fc9e9e0d3593017&tbm=nws&sxsrf=ADLYWILtjCg0sQL5EC2gS6xuXA7CsPC1tw:1732079949682&ei=TXE9Z_GxKfSh5OUP__GQ4AE&start={start}&sa=N&ved=2ahUKEwixjP7QlOqJAxX0ELkGHf84BBwQ8tMDegQIAxAE&biw=766&bih=668&dpr=1.35'
        pedido = requests.get(url_base)
        html_obtenido = pedido.text
        soup = BeautifulSoup(html_obtenido, "html.parser")

        all_span = soup.find_all(
            "h3",
            class_ = "zBAuLc l97dzf"
            )
            
        for index, i in enumerate(all_span):
            titulo = i.text
            data_noticias["titulo"].append(titulo)


        all_span = soup.find_all(
            "span", 
            class_ = "r0bn4c rQMQod"
            )
            
        for index, i in enumerate(all_span):
            fecha = i.text
            data_noticias["fecha"].append(fecha)


        all_span = soup.find_all(
            "a",
            )

        for index, i in enumerate(all_span):
            if i.has_attr("data-ved"):
                # print(index, i)
                _, link = i["href"].split("url?q=")
                link, _ = link.split("&sa=")
                # print(link)
                data_noticias["link"].append(link)

        all_span = soup.find_all(
            "div",
            class_ = "BNeawe s3v9rd AP7Wnd"
            )

        for index, i in enumerate(all_span):
            if index%2 == 0:
                bajada = i.text.split("...")[0]
                # print(bajada)
                data_noticias["bajada"].append(bajada)

        all_span = soup.find_all(
            "div",
            class_ = "BNeawe UPmit AP7Wnd lRVwie"
            )

        for index, i in enumerate(all_span):
            medio = i.text
            data_noticias["medio"].append(medio)

        start += 10

        print("data_noticias", len(data_noticias["medio"]))
        if len(data_noticias["medio"]) % 10:            
            break

        if start >= 500:
            break

    for i in data_noticias["medio"]:
        data_noticias["region"].append(region)
        data_noticias["comuna"].append(comuna)

    return data_noticias


print(get_data(query, "Biobío", "Talcahuano"))


# for i in get_data(soup).values():
#     print(len(i))

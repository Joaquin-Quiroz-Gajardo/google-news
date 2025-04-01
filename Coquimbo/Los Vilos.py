from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com"
link = "https://www.google.com/search?q=conflictos+ambientales+intext%3Alos+vilos&client=opera-gx&sca_esv=bbdbd4e0040378b7&biw=1377&bih=668&tbm=nws&sxsrf=ADLYWILz2aSHxJJ587VC1J4wkb8RSYJEZg%3A1728591434531&ei=SjYIZ-uVIPDP5OUPsb2P-QM&ved=0ahUKEwjr4qrz0ISJAxXwJ7kGHbHeIz8Q4dUDCA0&uact=5&oq=conflictos+ambientales+intext%3Alos+vilos&gs_lp=Egxnd3Mtd2l6LW5ld3MiJ2NvbmZsaWN0b3MgYW1iaWVudGFsZXMgaW50ZXh0OmxvcyB2aWxvc0jKFFCuA1imE3AAeACQAQCYAbcBoAHpCKoBAzguNLgBA8gBAPgBAZgCAaACvwHCAgUQIRigAZgDAIgGAZIHAzAuMaAH4w0&sclient=gws-wiz-news"

req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    for item in soup.find_all("div", attrs={"class": "Gx5Zad"}): #kCrYT
        raw_link=item.find("a", href=True)["href"]
        if "/search?q=" in raw_link:
            continue
        link = (raw_link.split("/url?q=")[1]).split("&sa=U&")[0]
        print(link)

        title, date=(item.find("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).get_text()).split("...")
        print(title)
        print(date)
        print("------------------------------------------")

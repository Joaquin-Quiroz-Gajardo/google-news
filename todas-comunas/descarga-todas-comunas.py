queries = [
    "protesta ambiental", 
    "manifestacion ambiental", 
    "manifestacion minera", 
    "protestas agua",
    ]

comunas = [
    "arica",
    "camarones",
    "putre",
    "general lagos",
    "iquique",
    "alto hospicio",
    "pozo almonte",
    "camiña",
    "huara",
    "pica",
    "antofagasta",
    "mejillones",
    "sierra gorda",
    "taltal",
    "calama",
    "ollague",
    "san pedro de atacama",
    "tocopilla",
    "maria elena",
    "copiapo",
    "caldera",
    "tierra amarilla",
    "chañaral",
    "diego de almagro",
    "vallenar",
    "alto de carmen",
    "freirina",
    "huasco",
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
    "valparaiso",
    "casablanca",
    "concon",
    "juan fernandez",
    "puchuncavi",
    "quintero",
    "viña del mar",
    "isla de pascua",
    "los andes",
    "calle larga",
    "rinconada",
    "san esteban",
    "la ligua",
    "cabildo",
    "papudo",
    "petorca",
    "zapallar",
    "quillota",
    "la calera",
    "hijuelas",
    "la cruz",
    "nogales",
    "san antonio",
    "algarrobo",
    "cartagena",
    "el quisco",
    "el tabo",
    "santo domingo",
    "san felipe",
    "catemu",
    "llay llay",
    "panquehue",
    "putaendo",
    "santa maria",
    "quilpue",
    "limache",
    "olmue",
    "villa alemana",
    "rancagua",
    "codegua",
    "coinco",
    "Coltauco",
    "Doñihue",
    "Graneros",
    "Las Cabras",
    "Machali",
    "Malloa",
    "Mostazal",
    "Olivar",
    "Peumo",
    "Pichidegua",
    "Quinta de Tilcoco",
    "Rengo",
    "Requinoa",
    "San Vicente",
    "Pichilemu",
    "La Estrella",
    "Litueche",
    "Marchigue",
    "Navidad",
    "Paredones",
    "San Fernando",
    "Chepica",
    "Chimbarongo",
    "Lolol",
    "Nancagua",
    "Palmilla",
    "Peralillo",
    "Placilla",
    "Pumanque",
    "Santa Cruz",
    "Talca",
    "Constitucion",
    "Curepto",
    "Empedrado",
    "Maule",
    "Pelarco",
    "Pencahue",
    "rio Claro",
    "San Clemente",
    "San Rafael",
    "Cauquenes",
    "Chanco",
    "Pelluhue",
    "Curico",
    "Hualañe",
    "Licanten",
    "Molina",
    "Rauco",
    "Romeral",
    "Sagrada Familia",
    "Teno",
    "Vichuquen",
    "Linares",
    "Colbun",
    "Longavi",
    "Parral",
    "Retiro",
    "San Javier",
    "Villa Alegre",
    "Yerbas Buenas",
    "Chillan",
    "Bulnes",
    "Chillan Viejo",
    "El Carmen",
    "Pemuco",
    "Pinto",
    "Quillon",
    "San Ignacio",
    "Yungay",
    "Quirihue",
    "Cobquecura",
    "Coelemu",
    "Ninhue",
    "Portezuelo",
    "Ranquil",
    "Treguaco",
    "San Carlos",
    "Coihueco",
    "Ñiquen",
    "San Fabian",
    "san Nicolas",
    "Concepcion",
    "Coronel",
    "Chiguayante",
    "Florida",
    "Hualqui",
    "Lota",
    "Penco",
    "San Pedro de La Paz",
    "Santa Juana",
    "Talcahuano",
    "Tome",
    "Hualpen",
    "Lebu",
    "Arauco",
    "Cañete",
    "Contulmo",
    "Curanilahue",
    "Los alamos",
    "Tirua",
    "Los angeles",
    "Antuco",
    "Cabrero",
    "Laja",
    "Mulchen",
    "Nacimiento",
    "Negrete",
    "Quilaco",
    "Quilleco",
    "San Rosendo",
    "Santa Barbara",
    "Tucapel",
    "Yumbel",
    "Alto Biobio",
    "Temuco",
    "Carahue",
    "Cunco",
    "Curarrehue",
    "Freire",
    "Galvarino",
    "Gorbea",
    "Lautaro",
    "Loncoche",
    "Melipeuco",
    "Nueva Imperial",
    "Padre Las Casas",
    "Perquenco",
    "Pitrufquen",
    "Pucon",
    "Saavedra",
    "Teodoro Schmidt",
    "Tolten",
    "Vilcun",
    "Villarrica",
    "Cholchol",
    "Angol",
    "Collipulli",
    "Curacautin",
    "Ercilla",
    "Lonquimay",
    "Los Sauces",
    "Lumaco",
    "Puren",
    "Renaico",
    "Traiguen",
    "Victoria",
    "Valdivia",
    "Corral",
    "Lanco",
    "Los Lagos",
    "Mafil",
    "Mariquina",
    "Paillaco",
    "Panguipulli",
    "La Union",
    "Futrono",
    "Lago Ranco",
    "Rio Bueno",
    "Puerto Montt",
    "Calbuco",
    "Cochamo",
    "Fresia",
    "Frutillar",
    "Los Muermos",
    "Llanquihue",
    "Maullin",
    "Puerto Varas",
    "Castro",
    "Ancud",
    "Chonchi",
    "Curaco de Velez",
    "Dalcahue",
    "Puqueldon",
    "Queilen",
    "Quellon",
    "Quemchi",
    "Quinchao",
    "Osorno",
    "Puerto Octay",
    "Purranque",
    "Puyehue",
    "Rio Negro",
    "San Juan de la Costa",
    "San Pablo",
    "Chaiten",
    "Futaleufu",
    "Hualaihue",
    "Palena",
    "Coyhaique",
    "Lago Verde",
    "Aysen",
    "Cisnes",
    "Guaitecas",
    "Cochrane",
    "O Higgins",
    "Tortel",
    "Chile Chico",
    "Rio Ibañez",
    "Punta Arenas",
    "Laguna Blanca",
    "Rio Verde",
    "San Gregorio",
    "Cabo de Hornos",
    "Antartica",
    "Porvenir",
    "Primavera",
    "Timaukel",
    "Natales",
    "Torres del Paine",
    "Santiago",
    "Cerrillos",
    "Cerro Navia",
    "Conchali",
    "El Bosque",
    "Estacion Central",
    "Huechuraba",
    "Independencia",
    "La Cisterna",
    "La Florida",
    "La Granja",
    "La Pintana",
    "La Reina",
    "Las Condes",
    "Lo Barnechea",
    "Lo Espejo",
    "Lo Prado",
    "Macul",
    "Maipu",
    "Ñuñoa",
    "Pedro Aguirre Cerda",
    "Peñalolen",
    "Providencia",
    "Pudahuel",
    "Quilicura",
    "Quinta Normal",
    "Recoleta",
    "Renca",
    "San Joaquin",
    "San Miguel",
    "San Ramon",
    "Vitacura",
    "Puente Alto",
    "Pirque",
    "San Jose de Maipo",
    "Colina",
    "Lampa",
    "Til Til",
    "San Bernardo",
    "Buin",
    "Calera de Tango",
    "Paine",
    "Melipilla",
    "Alhue",
    "Curacavi",
    "Maria Pinto",
    "San Pedro",
    "Talagante",
    "El Monte",
    "Isla de Maipo",
    "Padre Hurtado",
    "Peñaflor",
    
]

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.DataFrame([], columns=["title", "link", "date", "comuna"])

for comuna in comunas:
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
                    row = pd.DataFrame([[title, link, date, comuna]], columns=["title", "link", "date", "comuna"])
                    df = pd.concat([df, row], ignore_index=True)
                    print("------------------------------------------")
        except:
            continue

print(df)
df.to_csv("datos_todas_regiones_2.csv", index=False)
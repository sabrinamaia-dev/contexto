import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GNEWS_API_KEY")


url = "https://gnews.io/api/v4/top-headlines"

parametros = {
    "category": "technology",
    "lang": "pt",
    "country": "br",
    "max": 5,
    "apikey": api_key
}

resposta = requests.get(url, params=parametros, timeout=10)
dados = resposta.json()
noticias_reais = dados["articles"]

print("Notícias recebidas:", len(noticias_reais))

for noticia_real in noticias_reais:
    print("Título:", noticia_real["title"])
    print("Fonte:", noticia_real["source"]["name"])
    print("Link:", noticia_real["url"])
    print()
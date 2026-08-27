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

for numero, noticia_real in enumerate(noticias_reais, start=1):
    print("Notícia", numero)
    print("Título:", noticia_real["title"])
    print("Fonte:", noticia_real["source"]["name"])
    print("Descrição:", noticia_real.get("description") or "Sem descrição disponível")
    print("Link:", noticia_real["url"])
    print("-" * 50)
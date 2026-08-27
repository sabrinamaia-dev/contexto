import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

api_key = os.getenv("GNEWS_API_KEY")
inicio_periodo = datetime.now(timezone.utc) - timedelta(hours=24)
inicio_periodo = inicio_periodo.isoformat(timespec="seconds").replace("+00:00", "Z")
print("Início do período:", inicio_periodo)

url = "https://gnews.io/api/v4/top-headlines"

parametros = {
    "category": "technology",
    "lang": "pt",
    "country": "br",
    "from": inicio_periodo,
    "max": 5,
}
cabeçalhos = {
    "X-Api-Key": api_key
}

resposta = requests.get(url, params=parametros, headers=cabeçalhos, timeout=10)
resposta.raise_for_status()
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
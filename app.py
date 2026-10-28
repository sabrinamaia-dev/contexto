import csv
import os
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request


load_dotenv()

app = Flask(__name__)

URL_MANCHETES = "https://gnews.io/api/v4/top-headlines"
URL_BUSCA = "https://gnews.io/api/v4/search"
CAMINHO_CSV = os.path.join(app.root_path, "noticias.csv")
INTERESSES = {
    "technology": {
        "titulo": "As principais notícias de tecnologia",
        "tipo": "categoria",
        "valor": "technology",
    },
    "artificial_intelligence": {
        "titulo": "As principais notícias sobre inteligência artificial",
        "tipo": "busca",
        "valor": '"inteligência artificial" OR "artificial intelligence" OR OpenAI',
    },
    "business": {
        "titulo": "As principais notícias de negócios",
        "tipo": "categoria",
        "valor": "business",
    },
    "world": {
        "titulo": "As principais notícias do mundo",
        "tipo": "categoria",
        "valor": "world",
    },
    "fashion": {
        "titulo": "As principais notícias sobre moda",
        "tipo": "busca",
        "valor": '(moda OR "fashion week" OR "tendências de moda") AND NOT "moda de viola" AND NOT sertanejo',
    },
}


def buscar_e_salvar_noticias(interesse):
    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        raise RuntimeError("A variável GNEWS_API_KEY não foi encontrada no .env.")

    inicio_periodo = datetime.now(timezone.utc) - timedelta(hours=24)
    inicio_periodo = inicio_periodo.isoformat(timespec="seconds").replace("+00:00", "Z")
    print("Início do período:", inicio_periodo)

    configuracao = INTERESSES[interesse]
    parametros = {
        "lang": "pt",
        "country": "br",
        "from": inicio_periodo,
        "max": 5,
    }

    if configuracao["tipo"] == "categoria":
        url = URL_MANCHETES
        parametros["category"] = configuracao["valor"]
    else:
        url = URL_BUSCA
        parametros["q"] = configuracao["valor"]
        parametros["sortby"] = "publishedAt"

    cabecalhos = {
        "X-Api-Key": api_key
    }

    resposta = requests.get(
        url,
        params=parametros,
        headers=cabecalhos,
        timeout=10,
    )
    resposta.raise_for_status()
    dados = resposta.json()
    noticias_reais = dados.get("articles", [])

    if interesse == "fashion":
        termos_indesejados = ("moda viola", "moda de viola", "sertanejo")
        noticias_reais = [
            noticia
            for noticia in noticias_reais
            if not any(
                termo in f'{noticia.get("title", "")} {noticia.get("description", "")}'.lower()
                for termo in termos_indesejados
            )
        ]

    print("Notícias recebidas:", len(noticias_reais))

    for numero, noticia_real in enumerate(noticias_reais, start=1):
        print("Notícia", numero)
        print("Título:", noticia_real["title"])
        print("Fonte:", noticia_real["source"]["name"])
        print("Descrição:", noticia_real.get("description") or "Sem descrição disponível")
        print("Link:", noticia_real["url"])
        print("-" * 50)

    urls_salvas = set()

    if os.path.exists(CAMINHO_CSV):
        with open(CAMINHO_CSV, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                urls_salvas.add(linha["url"])

    print("URLs armazenadas:", len(urls_salvas))

    with open(CAMINHO_CSV, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        if os.path.getsize(CAMINHO_CSV) == 0:
            escritor.writerow(["titulo", "fonte", "data_publicacao", "url"])

        for noticia in noticias_reais:
            url = noticia["url"]

            if url not in urls_salvas:
                escritor.writerow([
                    noticia["title"],
                    noticia["source"]["name"],
                    noticia["publishedAt"],
                    url,
                ])

            urls_salvas.add(url)

    return noticias_reais


@app.route("/", methods=["GET", "POST"])
def pagina_inicial():
    noticias = []
    erro = None
    busca_realizada = request.method == "POST"
    interesse_selecionado = "technology"
    agora = datetime.now().astimezone()

    if busca_realizada:
        interesse_selecionado = request.form.get("interesse", "technology")

        if interesse_selecionado not in INTERESSES:
            interesse_selecionado = "technology"

        try:
            noticias = buscar_e_salvar_noticias(interesse_selecionado)
        except (requests.RequestException, RuntimeError, KeyError, ValueError) as problema:
            print("Erro ao gerar o briefing:", problema)
            erro = "Não foi possível gerar o briefing agora. Tente novamente em alguns instantes."

    return render_template(
        "index.html",
        noticias=noticias,
        erro=erro,
        busca_realizada=busca_realizada,
        interesse_selecionado=interesse_selecionado,
        titulo_briefing=INTERESSES[interesse_selecionado]["titulo"],
        data_atual=agora.strftime("%d.%m.%Y"),
        data_iso=agora.date().isoformat(),
    )


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG") == "1",
        use_reloader=False,
        port=int(os.getenv("PORT", "5050")),
    )

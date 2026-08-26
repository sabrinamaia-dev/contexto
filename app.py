noticias = [
    {
        "titulo": "IA transforma mercado de trabalho",
        "fonte": "Exemplo News",
        "categoria": "Tecnologia"
    },
    {
     "titulo": "Banco Central mantém taxa de juros",
     "fonte": "Exemplo Economia",
     "categoria": "Economia"
    }
]
categoria_escolhida = input("Digite a categoria desejada: ")
for noticia in noticias:
    if noticia["categoria"].lower() == categoria_escolhida.lower():
        print("Título:", noticia["titulo"])
        print("Fonte:", noticia["fonte"])
        print("Categoria:", noticia["categoria"])
        print()
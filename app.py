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
noticia_encontrada = False
for noticia in noticias:
    if noticia["categoria"].lower() == categoria_escolhida.lower():
        noticia_encontrada = True
        print("Título:", noticia["titulo"])
        print("Fonte:", noticia["fonte"])
        print("Categoria:", noticia["categoria"])
        print()
if not noticia_encontrada:
    print("Nenhuma notícia encontrada para a categoria selecionada.")

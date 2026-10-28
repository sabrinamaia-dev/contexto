# índice.

### O mundo é grande. Comece por aqui.

O **índice.** transforma notícias recentes em um briefing simples e personalizado. A pessoa escolhe um tema, a aplicação consulta a GNews, apresenta as matérias em cards editoriais e registra as notícias novas em um arquivo CSV local.

Este também é um projeto de aprendizado prático, construído durante minha transição para a área de tecnologia e dados.

## O que já funciona

- Interface web responsiva com a identidade visual do **índice.**, feita com Flask, HTML e CSS.
- Briefings de Tecnologia, Inteligência Artificial, Negócios, Mundo e Moda.
- Busca de notícias em português publicadas nas últimas 24 horas.
- Registro local das notícias em `noticias.csv`, sem repetir links já salvos.
- Proteção da chave da GNews por variável de ambiente.

## Tecnologias

- Python e Flask
- HTML e CSS
- API GNews
- Git e GitHub
- Gunicorn para execução em ambiente de hospedagem

## Como abrir no computador

No Terminal, entre na pasta do projeto:

```bash
cd /Users/sabrinamaia/contexto
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Instale ou atualize as dependências:

```bash
pip install -r requirements.txt
```

Na raiz do projeto, mantenha um arquivo `.env` com a sua chave:

```text
GNEWS_API_KEY=sua_chave_aqui
```

Inicie a aplicação:

```bash
python app.py
```

Depois, abra [http://127.0.0.1:5050](http://127.0.0.1:5050) no navegador.

## Como publicar na internet

O repositório inclui um arquivo `render.yaml`, que deixa o índice. preparado para o Render:

1. Crie uma conta no Render e conecte sua conta do GitHub.
2. No painel, escolha **New + > Blueprint**.
3. Selecione o repositório `sabrinamaia-dev/indice`.
4. Quando o Render solicitar, informe `GNEWS_API_KEY` no campo secreto.
5. Confirme a criação do serviço e aguarde o primeiro deploy.

Ao final, o Render gera um endereço público terminado em `.onrender.com`. A chave não fica salva no GitHub.

> No plano gratuito, o serviço pode pausar depois de um período sem visitas. A primeira abertura seguinte pode demorar um pouco. O arquivo `noticias.csv` da hospedagem também é temporário; para manter um histórico permanente na internet, o próximo passo será trocar o CSV por um banco de dados.

## Arquivos principais

- `app.py`: busca, filtra e salva as notícias; também entrega a página Flask.
- `templates/index.html`: estrutura e conteúdo da interface.
- `static/style.css`: identidade visual e comportamento responsivo.
- `render.yaml`: configuração segura para publicar no Render.
- `noticias.csv`: histórico local, ignorado pelo Git.
- `.env`: chave privada da GNews, ignorada pelo Git.

## Próximos passos

- Testar a publicação com um link público.
- Substituir o CSV por um banco de dados quando o histórico precisar ser permanente.
- Refinar os filtros de cada categoria.
- Acrescentar novas formas de personalização do briefing.

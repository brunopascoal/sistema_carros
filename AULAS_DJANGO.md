- Abstração - Imaginar as coisas
- Django ja vem muita coisa pronta, gestao de usuario, gestao de sessao

# Estrutura dos projetos:

    - Pasta app é o coração do projeto;

## Manage.py:
    
    Usar pra sempre, rodar o comando manage.py, ele importa as configurações do projeto, entende o escopo do projeto (os comandos podem ser rodados no django-admin);

## __init_.py:

    - Serve para o python entender e iniciar o projeto app;

## asgi e wsgi: 

    - Servem pra deploy, usado para aplicationserver

## Urls:

    - Definir todas as urls do projeto, /admin, /carros..

## Settings:

    - Configurações do projeto, configuração de banco de dados, outros.



---------------------------------------------------------------------------------------------------------------------------------------------


# Apps:

    - Cada app é uma divisão lógica, projeto carros teria: 1 app para registro de carros, controle de carros. 2 app teria venda de carros, vendedores de carros...

## tests.py:

    - Usado pra fazer testes;

## Apps.py:

    - Configurações do app

## Models.py:

    - Escrever os modelos, tabela do banco de dados, modelagem.

## Views.py:

    - Todas as views do app, a view é a logica de trazer e renderizar.

## Admin.py:

    - Acesso ao ADM, crud completo...

------------------------------------------------------------------------------------------------------------------------

# makemigrations e migrate

    - makemigrations olha o projeto inteiro, app por app, monta as migrations, que sao arquivos python que tem comandos para o banco de dados
    - migrate executa a migration, vai de fato pegar os arquivos na migrations criados e executar
    - sempre executar depois de criar os models


# ORM 

    - Utiliza dos models pra acessar o banco de dados, atraves do python ele faz as querys no BD

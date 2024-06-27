# Sistema para cadastro de carros

## Descrição do projeto

Este é um sistema de gestão de carros desenvolvido com Django, que permite a inserção de carros com imagens, e possui um sistema de login e registro de usuários. O projeto está organizado em três principais aplicativos: app, accounts e cars.


## Requisitos para rodar o projeto

### Setup de ambiente:

- [Python 3.10+](https://www.python.org/downloads/)
- [Django 3.2+](https://docs.djangoproject.com/en/stable/releases/3.2/)
- [Poetry](https://python-poetry.org/)

### Como rodar na minha máquina?

1. Clone o projeto:
   ```bash
   git clone https://github.com/brunopascoal/sistema_carros
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-projeto
   ```
3. Instale as dependências:
   ```bash
   poetry install
   ```
4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
6. Rode o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
7. Pronto 🎉

## Estrutura do projeto

### `app`

O app principal contém as configurações básicas do projeto.

- `asgi.py`: Configuração para ASGI.
- `settings.py`: Configurações globais do projeto Django.
- `urls.py`: Roteamento principal do projeto.
- `wsgi.py`: Configuração para WSGI.
- `templates/base.html`: Template base para herança nos outros templates.

### `accounts`

O app `accounts` gerencia todas as informações relacionadas a usuários e autenticação.

- `models.py`: Modelos relacionados a usuários (no momento, sem modelos definidos).
- `views.py`: Views para registro, login e logout de usuários.
- `templates`:
  - `login.html`: Template para a página de login.
  - `register.html`: Template para a página de registro.

### `cars`

O app `cars` gerencia todas as funcionalidades relacionadas aos carros.

- `models.py`: Modelos para Marca (Brand) e Carro (Car).
- `views.py`: Views para listagem, criação, atualização, detalhamento e deleção de carros.
- `forms.py`: Formulários para criação e edição de carros.
- `templates`:
- `car_delete.html`: Template para deleção de um carro.
- `car_detail.html`: Template para detalhamento de um carro.
- `car_update.html`: Template para atualização de um carro.
- `cars.html`: Template para listagem de carros.
- `new_car.html`: Template para criação de um novo carro.

### Base do Projeto

- `db.sqlite3`: Banco de dados SQLite.
- `manage.py`: Script de gerenciamento do Django.
- `media/cars`: Diretório para armazenar imagens dos carros.
- `poetry.lock` e `pyproject.toml`: Arquivos de configuração do Poetry para gerenciar dependências.

## Funcionalidades

- **Registro de Usuários**: Permite que novos usuários se registrem no sistema.
- **Login/Logout de Usuários**: Autenticação de usuários para acessar o sistema.
- **CRUD de Carros**: Criação, leitura, atualização e deleção de registros de carros.
- **Upload de Imagens**: Upload de imagens dos carros.

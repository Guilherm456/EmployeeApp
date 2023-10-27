# Aplicativo para gerir empregados

## Sobre o projeto

Este projeto é um aplicativo para gerir empregados, onde é possível cadastrar, editar, remover e listar empregados.

Também foi adicionado sistema para gerir departamentos, sendo possível realizar as mesmas operações que são possíveis com empregados.

### Modelos

![Diagrama de Classe](./readme/image/classe.png)

## Como executar o projeto

### Pré-requisitos

- Python >= 3.6

- Pip

### Instalação

1. Clone o repositório (`git clone URL`)
2. Instale as dependências (`pip install -r requirements.txt`)
3. Crie o arquivo `.env`, onde deve a chave `SECRET_KEY` com o conteúdo da chave secreta do Django (exemplo: `SECRET_KEY='super_secret123'`)
4. Caso queira sistema de autenticação, insira a chave `AUTH_VARIABLE` como `True` dentro da `.env` e crie um usuário para ter acesso às API's (`python manage.py createsuperuser`)
5. Crie as models no banco de dados (`python manage.py makemigrations`)
   > Por padrão, será carregado o banco de dados SQLite, caso queira utilizar POSTGRES (para pode fazer deploy na Vercel), adiciona na `.env`:
   - `DATABASE_OPTION` como `POSTGRES`
   - `POSTGRES_URL` com a URL do banco de dados
   - `POSTGRES_USER` com o usuário do banco de dados
   - `POSTGRES_HOST` com o host do banco de dados
   - `POSTGRES_PASSWORD` com a senha do banco de dados
   - `POSTGRES_DATABASE` com o nome do banco de dados
   - `POSTGRES_DB_PORT` com a porta do banco de dados
     > Sempre que houver alterações nos modelos, é necessário executar o comando acima para criar as migrações e o passo 6
6. Criar as tabelas no banco de dados (`python manage.py migrate`)
7. Execute o servidor (`python manage.py runserver`)

   > Caso queira executar os testes automatizados, execute o comando `python manage.py test`

8. Acesse o sistema em `http://localhost:8000/`

## API's

A aplicação conta com uma página Swagger (documentação da API) para consultar, a URL para consultar o Swagger da sua aplicação é `/swagger/`.

![Swagger](./readme/image/swagger.png)

### Empregados

- Listar empregados: `GET /api/v1/employees/`
  > O retorno da lista é paginada, você pode passar offset para o número da página e limit para limitar o número de retorno na lista (exemplo: `/api/v1/employees?limit=10&offset=0`)
- Criar empregado: `POST /api/v1/employees/`
  > Exemplo de JSON para criar um empregado: `{"name": "Empregado 1", "email": "empregado@gmail.com", "department": 1}`
- Editar empregado: `PUT /api/v1/employees/{id}/`
- Remover empregado: `DELETE /api/v1/employees/{id}/`

### Departamentos

- Listar departamentos: `GET /api/v1/departments/`
  > O retorno da lista é paginada, você pode passar offset para o número da página e limit para limitar o número de retorno na lista (exemplo: `/api/v1/employees?limit=10&offset=0`)
- Criar departamento: `POST /api/v1/departments/`
  > Exemplo de JSON para criar um departamento: `{"name": "Departamento 1", "description": "Descrição do departamento 1"}`
- Editar departamento: `PUT /api/v1/departments/{id}/`
- Remover departamento: `DELETE /api/v1/departments/{id}/`

### Login (opcional)

- Login: `POST /api-auth/login/`
- Logout: `POST /api-auth/logout/`

### Testes automatizados

Os testes presentes no sistema são simples: testam cada operação do CRUD (deletar, criar, listar e atualizar) para as API's dos departamentos e dos empregados. Também é feito pequenos testes com offset e limit para garantir que a paginação está funcionando corretamente.

### Docker

Foi adicionado o Dockerfile para facilitar a execução do projeto, para executar o projeto com o Docker, basta executar os seguintes comandos:
`docker build -t ocker build -t employee_service -f ./Dockerfile .`
`docker compose up -d`

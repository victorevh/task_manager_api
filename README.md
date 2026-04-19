# Task Manager API

API de gerenciamento de tarefas com usuários e projetos, construída com **FastAPI**, **SQLAlchemy**, **Alembic**, **PostgreSQL** e **Docker**.

---

# Tecnologias

* FastAPI
* SQLAlchemy
* Alembic (migrations)
* PostgreSQL
* Docker

---

# Pré-requisitos

Antes de começar, você precisa ter instalado:

* Docker + Docker Compose
* Python 3.11+ (opcional, para desenvolvimento local)

---

# Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=tasks

DATABASE_URL=postgresql://postgres:password@postgres:5432/tasks
```

---

# Rodando com Docker (RECOMENDADO)

## Subir o projeto

```bash
docker compose up --build
```

---

## Acessar a API

* API: http://localhost:8000
* Swagger: http://localhost:8000/docs

---

## Parar o projeto

```bash
CTRL + C
```

ou:

```bash
docker compose down
```

---

# Ambiente virtual (opcional - desenvolvimento local)

## Criar ambiente virtual

Windows (PowerShell):

```bash
py -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

---

## Ativar ambiente virtual

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Migrations (Alembic)

## Criar nova migration

```bash
alembic revision --autogenerate -m "descricao"
```

---

## Aplicar migrations

```bash
alembic upgrade head
```

---

## Reverter migration

```bash
alembic downgrade -1
```

---


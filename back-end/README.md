# Back-end - API REST

API construída com **FastAPI** para o Sistema de Gestão de Perdas no Varejo.

# Atenção
Isso é apenas a estrura inicial do back-end, não está completo.

## Pré-requisitos

- Python 3.13+
- pip

## Instalação

```bash
cd back-end
python -m venv .venv
.venv\Scripts\activate     # Windows
pip install fastapi uvicorn sqlalchemy
```

## Executar

```bash
uvicorn main:app --reload --port 80
```

A API estará disponível em `http://localhost:80`.

## Estrutura

```
back-end/
├── main.py              # Ponto de entrada, registra as rotas na aplicação
├── database.py          # Configuração do banco (SQLite + SQLAlchemy)
├── .gitignore           # Arquivos ignorados pelo Git
├── .venv/               # Ambiente virtual Python
├── models/
│   ├── __init__.py      # Exporta os modelos
│   └── schema.py        # Definição das tabelas do banco
└── routes/
    ├── __init__.py      # Exporta as rotas
    ├── home.py          # GET /        → Página inicial
    ├── login.py         # POST /login  → Autenticação
    ├── singup.py        # POST /singup → Cadastro de usuários
    ├── help.py          # GET /help    → Ajuda
    ├── products.py      # POST /products → Produtos
    ├── stocks.py        # POST /stocks   → Estoque
    ├── logs.py          # GET /logs    → Logs do sistema
    └── ai.py            # GET /ai      → Serviço de IA
```

## Rotas Disponíveis

| Método | Rota        | Arquivo       | Descrição               |
|--------|-------------|---------------|-------------------------|
| GET    | `/`         | `home.py`     | Página inicial           |
| POST   | `/login`    | `login.py`    | Autenticação de usuário  |
| POST   | `/singup`   | `singup.py`   | Cadastro de usuário      |
| GET    | `/help`     | `help.py`     | Página de ajuda          |
| POST   | `/products` | `products.py` | Gestão de produtos       |
| POST   | `/stocks`   | `stocks.py`   | Gestão de estoque        |
| GET    | `/logs`     | `logs.py`     | Logs de auditoria        |
| GET    | `/ai`       | `ai.py`       | Serviço de IA            |

## Tecnologias

- **FastAPI** — Framework web assíncrono
- **SQLAlchemy** — ORM para banco de dados
- **SQLite** — Banco de dados relacional
- **Uvicorn** — Servidor ASGI
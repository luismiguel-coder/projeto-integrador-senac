# Importando a classe FastAPI para criar a aplicação
from fastapi import FastAPI
# Importando o database para criar as tabelas no banco
import database
# Importando os models para que o SQLAlchemy reconheça as tabelas
from models import schema
# Importando o uvicorn para executar a aplicação
import uvicorn
# Importando os módulos de rotas (home, login, singup, help)
from routes import home, login, singup, help, ai, stocks, products

# Criando a instância da aplicação FastAPI com título e versão
app = FastAPI(title="API Projeto Integrador", version="1.0.0")

# Adicionando a rota da página inicial
app.include_router(home.router)
# Adicionando a rota de login
app.include_router(login.router)
# Adicionando a rota de cadastro (signup)
app.include_router(singup.router)
# Adicionando a rota de ajuda (help)
app.include_router(help.router)
# Adicionando a rota de IA
app.include_router(ai.router)
# Adicionando a rota de estoque
app.include_router(stocks.router)
# Adicionando a rota de produtos
app.include_router(products.router)

# Executando a aplicação
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

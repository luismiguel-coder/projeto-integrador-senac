# Importando o database para criar as tabelas no banco
import database
# Importando o uvicorn para executar a aplicação
import uvicorn
# Importando a classe FastAPI para criar a aplicação
from fastapi import FastAPI
# Importando os models para que o SQLAlchemy reconheça as tabelas
from models import modelProjetoIntegrador
# Importando os módulos de rotas (home, login, singup, help)
from routes import routerHome, routerLogin, routerSingup, routerHelp, routerAI, routerStocks, routerProducts
    
# Criando a instância da aplicação FastAPI com título e versão
app = FastAPI(title="API Projeto Integrador", version="1.0.0")

# Adicionando a rota da página inicial
app.include_router(routerHome)
# Adicionando a rota de login
app.include_router(routerLogin)
# Adicionando a rota de cadastro (signup)
app.include_router(routerSingup)
# Adicionando a rota de ajuda (help)
app.include_router(routerHelp)
# Adicionando a rota de IA
app.include_router(routerAI)
# Adicionando a rota de estoque
app.include_router(routerStocks)
# Adicionando a rota de produtos
app.include_router(routerProducts)

# Executando a aplicação
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

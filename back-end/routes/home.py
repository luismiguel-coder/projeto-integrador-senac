# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota GET para a página inicial
@router.get("/")
def home():
    # Retornando uma mensagem de boas-vindas
    return {"message": "Pagina inicial em construção"}

# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota GET para a página de ajuda
@router.get("/help")
def help():
    # Retornando uma mensagem de ajuda (por enquanto mock)
    return {"message": "Pagina de ajuda em construção"}

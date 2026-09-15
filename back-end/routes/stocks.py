# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota POST para estoque
@router.post("/stocks")
def stocks():
    # Retornando uma mensagem (por enquanto mock)
    return {"message": "Pagina de estoque em construção"}

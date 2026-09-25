# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota POST para produtos
@router.post("/products")
def produtos():
    # Retornando uma mensagem de produtos (por enquanto mock)
    return {"message": "Pagina de produtos em construção"}

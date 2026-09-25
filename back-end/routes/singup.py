# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota POST para cadastro (singup)
@router.post("/singup")
def singup():
    # Retornando uma mensagem de cadastro (por enquanto mock)
    return {"message": "Pagina de cadastro em construção"}

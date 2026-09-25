# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota POST para login
@router.post("/login")
def login():
    # Retornando uma mensagem de login (por enquanto mock)
    return {"message": "Pagina de login em construção"}

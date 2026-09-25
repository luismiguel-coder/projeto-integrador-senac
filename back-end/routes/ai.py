# Importando o APIRouter para criar rotas
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota GET para o serviço de IA
@router.get("/ai")
def ai():
    # Retornando uma mensagem de IA (por enquanto mock)
    return {"message": "Pagina de IA em construção"}

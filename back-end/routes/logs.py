# Logs de todo o sistema 100% auditável
from fastapi import APIRouter

# Criando a instância do router
router = APIRouter()

# Definindo a rota GET para os logs do sistema
@router.get("/logs")
def logs():
    # Retornando uma mensagem de logs (por enquanto mock)
    return {"message": "Pagina de logs em construção"}

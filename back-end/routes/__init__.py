# Importando todos os módulos de rotas
from .home import router as routerHome
from .login import router as routerLogin
from .singup import router as routerSingup
from .help import router as routerHelp
from .ai import router as routerAI
from .stocks import router as routerStocks
from .products import router as routerProducts

# Definindo quais módulos são exportados
__all__ = ["routerHome", "routerLogin", "routerSingup", "routerHelp", "routerAI", "routerStocks", "routerProducts"]

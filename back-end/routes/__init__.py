# Importando todos os módulos de rotas
from . import home
from . import login
from . import singup
from . import help
from . import ai
from . import stocks
from . import products

# Definindo quais módulos são exportados
__all__ = ["home", "login", "singup", "help", "ai", "stocks", "products"]

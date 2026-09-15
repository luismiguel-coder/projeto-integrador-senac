# Importando os tipos de colunas do SQLAlchemy
from sqlalchemy import Column, Integer, String
# Importando a classe Base do database
from database import Base


# Definindo o modelo Projeto_Integrador (tabela Projeto_Integrador)
class Projeto_Integrador(Base):
    # Nome da tabela no banco de dados
    __tablename__ = "Projeto_Integrador"

    # Coluna ID (chave primária, auto-incremento é padrão)
    id = Column(Integer, primary_key=True, index=True)

    # Coluna nome (obrigatória)
    nome = Column(String, nullable=False)

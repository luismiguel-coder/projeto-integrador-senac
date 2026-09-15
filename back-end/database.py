# Importando create_engine para criar a conexão com o banco de dados
from sqlalchemy import create_engine
# Importando declarative_base para criar a classe Base dos modelos
from sqlalchemy.ext.declarative import declarative_base
# Importando sessionmaker para criar as sessões do banco
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco SQLite (arquivo database.db)
DATABASE_URL = "sqlite:///database.db"

# Criando o engine de conexão com o banco
engine = create_engine(DATABASE_URL)

# Configurando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando a classe Base para os modelos herdarem
Base = declarative_base()


# Função para obter uma sessão do banco (dependência do FastAPI)
def get_db():
    # Criando uma nova sessão
    db = SessionLocal()
    try:
        # Retornando a sessão para usar na rota
        yield db
    finally:
        # Fechando a sessão após o uso
        db.close()


# Criando todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

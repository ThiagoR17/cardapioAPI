from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/BDcard"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def testar_conexao():
    try:
        # Criar uma instância da sessão
        session = SessionLocal()

        # Executar uma consulta simples para testar a conexão
        query = text("SELECT 1 ")
        result = session.execute(query)

        # Verificar se a conexão foi bem-sucedida
        if result.scalar() == 1:
            print("Conexão bem-sucedida!")
        else:
            print("Erro ao testar a conexão.")

        # Fechar a sessão
        session.close()

    except Exception as e:
        print("Erro ao conectar ao banco de dados:", str(e))

# Chamar a função de teste de conexão
testar_conexao()
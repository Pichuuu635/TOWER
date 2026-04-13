import psycopg2


URL_BANCO = "postgresql://neondb_owner:npg_ZaCb6qALfX5c@ep-wispy-frog-amleq76q.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    try:
        conn = psycopg2.connect(URL_BANCO)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None


if __name__ == "__main__":
    conexao = get_connection()
    if conexao:
        print("✅ Sucesso! O Python conectou no banco da nuvem.")
        conexao.close()

def criar_tabelas():
    conexao = get_connection()
    if conexao:
        cursor = conexao.cursor()
        # Comando SQL para criar a tabela de usuários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                login TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            );
        """)
        conexao.commit() # Salva a alteração no banco
        print("✅ Tabela 'usuarios' verificada/criada com sucesso!")
        cursor.close()
        conexao.close()

# Chame a função para testar
if __name__ == "__main__":
    criar_tabelas()

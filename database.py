from connections import conectar

def criar_tabelas():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(open("create_tables.sql", "r").read())
        conn.commit()
    except Exception as e:
        print(f'Não foi possivel criar as tabelas: {e}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()



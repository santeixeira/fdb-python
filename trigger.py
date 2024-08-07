from connections import conectar

def criar_trigger():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(open("trigger.sql", "r").read())
        conn.commit()
        print("Trigger criado com sucesso.")
    except Exception as e:
        print(f"Erro durante as operações: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        
criar_trigger()

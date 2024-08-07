from connections import conectar

def executar_procedure():
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute(open("procedure.sql", "r").read())
        print(f'Procedure criada com sucesso!')
        conn.commit()
        cur.execute("SELECT * FROM empregado_do_mes ('2023-10-01');")
        print(f"Funcionario {cur.fetchone()[1]} é o funcionario do mês" )
    except Exception as e:
        print(f'Erro ao executar a procedure: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

executar_procedure()
from connections import conectar

def executar_query(sql, params=None, commit=True):
    conn = conectar()
    cur = conn.cursor()

    try:
        if params:
            cur.execute(sql, params)
        else:
            cur.execute(sql)

        if commit:
            conn.commit()

    except Exception as e:
        print(f"Erro na query: {e}")
        conn.rollback()

    finally:
        cur.close()
        conn.close()

def inserir_embarcacao(embarcacao):
    sql =   """
            INSERT INTO embarcacoes (id_emb, nome, tipo) VALUES
                (%s, %s, %s)
            """
    executar_query(sql, embarcacao)

def inserir_empregados(empregado):
    sql =   """ 
            INSERT INTO empregados (id_emp, nome, data_nasc, funcao) VALUES
                (%s, %s, %s, %s)
            """
    executar_query(sql, empregado)

def inserir_tripulante(tripulante):
    sql_tripulante = """
        INSERT INTO tripulantes (id_trp, nome, data_nasc, funcao, id_emb) 
        VALUES (%s, %s, %s, %s, %s)
    """
    executar_query(sql_tripulante, tripulante)

def inserir_movimentacoes(movimentacao):
    sql = """
        INSERT INTO movimentacao (id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)
    """
    executar_query(sql, movimentacao)

def atribuir_empregado_movimentacao(empregado_movimentacao):
    sql = """
        INSERT INTO movimentacao_empregados (id_mov, id_emp) VALUES (%s, %s)
    """
    executar_query(sql, empregado_movimentacao)


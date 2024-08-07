from connections import conectar

def executar_sql(sql, params=None, fetch=False):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(sql, params)
        conn.commit()
        if fetch:
            return cursor.fetchall()
    except Exception as e:
        print(f"Erro na execução do SQL: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def inserir_nova_movimentacao(nova_movimentacao):
    sql_movimentacao = """
                        INSERT INTO movimentacao (id_mov, data, tipo, id_emb) VALUES
                        (%s, %s, %s, %s);
                        """
    executar_sql(sql_movimentacao, nova_movimentacao)

def inserir_nova_movimentacao_empregado(nova_movimentacao_empregado):
    sql_movimentacao_empregado = """
                                    INSERT INTO movimentacao_empregados (id_mov, id_emp) VALUES
                                        (%s, %s);
                                """
    executar_sql(sql_movimentacao_empregado, nova_movimentacao_empregado)

def retornar_quantidade_movimentacoes_cargueiro():
    sql_contagem_cargueiro = """
                                SELECT
                                    COUNT (mov.id_mov) AS num_mov
                                FROM
                                    movimentacao mov
                                WHERE mov.id_emb IN (SELECT emb.id_emb
                                                    FROM embarcacoes emb
                                                    WHERE emb.tipo = 'Cargueiro');
                            """
    resultado = executar_sql(sql_contagem_cargueiro, fetch=True)
    if resultado:
        print(f"Quantidade de Movimentações envolvendo Cargueiros: {resultado[0][0]}")


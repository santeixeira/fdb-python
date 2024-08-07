from connections import conectar

def consultar_embarcacoes_tripulantes():
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = """
            SELECT
                emb.id_emb,
                emb.nome AS nome_embarcacao,
                emb.tipo,
                COUNT (trp.id_trp) AS num_tripulantes
            FROM
                embarcacoes emb
            LEFT JOIN
                tripulantes trp ON emb.id_emb = trp.id_emb
            GROUP BY
                emb.id_emb, emb.nome, emb.tipo;
        """
        cursor.execute(sql)
        result = cursor.fetchall()

        for row in result:
            print(f"Embarcação ID: {row[0]}, Nome: {row[1]}, Número de Tripulantes: {row[2]}")

    except Exception as e:
        print(f"Erro ao consultar embarcações e tripulantes: {e}")

    finally:
        cursor.close()
        conn.close()

def consultar_empregados_movimentacao(movimentacao_id):
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = """
                SELECT *
                FROM
                    empregados emp
                WHERE emp.id_emp IN (SELECT me.id_emp
                                    FROM movimentacao_empregados me
                                    WHERE me.id_mov = %s);
                """
        cursor.execute(sql, (movimentacao_id,))
        result = cursor.fetchall()

        for row in result:
            print(f"Empregado Envolvido: {row[0]}")

    except Exception as e:
        print(f"Erro ao consultar empregados na movimentação: {e}")

    finally:
        cursor.close()
        conn.close()


def contar_movimentacoes_cargueiro():
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = """
                SELECT
                    COUNT (mov.id_mov) AS num_mov
                FROM
                    movimentacao mov
                WHERE mov.id_emb IN (SELECT emb.id_emb
                                    FROM embarcacoes emb
                                    WHERE emb.tipo = 'Cargueiro');
                """
        cursor.execute(sql)
        result = cursor.fetchone()

        print(f"Quantidade de Movimentações envolvendo Cargueiros: {result[0]}")

    except Exception as e:
        print(f"Erro ao contar movimentações de cargueiros: {e}")

    finally:
        cursor.close()
        conn.close()


opcao = input("Escolha a opção de consulta:\n1. Embarcações e Tripulantes\n2. Empregados em Movimentação\n3. Contar Movimentações de Cargueiros\n")
if opcao == '1':
    consultar_embarcacoes_tripulantes()
elif opcao == '2':
    movimentacao_id = input("Digite o ID da movimentação: ")
    consultar_empregados_movimentacao(movimentacao_id)
elif opcao == '3':
    contar_movimentacoes_cargueiro()
else:
    print("Opção inválida.")

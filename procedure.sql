DROP FUNCTION IF EXISTS empregado_do_mes (DATE);

CREATE OR REPLACE FUNCTION empregado_do_mes (data_ref DATE)
RETURNS TABLE (id_emp INT, emp_nome VARCHAR(50))
AS $$
BEGIN
	RETURN QUERY
	SELECT emp.id_emp, emp.nome
	FROM empregados emp
	WHERE emp.id_emp = (SELECT me.id_emp
					    FROM movimentacao_empregados me
					    WHERE me.id_mov IN (SELECT mov.id_mov
										    FROM movimentacao mov
										    WHERE EXTRACT(YEAR FROM data_ref) = EXTRACT(YEAR FROM mov.data)
										    AND EXTRACT(MONTH FROM data_ref) = EXTRACT(MONTH FROM mov.data))
					    GROUP BY me.id_emp
					    ORDER BY COUNT(*) DESC
					    LIMIT 1);
END;
$$ LANGUAGE plpgsql;
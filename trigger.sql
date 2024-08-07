CREATE OR REPLACE FUNCTION check_capitao ()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.funcao = 'Capitão' AND 'Capitao' IN (SELECT trp.funcao
								  				FROM tripulantes trp
								  				WHERE NEW.id_trp != trp.id_trp AND NEW.id_emb = trp.id_emb)
	THEN
		RAISE EXCEPTION 'Já existe capetão na embarcação';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER check_capitao_trigger BEFORE INSERT OR UPDATE ON tripulantes
FOR EACH ROW
EXECUTE FUNCTION check_capitao();

CREATE OR REPLACE FUNCTION check_manutencao ()
RETURNS TRIGGER AS
$$
BEGIN
	IF NEW.id_mov IN (SELECT mov.id_mov
					  FROM movimentacao mov
					  WHERE mov.tipo = 'Manutenção')
	AND NEW.id_emp NOT IN (SELECT emp.id_emp
					  FROM empregados emp
					  WHERE emp.funcao = 'Manutenção')
		THEN RAISE EXCEPTION 'Empregado não pode ser encarregado';
	END IF;
	RETURN NEW;
END;	
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER check_manutencao_trigger
BEFORE INSERT OR UPDATE ON movimentacao_empregados
FOR EACH ROW
EXECUTE FUNCTION check_manutencao();



DROP TABLE IF EXISTS embarcacoes CASCADE;
DROP TABLE IF EXISTS tripulantes CASCADE;
DROP TABLE IF EXISTS empregados CASCADE;
DROP TABLE IF EXISTS movimentacao CASCADE;
DROP TABLE IF EXISTS movimentacao_empregados CASCADE;

CREATE TABLE embarcacoes (
	id_emb INT,
	nome VARCHAR (30),
	tipo VARCHAR (30),
	PRIMARY KEY (id_emb)
);

CREATE TABLE tripulantes (
	id_trp INT,
	nome VARCHAR (50),
	data_nasc DATE,
	funcao VARCHAR (50),
	id_emb INT,
	PRIMARY KEY (id_trp),
	FOREIGN KEY (id_emb) REFERENCES embarcacoes (id_emb)
						 ON DELETE CASCADE
);

CREATE TABLE empregados (
	id_emp INT,
	nome VARCHAR (50),
	data_nasc DATE,
	funcao VARCHAR (50),
	PRIMARY KEY (id_emp)
);

CREATE TABLE movimentacao (
	id_mov INT,
	data DATE,
	tipo VARCHAR (50),
	id_emb INT,
	PRIMARY KEY (id_mov),
	FOREIGN KEY (id_emb) REFERENCES embarcacoes (id_emb)
						 ON DELETE CASCADE
);

CREATE TABLE movimentacao_empregados (
	id_mov INT,
	id_emp INT,
	FOREIGN KEY (id_mov) REFERENCES movimentacao (id_mov)
	                     ON DELETE CASCADE,
	FOREIGN KEY (id_emp) REFERENCES empregados (id_emp)
						 ON DELETE CASCADE
);
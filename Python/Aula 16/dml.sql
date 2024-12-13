-- DQL (Consultar Dados)
USE hospital;
SELECT * FROM pacientes;

SELECT id, nome, ativo
FROM pacientes;

-- DML (Inserir, Atualizar e Excluir Dados)

-- Insert
INSERT INTO pacientes (nome, cpf, data_nascimento)
VALUES ('Mateo', '00022233344', '1997-08-02');

INSERT INTO pacientes (nome, cpf, data_nascimento, ativo)
VALUES ('João', '11122233366', '1990-02-12', TRUE),
		('Vilmar', '11122233322', '1951-10-03', FALSE);

-- Ao Iniciar uma Transação, você pode persistir ou desfazer
START TRANSACTION;

-- Para desfazer, execute rollback.
ROLLBACK;

-- Para persistir, execute o commit.
COMMIT;

-- Update
UPDATE pacientes
SET nome = 'Pedro', ativo = FALSE
WHERE id = 1;

-- Delete
DELETE FROM pacientes
WHERE id = 1;


SELECT id, nome, crm, ativo, data_nascimento
FROM medicos
WHERE YEAR(data_nascimento) BETWEEN 1981 AND 2004;

-- Ex01
INSERT INTO medicos (nome, crm, data_nascimento)
VALUES ('Fabiano', '12345MG', '1990-10-02'),
		('Carlos', '12345PE', '1980-01-02');

-- Ex02
INSERT INTO medicos (nome, crm, data_nascimento, ativo)
VALUES ('Pedro', '12345CE', '1982-05-02', FALSE);

-- Ex03
UPDATE medicos
SET crm = '00000BA'
WHERE id = 2;

-- Ex04
DELETE FROM medicos
WHERE crm = '12345CE';

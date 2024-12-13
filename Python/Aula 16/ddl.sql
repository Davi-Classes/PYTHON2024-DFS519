-- DDL (Criando Tabelas e Banco de Dados)
-- Criando Banco de Dados
CREATE DATABASE hospital;
USE hospital;

-- Excluindo Banco de Dados
-- DROP DATABASE hospital;

-- Criando uma Tabela
CREATE TABLE pacientes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    ativo BOOL NOT NULL DEFAULT TRUE
);

CREATE TABLE medicos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    crm VARCHAR(8) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    ativo BOOL NOT NULL DEFAULT TRUE
);

ALTER TABLE medicos
MODIFY ativo BOOL NOT NULL DEFAULT TRUE;

-- Excluir uma Tabela
-- DROP TABLE medicos;

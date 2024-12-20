-- Active: 1733343726916@@127.0.0.1@3306@

DROP DATABASE IF EXISTS dbpython;

CREATE DATABASE dbpython;

CREATE TABLE dbpython.contatos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(255)
) ENGINE = InnoDB;
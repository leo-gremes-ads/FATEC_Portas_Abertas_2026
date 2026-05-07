DROP DATABASE IF EXISTS Portas_Abertas;

CREATE DATABASE Portas_Abertas;

USE Portas_Abertas;

CREATE TABLE IF NOT EXISTS Visitantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    escolaridade VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Interesses (    
    visitante_id INT NOT NULL,
    interesse VARCHAR(50) NOT NULL,
    PRIMARY KEY(visitante_id, interesse),
    FOREIGN KEY(visitante_id) REFERENCES Visitantes(id)
);


DROP TABLE IF EXISTS Mensagens;

CREATE TABLE Mensagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensagem VARCHAR(1024) NOT NULL
);
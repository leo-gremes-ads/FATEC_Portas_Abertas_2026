CREATE DATABASE IF NOT EXISTS Portas_Abertas;

USE Portas_Abertas;

CREATE TABLE IF NOT EXISTS Visitantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    escolaridade VARCHAR(100) NOT NULL,
    interesse VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS Mensagens;

CREATE TABLE Mensagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensagem VARCHAR(1024) NOT NULL
);

INSERT INTO Mensagens(mensagem) VALUES
('Quem não arrisca, não petisca.'),
('Deus ajuda quem cedo madruga.'),
('Água mole em pedra dura, tanto bate até que fura.'),
('Mais vale um pássaro na mão do que dois voando.'),
('Em casa de ferreiro, espeto de pau.'),
('Antes tarde do que nunca.'),
('Quem espera sempre alcança.'),
('Cada macaco no seu galho.'),
('Quem com ferro fere, com ferro será ferido.'),
('A pressa é inimiga da perfeição.'),
('Quem ri por último, ri melhor.'),
('Quem tudo quer, nada tem.'),
('O barato sai caro.'),
('Pau que nasce torto nunca se endireita.'),
('A união faz a força.'),
('Quem não chora, não mama.'),
('Santo de casa não faz milagre.'),
('Quem cala, consente.'),
('Diga-me com quem andas e te direi quem és.'),
('Casa de ferreiro, espeto de pau.'),
('Quem semeia vento, colhe tempestade.'),
('De grão em grão, a galinha enche o papo.'),
('Quem tem boca vai a Roma.'),
('Não deixe para amanhã o que pode fazer hoje.'),
('Quem vê cara não vê coração.'),
('Em briga de marido e mulher, ninguém mete a colher.'),
('Gato escaldado tem medo de água fria.'),
('Farinha pouca, meu pirão primeiro.'),
('Cada um colhe o que planta.'),
('O seguro morreu de velho.');
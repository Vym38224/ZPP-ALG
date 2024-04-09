CREATE TABLE Pacienti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    krestni_jmeno VARCHAR(50),
    prijmeni VARCHAR(50),
    rodne_cislo VARCHAR(11) UNIQUE,
    email VARCHAR(100) DEFAULT 'Není registrován',
    telefon VARCHAR(20) DEFAULT '',
    registrovany VARCHAR(3) DEFAULT 'ne' CHECK (registrovany IN ('ano', 'ne')),
    datum_registrace DEFAULT ''
);

-- Vložení záznamů
INSERT INTO Pacienti (krestni_jmeno, prijmeni, rodne_cislo, email, telefon, registrovany, datum_registrace) VALUES
('Tomáš', 'Marný', '800101/1234', 'tomas@marny.cz', '777545890', DEFAULT, '2020-03-28'),
('Marek', 'Procházka', '851026/1234', 'marek@prochazka.cz', '604585375', DEFAULT, '2017-07-19'),
('Tomáš', 'Pospíšil', '935511/6789', DEFAULT, DEFAULT, DEFAULT, DEFAULT),
('Adéla', 'Nováková', '840212/9876', 'adela@novakova.cz', '585321670', DEFAULT, '2019-01-07'),
('Matyáš', 'Havelka', '970922/5544', DEFAULT, DEFAULT, DEFAULT, DEFAULT),
('Barbora', 'Navrátilová', '861201/0099', 'barbora@navratilova.cz', '602555999', DEFAULT, '2018-12-13'),
('Veronika', 'Vlková', '800101/1234', 'veronika@vlkova.cz', '908987654', DEFAULT, '2019-01-07');


-- A: Zobrazte všechna křestní jména tak, aby se neopakovala.
SELECT DISTINCT krestni_jmeno FROM Pacienti;

-- B: Zobrazte všechna celá jména ve formátu "jmeno prijmeni" pojmenované cela_jmena.
SELECT krestni_jmeno || ' ' || prijmeni AS cela_jmena FROM Pacienti;

-- C: Zobrazte všechny registrované pacienty seřazené podle jejich data registrace od nejstarších.
SELECT * FROM Pacienti WHERE registrovany = 'ano' ORDER BY datum_registrace;

-- D: Zobrazte všechny pacienty, jejichž příjmení obsahuje podřetězec 'ov' nebo 'av'.
SELECT * FROM Pacienti WHERE prijmeni LIKE '%ov%' OR prijmeni LIKE '%av%';

-- E: Zobrazte všechny pacienty, kteří byli registrováni před 1. lednem 2020.
SELECT * FROM Pacienti WHERE registrovany = 'ano' AND datum_registrace < '2020-01-01';

-- F: Zobrazte všechny pacienty, kteří byli registrováni mezi 1. lednem 2019 a 31. prosincem 2020.
SELECT * FROM Pacienti WHERE registrovany = 'ano' AND datum_registrace BETWEEN '2019-01-01' AND '2020-12-31';

-- G: Zobrazte číslo (pocet_registrovanych) kolik pacientů je registrovaných.
SELECT COUNT(*) AS pocet_registrovanych FROM Pacienti WHERE registrovany = 'ano';

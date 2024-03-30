-- Vytvoření tabulky Pacienti
CREATE TABLE Pacienti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    krestni_jmeno VARCHAR(50),
    prijmeni VARCHAR(50),
    datum_registrace DATE
);

-- Vložení záznamů
INSERT INTO Pacienti (krestni_jmeno, prijmeni, datum_registrace) VALUES
('Jan', 'Novak', '2018-12-15'),
('Petr', 'Svoboda', '2019-02-20'),
('Marie', 'Novotna', '2020-03-10'),
('Jana', 'Kovarova', '2019-11-05'),
('Josef', 'Vesely', '2021-01-05'),
('Eva', 'Horakova', '2018-08-20');

-- 1: Zobrazte všechna křestní jména tak, aby se neopakovala.
SELECT DISTINCT krestni_jmeno FROM Pacienti;

-- 2: Zobrazte všechna celá jména ve formátu "jmeno prijmeni" pojmenované cela_jmena.
SELECT krestni_jmeno || ' ' || prijmeni AS cela_jmena FROM Pacienti;

-- 3: Zobrazte všechny registrované pacienty seřazené podle jejich data registrace od nejstarších.
SELECT * FROM Pacienti ORDER BY datum_registrace;

-- 4: Zobrazte všechny pacienty, jejichž příjmení obsahuje podřetězec 'ov' nebo 'av'.
SELECT * FROM Pacienti WHERE prijmeni LIKE '%ov%' OR prijmeni LIKE '%av%';

-- 5: Zobrazte všechny pacienty, kteří byli registrováni před 1. lednem 2020.
SELECT * FROM Pacienti WHERE datum_registrace < '2020-01-01';

-- 6: Zobrazte všechny pacienty, kteří byli registrováni mezi 1. lednem 2019 a 31. prosincem 2020.
SELECT * FROM Pacienti WHERE datum_registrace BETWEEN '2019-01-01' AND '2020-12-31';

-- 7: Zobrazte číslo (pocet_registrovanych) kolik pacientů je registrovaných.
SELECT COUNT(*) AS pocet_registrovanych FROM Pacienti;
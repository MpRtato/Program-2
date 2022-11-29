#Arts Inarts Kubilis

#TABULU IZVEIDE
CREATE TABLE Pasutitajs(
  Pasutitaja_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Vards varchar(30) NOT NULL,
  Uzvards varchar(30) NOT NULL,
  Personas_kods  varchar(12) NOT NULL,
  Epasts varchar(50),
  Telefona_nr varchar(16),
  Adrese varchar(100) NOT NULL,
  Pasta_indekss varchar(7) NOT NULL,
  Bankas_konts varchar(20) NOT NULL,

  UNIQUE(Personas_kods),
  UNIQUE(Bankas_konts)
);

CREATE TABLE Produkcija(
  Produkta_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Produkta_nosaukums varchar(100) NOT NULL,
  Produkta_veids varchar(40) NOT NULL,
  Cena float NOT NULL,
  Atlaide int,
  Skaits_noliktava int NOT NULL,

  UNIQUE(Produkta_nosaukums)
);

CREATE TABLE Darba_grafiks(
  Darba_grafika_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Sakums time NOT NULL,
  Beigas time NOT NULL,
  Dienas_nedela int NOT NULL
);

CREATE TABLE Darbinieki(
  Darbinieka_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Vards varchar(30) NOT NULL,
  Uzvards varchar(30) NOT NULL,
  Dzimums varchar(10) NOT NULL,
  Vecums int NOT NULL,
  Personas_kods  varchar(12) NOT NULL,
  Telefona_nr varchar(16) NOT NULL,
  Amats varchar(100) NOT NULL,
  Darba_grafika_ID int,
  Alga float NOT NULL,
  Bankas_konts varchar(20) NOT NULL,

  FOREIGN KEY(Darba_grafika_ID) REFERENCES Darba_grafiks(Darba_grafika_ID),

  UNIQUE(Personas_kods),
  UNIQUE(Bankas_konts)
);

CREATE TABLE Pasutijums(
  Pasutijuma_ID int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  Pasutitaja_ID int,
  Darbinieka_ID int,
  Sanemsanas_veids varchar(10) NOT NULL,
  Piegades_status varchar(14),
  Pasutisanas_laiks datetime,

  FOREIGN KEY(Pasutitaja_ID) REFERENCES Pasutitajs(Pasutitaja_ID),
  FOREIGN KEY(Darbinieka_ID) REFERENCES Darbinieki(Darbinieka_ID)
);

CREATE TABLE Pasutijums_Produkcija( #Starp tabula
  Pasutijuma_ID int,
  Produkta_ID int,

  FOREIGN KEY(Pasutijuma_ID) REFERENCES Pasutijums(Pasutijuma_ID),
  FOREIGN KEY(Produkta_ID) REFERENCES Produkcija(Produkta_ID)
);


#DATU IEVADE

#pasutitaju datu ievade
INSERT INTO Pasutitajs(Vards, Uzvards, Personas_kods, Epasts, Telefona_nr, Adrese, Pasta_indekss, Bankas_konts)
VALUES('Zinta', 'Mezecka', '010663-24029', 'Magonite187@gmail.com', '+37029627256', 'Latvija, Riga, Abrenes iela 11-5', 'LV-1003', 'LT225488766936844966');
INSERT INTO Pasutitajs(Vards, Uzvards, Personas_kods, Epasts, Telefona_nr, Adrese, Pasta_indekss, Bankas_konts)
VALUES('Magnuss', 'Jaunzems', '231178-15239', 'LIELAISmagnuss@inbox.lv','+37127783173', 'Latvija, Rezekne, Celtnieku iela 5', 'LV-4601', 'LV952381268213227251');
INSERT INTO Pasutitajs(Vards, Uzvards, Personas_kods, Epasts, Adrese, Pasta_indekss, Bankas_konts)
VALUES('Vairis', 'Sīmanis', '050996-16010', 'PesSerRisSpl@inbox.lv', 'Daugavpils, Oficieru iela 3', 'LV-5401', 'LV222758515533334588');

#produkcijas datu ievade
INSERT INTO Produkcija(Produkta_nosaukums, Produkta_veids, Cena, Atlaide, Skaits_noliktava)
VALUES('Melojosais spoguli 4x20.56, roza polimera', 'Spogulis', 29.99, 5, 1000);
INSERT INTO Produkcija(Produkta_nosaukums, Produkta_veids, Cena, Skaits_noliktava)
VALUES('Negu mehaniskais nagu slipis 2.1mm', 'Nagu vile', 19.83, 5);
INSERT INTO Produkcija(Produkta_nosaukums, Produkta_veids, Cena, Atlaide, Skaits_noliktava)
VALUES('Burundi sejas sartinatajs', 'Skaistum kopsanas lidzeklis', 9.99, 20, 201);
INSERT INTO Produkcija(Produkta_nosaukums, Produkta_veids, Cena, Skaits_noliktava)
VALUES('100g naku lakas nonemejs no boshch', 'Skaistum kopsanas lidzeklis', 20.00, 201);
INSERT INTO Produkcija(Produkta_nosaukums, Produkta_veids, Cena, Skaits_noliktava)
VALUES('Matu krasa neizdevusas austrijas makslinieka gaume', 'Matu krasa', 8.43, 3);

#darba grafiku datu ievade
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '15:00', 7);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '16:00', 6);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '17:00', 5);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '18:00', 4);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '19:00', 3);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('09:00', '20:00', 2);
INSERT INTO Darba_grafiks(Sakums, Beigas, Dienas_nedela)
VALUES('12:00', '14:01', 1);

#darbinieku datu ievade
INSERT INTO Darbinieki(Vards, Uzvards, Dzimums, Vecums, Personas_kods, Telefona_nr, Amats, Darba_grafika_ID, Alga, Bankas_konts)
VALUES('Gvido', 'Udentins', 'Virietis', 32, '300361-14228', '+37120867931', 'Ipasnieks', 7, 4000.09, 'BU049873269894338716');
INSERT INTO Darbinieki(Vards, Uzvards, Dzimums, Vecums, Personas_kods, Telefona_nr, Amats, Darba_grafika_ID, Alga, Bankas_konts)
VALUES('Orests', 'Avens', 'Virietis', 21, '120972-18003', '+37125220873', 'Kravejs', 3, 600.00, 'LV205265527325499177');
INSERT INTO Darbinieki(Vards, Uzvards, Dzimums, Vecums, Personas_kods, Telefona_nr, Amats, Darba_grafika_ID, Alga, Bankas_konts)
VALUES('Judite', 'Muizniece', 'Sieviete', 40, '210870-12020', '+37126454983', 'Kasieris', 2, 800.00, 'LV085392232451965853');
INSERT INTO Darbinieki(Vards, Uzvards, Dzimums, Vecums, Personas_kods, Telefona_nr, Amats, Darba_grafika_ID, Alga, Bankas_konts)
VALUES('Agita', 'Enina', 'Sieviete', 30, '170899-14106', '+37129540306', 'Kurjers', 1, 1163.64, 'LV318962238134898211');
INSERT INTO Darbinieki(Vards, Uzvards, Dzimums, Vecums, Personas_kods, Telefona_nr, Amats, Darba_grafika_ID, Alga, Bankas_konts)
VALUES('Imants', 'Sudmalis', 'Virietis', 24, '070462-22018', '+37121008316', 'Kurjers', 1, 1365.32, 'LV207912868531455983');

#pasutijumu datu ievade
INSERT INTO Pasutijums(Pasutitaja_ID, Darbinieka_ID, Sanemsanas_veids)
VALUES(1, 3, 'Uz vietas');
INSERT INTO Pasutijums(Pasutitaja_ID, Darbinieka_ID, Sanemsanas_veids, Piegades_status, Pasutisanas_laiks)
VALUES(2, 4, 'Ar kurjeru', 'Cela', '2022-11-22 23:00:02');
INSERT INTO Pasutijums(Pasutitaja_ID, Darbinieka_ID, Sanemsanas_veids, Piegades_status, Pasutisanas_laiks)
VALUES(2, 4, 'Ar kurjeru', 'Salona', '2022-11-23 12:49:57');
INSERT INTO Pasutijums(Pasutitaja_ID, Darbinieka_ID, Sanemsanas_veids, Piegades_status, Pasutisanas_laiks)
VALUES(3, 5, 'Ar kurjeru', 'Piegadats', '2022-10-28 15:05:34');

#pasutijums_produkcija/pasutito precu datu ievade
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(1, 1);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(1, 3);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(1, 2);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(2, 4);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(2, 4);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(3, 1);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(4, 5);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(4, 5);
INSERT INTO Pasutijums_Produkcija(Pasutijuma_ID, Produkta_ID)
VALUES(4, 5);

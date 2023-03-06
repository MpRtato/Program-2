#Augu datubaze

#datubazes izveidosana un izvelesanas
CREATE DATABASE augudatubaze;

USE augudatubaze;

#datubazes tabulu un ailu izveidosana
CREATE TABLE augi(
  id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nosaukums varchar(200) NOT NULL,
  latiniskais_nosaukums varchar(200) NOT NULL,
  skirne varchar(200) NOT NULL,
  apraksts varchar(1000) NOT NULL,
  veids varchar(100) NOT NULL,
  augsanas_ilgums int NOT NULL,
  dzivesilgums varchar(20) NOT NULL,
  izturiba varchar(20) NOT NULL,
  saknu_dzilums int NOT NULL,
  stadisanas_menesis varchar(20) NOT NULL,
  minimala_temperatura int NOT NULL,
  laistisanas_biezums int NOT NULL,
  gaismas_vide varchar(20) NOT NULL,
  vide varchar(100) NOT NULL

);

CREATE TABLE atsauces(
  id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  atsauce varchar(1000) NOT NULL

);

CREATE TABLE augi_atsauce(
auga_id int,
atsauces_Id int,

FOREIGN KEY(auga_id) REFERENCES augi(id),
FOREIGN KEY(atsauces_id) REFERENCES atsauces(id)

);

#datu ievade
#augu tabula
INSERT INTO augi(nosaukums, latiniskais_nosaukums, skirne, apraksts, veids, augsanas_ilgums, dzivesilgums, izturiba, saknu_dzilums, stadisanas_menesis, minimala_temperatura, laistisanas_biezums, gaismas_vide, vide)
VALUES('Augstas_krummellenes', 'Vaccinium_corymbosum', 'Northland', 'APRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTS', 'Ogu_krums', 4, 'Daudzgadiga', 'Liela', 23, 'Maijs', 10, 3, 'Saule', 'Mitra-skaba');
#izdzest!!!!!!!!!!
INSERT INTO augi(nosaukums, latiniskais_nosaukums, skirne, apraksts, veids, augsanas_ilgums, dzivesilgums, izturiba, saknu_dzilums, stadisanas_menesis, minimala_temperatura, laistisanas_biezums, gaismas_vide, vide)
VALUES('Augstas_krummellenes2', 'Vaccinium_corymbosum', 'Northland', 'APRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTSAPRAKSTS', 'Ogu_krums', 4, 'Daudzgadiga', 'Liela', 23, 'Maijs', 10, 3, 'Saule', 'Mitra-skaba');

#atsaucu tabula
INSERT INTO atsauces(atsauce)
VALUE('https://lv.wikipedia.org/wiki/Augst%C4%81s_kr%C5%ABmmellenes');
INSERT INTO atsauces(atsauce)
VALUE('https://www.gardeningknowhow.com/edible/fruits/blueberries/highbush-blueberry-plant-care-grow-highbush-blueberry-plants.htm');

#augi_atsauce starp tabula
INSERT INTO augi_atsauce(auga_id, atsauces_Id)
VALUES(1,1);
INSERT INTO augi_atsauce(auga_id, atsauces_Id)
VALUES(1,2);

SELECT * FROM augi;

DROP TABLE augi;
DROP TABLE atsauce;
DROP TABLE augi_atsauce;
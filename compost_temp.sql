-- **********************************
-- DDL for compost_temp.db

CREATE TABLE Compost(
  compost_id  INTEGER PRIMARY KEY AUTOINCREMENT,
  compost_temp float NOT NULL,
  outside_temp float,
  battery INTEGER NOT NULL,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (90.00,100.00,4140,'2018-01-04 16:10:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (81.00,90.00, 4130,'2018-02-04 16:11:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (90.00,95.00, 4120,'2018-03-04 16:12:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (85.00,87.00, 4110,'2018-04-05 16:13:00');
INSERT INTO Compost(compost_temp, outside_temp, battery) VALUES (95.00,100.00,4100);

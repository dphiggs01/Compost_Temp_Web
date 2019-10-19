-- **********************************
-- DDL for compost_temp.db
DROP TABLE  Compost;

CREATE TABLE Compost(
  compost_id  INTEGER PRIMARY KEY AUTOINCREMENT,
  compost_temp float NOT NULL,
  outside_temp float,
  battery INTEGER NOT NULL,
  date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (45.00,36.00,4140,'2018-01-04 16:10:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (48.00,32.00,4140,'2018-01-05 16:10:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (47.00,30.00,4140,'2018-01-07 16:10:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (48.00,31.00,4140,'2018-01-10 16:10:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (38.00,32.00, 4130,'2018-02-04 16:11:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (58.00,50.00, 4120,'2018-03-04 16:12:00');
INSERT INTO Compost(compost_temp, outside_temp, battery, date_created) VALUES (62.00,58.00, 4110,'2018-04-05 16:13:00');

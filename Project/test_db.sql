CREATE TABLE Person(
    id int not null AUTO_INCREMENT,
    name VARCHAR (255) NOT NULL,
    PRIMARY KEY(id) 
);
INSERT INTO Person (id,name)
VALUES (0,'Tomas'),(1,'Martin');
SELECT id, name FROM Person;
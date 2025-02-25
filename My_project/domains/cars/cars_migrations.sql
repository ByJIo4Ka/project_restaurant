CREATE TABLE car (
  car_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED,
  car_model VARCHAR(50),
  car_color VARCHAR(30)
);

ALTER TABLE car
CHANGE COLUMN car_color car_color_id INT;

show CREATE TABLE car;

CREATE TABLE car (
  `car_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `car_model` varchar(50) DEFAULT NULL,
  `car_color_id` int DEFAULT NULL,
  PRIMARY KEY (`car_id`)
);
DROP TABLE IF EXISTS dishes;     -- попросил исправить ошибку при переименовании таблицы с помощью deepseek
DROP TABLE IF EXISTS menu;

CREATE TABLE menu (
    names_id INT,
    names VARCHAR(50),
    price DECIMAL(10, 2),
    type_of_cooking VARCHAR(50),
    description TEXT,
    is_available BOOLEAN,
    created_at TIMESTAMP
);

ALTER TABLE menu RENAME TO dishes;

ALTER TABLE dishes DROP COLUMN names_id;

ALTER TABLE dishes
CHANGE COLUMN names dishes_names VARCHAR(50),
CHANGE COLUMN price dishes_price DECIMAL(10, 2),
CHANGE COLUMN type_of_cooking dishes_type_of_cooking VARCHAR(50),
CHANGE COLUMN description dishes_description TEXT,
CHANGE COLUMN is_available dishes_is_available BOOLEAN,
CHANGE COLUMN created_at dishes_created_at TIMESTAMP;

INSERT INTO dishes (dishes_names, dishes_price, dishes_type_of_cooking, dishes_description, dishes_is_available, dishes_created_at) VALUES
('Борщ', 250.00, 'Супы', 'Традиционный украинский борщ с говядиной и сметаной', true, '2023-10-01 12:00:00'),
('Цезарь', 180.00, 'Салаты', 'Салат с курицей, сухариками и соусом Цезарь.', true, '2023-10-01 12:00:00'),
('Тирамису', 150.00, 'Десерты', 'Классический итальянский десерт с кофе и маскарпоне.', true, '2023-10-01 12:00:00'),
('Стейк Рибай', 1200.00, 'Основные', 'Стейк из говяжей вырезки с соусом и овощами.', true, '2023-10-01 12:00:00'),
('Паста Карбонара', 350.00, 'Паста', 'Паста с беконом, сливочным соусом и пармезаном.', true, '2023-10-01 12:00:00'),
('Греческий салат', 220.00, 'Салаты', 'Салат с помидорами, огурцами, оливками и фетой.', true, '2023-10-01 12:00:00'),
('Пельмени', 300.00, 'Основные', 'Домашние пельмени с говядиной и свининой.', true, '2023-10-01 12:00:00'),
('Шоколадный фондан', 200.00, 'Десерты', 'Десерт с жидкой шоколадной начинкой и мороженым.', true, '2023-10-01 12:00:00');

SELECT * FROM dishes;
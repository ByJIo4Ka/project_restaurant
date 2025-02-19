DROP TABLE users;

CREATE TABLE users (
   user_login VARCHAR(50),
   user_password_hash CHAR(60),
   user_email VARCHAR(255),
   is_user_active TINYINT(1),
   user_last_name VARCHAR(50),
   user_first_name VARCHAR(50),
   user_patronymic VARCHAR(50),
   user_job_position VARCHAR(100),
   user_contact_info VARCHAR(255),
   user_car_model VARCHAR(50),
   user_car_color VARCHAR(30),
   user_short_description VARCHAR(1000),
   user_full_description TEXT,
   user_children_count TINYINT UNSIGNED,
   user_birth_date DATE,
   user_created_at TIMESTAMP,
   user_updated_at TIMESTAMP
);



INSERT INTO users (
user_login, user_password_hash, user_email, is_user_active,
user_last_name, user_first_name, user_patronymic, user_job_position,
user_contact_info, user_car_model, user_car_color,
user_short_description, user_full_description, user_children_count,
user_birth_date, user_created_at, user_updated_at
) VALUES
('ivan_89', 'qwerty123hashxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'ivan89@example.com', 1,
'Иванов', 'Иван', 'Александрович', 'Программист',
'+79161234567, ул. Ленина, д. 5, кв. 12', 'Toyota Camry, BMW X5', 'Черный, Белый',
'Люблю программировать.', 'Работаю разработчиком более 10 лет. Интересуюсь новыми технологиями.', 2,
'1989-04-15', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('petr_92', 'securehash456xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'petr92@example.com', 1,
'Петров', 'Петр', 'Викторович', 'Системный администратор',
'ул. Гагарина, д. 12', 'Honda Accord', 'Синий',
'Обеспечиваю стабильную работу серверов.', 'Работаю в сфере IT с 2015 года. Люблю администрировать сети.', 1,
'1992-07-22', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('sidorova_k', 'hash987654xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'kseniya.s@example.com', 1,
'Сидорова', 'Ксения', 'Андреевна', 'Менеджер по продажам',
'+79031234567', 'Volkswagen Polo', 'Красный',
'Занимаюсь продажами.', 'Работаю в сфере продаж более 8 лет. Люблю общаться с клиентами.', 0,
'1995-11-10', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('sergey_85', 'x1y2z3hashxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'sergey85@example.com', 1,
'Сергеев', 'Сергей', 'Олегович', 'Дизайнер',
'ул. Гоголя, д. 3, студия дизайна, +79175643210', 'BMW X5', 'Белый',
'Создаю дизайн для веб-проектов.', 'Работаю в индустрии дизайна 12 лет. Люблю экспериментировать с цветами.', 3,
'1985-03-05', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('natalia_k', 'hash654321xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'natalia.k@example.com', 1,
'Кузнецова', 'Наталья', 'Павловна', 'Маркетолог',
'+79876543210', 'Mazda 6', 'Серый',
'Продвигаю бренды в интернете.', 'Работаю в маркетинге 7 лет. Люблю креативные решения.', 2,
'1990-09-18', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('alexandr_m', 'a1b2c3hashxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'alex.m@example.com', 1,
'Михайлов', 'Александр', 'Дмитриевич', 'Инженер',
'ул. Строителей, д. 7, кв. 15, +79991234567, +74951234567', 'Lada Vesta', 'Белый',
'Проектирую сложные системы.', 'Работаю в сфере инженерии 9 лет. Разрабатываю сложные конструкции.', 1,
'1988-06-25', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('elena_t', 'hashabc123xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'elena.t@example.com', 1,
'Тихонова', 'Елена', 'Григорьевна', 'Учитель',
'+79251234567', 'Kia Rio', 'Желтый',
'Преподаю математику.', 'Работаю в школе 15 лет. Люблю обучать детей.', 2,
'1983-02-14', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('vladislav_r', 'hash567abcxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'vladislav.r@example.com', 1,
'Романов', 'Владислав', 'Иванович', 'Юрист',
'ул. Достоевского, д. 22, юридическая консультация, +74952345678', 'Mercedes-Benz C-Class', 'Серебристый',
'Консультирую по правовым вопросам.', 'Работаю юристом 11 лет. Помогаю клиентам решать юридические вопросы.', 0,
'1987-05-30', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('marina_s', 'hashxyz789xxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'marina.s@example.com', 1,
'Смирнова', 'Марина', 'Сергеевна', 'Фотограф',
'ул. Арбат, д. 18, фотостудия', 'Audi A3', 'Черный',
'Фотографирую людей и природу.', 'Работаю фотографом 6 лет. Люблю ловить эмоции в кадре.', 1,
'1993-12-07', '2024-02-13 12:00:00', '2024-02-13 12:00:00'),

('oleg_d', 'hash987abcxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'oleg.d@example.com', 1,
'Дмитриев', 'Олег', 'Петрович', 'Врач',
'ул. Центральная, д. 9, клиника Здоровье, +79111234567, +74951237890', 'Skoda Octavia', 'Синий',
'Помогаю людям оставаться здоровыми.', 'Работаю врачом 14 лет. Забочусь о здоровье пациентов.', 3,
'1982-08-21', '2024-02-13 12:00:00', '2024-02-13 12:00:00');

SELECT * from users
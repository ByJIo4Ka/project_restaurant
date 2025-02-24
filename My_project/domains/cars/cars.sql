CREATE TABLE 'cars' (
    'car_id' INT unsigned auto_increment PRIMARY KEY,
    'user_id' INT unsigned,
    'car_model' VARCHAR(50),
    'car_color' VARCHAR(30)
);

INSERT INTO 'cars' ('user_id', 'car_model', 'car_color') VALUES
    (1, 'Toyota Camry', 'Черный')
    (1, 'BMW X5', 'Белый');

SELECT * FROM cars;

INSERT INTO `users` (`user_login`, `user_password_hash`,
  `user_email`, `is_user_active`,
  `user_last_name`, `user_first_name`, `user_patronymic`, `user_job_position`,
  `user_short_description`, `user_full_description`, `user_children_count`,
  `user_birth_date`, `user_created_at`, `user_updated_at`) VALUES
  ('ivan_89', 'qwerty123hashxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'ivan89@example.com', 1,
  'Иванов', 'Иван', 'Александрович', 'Программист', 'Люблю программировать.', 'Работаю разработчиком более 10 лет.', 2, '1989-04-15', '2024-02-13 12:00:00', '2024-02-13 12:00:00');

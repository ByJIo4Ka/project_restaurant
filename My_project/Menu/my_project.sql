DROP TABLE menu;

CREATE TABLE menu (
    names_id INT,
    names VARCHAR(50),
    price INT,
    type_of_cooking VARCHAR(50),
    structure VARCHAR(255)
);

INSERT INTO menu (
names_id, names, price, type_of_cooking,
structure) VALUES
(1, 'Burger', 99, 'fastfood', 'Beef_Patty, Lettuce, Tomato, Cheese'),

(2, 'pizza_margarita', 340, 'fastfood', 'sousadge, cheese_pormisano, Tomato_cherry, gluten_free_dough'),

(3, 'pizza_paperonni', 300, 'fastfood', 'sousadge, cheese_pormisano, Tomato_cherry, common_dough');

SELECT * from menu
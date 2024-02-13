-- a script that creates a table second_table(id int, name varchar(256) and score int). and inserts mutiple values
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (
    1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 13),
    (4, "George", 8);

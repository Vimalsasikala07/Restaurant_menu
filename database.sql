
CREATE DATABASE restaurant_db;
USE restaurant_db;

CREATE TABLE menu (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10,2)
);

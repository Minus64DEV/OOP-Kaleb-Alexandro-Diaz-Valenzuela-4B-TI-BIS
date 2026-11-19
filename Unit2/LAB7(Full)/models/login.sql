CREATE DATABASE login_system_db;
USE login_system_db;

CREATE TABLE users(
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR (50) NOT NULL UNIQUE,
    password VARCHAR (25) NOT NULL,
    nombre VARCHAR (50) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO users(username, password,nombre) VALUES ('admin','admin123' , 'Superadmin');

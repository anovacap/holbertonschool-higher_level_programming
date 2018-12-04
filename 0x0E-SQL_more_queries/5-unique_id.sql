-- creates the table unique_id on your MySQL server
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS unique_id(
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256));

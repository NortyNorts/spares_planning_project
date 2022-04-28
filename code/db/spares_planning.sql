
DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS units;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE units (
    id SERIAL PRIMARY KEY,
    unit_type VARCHAR (255),
    serial_number VARCHAR (255),
    hours_run INT DEFAULT 1,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE
);

CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    number VARCHAR (255),
    number_per_unit INT DEFAULT 1,
    hour_exp INT DEFAULT 1,
    unit_id INT NOT NULL REFERENCES units(id) ON DELETE CASCADE
);



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
    hours_run INT,
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE
);

CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    number VARCHAR (255),
    number_per_unit INT,
    hour_exp INT,
    unit_id INT REFERENCES units(id) ON DELETE CASCADE
);


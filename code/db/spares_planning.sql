DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS units;

CREATE TABLE units (
    id SERIAL PRIMARY KEY,
    unit_type VARCHAR (255),
    serial_number VARCHAR (255),
    hours_run INT
);

CREATE TABLE parts (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    number VARCHAR (255),
    number_per_unit INT,
    hour_exp INT,
    unit_id INT REFERENCES units(id)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    unit_id INT REFERENCES units(id)
);
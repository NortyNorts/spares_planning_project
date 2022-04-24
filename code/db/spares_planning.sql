DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS units;
DROP TABLE IF EXISTS parts;

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    units_id INT REFERENCES units(id) ON DELETE CASCADE
);

CREATE TABLE units(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    serial_number VARCHAR (255),
    parts_id INT REFERENCES parts(id) ON DELETE CASCADE,
    hours_run INT
);

CREATE TABLE parts(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    number VARCHAR (255),
    number_per_unit INT,
    hour_exp INT
);
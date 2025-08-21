
CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(250) NOT NULL
   
);

DROP TABLE IF EXISTS parent_address;
CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_id  BIGSERIAL REFERENCES parent(id),
    county_name VARCHAR(250),
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(200) 
);

INSERT INTO parent
(name, email)
VALUES
('sammy Kioko','kioko@gmail.com'),
('Bonventure Oloo', 'oloo@gmail.com');

INSERT INTO parent_address
(county_name, town, longitude, latitude, house_no)
VALUES
('Kitui', 'Mutomo', 123.45, 124.24, 12345),
('Kisumu', 'Dunga', 124.75, 46.83,45689)

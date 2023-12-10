CREATE TABLE IF NOT EXISTS birds (
    id serial PRIMARY KEY,
    class_id DOUBLE PRECISION NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    labels VARCHAR(255) NOT NULL,
    data_set VARCHAR(255) NOT NULL,
    scientific_name VARCHAR(255) NOT NULL
);
-- in psql:
-- \copy table_name (col_1, col_2) FROM '/path/to/data.csv' DELIMITER ',' CSV HEADER;
COPY birds(class_id, file_path, labels, data_set, scientific_name) FROM '/Users/kielay/code/projects/flask-bird-api/data/birds.csv' DELIMITER ',' CSV HEADER;
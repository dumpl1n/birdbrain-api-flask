CREATE TABLE IF NOT EXISTS birds (
    id serial PRIMARY KEY,
    class_id INT NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    labels VARCHAR(255) NOT NULL,
    data_set VARCHAR(255) NOT NULL,
    scientific_name VARCHAR(255) NOT NULL
);
-- \copy table_name (col_1, col_2) FROM '/path/to/data.csv' DELIMITER ',' CSV HEADER;
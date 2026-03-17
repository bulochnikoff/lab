CREATE TABLE IF NOT EXISTS test (
    id SERIAL PRIMARY KEY,
    message TEXT
);
INSERT INTO test (message) VALUES ('Сервис работает');
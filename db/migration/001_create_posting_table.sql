CREATE TABLE IF NOT EXISTS postings
(
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(255),
    content TEXT
);

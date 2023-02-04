CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    senderID INTEGER,
    content TEXT,
    likes INTEGER,
    FOREIGN KEY (senderID) REFERENCES users(id) ON DELETE CASCADE,
    sent_at TIMESTAMP
);


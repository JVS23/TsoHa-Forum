CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS threads (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    likes INTEGER,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    created_at TIMESTAMP
);


CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    likes INTEGER,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    thread_id INTEGER REFERENCES threads ON DELETE CASCADE,
    sent_at TIMESTAMP
);


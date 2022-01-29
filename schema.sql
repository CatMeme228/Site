CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
)


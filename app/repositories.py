import sqlite3
from werkzeug.exceptions import abort
from flask import flash

def get_db_connection():
    conn= sqlite3.connect('C:/Users/tolab/PycharmProjects/Site/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_db_connection_users():
    connUsers= sqlite3.connect('C:/Users/tolab/PycharmProjects/Site/users.db')
    connUsers.row_factory = sqlite3.Row
    return connUsers


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * from posts').fetchall()
    conn.close()
    return posts


def add_posts(title, content):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (title, content))
    conn.commit()
    conn.close()


def update_posts(title, content, id):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ?'
                 ' WHERE id = ?',
                 (title, content, id))
    conn.commit()
    conn.close()

def delete_posts(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def add_user(name, email, password):
    conn = get_db_connection_users()
    conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                 (name, email, password))
    conn.commit()
    conn.close()
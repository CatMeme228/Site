from sqlalchemy import update
from app.models import db
from flask_sqlalchemy import SQLAlchemy
from app.models import Post, User




def get_post(post_id):
    return Post.query.get(post_id)


def get_all_posts():
    return Post.query.all()

def add_posts(title, content):
    new_post= Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()


def update_posts(title, content, id):
    db.session.execute(update(Post)
                       .where(Post.id == id)
                       .values(title=title, content= content))
    db.session.commit()

def delete_posts(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()

def add_user(user_name, email, userpassword):
    new_post = User(user_name= user_name, email=email, userpassword=userpassword)
    db.session.add(new_post)
    db.session.commit()
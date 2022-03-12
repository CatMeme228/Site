from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy
from app import app
from datetime import datetime
from flask_login import LoginManager, UserMixin

db= SQLAlchemy(app)
login_manager= LoginManager(app)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default= datetime.utcnow())
    title= db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(100), nullable=False, unique= True)
    email = db.Column(db.String(100), nullable=False, unique= True)
    password_hash = db.Column(db.String(100), nullable=False)
    created= db.Column(db.DateTime(), default=datetime.utcnow())

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    content = db.Column(db.Text(), nullable=False)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))


db.create_all(app=app)
db.session.commit()

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

def add_user(user_name, email, password_hash):
    new_user = User(user_name= user_name, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return  db.session.query(User).get(user_id)

def load_user_by_name(email):
   print(db.session.query(User).filter(User.email == email).first())
   return db.session.query(User).filter(User.email == email).first()

def add_comment(post_id, content):
    post = get_post(post_id)
    new_comment = Comment(post=post, content=content)
    db.session.add(new_comment)
    db.session.commit()

def get_comments(post_id):
    post = Post.query.get(post_id)
    comments = post.comments.all()
    return comments
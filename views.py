from os import abort

from flask import render_template, request, url_for, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from app.forms import User_registration_form, Comment_creation_form, User_login_form

from app.alchemy_repositories import get_all_posts, get_post, update_posts, delete_posts, add_user, add_posts, \
    add_comment, get_comments, load_user_by_name


@app.route('/')
def draw_main_page():
    posts= get_all_posts()
    return render_template('index.html', posts = posts)

@app.route('/about')
def draw_about_page():
    return render_template('about.html')

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    comments = get_comments(post_id)
    if post is None:
        abort(404)

    return render_template('post.html', post=post, comments=comments)



@app.route('/create', methods= ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Введите заголовок!')
        else:
            add_posts(title, content)
            return redirect(url_for('draw_main_page'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            update_posts(title, content, id)
            return redirect(url_for('draw_main_page'))

    return render_template('edit.html', post=post)


@app.route('/register/', methods=['get', 'post'])
def register_user():
    form = User_registration_form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        password_again = form.passwordRepeatFieled.data

        if password != password_again:
            flash('Enter equal passwords!')
        else:
            password_hash = generate_password_hash(password)
            print(f'{name} {email}')
            add_user(name, email, password_hash)
            return redirect(url_for('draw_main_page'))

    return render_template('registration.html', form=form)

@app.route('/login/', methods= ['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('personal_cabinet'))
    form= User_login_form()

    if form.validate_on_submit():
        user = load_user_by_name(form.name.data)
        print(user)

        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('personal_cabinet'))

    return render_template('login.html', form = form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You loggerd out')
    return redirect(url_for('login'))


@app.route('/personal_cabinet/')
@login_required
def personal_cabinet():
    return render_template('personal.html', user= current_user)


@app.route('/<int:post_id>/comments/create', methods=('GET', 'POST'))
def create_comment(post_id):
    form = Comment_creation_form()

    if form.validate_on_submit():
        content = form.content.data
        add_comment(post_id=post_id, content=content)
        return redirect(url_for('draw_main_page'))

    return render_template('create_comment.html', form=form)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    delete_posts(id)
    return redirect(url_for('draw_main_page'))


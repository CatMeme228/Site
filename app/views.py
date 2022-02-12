from flask import render_template, request, url_for, flash, redirect

from app import app
from app.forms import User_registration_form, Post_create_form

from app.alchemy_repositories import get_all_posts, get_post, update_posts, delete_posts, add_user, add_posts

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
    return render_template('post.html', post=post)



@app.route('/create', methods= ('GET', 'POST'))
def create():
    form = Post_create_form()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        add_posts(title, content)
        return redirect(url_for('draw_main_page'))

    return render_template('create.html', form=form)

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
            print(f'{name} {email}')
            add_user(name, email, password)
            return redirect(url_for('draw_main_page'))

    return render_template('registration.html', form=form)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    delete_posts(id)
    return redirect(url_for('draw_main_page'))
from flask import render_template, request, url_for, flash, redirect

from app import app

from app.repositories import get_all_posts, get_post, add_posts, update_posts, delete_posts, registration_user#, like_posts
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


@app.route('/registration', methods= ('GET', 'POST'))
def registration():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        if not name or not password:
            flash('Заполните все поля!')
        else:
            registration_user(name, password)
            return redirect(url_for('draw_main_page'))
    return render_template('registration.html')

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    delete_posts(id)
    return redirect(url_for('draw_main_page'))


'''@app.route('/<int:id>/like', methods=('POST',))
def like(id):
    like_posts(id)
    return redirect(url_for('draw_main_page'))


if __name__ == '__main__':
    app.run()
'''
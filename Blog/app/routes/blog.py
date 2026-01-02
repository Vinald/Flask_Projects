from flask import Flask, render_template, request, Blueprint, url_for

blog_route = Blueprint('blog_route', __name__, template_folder='templates/blogs')

POSTS = [
    {'id': 1, 'title': 'First Blog Post','author': 'Samuel ov', 'content': 'This is the content of the first blog post.', 'date_posted': 'April 20, 2024'},
    {'id': 2, 'title': 'Second Blog Post', 'author': 'Jane Doe', 'content': 'This is the content of the second blog post.', 'date_posted': 'April 21, 2024'}
]

@blog_route.route('/')
def index():
    return render_template('blogs/index.html', posts=POSTS)
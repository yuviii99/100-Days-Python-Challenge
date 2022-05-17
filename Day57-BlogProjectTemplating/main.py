from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
blogs = requests.get(url=blog_url).json()
post_objects = []
for post in blogs:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/blog/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post = requested_post)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
import smtplib

USER_EMAIL = "yuvisr1337@gmail.com"
PASSWORD = "Bholu#50960"

app = Flask(__name__)

posts = requests.get(url='https://api.npoint.io/026c1ac876bfd4876e5e').json()


def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=USER_EMAIL, to_addrs="ranayuvraj99@gmail.com", msg=email_message)


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)

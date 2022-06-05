from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = '313a40759d906dae6dcd118d49389aab'
TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
TMDV_MOVIE_URL = 'https://api.themoviedb.org/3/movie'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class MyForm(FlaskForm):
    rating = StringField(label='Your rating out of 10', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField(label='Update')


class AddMovieForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie', validators=[DataRequired()])


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

# new_movie = Movie( title="Phone Booth", year=2002, description="Publicist Stuart Shepard finds himself trapped in a
# phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help,
# Stuart's negotiation with the caller leads to a jaw-dropping climax.", rating=7.3, ranking=10, review="My favourite
# character was the caller.", img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg" )
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    form = MyForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        movie_title = add_movie_form.movie_title.data
        response = requests.get(url=TMDB_SEARCH_URL, params={
            "api_key": TMDB_API_KEY,
            "query": movie_title
        })
        # print(response.json()['results'][0]['id'])
        data = response.json()['results']
        return render_template("select.html", options=data)
    return render_template('add.html', form=add_movie_form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"{TMDV_MOVIE_URL}/{movie_api_id}"
        movie_img_url = 'https://image.tmdb.org/t/p/w500'
        response = requests.get(url=movie_api_url, params={"api_key": TMDB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data['original_title'],
            year=data['release_date'].split('-')[0],
            img_url=f"{movie_img_url}{data['poster_path']}",
            description=data['overview'],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)

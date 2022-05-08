from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-romantic-movies/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
title = soup.title.string.split("|")[0]
movie_names = [movie.getText() for movie in soup.select("span h2")]
movies = movie_names[::-1]

with open('movies.txt', 'w') as file:
    file.write(f"{title}\n\n")
    for movie in movies:
        file.write(f"{movie}\n")

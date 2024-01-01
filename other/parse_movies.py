import requests
from bs4 import BeautifulSoup

def parse_movies_kinopoisk(year):
    url = f'https://www.kinopoisk.ru/lists/top250/?year={year}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_titles = soup.find_all('span', {'class': 'selection-film-item-meta__name'})
    movies = [title.text for title in movie_titles]
    return movies

movies_2023_kinopoisk = parse_movies_kinopoisk(2023)
print(movies_2023_kinopoisk)
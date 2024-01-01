import requests
from bs4 import BeautifulSoup

def parse_movies(year):
    url = f'https://www.imdb.com/search/title/?title_type=feature&release_date={year}-01-01,{year}-12-31'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_titles = soup.find_all('h3', class_='lister-item-header')
    movies = [title.text.strip() for title in movie_titles]
    return movies

movies_2023 = parse_movies(2023)
print(movies_2023)
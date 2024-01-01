import imdb

def get_movies_for_year(year):
    ia = imdb.IMDb()
    movies = ia.get_movies(str(year))
    movie_titles = [movie['title'] for movie in movies]
    return movie_titles

# Получаем список фильмов, выпущенных в 2023 году
movies_2023 = get_movies_for_year(2023)
print(movies_2023)
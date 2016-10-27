import fresh_tomatoes
import media
import movie_api

movies = movie_api.retrieve_movies() # retrieves all the movie from tmdb API
fresh_tomatoes.open_movies_page(movies)

import requests
import media

# Constant needed for the queries
API_KEY = '26f256c704b552e697d2432f3ba4b8ae'
BASE_API_URL = "https://api.themoviedb.org/3/movie/"
BASE_YOUTUBE_TRAILER_URL = "https://www.youtube.com/watch?v="

POPULAR_MOVIES_QUERY = "popular?api_key="
TRAILER_KEY_QUERY = "/videos?api_key="
POSTER_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500/"


def retrieve_movies(): # Retrieve movies from Tmdb api
    resp = requests.get(BASE_API_URL + POPULAR_MOVIES_QUERY + API_KEY)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /movie/ {}'.format(resp.status_code))

    movies = [] # initializes the list that will be used to store the movies received from the request

    results = resp.json()["results"]
    for movie in results: # for each element in results create a movie object
        movie_id = movie['id'] # needed for movie_trailer
        movie_title = movie['title']
        movie_storyline = movie['overview']
        movie_trailer = retrieve_trailer(movie_id) # retrieves trailer url
        movie_poster = POSTER_IMAGE_BASE_URL + movie['poster_path']
        movies.append(media.Movie(movie_title,movie_storyline,movie_poster, movie_trailer))

    return movies


def retrieve_trailer(movie_id): # Retrieve the movie trailer url using the movie_id provided by the API
    resp = requests.get(BASE_API_URL + str(movie_id) + TRAILER_KEY_QUERY + API_KEY )
    results = resp.json()["results"] # json object containing all the trailers for the movie with id = movie_id
    key = results[0]['key'] # key that allows to complete the trailer url for the movie

    return BASE_YOUTUBE_TRAILER_URL + key

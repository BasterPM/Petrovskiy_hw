class Movie:
    released_films = set()

    def __init__(self, film_name):
        self.film_name = film_name
        if self.film_name in Movie.released_films:
            raise ValueError(f'Film: {self.film_name} has already been filmed')
        Movie.released_films.add(self.film_name)
        print(f'Film: {self.film_name} filmed')
        return


class Cinema:
    def __init__(self):
        self.poster = set()

    def add_movie(self, movie: Movie):
        if movie.film_name in Movie.released_films:
            self.poster.add(movie)
            return
        print(f'Film: {movie.film_name} has not yet been filmed')

    def remove_movie(self, movie: Movie):
        if movie in self.poster:
            self.poster.remove(movie)
            return
        print(f'Film: {movie.film_name} not released')

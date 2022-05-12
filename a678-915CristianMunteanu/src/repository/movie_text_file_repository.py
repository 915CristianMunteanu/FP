import os.path

from domain.entities import Movie
from repository.repository import MovieRepository


class MovieTextFileRepository(MovieRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
             self.update_file()
        self.load()

    def add_movie_to_repository(self, movie):
        super(MovieTextFileRepository,self).add_movie_to_repository(movie)
        self.update_file()

    def remove_movie_by_id(self, id):
        super(MovieTextFileRepository,self).remove_movie_by_id(id)
        self.update_file()

    def update_movie_by_id(self, movie_id, title, description, genre):
        super(MovieTextFileRepository,self).update_movie_by_id(movie_id, title, description, genre)
        self.update_file()

    def update_file(self):
        file = open(self.__file_name, "w")
        for movie in self._list_of_movies.values():
            file.write(str(movie.movie_id)+","+movie.title+","+movie.description+","+movie.genre+'\n')
        file.close()


    def load(self):
        with open(self.__file_name,"r") as file:
            for line in file.readlines():
                line=line.strip()
                movie_id, title, description, genre = line.split(sep=",",maxsplit=3)
                self.add_movie_to_repository(Movie(int(movie_id), title, description, genre))
        file.close()

from repository.repository import MovieRepository
import pickle
import os.path

class MovieBinaryFileRepository(MovieRepository):
    def __init__(self,file_name):
        super().__init__()
        self.__file_name=file_name
        if not os.path.exists(self.__file_name):
            self.save()
        self.load()
    def load(self):
        file=open(self.__file_name,"rb")
        self._list_of_movies=pickle.load(file)
        file.close()
    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._list_of_movies,file)
        file.close()
    def add_movie_to_repository(self, movie):
        super(MovieBinaryFileRepository,self).add_movie_to_repository(movie)
        self.save()
    def remove_movie_by_id(self, id):
        super(MovieBinaryFileRepository,self).remove_movie_by_id(id)
        self.save()
    def update_movie_by_id(self, movie_id, title, description, genre):
        super(MovieBinaryFileRepository,self).update_movie_by_id(int(movie_id), title, description, genre)
        self.save()

from data_structure import DataStructure
from domain.validators import MovieRentalException, MovieException, ClientException, RentalException
from domain.validators import MovieValidator

class RepositoryException(MovieRentalException):
    pass


class MovieRepository:
    """
    This is the repository for the movies, here are all the functions that manages the storage of the movies.
    """

    def __init__(self):
        self._list_of_movies = DataStructure()

    def find_movie_by_id(self, movie_id):
        """
        This function searches if there is a client in the list of clients with the given ID.
        :param movie_id: Integer value
        :return: If there is a movie with the given ID it returns the movie. If there is not, it returns None.
        """
        if movie_id in self._list_of_movies.keys():
            return self._list_of_movies[movie_id]
        return None



    def add_movie_to_repository(self, movie):
        """
        This function is used to add a given object(movie) to the list of all movies. Firstly, it checks if there is already a object with the given ID:
        If there is, a Error is raised. If there is not it validates the data then adds the object to the list.
        :param movie: An object created by the class Movie
        :return: Doesnt return anything.
        """
        MovieValidator.validate_movie(movie)
        if self.find_movie_by_id(int(movie.movie_id)) is not None:
            raise MovieException("There is already a movie with the given ID")
        else:
            self._list_of_movies[movie.movie_id] = movie

    def __getitem__(self, item):
        return self._list_of_movies[item]
    def return_list_of_all_movies(self):
        """
        This function is used to return the list_of_all_movies.
        :return: list_of_movies,which is a list of objects created by the class Movies
        """
        return list(self._list_of_movies.values())

    def remove_movie_by_id(self, id):
        """
        This function deletes the movie that has the
        :param id:
        :return:
        """
        del self._list_of_movies[id]

    def update_movie_by_id(self, movie_id, title, description, genre):
        self._list_of_movies[movie_id].title = title
        self._list_of_movies[movie_id].description = description
        self._list_of_movies[movie_id].genre = genre

    def set_list_of_movies(self, value):
        self._list_of_movies = value

    def return_dictionary_of_all_movies(self):
        return self._list_of_movies


class ClientRepository:
    """
    This is the repository for the clients, here are all the functions that manages the storage of the clients.
    """

    def __init__(self):
        self._list_of_clients = DataStructure()

    def find_client_by_id(self, client_id):
        """
        This function searches if there is a client in the list of clients with the given ID.
        :param client_id: Integer value
        :return: If there is a client with the given ID it returns the client. If there is not, it returns None
        """
        if client_id in self._list_of_clients.keys():
            return self._list_of_clients[client_id]
        return None

    def add_client_to_repository(self, client):
        """
        This function is used to add a given object(client) to the list of all movies. Firstly, it checks if there is already a object with the given ID:
        If there is, a Error is raised. If there is not it validates the data then adds the object to the list.
        :param client: An object created by the class Client
        :return: Doesnt return anything.
        """
        if str(client.client_id).isnumeric():
            client.client_id=int(client.client_id)
            if self.find_client_by_id(int(client.client_id)) is not None:
                raise ClientException("There is already a client with the given ID")
            else:
                self._list_of_clients[client.client_id] = client
        else:
            raise ClientException("The ID is not right!")

    def return_list_of_all_clients(self):
        """
        This function is used to return the list_of_all_clients.
        :return: list_of_clients,which is a list of objects created by the class Client
        """
        return list(self._list_of_clients.values())

    def remove_client_by_id(self, id):
        """
        This function deletes the movie that has the
        :param id:
        :return:
        """
        del self._list_of_clients[id]

    def update_client_by_id(self, client_id, name):
        self._list_of_clients[client_id].name = name

    def set_list_of_clients(self, value):
        self._list_of_clients = value

    def return_dictionary_of_all_clients(self):
        return self._list_of_clients


class RentalRepository:
    """
    This is the repository for the rentals, here are all the functions that manages the storage of the rentals.
    """

    def __init__(self, movie_repository, client_repository):
        self._list_of_rentals = DataStructure()
        self._movie_repository = movie_repository
        self._client_repository = client_repository

    def find_rental_by_id(self, rental_id):
        """
        This function searches if there is a client in the list of clients with the given ID.
        :param rental_id: Integer value
        :return: If there is a rental with the given ID it returns the client. If there is not, it returns None
        """
        if rental_id in self._list_of_rentals.keys():
            return self._list_of_rentals[rental_id]
        return None

    def add_rental_to_repository(self, rental):
        """
        This function is used to add a given object(rental) to the list of all movies. Firstly, it checks if there is already a object with the given ID:
        If there is, a Error is raised. If there is not it validates the data then adds the object to the list.
        :param rental: An object created by the class Rental
        :return: Doesnt return anything.
        """
        if self._movie_repository.find_movie_by_id(
                rental.movie_id) is not None and self._client_repository.find_client_by_id(
                rental.client_id) is not None:
            if self.find_rental_by_id(rental.rental_id) is not None:
                raise RentalException("There is already a rental with the given ID")
            self._list_of_rentals[rental.rental_id] = rental
        else:
            raise RentalException("Movie_id or client_id not found!")

    def return_list_of_all_rentals(self):
        """
        This function is used to return the list_of_all_rentals.
        :return: list_of_rentals,which is a list of objects created by the class Rental
        """
        return list(self._list_of_rentals.values())

    def set_list_of_rentals(self, value):
        self._list_of_rentals = value

    def find_rental_return_date(self, rental_id):
        if self.find_rental_by_id(rental_id) is None:
            raise RepositoryException("There is not a rental with the given ID")
        else:
            return self._list_of_rentals[rental_id].returned_date

    def set_return_date(self, rental_id, return_date):
        self._list_of_rentals[rental_id].returned_date = return_date

    def return_dictionary_of_all_rentals(self):
        return self._list_of_rentals


class UndoRepository:
    def __init__(self):
        self.__data = list()

    def add_operation(self, object_to_undo, object_to_redo):
        self.__data.append((object_to_undo, object_to_redo))

    def pop_operation(self):
        if len(self.__data) == 0:
            raise Exception("You cant undo anything now!")
        else:
            out = self.__data.pop()
            return out[0], out[1]


class RedoRepository:
    def __init__(self):
        self.__data = list()

    def add_operation(self, object_to_redo, object_to_undo):
        self.__data.append((object_to_redo, object_to_undo))

    def pop_operation(self):
        if len(self.__data) == 0:
            raise Exception("You cant redo anything now!")
        else:
            out = self.__data.pop()
            return out[0], out[1]

    def clear_data_from_redo(self):
        self.__data.clear()

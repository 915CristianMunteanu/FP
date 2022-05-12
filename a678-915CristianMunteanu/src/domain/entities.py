class Movie:
    def __init__(self, movie_id, title, description, genre):
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def movie_id(self):
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, value):
        self.__movie_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    def __eq__(self, other_movie):
        if self.movie_id == other_movie.movie_id:
            if self.title == other_movie.title:
                if self.description == other_movie.description:
                    if self.genre == other_movie.genre:
                        return True
        return False


class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __eq__(self, other_client):
        if self.__client_id == other_client.client_id:
            if self.__name == other_client.name:
                return True
        return False


class Rental:
    def __init__(self, rental_id, movie_id, client_id, rented_date, due_date, returned_date):
        self.__rental_id = rental_id
        self.__movie_id = movie_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @rental_id.setter
    def rental_id(self, value):
        self.__rental_id = value

    @property
    def movie_id(self):
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, value):
        self.movie_id = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, value):
        self.rented_date = value

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, value):
        self.__returned_date = value

    def __eq__(self, other_rental):
        if self.__rental_id == other_rental.rental_id:
            if self.__client_id == other_rental.client_id:
                if self.__movie_id == other_rental.movie_id:
                    if self.__due_date == other_rental.due_date:
                        if self.__returned_date == other_rental.returned_date:
                            return True
        return False

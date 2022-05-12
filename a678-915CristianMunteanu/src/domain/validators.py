

class MovieRentalException(Exception):
    pass
class MovieException(MovieRentalException):
    pass
class ClientException(MovieRentalException):
    pass
class RentalException(MovieRentalException):
    pass

class MovieValidator():
    @staticmethod
    def validate_movie(movie):
        if str(movie.movie_id).isdigit():
            movie.movie_id=int(movie.movie_id)
        else:
            raise MovieException("The ID is not right!")

class ClientValidator():
    @staticmethod
    def validate_client(client):
        if str(client.client_id).isnumeric():
            client.client_id=int(client.client_id)
        else:
            raise ClientException("The ID cant be a string!")

class RentalValidator():
    @staticmethod
    def validate_rental(rental):
        if rental.rental_id.isnumeric():
            rental.rental_id = int(rental.rental_id)
        else:
            raise RentalException("The ID cant be a string!")

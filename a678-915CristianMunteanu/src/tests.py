import datetime
import unittest

from domain.entities import Movie, Client, Rental
from domain.validators import ClientValidator, MovieValidator, RentalValidator, MovieException, ClientException, \
    RentalException
from repository.repository import ClientRepository, MovieRepository, RentalRepository, UndoRepository, RedoRepository
from services.RedoService import RedoService
from services.UndoService import UndoService
from services.services import ClientService, MovieService, RentalService

# client_validator=ClientValidator()
# client_repository=ClientRepository(client_validator)
# movie_validator=MovieValidator()
# movie_repository=MovieRepository(movie_validator)
# rental_validator=RentalValidator()
# rental_repository=RentalRepository(rental_validator,movie_repository,client_repository)
# movie_service=MovieService(movie_repository,rental_repository)
# client_service=ClientService(client_repository,rental_repository)
# rental_service=RentalService(rental_repository,movie_repository,client_repository)



# class Test():
#     def __init__(self, movie_service, client_service, rental_service, movie_repository, client_repository,
#                  rental_repository):
#         self.__movie_service = movie_service
#         self.__client_service = client_service
#         self.__rental_service = rental_service
#         self.__movie_repository = movie_repository
#         self.__client_repository = client_repository
#         self.__rental_repository = rental_repository
#
#     def test_add_movie___with_movie_id_integer_and_not_already_existing___AssertsTrue(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             list_of_all_movies_before_add = [Movie(1, "Batman", "It was a good movie", "Horror"),
#                                              Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                              Movie(3, "Fast and Furios", "Beautiful Cars", "Action"),
#                                              Movie(4, "Bay Driver", "Dont look back", "Action")]
#             self.__movie_service.add_movie("4", "Bay Driver", "Dont look back", "Action")
#             list_of_all_movies_after_add = self.__movie_service.return_list_of_all_movies_to_console()
#             for current_movie_index in range(0, len(list_of_all_movies_after_add)):
#                 assert list_of_all_movies_before_add[current_movie_index].__eq__(
#                     list_of_all_movies_after_add[current_movie_index])
#
#         except:
#             assert False
#
#     def test_add_movie___with_movie_id_not_integer___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.add_movie("abc", "Bay Driver", "Dont look back", "Action")
#             assert False
#         except:
#             assert True
#
#     def test_add_movie___with_movie_id_integer_but_already_existing___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.add_movie("1", "Bay Driver", "Dont look back", "Action")
#             assert False
#         except:
#             assert True
#
#     def test_add_client___with_client_id_integer_and_not_already_existing___AssertsTrue(self):
#         self.__client_repository.set_list_of_clients(
#             {1: Client(1, "Peter Pan"), 2: Client(2, "Toma Marian"), 3: Client(3, "Hutu Lutu")})
#         try:
#             list_of_all_clients_before_add = [Client(1, "Peter Pan"), Client(2, "Toma Marian"), Client(3, "Hutu Lutu"),
#                                               Client(4, "Bay Driver")]
#             self.__client_service.add_client("4", "Bay Driver")
#             list_of_all_clients_after_add = self.__client_service.return_list_of_all_clients_to_console()
#             for current_client_index in range(0, len(list_of_all_clients_after_add)):
#                 assert list_of_all_clients_before_add[current_client_index].__eq__(
#                     list_of_all_clients_after_add[current_client_index])
#
#         except:
#             assert False
#
#     def test_add_client___with_client_id_not_integer___AssertsFalse(self):
#         self.__client_repository.set_list_of_clients(
#             {1: Client(1, "Peter Pan"), 2: Client(2, "Toma Marian"), 3: Client(3, "Hutu Lutu")})
#         try:
#             self.__client_service.add_client("abc", "Bay Driver")
#             assert False
#         except:
#             assert True
#
#     def test_add_client___with_client_id_integer_but_already_existing___AssertsFalse(self):
#         self.__client_repository.set_list_of_clients(
#             {1: Client(1, "Peter Pan"), 2: Client(2, "Toma Marian"), 3: Client(3, "Hutu Lutu")})
#         try:
#             self.__client_service.add_client("2", "Bay Driver")
#             assert False
#         except:
#             assert True
#
#     def test_add_rental___with_rental_id_integer_and_not_existing_and_movie_id_and_client_id_existing___AssertsTrue(
#             self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             list_of_all_rentals_before_add = [
#                 Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#                 Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#                 Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None),
#                 Rental(4, 15, 15, date4, date4 + datetime.timedelta(days=10), date4 + datetime.timedelta(days=14))]
#             self.__rental_service.add_rental(4, 15, 15, date4, date4 + datetime.timedelta(days=10),
#                                              date4 + datetime.timedelta(days=14))
#             list_of_all_rentals_after_add = self.__rental_repository.return_list_of_all_rentals()
#             for current_rental_index in range(0, len(list_of_all_rentals_after_add)):
#                 assert list_of_all_rentals_before_add[current_rental_index].__eq__(
#                     list_of_all_rentals_after_add[current_rental_index])
#         except:
#             assert False
#
#     def test_add_rental___with_rental_id_not_integer___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.add_rental("abc", 15, 15, date4, date4 + datetime.timedelta(days=10),
#                                              date4 + datetime.timedelta(days=14))
#             assert False
#         except:
#             assert True
#
#     def test_add_rental___with_movie_id_or_client_id_not_existing___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.add_rental(1, 25, 15, date4, date4 + datetime.timedelta(days=10),
#                                              date4 + datetime.timedelta(days=14))
#             assert False
#         except:
#             assert True
#
#     def test_add_rental___with_movie_id_or_client_not_integer___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.add_rental(1, "abc", 15, date4, date4 + datetime.timedelta(days=10),
#                                              date4 + datetime.timedelta(days=14))
#             assert False
#         except:
#             assert True
#
#     def test_remove_movie___with_movie_id_not_existing_but_integer___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.remove_by_id("5")
#         except:
#             assert True
#
#     def test_remove_movie___with_movie_id_not_integer___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.remove_by_id("abc")
#         except:
#             assert True
#
#     def test_remove_client___with_client_not_integer___AssertsFalse(self):
#         self.__client_repository.set_list_of_clients(
#             {1: Client(1, "Peter Pan"), 2: Client(2, "Toma Marian"), 3: Client(3, "Hutu Lutu")})
#         try:
#             self.__client_service.remove_by_id("abc")
#         except:
#             assert True
#
#     def test_update_movie___with_movie_id_integer_and_existing___AssertsTrue(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             list_of_movies_updated = [Movie(1, "Batman", "It was a good movie", "Horror"),
#                                       Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                       Movie(3, "nothing", " Cars", "Thriller")]
#             self.__movie_service.update_movie_by_id("3", "nothing", " Cars", "Thriller")
#             list = self.__movie_service.return_list_of_all_movies_to_console()
#             for current_movie_index in range(0, len(list)):
#                 assert list_of_movies_updated[current_movie_index].__eq__(list[current_movie_index])
#         except:
#             return False
#
#     def test_update_movie___with_movie_id_integer_but_not_existing___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.update_movie_by_id("5", "nothing", " Cars", "Thriller")
#             assert False
#         except:
#             assert True
#
#     def test_update_movie___with_movie_id_not_integer___AssertsFalse(self):
#         self.__movie_repository.set_list_of_movies({1: Movie(1, "Batman", "It was a good movie", "Horror"),
#                                                     2: Movie(2, "IronMan", "It was a good movie", "Horror"),
#                                                     3: Movie(3, "Fast and Furios", "Beautiful Cars", "Action")})
#         try:
#             self.__movie_service.update_movie_by_id("abc", "nothing", " Cars", "Thriller")
#             assert False
#         except:
#             assert True
#
#     def test_update_client___with_client_id_not_integer___AssertsFalse(self):
#         self.__client_repository.set_list_of_clients(
#             {1: Client(1, "Peter Pan"), 2: Client(2, "Toma Marian"), 3: Client(3, "Hutu Lutu"),
#              4: Client(4, "Bay Driver")})
#         try:
#             self.__client_service.update_client_by_id(4, "Tom Cruise")
#             assert False
#         except:
#             assert True
#
#     def test_rent_movie___with_rental_id_already_existing___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.check_rental('2', '15', '15', date4, date4 + datetime.timedelta(days=10), None)
#             assert False
#         except:
#             assert True
#
#     def test_rent_movie___with_movie_id_not_existing___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.check_rental('4', '26', '15', date4, date4 + datetime.timedelta(days=10), None)
#             assert False
#         except:
#             assert True
#
#     def test_rent_movie___with_client_id_not_existing___AssertsFalse(self):
#         self.__movie_service.generate_20_movies()
#         self.__client_service.generate_20_clients()
#         date1 = datetime.datetime(2021, 6, 6)
#         date2 = datetime.datetime(2020, 1, 12)
#         date3 = datetime.datetime(2020, 4, 13)
#         date4 = datetime.datetime(2020, 5, 5)
#         self.__rental_repository.set_list_of_rentals(
#             {1: Rental(1, 12, 16, date1, date1 + datetime.timedelta(days=10), date1 + datetime.timedelta(days=14)),
#              2: Rental(2, 14, 15, date2, date2 + datetime.timedelta(days=14), date2 + datetime.timedelta(days=3)),
#              3: Rental(3, 12, 16, date2, date3 + datetime.timedelta(days=14), None)})
#         try:
#             self.__rental_service.check_rental('4', '15', '26', date4, date4 + datetime.timedelta(days=10), None)
#             assert False
#         except:
#             assert True
#
#     def test_Movie_class___with_proper_data___AssertsTrue(self):
#         new_movie = Movie(123, "Batman", "It was a good movie", "Horror")
#         assert new_movie.__eq__(Movie(123, "Batman", "It was a good movie", "Horror"))
#
#     def test_Client_class___with_proper_data___AssertsTrue(self):
#         new_client = Client(123, "Peter Pan")
#         assert new_client.__eq__(Client(123, "Peter Pan"))


class TestMovie(unittest.TestCase):
    def setUp(self) -> None:
        self.__undo_repository=UndoRepository()
        self.__redo_repository=RedoRepository()
        self.__undo_service = UndoService(self.__undo_repository,self.__redo_repository)
        self.__redo_service = RedoService(self.__redo_repository,self.__undo_repository)
        self.__movie_validator=MovieValidator()
        self.__movie_repository=MovieRepository(self.__movie_validator)
        self.__rental_validator=RentalValidator()
        self.__client_validator=ClientValidator()
        self.__client_repository=ClientRepository(self.__client_validator)
        self.__rental_repository=RentalRepository(self.__rental_validator,self.__movie_repository,self.__client_repository)
        self.__movie_service=MovieService(self.__movie_repository,self.__client_repository,self.__rental_repository,self.__undo_service,self.__redo_service)
        self.__movie_service.add_movie("12","Batman","Decent Movie","Thriller")
        self.__movie_service.add_movie("13","Fast","Bad","Action")
        self.__movie_service.add_movie("14","Baby Driver","NOt great","Romantic")
    def tearDown(self) -> None:
        pass

    def test_Movie_class___with_proper_data___AssertsTrue(self):
        new_movie = Movie(123, "Batman", "It was a good movie", "Horror")
        self.assertEqual(new_movie.movie_id,123)
        self.assertEqual(new_movie.title,"Batman")
        self.assertEqual(new_movie.description,"It was a good movie")
        self.assertEqual(new_movie.genre,"Horror")
        new_movie.movie_id=22
        new_movie.title="Fast and Furios"
        new_movie.genre="Thriller"
        self.assertEqual(new_movie.movie_id, 22)
        self.assertEqual(new_movie.title, "Fast and Furios")
        self.assertEqual(new_movie.genre, "Thriller")
    def test_add_movie___with_movie_id_integer___Is_Going_to_Be_In_the_list(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        self.__movie_service.add_movie("23","Ceva","Altceva","romantic")
        list_of_expected_movies.append(Movie(23,"Ceva","Altceva","romantic"))
        self.assertEqual(self.__movie_service.return_list_of_all_movies_to_console(),list_of_expected_movies)
    def test_add_movie___with_movie_id_already_existing___A_Movie_Exception_Is_Raised_There_is_already_a_movie_with_the_given_ID(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.add_movie("12","Ceva","Altceva","Horror")
        self.assertEqual(str(error.exception),"There is already a movie with the given ID")
    def test_add_movie___with_movie_id_not_integer___A_Movie_Exception_Is_Raised_The_ID_is_not_right(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.add_movie("1a","Ceva","Altceva","Horror")
        self.assertEqual(str(error.exception),"The ID is not right!")

    def test_remove_movie___with_proper_data___movie_will_not_be_in_the_list(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        del list_of_expected_movies[2]
        self.__movie_service.remove_by_id("14")
        self.assertEqual(self.__movie_service.return_list_of_all_movies_to_console(),list_of_expected_movies)
    def test_remove_movie___with_movie_id_integer_but_not_existing___A_Movie_exception_is_raised_There_is_not_a_movie_with_given_ID(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.remove_by_id("99")
        self.assertEqual(str(error.exception),"There is not a movie with the given ID!")
    def test_remove_movie___with_movie_id_not_integer___A_movie_exception_is_raised_The_id_should_be_an_integer(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.remove_by_id("1a")
        self.assertEqual(str(error.exception),"The id should be an integer")
    def test_update_movie___with_proper_data___updated_movie_will_be_in_the_list(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        list_of_expected_movies[0].title="Fast and Furious"
        list_of_expected_movies[0].description="good"
        list_of_expected_movies[0].genre="horror"
        self.__movie_service.update_movie_by_id("12","Fast and Furious","good","horror")
        self.assertEqual(self.__movie_service.return_list_of_all_movies_to_console(),list_of_expected_movies)
    def test_update_movie___with_movie_id_integer_but_not_existing___A_Movie_exception_is_raised_There_is_not_a_movie_with_the_given_ID(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.update_movie_by_id("99","Fast","good","Horror")
        self.assertEqual(str(error.exception),"There is not a movie with the given ID!")
    def test_update_movie___with_movie_id_not_integer___A_Movie_exception_is_raiesd_The_ID_must_be_an_integer(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.update_movie_by_id("1a","fast","good","thriller")
        self.assertEqual(str(error.exception),"The ID must be an integer!")
    def test_search_movie_by_id___with_proper_data___movie_with_given_id_will_be_found(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        movie_to_be_found=list_of_expected_movies[0]
        self.assertEqual(self.__movie_service.search_movie_by_id("12"),movie_to_be_found)
    def test_search_movie_by_id___with_movie_id_integer_but_not_existing___A_movie_exception_is_raised_There_is_not_a_movie_with_the_given_id(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.search_movie_by_id("99")
        self.assertEqual(str(error.exception),"There is not a movie with the given ID!")
    def test_search_movie_by_id___with_movie_id_not_integer___A_movie_exception_is_raised_The_id_introduced_is_not_right(self):
        with self.assertRaises(MovieException) as error:
            self.__movie_service.search_movie_by_id("1a")
        self.assertEqual(str(error.exception),"The id introduced is not right!")
    def test_search_movie_by_title___with_proper_data___Matching_titles_will_be_found(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        del list_of_expected_movies[2]
        self.assertEqual(list_of_expected_movies,self.__movie_service.search_movie_by_title("t"))
    def test_search_movie_by_description___with_proper_data___Matching_descriptions_will_be_found(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        del list_of_expected_movies[2]
        self.assertEqual(list_of_expected_movies,self.__movie_service.search_movie_by_description("d"))

    def test_search_movie_by_genre___with_proper_data___Matching_genres_will_be_found(self):
        list_of_expected_movies=self.__movie_service.return_list_of_all_movies_to_console()
        del list_of_expected_movies[1]
        del list_of_expected_movies[1]
        self.assertEqual(list_of_expected_movies,self.__movie_service.search_movie_by_genre("h"))

    def testMovie(self):
        self.test_Movie_class___with_proper_data___AssertsTrue()
        self.test_add_movie___with_movie_id_integer___Is_Going_to_Be_In_the_list()
        self.test_add_movie___with_movie_id_not_integer___A_Movie_Exception_Is_Raised_The_ID_is_not_right()
        self.test_add_movie___with_movie_id_already_existing___A_Movie_Exception_Is_Raised_There_is_already_a_movie_with_the_given_ID()
        self.test_remove_movie___with_proper_data___movie_will_not_be_in_the_list()
        self.test_remove_movie___with_movie_id_integer_but_not_existing___A_Movie_exception_is_raised_There_is_not_a_movie_with_given_ID()
        self.test_update_movie___with_proper_data___updated_movie_will_be_in_the_list()
        self.test_update_movie___with_movie_id_integer_but_not_existing___A_Movie_exception_is_raised_There_is_not_a_movie_with_the_given_ID()
        self.test_update_movie___with_movie_id_not_integer___A_Movie_exception_is_raiesd_The_ID_must_be_an_integer()
        self.test_search_movie_by_id___with_proper_data___movie_with_given_id_will_be_found()
        self.test_search_movie_by_id___with_movie_id_integer_but_not_existing___A_movie_exception_is_raised_There_is_not_a_movie_with_the_given_id()
        self.test_search_movie_by_id___with_movie_id_not_integer___A_movie_exception_is_raised_The_id_introduced_is_not_right()
        self.test_search_movie_by_title___with_proper_data___Matching_titles_will_be_found()
        self.test_search_movie_by_description___with_proper_data___Matching_descriptions_will_be_found()
        self.test_search_movie_by_genre___with_proper_data___Matching_genres_will_be_found()
class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.__undo_repository = UndoRepository()
        self.__redo_repository = RedoRepository()
        self.__undo_service = UndoService(self.__undo_repository, self.__redo_repository)
        self.__redo_service = RedoService(self.__redo_repository, self.__undo_repository)
        self.__movie_validator = MovieValidator()
        self.__movie_repository = MovieRepository(self.__movie_validator)
        self.__rental_validator = RentalValidator()
        self.__client_validator = ClientValidator()
        self.__client_repository = ClientRepository(self.__client_validator)
        self.__rental_repository = RentalRepository(self.__rental_validator, self.__movie_repository,
                                                    self.__client_repository)
        self.__client_service = ClientService(self.__movie_repository,self.__client_repository,self.__rental_repository,self.__undo_service,self.__redo_service)
        self.__client_service.add_client("12","Gicu")
        self.__client_service.add_client("13","Nema")
        self.__client_service.add_client("14","Cornel")
    def test_Client_class___with_proper_data___Asserts_true(self):
        new_client=Client(16,"Kuruma")
        self.assertEqual(new_client.client_id,16)
        self.assertEqual(new_client.name,"Kuruma")
        new_client.client_id=18
        new_client.name="Lutu"
        self.assertEqual(new_client.client_id,18)
        self.assertEqual(new_client.name,"Lutu")
    def test_add_client___with_proper_data___is_going_to_be_in_the_list(self):
        list_of_expected_clients=self.__client_service.return_list_of_all_clients_to_console()
        self.__client_service.add_client("15","Mihai")
        list_of_expected_clients.append(Client(15,"Mihai"))
        self.assertEqual(self.__client_service.return_list_of_all_clients_to_console(),list_of_expected_clients)
    def test_add_client___with_client_id_not_integer___A_client_exception_is_raised_The_id_is_not_right(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.add_client("1a","Popa")
        self.assertEqual(str(error.exception),"The ID is not right!")
    def test_add_client___with_client_id_already_existing___A_client_exception_is_raised_There_is_already_a_client_with_the_given_id(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.add_client("12","Popa")
        self.assertEqual(str(error.exception),"There is already a client with the given ID")

    def test_update_client___with_proper_data___updated_client_is_going_to_be_in_the_list(self):
        list_of_expected_clients = self.__client_service.return_list_of_all_clients_to_console()
        list_of_expected_clients[0].name="Cornel"
        self.__client_service.update_client_by_id("12","Cornel")
        self.assertEqual(self.__client_service.return_list_of_all_clients_to_console(),list_of_expected_clients)

    def test_update_client___with_client_id_integer_but_not_existing___A_client_exception_is_raised_There_was_not_any_client_with_the_given_id(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.update_client_by_id("17","Cornel")
        self.assertEqual(str(error.exception),"There is not a client with the given ID!")
    def test_update_client___with_client_id_not_integer___A_client_exception_is_raised_The_ID_is_not_right(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.update_client_by_id("1a","Cornel")
        self.assertEqual(str(error.exception),"The ID is not right!")
    def test_remove_client___with_proper_data___deleted_client_will_not_be_in_the_list_anymore(self):
        list_of_expected_clients= self.__client_service.return_list_of_all_clients_to_console()
        del list_of_expected_clients[0]
        self.__client_service.remove_by_id("12")
        self.assertEqual(self.__client_service.return_list_of_all_clients_to_console(),list_of_expected_clients)
    def test_remove_client___with_client_id_integer_but_not_existing___A_client_exceptions_is_raised_There_is_not_a_client_with_the_given_ID(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.remove_by_id("17")
        self.assertEqual(str(error.exception),"There is not a client with the given ID!")

    def test_remove_client___with_client_id_not_integer___A_client_exception_is_raised_The_id_should_be_an_integer(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.remove_by_id("1a")
        self.assertEqual(str(error.exception),"The id should be an integer")

    def test_search_client_by_id___with_proper_data___A_client_with_given_id_will_be_found(self):
        list_of_expected_clients=self.__client_service.return_list_of_all_clients_to_console()
        client_to_be_found=list_of_expected_clients[0]
        self.__client_service.search_client_by_id("12")
        self.assertEqual(self.__client_service.search_client_by_id("12"),client_to_be_found)
    def test_search_client_by_id___with_client_id_not_integer___A_client_exception_is_raised_The_id_introduced_is_not_right(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.search_client_by_id("1a")
        self.assertEqual(str(error.exception),"The id introduced is not right!")
    def test_search_client_by_id___with_client_id_not_existing___A_client_exception_is_raised_There_was_not_any_client_with_the_given_id(self):
        with self.assertRaises(ClientException) as error:
            self.__client_service.search_client_by_id("19")
        self.assertEqual(str(error.exception),"There was not any client with the given id!")
    def test_search_client_by_name___with_proper_data___list_of_matching_clients_will_be_returned(self):
        list_of_expected_clients=self.__client_service.return_list_of_all_clients_to_console()
        del list_of_expected_clients[0]
        self.assertEqual(list_of_expected_clients,self.__client_service.search_client_by_name("e"))


    def testClient(self):
        self.test_search_client_by_name___with_proper_data___list_of_matching_clients_will_be_returned()
        self.test_search_client_by_id___with_client_id_not_existing___A_client_exception_is_raised_There_was_not_any_client_with_the_given_id()
        self.test_search_client_by_id___with_client_id_not_integer___A_client_exception_is_raised_The_id_introduced_is_not_right()
        self.test_search_client_by_id___with_proper_data___A_client_with_given_id_will_be_found()
        self.test_Client_class___with_proper_data___Asserts_true()
        self.test_add_client___with_proper_data___is_going_to_be_in_the_list()
        self.test_add_client___with_client_id_not_integer___A_client_exception_is_raised_The_id_is_not_right()
        self.test_add_client___with_client_id_already_existing___A_client_exception_is_raised_There_is_already_a_client_with_the_given_id()
        self.test_update_client___with_proper_data___updated_client_is_going_to_be_in_the_list()
        self.test_update_client___with_client_id_integer_but_not_existing___A_client_exception_is_raised_There_was_not_any_client_with_the_given_id()
        self.test_update_client___with_client_id_not_integer___A_client_exception_is_raised_The_ID_is_not_right()
        self.test_remove_client___with_proper_data___deleted_client_will_not_be_in_the_list_anymore()
        self.test_remove_client___with_client_id_integer_but_not_existing___A_client_exceptions_is_raised_There_is_not_a_client_with_the_given_ID()
        self.test_remove_client___with_client_id_not_integer___A_client_exception_is_raised_The_id_should_be_an_integer()
class TestRental(unittest.TestCase):
    def setUp(self) -> None:
        self.__undo_repository = UndoRepository()
        self.__redo_repository = RedoRepository()
        self.__undo_service = UndoService(self.__undo_repository, self.__redo_repository)
        self.__redo_service = RedoService(self.__redo_repository, self.__undo_repository)
        self.__movie_validator = MovieValidator()
        self.__movie_repository = MovieRepository(self.__movie_validator)
        self.__rental_validator = RentalValidator()
        self.__client_validator = ClientValidator()
        self.__client_repository = ClientRepository(self.__client_validator)
        self.__rental_repository = RentalRepository(self.__rental_validator, self.__movie_repository,
                                                    self.__client_repository)
        self.__movie_service=MovieService(self.__movie_repository,self.__client_repository,self.__rental_repository,self.__undo_service,self.__redo_service)
        self.__client_service = ClientService(self.__movie_repository,self.__client_repository,self.__rental_repository,self.__undo_service,self.__redo_service)
        self.__rental_service = RentalService(self.__rental_repository, self.__movie_repository,self.__client_repository)
        rent_date_1=datetime.datetime(2021,12,1)
        returned_date_1=datetime.datetime(2021,12,18)
        due_date_1=datetime.datetime(2021,12,19)
        rent_date_2=datetime.datetime(2021,11,12)
        returned_date_2=datetime.datetime(2021,12,12)
        due_date_2=datetime.datetime(2021,12,27)
        rent_date_3=datetime.datetime(2020,12,29)
        due_date_3=datetime.datetime(2021,1,25)
        returned_date_3=None
        self.__movie_service.add_movie("12", "Batman", "Decent Movie", "Thriller")
        self.__movie_service.add_movie("13", "Fast", "Bad", "Action")
        self.__movie_service.add_movie("14", "Baby Driver", "NOt great", "Romantic")
        self.__client_service.add_client("1","Gicu")
        self.__client_service.add_client("2","Nema")
        self.__client_service.add_client("3","Cornel")
        self.__rental_service.add_rental("1","12","1",rent_date_1,due_date_1,returned_date_1)
        self.__rental_service.add_rental("11","13","2",rent_date_2,due_date_2,returned_date_2)
        self.__rental_service.add_rental("111","13","2",rent_date_3,due_date_3,returned_date_3)


    def test_Rental_class___with_proper_data___Asserts_true(self):
        new_rental=Rental(10,12,1,datetime.datetime(2021,12,3),datetime.datetime(2021,12,18),None)
        self.assertEqual(new_rental.rental_id,10)
        self.assertEqual(new_rental.movie_id,12)
        self.assertEqual(new_rental.client_id,1)
        self.assertEqual(new_rental.rented_date,datetime.datetime(2021,12,3))
        self.assertEqual(new_rental.due_date,datetime.datetime(2021,12,18))
        self.assertEqual(new_rental.returned_date,None)

    def test_rent_a_movie___with_proper_data___new_rent_will_be_in_the_list(self):
        list_of_expected_rentals=self.__rental_service.return_list_of_rentals_to_console()
        new_rental = Rental(10, 12, 1, datetime.datetime(2021, 12, 3), datetime.datetime(2021, 12, 18), None)
        list_of_expected_rentals.append(new_rental)
        self.__rental_service.add_rental("10","12","1",datetime.datetime(2021, 12, 3), datetime.datetime(2021, 12, 18), None)
        self.assertEqual(list_of_expected_rentals,self.__rental_service.return_list_of_rentals_to_console())

    def test_rent_a_movie___with_rental_id_integer_but_already_existing___A_rental_exception_is_raised_there_is_already_a_rental_with_the_given_id(self):
        with self.assertRaises(RentalException) as error:
            self.__rental_service.add_rental("1","12","1",datetime.datetime(2021, 12, 3), datetime.datetime(2021, 12, 18), None)
        self.assertEqual(str(error.exception),"There is already a rental with the given ID")
    def test_rent_a_movie___with_rental_id_not_integer___A_rental_exception_is_raised_The_id_is_not_right(self):
        with self.assertRaises(RentalException) as error:
            self.__rental_service.add_rental("1a", "12", "1", datetime.datetime(2021, 12, 3),
                                             datetime.datetime(2021, 12, 18), None)
        self.assertEqual(str(error.exception),"The ID is not right!")

    def test_rent_a_movie___with_movie_id_not_existing___A_rental_exception_is_raised_Movie_id_or_client_id_not_found(self):
        with self.assertRaises(RentalException) as error:
            self.__rental_service.add_rental("1", "99", "1", datetime.datetime(2021, 12, 3),
                                             datetime.datetime(2021, 12, 18), None)
        self.assertEqual(str(error.exception),"Movie_id or client_id not found!")

    def test_movie_statistics___with_proper_data___sorted_list_of_movies_will_be_created(self):
        list_of_all_movies=self.__movie_service.return_list_of_all_movies_to_console()
        list_of_all_movie_ids_with_number_of_days = self.__movie_service.calculate_rental_day_for_each_movie()
        list_of_sorted_movies = self.__movie_service.create_sorted_list_of_movies(list_of_all_movie_ids_with_number_of_days)
        list_of_expected_sorted_movies=[]
        list_of_expected_sorted_movies.append(list_of_all_movies[1])
        list_of_expected_sorted_movies.append(list_of_all_movies[0])
        list_of_expected_sorted_movies.append(list_of_all_movies[2])
        self.assertEqual(list_of_expected_sorted_movies,list_of_sorted_movies)
    def test_client_statistics___with_proper_data___sorted_list_of_clients_will_be_created(self):
        list_of_all_client_ids_with_number_of_days = self.__client_service.calculate_rental_day_for_each_client()
        list_of_all_clients_sorted = self.__client_service.create_sorted_list_of_clients(
            list_of_all_client_ids_with_number_of_days)
        list_of_all_clients=self.__client_service.return_list_of_all_clients_to_console()
        expected_list_of_all_clients_sorted=[]
        expected_list_of_all_clients_sorted.append(list_of_all_clients[1])
        expected_list_of_all_clients_sorted.append(list_of_all_clients[0])
        expected_list_of_all_clients_sorted.append(list_of_all_clients[2])
        self.assertEqual(list_of_all_clients_sorted,expected_list_of_all_clients_sorted)

    def test_late_rentals_statistics___with_proper_data___sorted_list_of_late_rentals_will_be_created(self):
        list_of_all_rentals=self.__rental_service.return_list_of_rentals_to_console()
        list_of_all_late_rental_ids_with_number_of_days=self.__rental_service.calculate_rental_day_for_each_late_rental()
        list_of_all_late_rentals_sorted=self.__rental_service.create_list_of_sorted_rentals(list_of_all_late_rental_ids_with_number_of_days)
        expected_list_of_all_late_rentals_sorted=[]
        expected_list_of_all_late_rentals_sorted.append(list_of_all_rentals[2])
        self.assertEqual(list_of_all_late_rentals_sorted,expected_list_of_all_late_rentals_sorted)


    def testRental(self):
        self.test_Rental_class___with_proper_data___Asserts_true()
        self.test_rent_a_movie___with_proper_data___new_rent_will_be_in_the_list()
        self.test_rent_a_movie___with_rental_id_integer_but_already_existing___A_rental_exception_is_raised_there_is_already_a_rental_with_the_given_id()
        self.test_rent_a_movie___with_rental_id_not_integer___A_rental_exception_is_raised_The_id_is_not_right()
        self.test_rent_a_movie___with_movie_id_not_existing___A_rental_exception_is_raised_Movie_id_or_client_id_not_found()
        self.test_movie_statistics___with_proper_data___sorted_list_of_movies_will_be_created()
        self.test_client_statistics___with_proper_data___sorted_list_of_clients_will_be_created()

if __name__ == '__main__':
    unittest.main()




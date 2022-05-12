from data_structure import shell_sort
from domain.entities import Movie, Client, Rental
import random
import datetime

from domain.validators import MovieException, ClientException, RentalException


class MovieService:
    """
    This is the class that contains all the function that manages the operations on movies.
    """

    def __init__(self, movie_repository,client_repository, rental_repository,undo_service,redo_service):
        self.__movie_repository = movie_repository
        self.__rental_repository = rental_repository
        self.__client_repository = client_repository
        self.__undo_service=undo_service
        self.__redo_service=redo_service
    def add_movie(self, movie_id, title, description, genre):
        """
        This function is used to create a new_movie and add it to the list of movies, in the repository.
        :param movie_id: Integer value
        :param title: String
        :param description: String
        :param genre: String
        :return: This function doesnt return anything.
        """
        new_movie = Movie(movie_id, title, description, genre)
        self.__movie_repository.add_movie_to_repository(new_movie)
        self.__redo_service.clear_data_from_repository()
        self.__undo_service.add_operation(self.__movie_repository.remove_movie_by_id,(int(movie_id),),self.__movie_repository.add_movie_to_repository,(Movie(movie_id,title,description,genre),))



    def return_list_of_all_movies_to_console(self):
        """
        This function is used to get the list_of_all_movies from the repository and returns it.
        :return: Returns list_of_movies,which is a list of objects created by the class Movies
        """
        return self.__movie_repository.return_list_of_all_movies()

    def generate_20_movies(self):
        """
        This function has 2 list with 21 initialized values and then it shuffles them and creates 20 objects of the class Movie with these values.
        :return:
        """
        list_of_possible_titles = ["Frozen", "Iron Man 3", "Despicable Me 2", "The Hobbit: The Desolation of Smaug",
                                   "The Hunger Games: Catching Fire", "Fast & Furious 3", "Fast & Furious 6", "Gravity",
                                   "Man of Steel", "Jhon Wick", "Love another drugs", "Red Notice", "Rick and Morty",
                                   "Schumacher", "The Guilty", "The Purdge", "Rush", "Baby Driver",
                                   "The Wolf of the Wallstreet", "Batman 3", "Titanic"]
        list_of_possible_descriptions = ["A guy fights other guy"
            , "A girl fight other girl"
            , "Love and peace on mother Earth",
                                         "Always drink your coffe in the morning, so you wont get what this guy got."
            , "A big bear eating honey",
                                         "Batman rises again",
                                         "He said he will be back",
                                         "Geometry movie and cool stuff",
                                         "The big galaxy is not what you think!",
                                         "Eleven comes back from the underworld",
                                         "Fast car goes brrr",
                                         "The Haunted house was in the corner",
                                         "The doll killed them all",
                                         "The dog really loved his human",
                                         "The cat hates water",
                                         "Killer kills everyone!",
                                         "You can not fall asleep watching this movie!",
                                         "You will not want to sleep again after that movie",
                                         "Dont watch in the mirror", "Great movie, bad actors", "Just dont watch it!",
                                         "Just watch it!"]
        list_of_possible_genres = ["horror", "comedy", "action", "adventure", "thriller", "SF", "documentary",
                                   "romantic"]
        random.shuffle(list_of_possible_descriptions)
        random.shuffle(list_of_possible_titles)
        for current_generated_movie_index in range(1, 21):
            random.shuffle(list_of_possible_genres)
            if self.__movie_repository.find_movie_by_id(current_generated_movie_index) is None:
                self.add_movie(str(current_generated_movie_index),
                               list_of_possible_titles[current_generated_movie_index],
                               list_of_possible_descriptions[current_generated_movie_index], list_of_possible_genres[0])

    def remove_by_id(self, id):
        if id.isnumeric():
            id = int(id)
            if self.__movie_repository.find_movie_by_id(id) is None:
                raise MovieException("There is not a movie with the given ID!")
            else:
                deleted_movie=self.__movie_repository.find_movie_by_id(id)
                self.__movie_repository.remove_movie_by_id(id)
                self.__redo_service.clear_data_from_repository()
                self.__undo_service.add_operation(self.__movie_repository.add_movie_to_repository,(deleted_movie,),self.__movie_repository.remove_movie_by_id,(int(id),))
        else:
            raise MovieException("The id should be an integer")

    def update_movie_by_id(self, movie_id, title, description, genre):
        if movie_id.isnumeric():
            movie_id = int(movie_id)
            if self.__movie_repository.find_movie_by_id(movie_id) is None:
                raise MovieException("There is not a movie with the given ID!")
            else:
                old_movie=self.__movie_repository.find_movie_by_id(movie_id)
                old_movie=Movie(old_movie.movie_id,old_movie.title,old_movie.description,old_movie.genre)
                self.__redo_service.clear_data_from_repository()
                self.__movie_repository.update_movie_by_id(movie_id, title, description, genre)
                self.__undo_service.add_operation(self.__movie_repository.update_movie_by_id,(old_movie.movie_id,old_movie.title,old_movie.description,old_movie.genre),self.__movie_repository.update_movie_by_id,(movie_id,title,description,genre))
        else:
            raise MovieException("The ID must be an integer!")

    def search_movie_by_id(self, movie_id):
        if movie_id.isnumeric():
            movie_id = int(movie_id)
            if self.__movie_repository.find_movie_by_id(movie_id) is not None:
                return self.__movie_repository.find_movie_by_id(movie_id)
            else:
                raise MovieException("There is not a movie with the given ID!")
        else:
            raise MovieException("The id introduced is not right!")

    def search_movie_by_title(self, movie_title):
        movie_title = movie_title.lower()
        list_of_all_movies = self.__movie_repository.return_list_of_all_movies()
        list_of_movies_to_display = []
        for current_movie_index in list_of_all_movies:
            current_title = current_movie_index.title.lower()
            if movie_title in current_title:
                list_of_movies_to_display.append(current_movie_index)
        return list_of_movies_to_display

    def search_movie_by_description(self, movie_description):
        movie_description = movie_description.lower()
        list_of_all_movies = self.__movie_repository.return_list_of_all_movies()
        list_of_movies_to_display = []
        for current_movie_index in list_of_all_movies:
            current_description = current_movie_index.description.lower()
            if movie_description in current_description:
                list_of_movies_to_display.append(current_movie_index)
        return list_of_movies_to_display

    def search_movie_by_genre(self, movie_genre):
        movie_genre = movie_genre.lower()
        list_of_all_movies = self.__movie_repository.return_list_of_all_movies()
        list_of_movies_to_display = []
        for current_movie_index in list_of_all_movies:
            current_description = current_movie_index.genre.lower()
            if movie_genre in current_description:
                list_of_movies_to_display.append(current_movie_index)
        return list_of_movies_to_display

    def calculate_rental_day_for_each_movie(self):
        list_of_all_movies = self.__movie_repository.return_list_of_all_movies()
        list_of_all_rentals = self.__rental_repository.return_list_of_all_rentals()
        list_of_total_rent_days=[]
        for current_movie_index in list_of_all_movies:
            total_rent_days=0
            for current_rental_index in list_of_all_rentals:
                if current_rental_index.movie_id==current_movie_index.movie_id and current_rental_index.returned_date != None:
                    rented_days=(current_rental_index.returned_date-current_rental_index.rented_date).days
                    total_rent_days += rented_days
                elif current_rental_index.movie_id==current_movie_index.movie_id:
                    today = datetime.datetime.today()
                    rented_days= (today-current_rental_index.rented_date).days
                    total_rent_days += rented_days
            list_of_total_rent_days.append([current_movie_index.movie_id,total_rent_days])
        list_of_total_rent_days=shell_sort(list_of_all_rentals)
        return list_of_total_rent_days

    def return_number_of_days(self,movie):
        return movie[1]
    def create_sorted_list_of_movies(self,list_of_movie_ids_with_rented_days):
        list_of_all_movies=self.__movie_repository.return_dictionary_of_all_movies()
        list_of_movies_with_rented_days=[]
        for current_movie_index in list_of_movie_ids_with_rented_days:
            list_of_movies_with_rented_days.append(list_of_all_movies[current_movie_index[0]])
        return list_of_movies_with_rented_days

class ClientService:
    """
    This is the class that contains all the function that manages the operations on clients.
    """

    def __init__(self,movie_repository, client_repository,rental_repository,undo_service,redo_service):
        self.__movie_repository = movie_repository
        self.__client_repository = client_repository
        self.__rental_repository=rental_repository
        self.__undo_service=undo_service
        self.__redo_service=redo_service
    def add_client(self, client_id, name):
        """
        This function is used to create a new_client and add it to the list of clients, in the repository.
        :param client_id:Integer value
        :param name:String
        :return:
        """
        new_client = Client(client_id, name)
        self.__client_repository.add_client_to_repository(new_client)
        self.__redo_service.clear_data_from_repository()
        self.__undo_service.add_operation(self.__client_repository.remove_client_by_id, (int(client_id),),
                                          self.__client_repository.add_client_to_repository, (Client(client_id,name),))

    def generate_20_clients(self):
        """
        This function has one list with 21 initialized values and then it shuffles them and creates 20 objects of the class Movie with these values
        """
        list_of_possible_names = ["Tom Ford", "Gigi Becali", "Popescu Mihai", "Mihai Daniel", "Andreea Bostanica",
                                  "Mara Ognean", "Acel Mihai", "Kuruma Vohusa", "Lori Mihaiel", "Freud Zsigmond",
                                  "Cristi Munteanu", "Cozma Andrei", "Denisa Caruntu", "Asofronie Rares", "Rosca Rares",
                                  "Iasmy Hugo", "Gastry Michael", "Hughis Han", "Ginghis Han", "Napoleon Bonaparte",
                                  "Esmeralda Martinez"]
        random.shuffle(list_of_possible_names)
        index = 1
        for current_generated_client_index in range(1, 21):
            if self.__client_repository.find_client_by_id(current_generated_client_index) is None:
                self.add_client(str(index),
                                list_of_possible_names[current_generated_client_index])
            index += 1

    def return_list_of_all_clients_to_console(self):
        """
        This function is used to get the list_of_all_clients from the repository and returns it.
        :return: Returns list_of_clients,which is a list of objects created by the class Client
        """
        return self.__client_repository.return_list_of_all_clients()

    def remove_by_id(self, id):
        if str(id).isnumeric():
            id = int(id)
            if self.__client_repository.find_client_by_id(id) is None:
                raise ClientException("There is not a client with the given ID!")
            else:
                deleted_client = self.__client_repository.find_client_by_id(id)
                self.__client_repository.remove_client_by_id(id)
                self.__redo_service.clear_data_from_repository()
                self.__undo_service.add_operation(self.__client_repository.add_client_to_repository, (deleted_client,),self.__client_repository.remove_client_by_id, (int(id),))

        else:
            raise ClientException("The id should be an integer")

    def update_client_by_id(self, client_id, name):
        if str(client_id).isnumeric():
            client_id = int(client_id)
            if self.__client_repository.find_client_by_id(client_id) is None:
                raise ClientException("There is not a client with the given ID!")
            else:
                old_client=self.__client_repository.find_client_by_id(client_id)
                old_client=Client(old_client.client_id,old_client.name)
                self.__redo_service.clear_data_from_repository()
                self.__client_repository.update_client_by_id(client_id, name)
                self.__undo_service.add_operation(self.__client_repository.update_client_by_id,(old_client.client_id,old_client.name),self.__client_repository.update_client_by_id,(client_id,name))
        else:
            raise ClientException("The ID is not right!")

    def search_client_by_id(self, client_id):
        if client_id.isnumeric():
            client_id = int(client_id)
            if self.__client_repository.find_client_by_id(client_id) is not None:
                return self.__client_repository.find_client_by_id(client_id)
            else:
                raise ClientException("There was not any client with the given id!")

        else:
            raise ClientException("The id introduced is not right!")

    def search_client_by_name(self, client_name):
        client_name = client_name.lower()
        list_of_all_clients = self.__client_repository.return_list_of_all_clients()
        list_of_clients_to_display = []
        for current_client_index in range(0, len(list_of_all_clients)):
            current_client_name = list_of_all_clients[current_client_index].name.lower()
            if client_name in current_client_name:
                list_of_clients_to_display.append(list_of_all_clients[current_client_index])
        return list_of_clients_to_display
    def calculate_rental_day_for_each_client(self):
        list_of_all_clients = self.__client_repository.return_list_of_all_clients()
        list_of_all_rentals = self.__rental_repository.return_list_of_all_rentals()
        list_of_total_rent_days=[]
        for current_movie_index in list_of_all_clients:
            total_rent_days=0
            for current_rental_index in list_of_all_rentals:
                if current_rental_index.client_id==current_movie_index.client_id and current_rental_index.returned_date != None:
                    rented_days=(current_rental_index.returned_date-current_rental_index.rented_date).days
                    total_rent_days += rented_days
                elif current_rental_index.client_id==current_movie_index.client_id:
                    today = datetime.datetime.today()
                    rented_days= (today-current_rental_index.rented_date).days
                    total_rent_days += rented_days
            list_of_total_rent_days.append([current_movie_index.client_id,total_rent_days])
        list_of_total_rent_days.sort(reverse=True,key=self.return_number_of_days)
        return list_of_total_rent_days
    def return_number_of_days(self,client):
        return client[1]
    def create_sorted_list_of_clients(self,list_of_client_ids_with_rented_days):
        list_of_all_clients=self.__client_repository.return_dictionary_of_all_clients()
        list_of_clients_with_rented_days=[]
        for current_client_index in list_of_client_ids_with_rented_days:
            list_of_clients_with_rented_days.append(list_of_all_clients[current_client_index[0]])
        return list_of_clients_with_rented_days

class RentalService:
    """
    This is the class that contains all the functions that manages the operations on rentals.
    """

    def __init__(self, rental_repository, movie_repository, client_repository):
        self.__rental_repository = rental_repository
        self.__movie_repository = movie_repository
        self.__client_repository = client_repository

    def add_rental(self, rental_id, client_id, movie_id, rented_date, due_date, return_date):
        """
        This function is used to get a new rental and to add it to the list_of_all_rentals.
        :param rental_id: Integer
        :param client_id: Integer
        :param movie_id: Integer
        :param rented_date: Date
        :param due_date: date>rented_date
        :param return_date: Date, or None, if the movie wasnt returned yet.
        :return: This function doesnt return anything.
        """
        if client_id.isnumeric() and rental_id.isnumeric() and movie_id.isnumeric():
            client_id=int(client_id)
            rental_id=int(rental_id)
            movie_id=int(movie_id)
            new_rental = Rental(rental_id, client_id, movie_id, rented_date, due_date, return_date)
            self.__rental_repository.add_rental_to_repository(new_rental)
        else:
            raise RentalException("The ID is not right!")

    def generate_20_rentals(self):
        """
        This function generates 20 rentals, using the random library, and datetime.
        :return:
        """
        start_date = datetime.datetime(2020, 1, 1)
        end_date = datetime.datetime(2021, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_to_create_non_returned_rental = random.randint(2, 6)
        for current_generated_rental_index in range(1, 21):
            random_number_of_days = random.randrange(days_between_dates)
            rented_date = start_date + datetime.timedelta(days=random_number_of_days)
            due_date = rented_date + datetime.timedelta(days=15)
            days_after_which_the_client_returned = random.randrange(30)
            return_date = rented_date + datetime.timedelta(days=days_after_which_the_client_returned)
            client_id = random.randint(1, 19)
            movie_id = random.randint(1, 20)
            if current_generated_rental_index % random_number_to_create_non_returned_rental == 0:
                return_date = None
            if self.__rental_repository.find_rental_by_id(current_generated_rental_index) is None:
                self.add_rental(str(current_generated_rental_index), str(client_id), str(movie_id), rented_date, due_date, return_date)

    def return_list_of_rentals_to_console(self):
        """
        This function is used to return the list of all rentals
        :return:
        """
        return self.__rental_repository.return_list_of_all_rentals()

    def check_rental(self, rental_id, movie_id, client_id, rented_date, due_date, return_date):
        if self.__movie_repository.find_movie_by_id(
                int(movie_id)) is None or self.__client_repository.find_client_by_id(int(client_id)) is None:
            raise RentalException("client/movie not found")
        elif rental_id.isnumeric() and movie_id.isnumeric() and client_id.isnumeric():
            rental_id = int(rental_id)
            movie_id = int(movie_id)
            client_id = int(client_id)
            rental_found_by_client_id = self.find_rental_by_client_id(client_id)
        else:
            raise RentalException("The ids must be integers")
        if rented_date > due_date:
            raise RentalException("The due_date is not right!")

        elif rental_found_by_client_id is None:
            self.add_rental(str(rental_id), str(movie_id), str(client_id), rented_date, due_date, return_date)
        elif rental_found_by_client_id.returned_date is None:
            raise RentalException("Cant rent because the last movie wasnt returned!")
        else:
            self.add_rental(str(rental_id), str(movie_id), str(client_id), rented_date, due_date, return_date)

    def find_rental_by_client_id(self, client_id):
        list_of_all_rentals = self.__rental_repository.return_list_of_all_rentals()
        for current_rental_index in range(0, len(list_of_all_rentals)):
            if list_of_all_rentals[current_rental_index].client_id == client_id:
                return list_of_all_rentals[current_rental_index]
        return None

    def return_movie(self, rental_id, movie_id, client_id):
        if self.__movie_repository.find_movie_by_id(
                int(movie_id)) is None or self.__client_repository.find_client_by_id(int(client_id)) is None:
            raise RentalException("client/movie not found")
        elif rental_id.isnumeric() and movie_id.isnumeric() and client_id.isnumeric():
            rental_id = int(rental_id)
            movie_id = int(movie_id)
            client_id = int(client_id)
            if self.__rental_repository.find_rental_by_id(
                    rental_id).movie_id != movie_id or self.__rental_repository.find_rental_by_id(
                    rental_id).client_id != client_id:
                raise RentalException("The informations introduced are not right!")
            elif self.__rental_repository.find_rental_return_date(rental_id) is not None:
                raise RentalException("The movie that you want to return was already returned!")
            else:
                return_date = datetime.datetime.today()
                return_date = return_date.replace(hour=0, minute=0, second=0, microsecond=0)
                self.__rental_repository.find_rental_by_id(rental_id).returned_date = return_date

    def calculate_rental_day_for_each_late_rental(self):
        list_of_all_rentals = self.__rental_repository.return_list_of_all_rentals()
        list_of_total_rent_day_for_late_rentals=[]
        for current_rental_index in list_of_all_rentals:
            total_rent_days=0
            if current_rental_index.returned_date is None:
                today = datetime.datetime.today()
                rented_days = (today - current_rental_index.rented_date).days
                total_rent_days += rented_days
                list_of_total_rent_day_for_late_rentals.append([current_rental_index.rental_id, total_rent_days])
        list_of_total_rent_day_for_late_rentals.sort(reverse=True, key=self.return_number_of_days)
        return list_of_total_rent_day_for_late_rentals
    def return_number_of_days(self,rental):
        return rental[1]
    def create_list_of_sorted_rentals(self,list_of_rental_ids_with_rented_days):
        list_of_all_rentals=self.__rental_repository.return_dictionary_of_all_rentals()
        list_of_rental_with_rented_days=[]
        for current_rental_index in list_of_rental_ids_with_rented_days:
            list_of_rental_with_rented_days.append(list_of_all_rentals[current_rental_index[0]])
        print(list_of_rental_with_rented_days)
        return list_of_rental_with_rented_days
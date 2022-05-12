import datetime
from datetime import date
from domain.validators import MovieRentalException, RentalException, ClientException, MovieException


class Console:
    """
    This is the Console, that will contain all the UI functions. We will run this in the main.py.
    """

    def __init__(self, movie_service, client_service, rental_service,undo_service,redo_service):
        self.__movie_service = movie_service
        self.__client_service = client_service
        self.__rental_service = rental_service
        self.__undo_service= undo_service
        self.__redo_service=redo_service

    def add_movie_ui(self):
        """
        This function is a UI function that gets 4 inputs: movie_id,title,description,genre.
        If there was a Exception raised, it prints the exception, if not, it accesses the add_movie function from the class MovieService, in services.py
        :return: This function doesnt return anything.
        """
        movie_id_of_movie_to_add = input("Whats the id of the movie you want to add?")
        title_of_movie_to_add = input("Whats the title of the movie you want to add?")
        description_of_movie_to_add = input("Whats the description of the movie you want to add?")
        genre_of_movie_to_add = input("Whats the genre of the movie you want to add?")
        try:
            self.__movie_service.add_movie(movie_id_of_movie_to_add, title_of_movie_to_add, description_of_movie_to_add,
                                           genre_of_movie_to_add)
        except MovieRentalException as error:
            print(error)

    def add_client_ui(self):
        client_id_to_add = input("Whats the id of the client you want to add?")
        name_of_client_to_add = input("Whats the name of the client you want to add?")
        try:
            self.__client_service.add_client(client_id_to_add, name_of_client_to_add)
        except MovieRentalException as error:
            print(error)

    def list_client_ui(self):
        for current_client in self.__client_service.return_list_of_all_clients_to_console():
            print("Client ID: " + str(current_client.client_id) + " Name " + str(
                current_client.name))

    def list_movie_ui(self):
        """
        This is a UI function that gets the list_of_all_movies and goes throught the list, printing everything.
        :return:
        """
        list_of_all_movies = self.__movie_service.return_list_of_all_movies_to_console()
        for current_movie_index in range(0, len(list_of_all_movies)):
            print("Movie ID: " + str(list_of_all_movies[current_movie_index].movie_id) + " Title " + str(
                list_of_all_movies[current_movie_index].title) + " Description: " + str(
                list_of_all_movies[current_movie_index].description) + " Genre:" + str(
                list_of_all_movies[current_movie_index].genre))

    def remove_movie_ui(self):
        """
        This is a UI function that gets an input, which is the ID we need to delete.
        :return:
        """
        id_that_we_need_to_delete=input("Whats the id of the movie that you want to delete?")
        try:
            self.__movie_service.remove_by_id(id_that_we_need_to_delete)
        except MovieRentalException as error:
            print(error)
    def remove_client_ui(self):
        """
        This is a UI function that gets an input, which is the ID we need to delete.
        :return:
        """

        id_that_we_need_to_delete=input("Whats the id of the movie that you want to delete?")
        try:
            self.__client_service.remove_by_id(id_that_we_need_to_delete)
        except MovieRentalException as error:
            print(error)

    def update_movie_ui(self):
        movie_id=input("Whats the id you want to change?")
        title=input("whats the title you want to change?")
        description=input("Whats the description you want to change?")
        genre=input("Whats the genre you want to change?")
        try:
            self.__movie_service.update_movie_by_id(movie_id,title,description,genre)
        except MovieRentalException as error:
            print(error)



    def update_client_ui(self):
        client_id=input("Whats the id you want to change?")
        name=input("whats the name you want to change?")
        try:
            self.__client_service.update_client_by_id(client_id,name)
        except MovieRentalException as error:
            print(error)

    def list_rentals_ui(self):
        """
        This is a function that gets the list of all rentals and prints everything.
        :return:
        """
        list_of_all_rentals = self.__rental_service.return_list_of_rentals_to_console()
        for current_rental_index in range(0, len(list_of_all_rentals)):
            print("Rental ID " + str(list_of_all_rentals[current_rental_index].rental_id) + " Client ID " + str(
                list_of_all_rentals[current_rental_index].client_id) + " Movie ID " + str(
                list_of_all_rentals[current_rental_index].movie_id) + "Rental Date " + str(
                list_of_all_rentals[current_rental_index].rented_date) + " Due Date " + str(
                list_of_all_rentals[current_rental_index].due_date) + " Return Date " + str(
                list_of_all_rentals[current_rental_index].returned_date))
    def rent_a_movie_ui(self):
        rental_id=input("whats the rental id ?")
        movie_id=input("Whats the movie id you want to rent?")
        client_id=input("Whats the client id you want to rent?")
        rented_date=datetime.datetime.today()
        rented_date=rented_date.replace(hour=0, minute=0, second=0, microsecond=0)
        year=input("Whats the year you want to return the movie?")
        month=input("Whats the month you want to return the movie?")
        day=input("Whats the day you want to return the movie?")
        if year.isnumeric() and month.isnumeric() and day.isnumeric():
            due_date=datetime.datetime(int(year),int(month),int(day))
        else:
            print("Year,month and day should be integers")
        return_date=None
        try:
            self.__rental_service.check_rental(str(rental_id),str(movie_id),str(client_id),rented_date,due_date,return_date)
        except RentalException as error:
            print(error)
    def return_a_movie_ui(self):
        rental_id=input("whats the rental id ?")
        movie_id=input("Whats the movie id you want to return?")
        client_id=input("Whats the client id you want to return?")
        try:
            self.__rental_service.return_movie(rental_id,movie_id,client_id)
        except RentalException as error:
            print(error)
    def search_clients_ui(self):
        search_type=input("what do you want to search the clients by? ID or Name")
        if search_type=="id":
            try:
                client_id=input("Whats the id you want to search?")
                client_to_display=self.__client_service.search_client_by_id(client_id)
                print("Client ID: " + str(client_to_display.client_id) + " Name " + str(
                    client_to_display.name))
            except ClientException as error:
                print(error)
        elif search_type=="name":
            try:
                client_name=input("Whats the name you want to search?")
                list_of_clients_to_display=self.__client_service.search_client_by_name(client_name)
                if len(list_of_clients_to_display)==0:
                    raise ClientException("There is not any client with the given name!")
                for current_client in list_of_clients_to_display:
                    print("Client ID: " + str(current_client.client_id) + " Name " + str(
                        current_client.name))
            except ClientException as error:
                print(error)
    def search_movies_ui(self):
        search_type=input("What do you want to search the movies by? id,title,description,genre")
        if search_type=="id":
            try:
                movie_id=input("Whats the id you want to search?")
                movie_to_display=self.__movie_service.search_movie_by_id(movie_id)
                print("Movie ID: " + str(movie_to_display.movie_id) + " Title " + str(
                    movie_to_display.title) + " Description: " + str(
                    movie_to_display.description) + " Genre:" + str(
                    movie_to_display.genre))
            except MovieException as error:
                print(error)
        elif search_type=="title":
            try:
                movie_title=input("Whats the title you want to search?")
                list_of_movies_to_display=self.__movie_service.search_movie_by_title(movie_title)
                if len(list_of_movies_to_display)==0:
                    raise MovieException("There is not any movie with the given title!")
                for current_movie in list_of_movies_to_display:
                    print("Movie ID: " + str(current_movie.movie_id) + " Title " + str(
                        current_movie.title) + " Description: " + str(
                        current_movie.description) + " Genre:" + str(
                        current_movie.genre))
            except MovieException as error:
                print(error)
        elif search_type=="description":
            try:
                movie_description=input("Whats the description you want to search?")
                list_of_movies_to_display=self.__movie_service.search_movie_by_description(movie_description)
                if len(list_of_movies_to_display)==0:
                    raise MovieException("There is not any movie with the given title!")
                for current_movie in list_of_movies_to_display:
                    print("Movie ID: " + str(current_movie.movie_id) + " Title " + str(
                        current_movie.title) + " Description: " + str(
                        current_movie.description) + " Genre:" + str(
                        current_movie.genre))
            except MovieException as error:
                print(error)
        elif search_type=="genre":
            try:
                movie_genre=input("Whats the description you want to search?")
                list_of_movies_to_display=self.__movie_service.search_movie_by_genre(movie_genre)
                if len(list_of_movies_to_display)==0:
                    raise MovieException("There is not any movie with the given title!")
                for current_movie in list_of_movies_to_display:
                    print("Movie ID: " + str(current_movie.movie_id) + " Title " + str(
                        current_movie.title) + " Description: " + str(
                        current_movie.description) + " Genre:" + str(
                        current_movie.genre))
            except MovieException as error:
                print(error)
    def print_sorted_list_of_movies(self):
        list_of_all_movie_ids_with_number_of_days=self.__movie_service.calculate_rental_day_for_each_movie()
        list_of_all_movies=self.__movie_service.create_sorted_list_of_movies(list_of_all_movie_ids_with_number_of_days)
        for current_movie_index in list_of_all_movies:
            print("Movie ID: " + str(current_movie_index.movie_id) + " Title " + str(
                current_movie_index.title) + " Description: " + str(
                current_movie_index.description) + " Genre:" + str(
                current_movie_index.genre))
    def print_sorted_list_of_clients(self):
        list_of_all_client_ids_with_number_of_days=self.__client_service.calculate_rental_day_for_each_client()
        list_of_all_clients=self.__client_service.create_sorted_list_of_clients(list_of_all_client_ids_with_number_of_days)
        for current_client_index in list_of_all_clients:
            print("Client ID: " + str(current_client_index.client_id) + " Name " + str(
                current_client_index.name))
    def print_sorted_list_of_late_rentals(self):
        list_of_all_late_rental_ids_with_number_of_days=self.__rental_service.calculate_rental_day_for_each_late_rental()
        list_of_all_rentals=self.__rental_service.create_list_of_sorted_rentals(list_of_all_late_rental_ids_with_number_of_days)

        for current_rental_index in list_of_all_rentals:
            print("Rental ID " + str(current_rental_index.rental_id) + " Client ID " + str(
                current_rental_index.client_id) + " Movie ID " + str(
                current_rental_index.movie_id) + "Rental Date " + str(
                current_rental_index.rented_date) + " Due Date " + str(
                current_rental_index.due_date) + " Return Date " + str(
                current_rental_index.returned_date))
    def run_console(self):
        """
        This is a UI function that runs the console and also prints the menu.
        :return: This function doesnt return anything.
        """
        # self.__movie_service.generate_20_movies()
        # self.__client_service.generate_20_clients()
        # self.__rental_service.generate_20_rentals()
        while True:
            self.print_menu()
            user_command = self.read_command()
            if user_command == 'a1':
                self.add_movie_ui()
            elif user_command == 'a2':
                self.add_client_ui()
            elif user_command == 'l1':
                self.list_movie_ui()
            elif user_command == 'l2':
                self.list_client_ui()
            elif user_command == 'r1':
                self.remove_movie_ui()
            elif user_command == 'r2':
                self.remove_client_ui()
            elif user_command == "l3":
                self.list_rentals_ui()
            elif user_command == "u1":
                self.update_movie_ui()
            elif user_command == "u2":
                self.update_client_ui()
            elif user_command == "rent":
                self.rent_a_movie_ui()
            elif user_command == "return":
                self.return_a_movie_ui()
            elif user_command == "stat":
                statistics_type=input("What statistics you want to see?movies, clients,late rentals?")
                if statistics_type=="movies":
                    self.print_sorted_list_of_movies()
                elif statistics_type=="clients":
                    self.print_sorted_list_of_clients()
                elif statistics_type=="late":
                    self.print_sorted_list_of_late_rentals()
            elif user_command == "search":
                object_to_search=input("What do you want to search client or movie?")
                if object_to_search=="client":
                    self.search_clients_ui()
                else:
                    self.search_movies_ui()
            elif user_command == "undo":
                self.__undo_service.pop_out()
            elif user_command == "redo":
                self.__redo_service.pop_out()
    def read_command(self):
        """
        This is a UI function that gets an input and returns the given value.
        It is used to read a command
        :return: Returns a string.
        """
        user_command = input("What do you want to do with the program?")
        return user_command

    def print_menu(self):
        """
        This is a UI function that prints the option that the user has.
        :return: This function doesnt return anything.
        """
        print("Write a1 to add movies")
        print("Write a2 to add clients")
        print("Write l1 to list movies")
        print("Write l2 to list clients")
        print("Write l3 to list rentals")
        print("write r1 to remove movies")
        print("write r2 to remove clients")
        print("write u1 to update movies")
        print("write u2 to update clients")
        print("write rent to add a rental")
        print("write stat to calculate statistics!")
        print("write search to search for clients/movies!")

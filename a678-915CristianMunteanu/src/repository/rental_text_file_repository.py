import datetime
import os

from repository.repository import RentalRepository

from domain.entities import Rental


class RentalTextFileRepository(RentalRepository):
    def __init__(self,file_name,movie_repository,client_repository):
        super().__init__(movie_repository,client_repository)
        self.__file_name=file_name
        if not os.path.exists(self.__file_name):
            self.update_file()
        self.load()

    def load(self):
        with open(self.__file_name,"rt") as file:
            for line in file.readlines():
                line=line.strip()
                rental_id,movie_id,client_id,rented_date_str,due_date_str,returned_date_str=line.split(",")
                rented_date=datetime.datetime.strptime(rented_date_str,"%Y-%m-%d %H:%M:%S").date()
                due_date=datetime.datetime.strptime(due_date_str,"%Y-%m-%d %H:%M:%S").date()
                if returned_date_str == "None":
                    returned_date=None
                else:
                    returned_date=datetime.datetime.strptime(returned_date_str,"%Y-%m-%d %H:%M:%S").date()
                self.add_rental_to_repository(Rental(int(rental_id),int(movie_id),int(client_id),rented_date,due_date,returned_date))
        file.close()
    def update_file(self):
        file=open(self.__file_name,"wt")
        for rental in self._list_of_rentals.values():
            file.write(f"{rental.rental_id},{rental.movie_id},{rental.client_id},{rental.rented_date} 00:00:00,{rental.due_date} 00:00:00,{rental.returned_date}\n")
        file.close()
    def add_rental_to_repository(self, rental):
        super().add_rental_to_repository(rental)
        self.update_file()
    def set_return_date(self, rental_id, return_date):
        super().set_return_date(rental_id,return_date)
        self.update_file()
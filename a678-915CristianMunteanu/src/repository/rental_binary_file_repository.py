from repository.repository import RentalRepository
import pickle
import os.path

class RentalBinaryFileRepository(RentalRepository):
    def __init__(self,file_name,movie_repository,client_repository):
        super().__init__(movie_repository,client_repository)
        self.__file_name=file_name
        if not os.path.exists(self.__file_name):
            self.save()
        self.load()
    def load(self):
        file=open(self.__file_name,"rb")
        self._list_of_rentals=pickle.load(file)
        file.close()
    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._list_of_rentals,file)
        file.close()
    def add_rental_to_repository(self, rental):
        super(RentalBinaryFileRepository,self).add_rental_to_repository(rental)
        self.save()
    def set_return_date(self, rental_id, return_date):
        super().set_return_date(int(rental_id),return_date)
        self.save()
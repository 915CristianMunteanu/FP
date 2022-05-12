from repository.repository import  ClientRepository
import pickle
import os.path

class ClientBinaryFileRepository(ClientRepository):
    def __init__(self,file_name):
        super().__init__()
        self.__file_name=file_name
        if not os.path.exists(self.__file_name):
            self.save()
        self.load()
    def load(self):
        file=open(self.__file_name,"rb")
        self._list_of_clients=pickle.load(file)
        file.close()
    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._list_of_clients,file)
        file.close()
    def add_client_to_repository(self, client):
        super(ClientBinaryFileRepository,self).add_client_to_repository(client)
        self.save()
    def remove_client_by_id(self, id):
        super(ClientBinaryFileRepository,self).remove_client_by_id(id)
        self.save()
    def update_client_by_id(self, client_id, name):
        super(ClientBinaryFileRepository,self).update_client_by_id(int(client_id),name)
        self.save()


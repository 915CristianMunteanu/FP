import os

from repository.repository import ClientRepository

from domain.entities import Client


class ClientTextFileRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        if not os.path.exists(self.__file_name):
            self.update_file()
        self.load()

    def update_file(self):
        file = open(self.__file_name, "wt")
        for client in self._list_of_clients.values():
            file.write(f"{client.client_id},{client.name}\n")
        file.close()

    def load(self):
        with open(self.__file_name, "r") as file:
            for line in file.readlines():
                line = line.strip()
                client_id,name = line.split(sep=",", maxsplit=1)
                self.add_client_to_repository(Client(int(client_id), name))
        file.close()

    def add_client_to_repository(self, client):
        super(ClientTextFileRepository,self).add_client_to_repository(client)
        self.update_file()

    def remove_client_by_id(self, id):
        super(ClientTextFileRepository,self).remove_client_by_id(id)
        self.update_file()

    def update_client_by_id(self, client_id, name):
        super(ClientTextFileRepository,self).update_client_by_id(client_id, name)
        self.update_file()

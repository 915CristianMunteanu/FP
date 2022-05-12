
class Settings:
    def __init__(self):
        self.__repository_type="inmemory"
        self.__movies_file_name=""
        self.__clients_file_name=""
        self.__rentals_file_name=""
        file=open("settings.properties","rt")
        repository_line=file.readline().strip()
        movies_line=file.readline().strip()
        clients_line=file.readline().strip()
        rentals_line=file.readline().strip()
        repository_line=repository_line[repository_line.find("=")+2:]
        movies_line=movies_line[movies_line.find("=")+2:]
        clients_line=clients_line[clients_line.find("=")+2:]
        rentals_line=rentals_line[rentals_line.find("=")+2:]
        self.__repository_type=repository_line
        self.__movies_file_name=movies_line[1:-1]
        self.__clients_file_name=clients_line[1:-1]
        self.__rentals_file_name=rentals_line[1:-1]
    @property
    def repository_type(self):
        return self.__repository_type

    @repository_type.setter
    def repository_type(self, value):
        self.__repository_type=value
    @property
    def movies_file_name(self):
        return self.__movies_file_name

    @movies_file_name.setter
    def movies_file_name(self, value):
        self.__movies_file_name=value

    @property
    def clients_file_name(self):
        return self.__clients_file_name

    @clients_file_name.setter
    def clients_file_name(self, value):
        self.__clients_file_name=value

    @property
    def rentals_file_name(self):
        return self.__rentals_file_name

    @rentals_file_name.setter
    def rentals_file_name(self, value):
        self.__rentals_file_name=value
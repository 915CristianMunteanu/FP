from data_structure import DataStructure, shell_sort
from repository.client_binary_file_repository import ClientBinaryFileRepository
from repository.client_text_file_repository import ClientTextFileRepository
from repository.movie_binary_file_repository import MovieBinaryFileRepository
from repository.rental_binary_file_repository import RentalBinaryFileRepository
from repository.repository import UndoRepository, RedoRepository, ClientRepository, MovieRepository, RentalRepository
from services.RedoService import RedoService
from services.UndoService import UndoService
from services.services import MovieService, ClientService, RentalService

from repository.movie_text_file_repository import MovieTextFileRepository
from repository.rental_text_file_repository import RentalTextFileRepository
from settings import Settings
from ui.console import Console

if __name__=='__main__':
    settings=Settings()
    movie_repository=None
    client_repository=None
    rental_repository=None
    if settings.repository_type=="inmemory":
        movie_repository=MovieRepository()
        client_repository=ClientRepository()
        rental_repository = RentalRepository(movie_repository,client_repository)
    elif settings.repository_type=="textfiles":
        movie_repository=MovieTextFileRepository(settings.movies_file_name)
        client_repository=ClientTextFileRepository(settings.clients_file_name)
        rental_repository=RentalTextFileRepository(settings.rentals_file_name,movie_repository,client_repository)
    elif settings.repository_type=="binaryfiles":
        movie_repository = MovieBinaryFileRepository(settings.movies_file_name)
        client_repository = ClientBinaryFileRepository(settings.clients_file_name)
        rental_repository = RentalBinaryFileRepository(settings.rentals_file_name, movie_repository,client_repository)

    undo_repository = UndoRepository()
    redo_repository = RedoRepository()
    undo_service = UndoService(undo_repository, redo_repository)
    redo_service = RedoService(redo_repository, undo_repository)
    movie_service = MovieService(movie_repository, client_repository, rental_repository, undo_service, redo_service)
    client_service = ClientService(movie_repository, client_repository, rental_repository, undo_service, redo_service)
    rental_service = RentalService(rental_repository, movie_repository, client_repository)
    console = Console(movie_service, client_service, rental_service, undo_service, redo_service)
    print(settings.repository_type)
    console.run_console()

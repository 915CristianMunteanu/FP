from domain.validators import MovieValidator, ClientValidator, RentalValidator
from repository.repository import MovieRepository, ClientRepository, RentalRepository, RedoRepository, UndoRepository
from services.RedoService import RedoService
from services.UndoService import UndoService
from services.services import MovieService, ClientService, RentalService
from ui.console import Console
undo_repository=UndoRepository()
redo_repository=RedoRepository()
undo_service = UndoService(undo_repository,redo_repository)
redo_service = RedoService(redo_repository,undo_repository)
client_validator = ClientValidator()
client_repository = ClientRepository(client_validator)
movie_validator = MovieValidator()
movie_repository = MovieRepository(movie_validator)
rental_validator = RentalValidator()
rental_repository = RentalRepository(rental_validator, movie_repository, client_repository)
movie_service = MovieService(movie_repository, client_repository, rental_repository,undo_service,redo_service)
client_service = ClientService(movie_repository, client_repository, rental_repository,undo_service,redo_service)
rental_service = RentalService(rental_repository, movie_repository, client_repository)
console = Console(movie_service, client_service, rental_service, undo_service,redo_service)

console.run_console()

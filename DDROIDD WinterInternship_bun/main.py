from Repositories.Repository import ChildRepository, ItemRepository, LetterRepository
from SantaClauseConsoleApp import Program
from UI.Console import Console

if __name__ == '__main__':
    child_repository = ChildRepository()
    item_repository = ItemRepository()
    letter_repository = LetterRepository(child_repository, item_repository)
    console = Console()
    program_to_run=Program(child_repository,item_repository,letter_repository,console)


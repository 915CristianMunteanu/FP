from UI.console import Console
from doimain.board import Board
from services.board_service import BoardService


def main():
    board=Board(6,7)
    board_service=BoardService(board)
    console=Console(board_service)
    console.run_game()
main()
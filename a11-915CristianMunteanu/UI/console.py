from doimain.cell_validator import PositionShouldBeTheLowestPossible, PositionIsOutsideTheBoard, PositionAlreadyTaken


class Console:
    def __init__(self,board_service):
        self.__board_service=board_service
    def print_board(self):

        for row in range(5,-1,-1):
            for column in range(0,7):
                print(self.__board_service.get_value_from_certain_position_on_board(row,column),end=" ")
            print()

    def run_game(self):
        turn = 0
        self.print_board()
        while True:
            if turn == 0:
                print("Player turn:")
                new_line = input("line=")
                new_column = input("column=")
                try:
                    new_line = int(new_line)
                    new_column = int(new_column)
                except ValueError:
                    print("Invalid input!")
                    continue
                try:
                    if self.__board_service.player_move(new_line, new_column) is True:
                        self.print_board()
                        print("You won!")
                        exit()

                    self.print_board()
                except PositionAlreadyTaken as error:
                    print(error)
                    continue
                except PositionIsOutsideTheBoard as error:
                    print(error)
                    continue
                except PositionShouldBeTheLowestPossible as error:
                    print(error)
                    continue

            else:
                print("Computer move:")
                if self.__board_service.computer_move() is True:
                    self.print_board()
                    print('Computer won! You have lost!')
                    exit()
                self.print_board()

            turn = 1 - turn
from doimain.board_validator import BoardValidator
from doimain.cell import Cell
from doimain.cell_validator import CellValidator


class BoardService:
    def __init__(self, board):
        self.__board = board
        self.__last_player_cell = Cell
        self.__number_of_rounds = 0

    def player_move(self, row, column):
        if CellValidator(self.__board, row, column).validate() is True:
            self.__last_player_cell = Cell(row, column, "X")
            self.__number_of_rounds += 1
            self.__board.set_value_from_certain_position_on_board(row, column, "X")
            return self.check_for_winning()

    def computer_move(self):
        computer_cell = self.strategy()
        if computer_cell is not None:
            self.__board.set_value_from_certain_position_on_board(computer_cell.row, computer_cell.column, "Y")
        else:
            return False
        return self.check_for_winning()

    def get_board(self, row, column):
        return self.__board.get_value_from_certain_position_on_board(row, column)

    def strategy(self):
        cell_to_be_completed=None
        for row in range(0,6):
            for column in range(0,7):
                if self.__board.get_value_from_certain_position_on_board(row,column)==0:
                    if row >=1 and self.__board.get_value_from_certain_position_on_board(row-1,column)==0:
                        continue
                    self.__board.set_value_from_certain_position_on_board(row,column,"X")
                    if self.check_for_winning() is True:
                        cell_to_be_completed=Cell(row,column,"Y")
                    self.__board.set_value_from_certain_position_on_board(row,column,"Y")
                    if self.check_for_winning() is True:

                        return Cell(row,column,"Y")
                    self.__board.set_value_from_certain_position_on_board(row,column,0)
        if cell_to_be_completed is None:
            possible_cells=self.get_position_next_to_player_move()
            if len(possible_cells)==0:
                cell_to_be_completed=self.get_next_free_position()
                return cell_to_be_completed
            cell_to_be_completed=possible_cells[0]
        return cell_to_be_completed

    def get_position_next_to_player_move(self):
        possible_cells=[]
        if BoardValidator().validate(self.__last_player_cell.row + 1,self.__last_player_cell.column,self.__board) is True:
            possible_cells.append(Cell(self.__last_player_cell.row+1,self.__last_player_cell.column,"Y"))
        possible_ways=[-1,0,1]
        for possible_way in possible_ways:
            new_row=self.__last_player_cell.row+possible_way
            left_column=self.__last_player_cell.column-1
            right_column=self.__last_player_cell.column+1
            if BoardValidator.validate(new_row, left_column, self.__board) is True and BoardValidator.validate(
                    new_row - 1, left_column, self.__board) and self.__board.get_value_from_certain_position_on_board(new_row - 1,
                                                                                        left_column) != 0 and self.__board.get_value_from_certain_position_on_board(
                new_row, left_column) == 0:
                possible_cells.append(Cell(new_row, left_column, 'Y'))

            if BoardValidator.validate(new_row, right_column,
                                       self.__board) is True and BoardValidator.validate(new_row - 1, right_column,
                                                                                         self.__board) and self.__board.get_value_from_certain_position_on_board(
                new_row - 1,
                right_column) != 0 and self.__board.get_value_from_certain_position_on_board(
                new_row, right_column) == 0:
                possible_cells.append(Cell(new_row, right_column, 'Y'))
        return possible_cells
    def get_next_free_position(self):
        for row in range(0,6):
            for column in range(6,-1,-1):
                if self.__board.get_value_from_certain_position_on_board(row,column)==0:
                    return Cell(row,column,"Y")
        return None

    def check_for_winning(self):
        if self.check_winning_on_column() is True:
            return True
        if self.check_winning_on_row() is True:
            return True
        if self.check_winning_on_main_diagonal() is True:
            return True
        if self.check_winning_on_second_diagonal() is True:
            return True
        return False

    def check_winning_on_column(self):
        for column in range(0, 2):
            for row in range(0, 6):
                if (self.__board.get_value_from_certain_position_on_board(row,
                                                                         column) == self.__board.get_value_from_certain_position_on_board(
                    row, column + 1) == self.__board.get_value_from_certain_position_on_board(row,column + 2) == self.__board.get_value_from_certain_position_on_board(
                    row, column + 3)) and self.__board.get_value_from_certain_position_on_board(row,
                                                                         column)!=0:
                    return True
        return False

    def check_winning_on_row(self):
        for row in range(0, 2):
            for column in range(0, 5):
                if (self.__board.get_value_from_certain_position_on_board(row,
                                                                         column) == self.__board.get_value_from_certain_position_on_board(
                    row + 1, column) == self.__board.get_value_from_certain_position_on_board(row + 2,
                                                                                              column) == self.__board.get_value_from_certain_position_on_board(
                    row + 3, column)) and self.__board.get_value_from_certain_position_on_board(row,
                                                                         column)!=0:
                    return True
        return False

    def check_winning_on_main_diagonal(self):
        for row in range(3, 6):
            for column in range(0, 3):
                if (self.__board.get_value_from_certain_position_on_board(row,
                                                                         column) == self.__board.get_value_from_certain_position_on_board(
                    row - 1, column + 1) == self.__board.get_value_from_certain_position_on_board(row - 2,
                                                                                                  column + 2) == self.__board.get_value_from_certain_position_on_board(
                    row - 3, column + 3)) and self.__board.get_value_from_certain_position_on_board(row,
                                                                         column)!=0:
                    return True
        return False

    def check_winning_on_second_diagonal(self):
        for row in range(3, 6):
            for column in range(3, 5):
                if (self.__board.get_value_from_certain_position_on_board(row,
                                                                          column) == self.__board.get_value_from_certain_position_on_board(
                    row - 1, column - 1) == self.__board.get_value_from_certain_position_on_board(row - 2,
                                                                                                  column - 2) == self.__board.get_value_from_certain_position_on_board(
                    row - 3, column - 3)) and self.__board.get_value_from_certain_position_on_board(row,
                                                                                                    column) != 0:
                    return True
        return False

    # def check_for_winning(self, row, column):
    #     quantity = 4
    #
    #     is_row_good_for_win = (self.move_in_direction(row, column, quantity, 1, 0) + self.move_in_direction(row, column,
    #                                                                                                         quantity,
    #                                                                                                         -1,
    #                                                                                                         0) - 1) >= 4
    #     is_column_good_for_win = (self.move_in_direction(row, column, quantity, 0, 1) + self.move_in_direction(row,
    #                                                                                                            column,
    #                                                                                                            quantity,
    #                                                                                                            0,
    #                                                                                                            -1) - 1) >= 4
    #
    #     is_main_diagonal_good_for_win = (self.move_in_direction(row, column, quantity, 1, 1) + self.move_in_direction(
    #         row, column, quantity,
    #         -1, -1) - 1) >= 4
    #
    #     is_second_diagonal_good_for_win = (self.move_in_direction(row, column, quantity, -1,
    #                                                               1) + self.move_in_direction(row, column, quantity,
    #                                                                                           1,
    #                                                                                           -1) - 1) >= 4
    #
    #     return is_row_good_for_win or is_column_good_for_win or is_main_diagonal_good_for_win or is_second_diagonal_good_for_win
    #
    # def move_in_direction(self, row, column, quantity, row_factor=1, column_factor=1):
    #     good_cells_for_win: int = 1
    #     for displacement in range(1, quantity):
    #         new_row = row + displacement * row_factor
    #         new_column = column + displacement * column_factor
    #         if BoardValidator.validate(new_row, new_column, self.__board) is True and self.__board.get_value_from_certain_position_on_board(new_row,
    #                                                                                                          new_column) != 0:
    #             if self.__board.get_value_from_certain_position_on_board(new_row, new_column) == self.__board.get_value_from_certain_position_on_board(row, column):
    #                 good_cells_for_win += 1
    #             else:
    #                 break
    #         else:
    #             break
    #
    #     return good_cells_for_win
    def get_value_from_certain_position_on_board(self,row,column):
        return self.__board.get_value_from_certain_position_on_board(row,column)
    def get_rows(self):
        return self.__board.get_rows()
    def get_columns(self):
        return self.__board.get_columns()
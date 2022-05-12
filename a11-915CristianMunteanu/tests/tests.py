import unittest

from doimain.board import Board
from services.board_service import BoardService


class TestBoardService(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board(6, 7)
        self.__board_service = BoardService(self.__board)

    def test_board_get_rows___with_proper_data___AssertsTrue(self):
        self.assertEqual(self.__board.get_rows(), 6)

    def test_board_get_columns___with_proper_data___AssertsTrue(self):
        self.assertEqual(self.__board.get_columns(), 7)

    def test_board_get_board___with_proper_data___AssertsTrue(self):
        board = [[0] * 7 for i in range(6)]
        self.assertEqual(self.__board.get_board(), board)

    def test_board_get_value_from_certain_position_on_board___with_value_being_0___AssertsTrue(self):
        board = [[0] * 7 for i in range(6)]
        self.assertEqual(self.__board.get_value_from_certain_position_on_board(3, 3), 0)

    def test_board_set_value_from_certain_position_on_board___with_proper_data___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(3, 3, "X")
        self.assertEqual(self.__board.get_value_from_certain_position_on_board(3, 3), "X")

    def test_board_get_value_from_certain_position_on_board___with_value_being_1___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(2, 2, 1)
        self.assertEqual(self.__board.get_value_from_certain_position_on_board(2, 2), 1)

    def test_board_service_check_winning_on_column___with_winning_situation___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(0, 1, "X")
        self.__board.set_value_from_certain_position_on_board(0, 2, "X")
        self.__board.set_value_from_certain_position_on_board(0, 3, "X")
        self.assertEqual(self.__board_service.check_winning_on_column(), True)

    def test_board_service_check_winning_on_column___without_winning_situation___AssertsFalse(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(0, 1, "X")
        self.__board.set_value_from_certain_position_on_board(0, 2, "X")
        self.__board.set_value_from_certain_position_on_board(0, 3, "Y")
        self.assertEqual(self.__board_service.check_winning_on_column(), False)

    def test_board_service_check_winning_on_row___with_winning_situation___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(1, 0, "X")
        self.__board.set_value_from_certain_position_on_board(2, 0, "X")
        self.__board.set_value_from_certain_position_on_board(3, 0, "X")
        self.assertEqual(self.__board_service.check_winning_on_row(), True)

    def test_board_service_check_winning_on_row___without_winning_situation___AssertsFalse(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(1, 0, "X")
        self.__board.set_value_from_certain_position_on_board(2, 0, "X")
        self.__board.set_value_from_certain_position_on_board(3, 0, "Y")
        self.assertEqual(self.__board_service.check_winning_on_row(), False)

    def test_board_service_check_winning_on_second_diagonal___with_winning_situation___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(1, 1, "X")
        self.__board.set_value_from_certain_position_on_board(2, 2, "X")
        self.__board.set_value_from_certain_position_on_board(3, 3, "X")
        self.assertEqual(self.__board_service.check_winning_on_second_diagonal(),True)
    def test_board_service_check_winning_on_second_diagonal___without_winning_situation___AssertsFalse(self):
        self.__board.set_value_from_certain_position_on_board(0, 0, "X")
        self.__board.set_value_from_certain_position_on_board(1, 1, "X")
        self.__board.set_value_from_certain_position_on_board(2, 2, "X")
        self.__board.set_value_from_certain_position_on_board(3, 3, "Y")
        self.assertEqual(self.__board_service.check_winning_on_second_diagonal(),False)
    def test_board_service_check_winning_on_main_diagonal___with_winning_situation___AssertsTrue(self):
        self.__board.set_value_from_certain_position_on_board(0, 5, "X")
        self.__board.set_value_from_certain_position_on_board(1, 4, "X")
        self.__board.set_value_from_certain_position_on_board(2, 3, "X")
        self.__board.set_value_from_certain_position_on_board(3, 2, "X")
        self.assertEqual(self.__board_service.check_winning_on_main_diagonal(),True)
    def test_board_service_check_winning_on_main_diagonal___without_winning_situation___AssertsFalse(self):
        self.__board.set_value_from_certain_position_on_board(0, 5, "X")
        self.__board.set_value_from_certain_position_on_board(1, 4, "X")
        self.__board.set_value_from_certain_position_on_board(2, 3, "X")
        self.__board.set_value_from_certain_position_on_board(3, 2, "Y")
        self.assertEqual(self.__board_service.check_winning_on_main_diagonal(),False)
    def test_board_service_get_next_free_position___with_proper_data___First_cell_is_found(self):
        for row in range(5, -1, -1):
            for column in range(0, 7):
                self.__board.set_value_from_certain_position_on_board(row, column,0)
        self.assertEqual(self.__board_service.get_next_free_position().row,0)
        self.assertEqual(self.__board_service.get_next_free_position().column,6)
        self.assertEqual(self.__board_service.get_next_free_position().value,"Y")
    def test_board_service_get_next_free_position___with_board_full___The_returned_cell_is_none(self):
        for row in range(5, -1, -1):
            for column in range(0, 7):
                self.__board.set_value_from_certain_position_on_board(row, column,"Y")
        self.assertEqual(self.__board_service.get_next_free_position(),None)

    def test_board_service_get_position_next_to_player_move___with_position_from_above_free___the_returned_cell_will_be_the_one_from_above_last_move(self):
        for row in range(5, -1, -1):
            for column in range(0, 7):
                self.__board.set_value_from_certain_position_on_board(row, column, 0)
        self.__board_service.player_move(0,0)
        possible_positions=self.__board_service.get_position_next_to_player_move()
        self.assertEqual(possible_positions[0].row,1)
        self.assertEqual(possible_positions[0].column,0)
    def test_board_service_get_position_next_to_player_move___with_position_from_above_not_free___the_returned_cell_will_be_the_neighbour(self):
        for row in range(5, -1, -1):
            for column in range(0, 7):
                self.__board.set_value_from_certain_position_on_board(row, column, "X")
        self.__board.set_value_from_certain_position_on_board(5, 0, 0)
        self.__board_service.player_move(5, 0)
        self.__board.set_value_from_certain_position_on_board(5,1,0)
        cell=self.__board_service.get_position_next_to_player_move()
        self.assertEqual(cell[0].row,5)
        self.assertEqual(cell[0].column,1)
    def test(self):
        self.test_board_get_rows___with_proper_data___AssertsTrue()
        self.test_board_get_columns___with_proper_data___AssertsTrue()
        self.test_board_get_board___with_proper_data___AssertsTrue()
        self.test_board_get_value_from_certain_position_on_board___with_value_being_0___AssertsTrue()
        self.test_board_get_value_from_certain_position_on_board___with_value_being_0___AssertsTrue()
        self.test_board_set_value_from_certain_position_on_board___with_proper_data___AssertsTrue()
        self.test_board_get_value_from_certain_position_on_board___with_value_being_1___AssertsTrue()
        self.test_board_service_check_winning_on_column___with_winning_situation___AssertsTrue()
        self.test_board_service_check_winning_on_column___without_winning_situation___AssertsFalse()
        self.test_board_service_check_winning_on_row___with_winning_situation___AssertsTrue()
        self.test_board_service_check_winning_on_row___without_winning_situation___AssertsFalse()
        self.test_board_service_check_winning_on_second_diagonal___with_winning_situation___AssertsTrue()
        self.test_board_service_check_winning_on_second_diagonal___without_winning_situation___AssertsFalse()
        self.test_board_service_check_winning_on_main_diagonal___without_winning_situation___AssertsFalse()
        self.test_board_service_check_winning_on_main_diagonal___with_winning_situation___AssertsTrue()
        self.test_board_service_get_next_free_position___with_proper_data___First_cell_is_found()
        self.test_board_service_get_next_free_position___with_board_full___The_returned_cell_is_none()
        self.test_board_service_get_position_next_to_player_move___with_position_from_above_free___the_returned_cell_will_be_the_one_from_above_last_move()
        self.test_board_service_get_position_next_to_player_move___with_position_from_above_not_free___the_returned_cell_will_be_the_neighbour()

if __name__ == '__main__':
    unittest.main()

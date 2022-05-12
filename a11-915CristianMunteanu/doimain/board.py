class Board:
    def __init__(self,rows,columns):
        self.__rows=rows
        self.__columns=columns
        self.__board = [[0] * columns for i in range(rows)]

    def get_columns(self):
        return self.__columns
    def get_rows(self):
        return self.__rows
    def get_board(self):
        return self.__board
    def get_value_from_certain_position_on_board(self,row,column):
        return self.__board[row][column]
    def set_value_from_certain_position_on_board(self,row,column,value):
        self.__board[row][column]=value
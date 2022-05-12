class PositionShouldBeTheLowestPossible(Exception):
    def __init__(self,exception_message):
        super().__init__(exception_message)

class PositionAlreadyTaken(Exception):
    def __init__(self, exception_message):
        super().__init__(exception_message)

class PositionIsOutsideTheBoard(Exception):
    def __init__(self,exception_message):
        super().__init__(exception_message)


class CellValidator:
    def __init__(self,board,row,column):
        self.__board=board
        self.__row=row
        self.__column=column

    def validate(self):
        if self.__row <0 or self.__row>6:
            raise PositionIsOutsideTheBoard("The row introduced is not right!")
        if self.__column<0 or self.__column>7:
            raise PositionIsOutsideTheBoard("The column introduced is not right!")
        if self.__row!=0 and self.__board.get_value_from_certain_position_on_board(self.__row-1,self.__column)==0:
            raise PositionShouldBeTheLowestPossible("This is not the lowest position!")
        if self.__board.get_value_from_certain_position_on_board(self.__row,self.__column)!=0:
            raise PositionAlreadyTaken("The position is already taken!")
        return True
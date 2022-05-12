class Letter:
    def __init__(self,child_id,letter_id,date_when_was_written,item_1,item_2):
        self.__child_id=child_id
        self.__letter_id=letter_id
        self.__date_when_was_written=date_when_was_written
        self.__item_1=item_1
        self.__item_2=item_2
    @property
    def date_when_was_written(self):
        return self.__date_when_was_written

    @date_when_was_written.setter
    def date_when_was_written(self, value):
        self.__date_when_was_written=value
    @property
    def item_1(self):
        return self.__item_1

    @item_1.setter
    def item_1(self, value):
        self.__item_1=value

    @property
    def item_2(self):
        return self.__item_2

    @item_2.setter
    def item_2(self, value):
        self.__item_2=value
    @property
    def child_id(self):
        return self.__child_id

    @child_id.setter
    def child_id(self, value):
        self.__child_id=value

    @property
    def letter_id(self):
        return self.__letter_id

    @letter_id.setter
    def letter_id(self, value):
        self.__letter_id=value
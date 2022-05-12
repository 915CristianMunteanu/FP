class Item:
    def __init__(self,item_id,item_name):
        self.__item_id=item_id
        self.__item_name=item_name
    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        self.__item_id=value

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value):
        self.__item_name=value

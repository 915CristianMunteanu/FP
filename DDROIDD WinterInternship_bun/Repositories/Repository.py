class ChildRepository:
    def __init__(self):
        self.__list_of_all_childs=[]
    def check_if_child_exists(self,child):
        if type(child.child_id) is str:
            if child.child_id.isnumeric():
                child.child_id=int(child.child_id)
                for current_child_index in range(0,len(self.__list_of_all_childs)):
                    if self.__list_of_all_childs[current_child_index].child_id==child.child_id:
                        return self.__list_of_all_childs[current_child_index]
                    return None
    def add_child_to_repository(self,child):
        if self.check_if_child_exists(child)is None:
            self.__list_of_all_childs.append(child)
        else:
            raise ValueError("Child already exists!")
    def return_list_of_all_childs(self):
        return self.__list_of_all_childs
    def find_child_by_id(self,child_id):
        for child in self.__list_of_all_childs:
            if child.child_id==child_id:
                return child
        return None
class ItemRepository:
    def __init__(self):
        self.__list_of_all_items=[]
    def check_if_item_exists(self,item):
        if type(item.item_id) is str:
            if item.item_id.isnumeric():
                item.item_id=int(item.item_id)
                for current_item_index in range(0,len(self.__list_of_all_items)):
                    if self.__list_of_all_items[current_item_index].item_id==item.item_id:
                        return self.__list_of_all_items[current_item_index]
                    return None

    def add_item_to_repository(self,item):
        if self.check_if_item_exists(item) is None:
            self.__list_of_all_items.append(item)
        else:
            raise ValueError("Item already exists!")
    def return_list_of_all_items(self):
        return self.__list_of_all_items
    def find_item_by_name(self,name):
        for item in self.__list_of_all_items:
            if item.item_name==name:
                return item
        return None

class LetterRepository:
    def __init__(self,child_repository,item_repository):
        self.__child_repository=child_repository
        self.__item_repository=item_repository
        self.__list_of_all_letters=[]
    def check_if_letter_to_be_add_has_the_rights_atributtes(self,letter):
            for current_letter_index in range(0,len(self.__list_of_all_letters)):
                if self.__list_of_all_letters[current_letter_index].letter_id==letter.letter_id:
                    return self.__list_of_all_letters[current_letter_index]
                return None

    def add_letter_to_repository(self,letter):
        if self.check_if_letter_to_be_add_has_the_rights_atributtes(letter) is None:
            self.__list_of_all_letters.append(letter)
        else:
            raise ValueError("Letter already exists!")

    def return_list_of_all_letters(self):
        return self.__list_of_all_letters
class BuildReportHandler():
    def __init__(self,letter_repository,item_repository):
        self.__letter_repository=letter_repository
        self.__item_repository=item_repository
        self.__dictionary_of_all_items_with_quantity={}
    def calculate_dictionary_of_all_items_with_quantity(self):
        for item in self.__item_repository.return_list_of_all_items():
            self.__dictionary_of_all_items_with_quantity[item.item_name]=0
        for letter in self.__letter_repository.return_list_of_all_letters():
            self.__dictionary_of_all_items_with_quantity[letter.item_1.item_name]+=1
            self.__dictionary_of_all_items_with_quantity[letter.item_2.item_name]+=1
        return self.__dictionary_of_all_items_with_quantity
    def sort_dictionary_of_all_items_with_quantity(self,dictionary):
        return dict(sorted(dictionary.items(),key=lambda item:item[1], reverse=True))
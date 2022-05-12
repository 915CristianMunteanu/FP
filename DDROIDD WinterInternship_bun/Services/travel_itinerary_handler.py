class TravelItineraryHandler:
    def __init__(self,child_repository):
        self.__child_repository=child_repository
        self.__list_of_city_and_address=[]
    def create_list_of_city_and_address(self):
        for child in self.__child_repository.return_list_of_all_childs():
            full_address=child.address
            full_address=full_address.split(sep=" ",maxsplit=1)
            city=full_address[0]
            self.__list_of_city_and_address.append([city,child.address])
        return self.__list_of_city_and_address
    def sort_list_of_city_and_address(self,list):
        sorted_list=sorted(list,key=lambda element: element[0])
        return sorted_list
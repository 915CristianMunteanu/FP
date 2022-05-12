import datetime

from BehaviourEnum import BehaviourEnum
from Entities.Child import Child
from Entities.Item import Item
from Entities.Letter import Letter
from Services.build_report_handler import BuildReportHandler
from Services.text_from_file_interpreter import TextFromFileInterpreter
from Services.travel_itinerary_handler import TravelItineraryHandler
from Services.write_into_file_letters import WriteIntoFileLetters


class Program:
    def __init__(self,child_repository,item_repository,letter_repository,console):
        self.__child_repository=child_repository
        self.__item_repository=item_repository
        self.__letter_repository=letter_repository
        self.__console=console
        self.Question1()
        self.Question2()
        self.Question3()
        self.Question4()
        self.Question5()
        self.Question6()

    def Question1(self):
        print(" \n The solution to be displayed for Question 1 is: \n")
        first_child=Child(1,"Peter Pan",datetime.date(2006,6,6),"Cluj-Napoca Strada Bogdan Petriceicu Hasdeu 92",BehaviourEnum.Good)
        second_child=Child(2,"Damian Lucacu",datetime.date(2004,12,23),"Costinesti Strada Dealu Mare 14",BehaviourEnum.Bad)
        third_child=Child(3,"Octavian Caruntu",datetime.date(2012,3,26),"Dorohoi Bulevardul Victoriei 121",BehaviourEnum.Good)
        item_one=Item(1,"Small Dinosaur")
        item_two=Item(2,"Red Car")
        item_three=Item(3,"Cat")
        item_four=Item(4,"Magical Set")
        item_five=Item(5,"Play-Doh")
        item_six=Item(6,"iPad")
        first_childs_letter=Letter(1,1,datetime.date(2021,12,16),item_one,item_two)
        second_childs_letter=Letter(2,2,datetime.date(2021,12,22),item_three,item_four)
        third_childs_letter=Letter(3,3,datetime.date(2021,12,1),item_five,item_six)
        # console.print_child(first_child)
        # console.print_child(second_child)
        # console.print_child(third_child)
        # console.print_item(item_one)
        # console.print_item(item_two)
        # console.print_item(item_three)
        # console.print_item(item_four)
        # console.print_item(item_five)
        # console.print_item(item_six)
        # console.print_letter(first_childs_letter)
        # console.print_letter(second_childs_letter)
        # console.print_letter(third_childs_letter)
        # console.print_letter_with_all_info(first_childs_letter,first_child)
        # console.print_letter_with_all_info(second_childs_letter,second_child)
        # console.print_letter_with_all_info(third_childs_letter,third_child)
        self.__child_repository.add_child_to_repository(first_child)
        self.__child_repository.add_child_to_repository(second_child)
        self.__child_repository.add_child_to_repository(third_child)
        self.__item_repository.add_item_to_repository(item_one)
        self.__item_repository.add_item_to_repository(item_two)
        self.__item_repository.add_item_to_repository(item_three)
        self.__item_repository.add_item_to_repository(item_four)
        self.__item_repository.add_item_to_repository(item_five)
        self.__item_repository.add_item_to_repository(item_six)
        self.__letter_repository.add_letter_to_repository(first_childs_letter)
        self.__letter_repository.add_letter_to_repository(second_childs_letter)
        self.__letter_repository.add_letter_to_repository(third_childs_letter)
        for child in self.__child_repository.return_list_of_all_childs():
            self.__console.print_child(child)
        for item in self.__item_repository.return_list_of_all_items():
            self.__console.print_item(item)
        for letter in self.__letter_repository.return_list_of_all_letters():
            self.__console.print_letter(letter)
        for letter in self.__letter_repository.return_list_of_all_letters():
            self.__console.print_letter_with_all_info(letter,self.__child_repository.find_child_by_id(letter.child_id))


    def Question2(self):
        """
        Reading the age from the file doesnt give me enough informations about the date of birth of the child, so I used month 1 and day 1 for every child in that case.
        """
        print("\n The solution to be displayed for Question 2 is: \n")
        text_from_file_interpreter_1=TextFromFileInterpreter("letter_one.txt")
        text_from_file_interpreter_1.read_from_file()
        name, age, address, behaviour, item_one_name, item_two_name,date=text_from_file_interpreter_1.read_from_file()
        if self.__item_repository.find_item_by_name(item_one_name) is not None:
            item_one=self.__item_repository.find_item_by_name(item_one_name)
        else:
            item_one=Item(len(self.__item_repository.return_list_of_all_items())+1,item_one_name)
            self.__item_repository.add_item_to_repository(item_one)
        if self.__item_repository.find_item_by_name(item_two_name) is not None:
            item_two=self.__item_repository.find_item_by_name(item_two_name)
        else:
            item_two=Item(len(self.__item_repository.return_list_of_all_items())+1,item_two_name)
            self.__item_repository.add_item_to_repository(item_two)
        if behaviour=="Good":
            child_behaviour=BehaviourEnum.Good
        else:
            child_behaviour=BehaviourEnum.Bad
        year=2021-age
        first_read_child=Child(len(self.__child_repository.return_list_of_all_childs())+1,name,datetime.date(year,1,1),address,child_behaviour)
        first_read_letter=Letter(first_read_child.child_id,len(self.__letter_repository.return_list_of_all_letters())+1,date,item_one,item_two)
        self.__letter_repository.add_letter_to_repository(first_read_letter)
        self.__child_repository.add_child_to_repository(first_read_child)
        text_from_file_interpreter_2=TextFromFileInterpreter("letter_two.txt")
        text_from_file_interpreter_2.read_from_file()
        name, age, address, behaviour, item_one_name, item_two_name,date=text_from_file_interpreter_2.read_from_file()
        if self.__item_repository.find_item_by_name(item_one_name) is not None:
            item_one=self.__item_repository.find_item_by_name(item_one_name)
        else:
            item_one=Item(len(self.__item_repository.return_list_of_all_items())+1,item_one_name)
            self.__item_repository.add_item_to_repository(item_one)
        if self.__item_repository.find_item_by_name(item_two_name) is not None:
            item_two=self.__item_repository.find_item_by_name(item_two_name)
        else:
            item_two=Item(len(self.__item_repository.return_list_of_all_items())+1,item_two_name)
            self.__item_repository.add_item_to_repository(item_two)
        if behaviour=="Good":
            child_behaviour=BehaviourEnum.Good
        else:
            child_behaviour=BehaviourEnum.Bad
        year=2021-age
        second_read_child=Child(len(self.__child_repository.return_list_of_all_childs())+1,name,datetime.date(year,1,1),address,child_behaviour)
        second_read_letter = Letter(second_read_child.child_id,
                                   len(self.__letter_repository.return_list_of_all_letters()) + 1, date, item_one,
                                   item_two)
        self.__letter_repository.add_letter_to_repository(second_read_letter)
        self.__child_repository.add_child_to_repository(second_read_child)
        text_from_file_interpreter_3=TextFromFileInterpreter("letter_three.txt")
        text_from_file_interpreter_3.read_from_file()
        name, age, address, behaviour, item_one_name, item_two_name,date=text_from_file_interpreter_3.read_from_file()
        if self.__item_repository.find_item_by_name(item_one_name) is not None:
            item_one=self.__item_repository.find_item_by_name(item_one_name)
        else:
            item_one=Item(len(self.__item_repository.return_list_of_all_items())+1,item_one_name)
            self.__item_repository.add_item_to_repository(item_one)
        if self.__item_repository.find_item_by_name(item_two_name) is not None:
            item_two=self.__item_repository.find_item_by_name(item_two_name)
        else:
            item_two=Item(len(self.__item_repository.return_list_of_all_items())+1,item_two_name)
            self.__item_repository.add_item_to_repository(item_two)
        if behaviour=="Good":
            child_behaviour=BehaviourEnum.Good
        else:
            child_behaviour=BehaviourEnum.Bad
        year=2021-age
        third_read_child=Child(len(self.__child_repository.return_list_of_all_childs())+1,name,datetime.date(year,1,1),address,child_behaviour)
        third_read_letter = Letter(third_read_child.child_id,
                                   len(self.__letter_repository.return_list_of_all_letters()) + 1, date, item_one,
                                   item_two)
        self.__letter_repository.add_letter_to_repository(third_read_letter)
        self.__child_repository.add_child_to_repository(third_read_child)
        self.__console.print_child(first_read_child)
        self.__console.print_child(second_read_child)
        self.__console.print_child(third_read_child)
    def Question3(self):
        write_into_file_letters=WriteIntoFileLetters("letters_output.txt",self.__letter_repository,self.__child_repository)
        write_into_file_letters.write_into_file_all_letters_from_repository_with_all_informations()
    def Question4(self):
        print("\n The solution to be displayed for Question 4 is: \n")
        build_report_handler=BuildReportHandler(self.__letter_repository,self.__item_repository)
        dictionary=build_report_handler.calculate_dictionary_of_all_items_with_quantity()
        dictionary=build_report_handler.sort_dictionary_of_all_items_with_quantity(dictionary)
        for key in dictionary:
            print(str(key)+" - "+str(dictionary[key]))
    def Question5(self):
        """
        I didnt actually knew what Singleton Pattern means, but after a search on google I understood what Singleton Pattern is and I think I am using Singleton Pattern for my classes, except for Child,Letter and Item classes.
        For the other ones I am creating one single instance of every class that I am using in my main module, which is SantaClauseConsoleApp.py
        I dont what more I should write here, because I am still a little bit confuse about the Singleton Pattern.
        """
    def Question6(self):
        print("\n The solution to be displayed for Question 5 is: \n")
        travel_itinerary_handler=TravelItineraryHandler(self.__child_repository)
        list=travel_itinerary_handler.create_list_of_city_and_address()
        list=travel_itinerary_handler.sort_list_of_city_and_address(list)
        for current_address_index in range(0,len(list)):
            print(list[current_address_index][1])
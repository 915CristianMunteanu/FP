import datetime


class WriteIntoFileLetters:
    def __init__(self, file_name,letter_repository,child_repository):
        self.__file_name = file_name
        self.__letter_repository=letter_repository
        self.__child_repository=child_repository

    def calculate_age(self, child):
        today = datetime.date.today()
        this_year_birthday = datetime.date(today.year, child.date_of_birth.month, child.date_of_birth.day)
        if this_year_birthday < today:
            age = today.year - child.date_of_birth.year
        else:
            age = today.year - child.date_of_birth.year - 1
        return age

    def write_into_file_all_letters_from_repository_with_all_informations(self):
        file = open(self.__file_name, "wt")
        list_of_all_letters=self.__letter_repository.return_list_of_all_letters()
        list_of_all_childs=self.__child_repository.return_list_of_all_childs()
        letter_counter=0
        while letter_counter<len(list_of_all_letters):
            letter=list_of_all_letters[letter_counter]
            child=list_of_all_childs[letter_counter]
            file.write(
                f"{letter.date_when_was_written}\nDear Santa,\nI am {child.child_name}\nI am {self.calculate_age(child)} years old. I live at {child.address}. I have been a very {child.child_behaviour.name} child this year.\nWhat I would like the most this Christmas is:\n{letter.item_1.item_name},{letter.item_2.item_name}\n\n")
            letter_counter+=1
        file.close()

import datetime
import os


class TextFromFileInterpreter:
    def __init__(self, file_name):
        self.__file_name = file_name

    def read_from_file(self):
        if os.path.exists(self.__file_name):
            with open(self.__file_name, "r") as file:
                line_counter = 0
                for line in file.readlines():
                    line=line.strip()
                    if line_counter==2:
                        splitted_line=line.split(sep=" ",maxsplit=2)
                        name=splitted_line[2]

                    if line_counter==3:
                        splitted_line=line.split(sep=".")
                        line_to_get_age=splitted_line[0]
                        line_to_get_address=splitted_line[1]
                        line_to_get_behaviour=splitted_line[2]
                        line_to_get_age=line_to_get_age.split()
                        age=int(line_to_get_age[2])

                        line_to_get_address=line_to_get_address.strip()
                        line_to_get_address=line_to_get_address.split(sep=" ",maxsplit=3)
                        address=line_to_get_address[3]

                        line_to_get_behaviour=line_to_get_behaviour.strip()
                        line_to_get_behaviour=line_to_get_behaviour.split()
                        behaviour=line_to_get_behaviour[5]

                    if line_counter==5:
                        item_one_name,item_two_name=line.split(",")
                    if line_counter==0:
                        date=datetime.datetime.strptime(line,'%Y-%m-%d').date()


                    line_counter += 1
                file.close()
                return name,age,address,behaviour,item_one_name,item_two_name,date

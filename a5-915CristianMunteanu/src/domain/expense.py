

class Expense:
    """
    This class defines the expenses and contains the getter and setter functions.
    """
    def __init__(self, day, amount, type):
        self.__day = day
        self.__amount = amount
        self.__type = type

    @property
    def day(self):
        """
        This is a getter function.
        :return: It returns self.__day parameter, which is an integer value between 1 and 30.
        """
        return self.__day

    @day.setter
    def day(self, value):
        """
        This is a setter function that sets the value from the variable value to self.__day.
        :param value: Integer value from 1 to 30.
        :return:This function doesnt return anything.
        """
        if value.isnumeric() != True:
            raise ValueError("The parameter given is not a number!")
        else:
            if value < 1 or value > 30:
                raise ValueError("The parameter given is not from 1 to 30!")
            else:
                self.__day = value

    @property
    def amount(self):
        """
        This is a getter function.
        :return: It returns self.__amount parameter, which is an integer positive value.
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        """
        This is a setter function that sets the value from the variable value to self.__amount.
        :param value: Positive Integer
        :return: This function doesnt return anything.
        """
        if value.isnumeric() != True:
            raise ValueError("The parameter given is not a number!")
        else:
            self.__amount = value

    @property
    def type(self):
        """
        This is a getter function.
        :return: This function doesnt return anything.
        """
        return self.__type

    @type.setter
    def type(self, value):
        """
        This is a setter function that sets the value from the variable value to self.__type.
        :param value: Is a string.
        :return: This function doesnt return anything.
        """
        self.__type = value
    def __eq__(self, expense_to_compare):
        if self.__type!= expense_to_compare.type:
            return False
        if self.__day!= expense_to_compare.day:
            return False
        if self.__type!= expense_to_compare.type:
            return False
        return True



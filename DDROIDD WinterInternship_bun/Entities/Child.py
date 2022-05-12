class Child:
    """
    This is a class that creates an entity of the type Child, that has the following attributes:
    child_id=Should be an integer value, and most important, an unique one!
    child_name=Should be a string of characters!
    date_of_birth=For that attribute, im going to use a built-in library from python. (Datetime) It will be a date in the form: %dd-%mm-%yyyy.
    adress=Should be a string of characters, containing also digits.
    child_behaviour=This attribute is going to be either GOOD or BAD, depending on the enum.
    """
    def __init__(self,child_id,child_name,date_of_birth,address,child_behaviour):
        self.__child_id=child_id
        self.__child_name=child_name
        self.__date_of_birth=date_of_birth
        self.__address=address
        self.__child_behaviour=child_behaviour
    @property
    def child_id(self):
        return self.__child_id

    @child_id.setter
    def child_id(self, value):
        self.__child_id=value

    @property
    def child_name(self):
        return self.__child_name

    @child_name.setter
    def child_name(self, value):
        self.__child_name=value

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def deta_of_birth(self, value):
        self.__date_of_birth=value
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address=value

    @property
    def child_behaviour(self):
        return self.__child_behaviour

    @child_behaviour.setter
    def child_behaviour(self, value):
        self.__child_behaviour=value


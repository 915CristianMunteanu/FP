class UndoRedoEntity:
    def __init__(self,function, *function_parameters):
        self.__function=function
        self.__function_parameters=function_parameters
    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        self.__function=value
    @property
    def function_parameters(self):
        return self.__function_parameters

    @function_parameters.setter
    def function_parameters(self, value):
        self.__function_parameters=value
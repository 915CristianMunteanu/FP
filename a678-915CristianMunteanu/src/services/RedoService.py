import functools

from domain.UndoRedoEntity import UndoRedoEntity


class RedoService:
    def __init__(self,redo_repository,undo_repository):
        self.__undo_repository=undo_repository
        self.__redo_repository=redo_repository
    def add_operation(self,function_redo,parameters_redo,function_undo,parameters_undo):
        undo_entity=UndoRedoEntity(function_undo,*parameters_undo)
        redo_entity=UndoRedoEntity(function_redo,*parameters_redo)
        self.__redo_repository.add_operation(redo_entity,undo_entity)
    def pop_out(self):
        redo_operation,undo_operation=self.__redo_repository.pop_operation()
        function_to_execute=functools.partial(redo_operation.function,*redo_operation.function_parameters)
        function_to_execute()
        self.__undo_repository.add_operation(undo_operation,redo_operation)
    def clear_data_from_repository(self):
        self.__redo_repository.clear_data_from_redo()
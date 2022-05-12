import functools

from domain.UndoRedoEntity import UndoRedoEntity


class UndoService:
    def __init__(self,undo_repository,redo_repository):
        self.__undo_repository=undo_repository
        self.__redo_repository=redo_repository
    def add_operation(self,function_undo,parameters_undo,function_redo,parameters_redo):
        undo_entity=UndoRedoEntity(function_undo,*parameters_undo)
        redo_entity=UndoRedoEntity(function_redo,*parameters_redo)
        self.__undo_repository.add_operation(undo_entity,redo_entity)
    def pop_out(self):
        undo_operation,redo_operation=self.__undo_repository.pop_operation()
        function_to_execute=functools.partial(undo_operation.function,*undo_operation.function_parameters)
        function_to_execute()
        self.__redo_repository.add_operation(redo_operation,undo_operation)



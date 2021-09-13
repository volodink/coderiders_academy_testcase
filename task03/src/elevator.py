class Elevator:
    def __init__(self, elevator_id) -> None:
        self.__id__: int = elevator_id
        self.__floor__: int = 1
    
    def set_floor(self, floor) -> None:
        self.__floor__ = floor

    def get_floor(self) -> int:
        return self.__floor__
    
    def get_id(self) -> int:
        return self.__id__
       
    def __str__(self) -> str:
        return f'Elevator(id={self.__id__}, floor={self.__floor__})'

    def __repr__(self) -> str:
        return f'Elevator(id={self.__id__}, floor={self.__floor__})'

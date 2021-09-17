"""
    Elevator entity class module.
"""


class Elevator:
    """
        Elevator entity class.
    """
    def __init__(self, elevator_id: int) -> None:
        self.__id__: int = elevator_id
        self.__floor__: int = 1

    def set_floor(self, floor: int) -> None:
        """
            Sets value of user floor

        Args:
            floor: int User floor is now

        Returns:
            None
        """
        self.__floor__ = floor

    def get_floor(self) -> int:
        """
            Gets elevator floor

        Returns:
            int Elevator floor
        """
        return self.__floor__

    def get_id(self) -> int:
        """
            Gets elevator id

        Returns:
            int Elevator id
        """
        return self.__id__

    def __str__(self) -> str:
        """
            To string override

        Returns:
            str String representation of Elevator class
        """
        return f'Elevator(id={self.__id__}, floor={self.__floor__})'

    def __repr__(self) -> str:
        """
            To string override

        Returns:
            str String representation of Elevator class
        """
        return f'Elevator(id={self.__id__}, floor={self.__floor__})'

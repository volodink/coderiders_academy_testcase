"""
    Coderiders Academy Task 3 main application class.
"""

from src.building import Building
from loguru import logger


class Application:
    """
        Application class.
    """
    def __init__(self) -> None:
        logger.info('Application.init')
        self.building = Building(floor_count=9, elevator_count=3)
        logger.debug(f'Building created as: {self.building}')
        logger.success('Application.init done.')

    def run(self) -> None:
        """
            Main application loop. Press X to win.
        Returns:
            None
        """
        logger.info("Enter floor number or * for exit.")

        while True:
            floor = input('You clicked at floor:')
            logger.debug(f'You clicked at floor: {floor}, {type(floor)}')
            if floor == "*":
                logger.info("Got * , will exit now.")
                break
            else:
                logger.info("Got something else...")
                try:
                    floor = int(floor)
                    logger.debug(f'You clicked at floor: {floor}')
                    logger.success('Got valid floor number (at least a number :)), will proceed to call the elevator.')
                    elevator_id = self.building.call_elevator(floor)
                    if elevator_id is None:
                        print(f"Can't send elevator to {floor} floor, sorry.")
                    else:
                        print(f"Elevator {elevator_id} arrived at {floor} floor")
                except ValueError:
                    print('Wrong input format. Please, try again.')
                    logger.warning('Wrong input format. Please, try again.')

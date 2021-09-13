from typing import List

from src.elevator import Elevator
from loguru import logger


class Building:
    def __init__(self, floor_count=9, elevator_count=3):
        logger.info("Building init.")
        self.__floor_count__ = floor_count
        self.__elevator_count__ = elevator_count
        self.__elevators__ = [Elevator(elevator_id) for elevator_id in range(elevator_count)]
        logger.debug(f'Elevators in building: {self.__elevators__}')
        logger.success(
            f"Building init done. The building has {self.__floor_count__} floors and {elevator_count} elevators.")

    def get_state(self) -> List[tuple]:
        logger.info("Getting building state...")
        return [(elevator.get_id(), elevator.get_floor()) for elevator in self.__elevators__]

    def call_elevator(self, user_floor: int):
        logger.opt(colors=True).info(f"User called elevator at <RED>{user_floor}</RED> floor.")

        # 0. Check wrong input
        if 1 <= user_floor <= 9:
            logger.success("Floor value in allowed range, we will proceed.")
        else:
            logger.critical(f"The floor {user_floor} does not exists! Where did you get The Button? O_O")
            return None

        # 1. Send elevator to 1st floor if there is no such
        logger.info("System is updating ...")
        logger.info("Checking first floor elevator availability...")
        first_floor_elevator_available, first_floor_elevator_id = self.is_elevator_available(1)
        if first_floor_elevator_available:
            logger.opt(colors=True).info(f"Elevator <RED>{first_floor_elevator_id}</RED> available at 1st floor. Nice!")
        else:
            logger.opt(colors=True).info("There is no elevators on first floor...")
            logger.info(f"Getting elevator, nearest to the 1st floor.")
            first_floor_elevator_id = self.get_nearest_elevator_id(1)
            logger.opt(colors=True).info(
                f"Sent elevator <RED>{first_floor_elevator_id}</RED> at 1st floor. Reason: no elevators on 1st floor")
            self.move_elevator(first_floor_elevator_id, 1)

        # 2. Check available elevator on floor if yes -> return such
        elevator_available, elevator_id = self.is_elevator_available(user_floor)
        if elevator_available:
            logger.info(f"Elevator {elevator_id} available on {user_floor}.")
            return elevator_id
        else:
            logger.opt(colors=True).info(f"Elevator not available on <RED>{user_floor}</RED>, will call then.")

        # 3. Finally, if there is no elevator on floor, send nearest elevator.
        logger.opt(colors=True).info(f"Getting nearest elevator to <RED>{user_floor}</RED> floor.")
        nearest_elevator_id = self.get_nearest_elevator_id(user_floor, [first_floor_elevator_id])

        # 4. Send elevator to 'user_on_floor' floor
        logger.info(f"Sending {nearest_elevator_id} to {user_floor}.")

        self.move_elevator(nearest_elevator_id, user_floor)

        # 5. Elevator is moving
        logger.warning("Mind the gap! OMG! Elevator is moving... O_O")

        # 6. Elevator arrived at 'user_on_floor' floor
        logger.success(f"Elevator {nearest_elevator_id} arrived to floor {user_floor}")

        logger.debug(f'Building state now is -> {self.get_state()}')

        return nearest_elevator_id

    def __str__(self):
        return f'Building(' \
               f'floor_count={self.__floor_count__}, ' \
               f'elevator_count={self.__elevator_count__}, ' \
               f'elevators_state={self.get_state()})'

    def get_nearest_elevator_id(self, user_floor: int, exclude_ids=None):
        if exclude_ids is None:
            exclude_ids = []

        logger.opt(colors=True).info(
            f"Getting nearest elevator id to <RED>{user_floor}</RED>, excluding elevators: <RED>{exclude_ids}</RED>")
        building_state = self.get_state()
        logger.debug(f'Building state now is -> {building_state}')

        distances = [(e[0], (abs(user_floor - e[1]))) for e in building_state if not e[0] in exclude_ids]
        logger.opt(colors=True).debug(f"Distances: {distances}")

        logger.info("Sorting by distance increase.")
        sorted_distances = sorted(distances, key=lambda tup: tup[1])
        logger.opt(colors=True).debug(f"Sorted distances: {sorted_distances}")

        nearest_elevator_id = sorted_distances[0][0]
        logger.opt(colors=True).info(f"Minimum distance: <RED>{sorted_distances[0][1]}</RED>.")
        logger.opt(colors=True).info(f"Nearest elevator id: <RED>{nearest_elevator_id}</RED>.")

        return nearest_elevator_id

    def is_elevator_available(self, floor) -> tuple:
        for elevator in self.__elevators__:
            if elevator.get_floor() == floor:
                return True, elevator.get_id()
        return False, None

    def move_elevator(self, elevator_id, floor):
        for elevator in self.__elevators__:
            if elevator.get_id() == elevator_id:
                elevator.set_floor(floor)
                break

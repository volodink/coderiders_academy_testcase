from src import building
from src.building import Building
from src.elevator import Elevator


def test_elevator_set_get_floor():
    elev = Elevator(1)
    elev.set_floor(1)
    assert 1 == elev.get_floor()


def test_elevator_get_id():
    elev = Elevator(1)
    assert 1 == elev.get_id()


def test_nearest_elevator_metric():
    building = Building(floor_count=9, elevator_count=3)
    assert 0 == building.get_nearest_elevator_id(1)


def test_is_elevator_available():
    building = Building(floor_count=9, elevator_count=3)
    assert True, 0 == building.is_elevator_available(1)


def test_building_elevators_state_is_correct():
    building = Building(floor_count=9, elevator_count=3)
    assert 1 == building.call_elevator(2)
    assert 0 == building.call_elevator(1)
    assert 1 == building.call_elevator(9)
    assert 2 == building.call_elevator(3)


def test_user_input_is_correct():
    building = Building(floor_count=9, elevator_count=3)
    assert building.call_elevator(-1) is None


def test_unusual_building_elevators_state_is_correct():
    building = Building(floor_count=5, elevator_count=2)
    assert 1 == building.call_elevator(2)
    assert 0 == building.call_elevator(1)
    assert 1 == building.call_elevator(5)
    assert 1 == building.call_elevator(3)


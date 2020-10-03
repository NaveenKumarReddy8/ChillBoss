import pytest
from pytest_mock import MockerFixture

from happyboss.move import Pointer

SCREEN_WIDTH: int = 1000
SCREEN_LENGTH: int = 750

DEFAULT_LENGTH: int = 100


@pytest.fixture()
def pointer(mocker: MockerFixture):
    mocker.patch("happyboss.move.size", return_value=(SCREEN_WIDTH, SCREEN_LENGTH))
    return Pointer()


def test_get_random_coordinates(pointer):
    random_x_coordinate: int
    random_y_coordinate: int
    random_x_coordinate, random_y_coordinate = pointer._get_random_coordinates()
    assert random_x_coordinate in range(SCREEN_WIDTH) and random_y_coordinate in range(
        SCREEN_LENGTH
    )


@pytest.mark.parametrize(
    "x_center, y_center, length, result",
    [
        (500, 300, 50, ((475, 275), (525, 275), (525, 325), (475, 325))),
        (1000, 1500, 100, ((950, 1450), (1050, 1450), (1050, 1550), (950, 1550))),
    ],
)
def test_get_square_coordinates(x_center, y_center, length, result, pointer):
    pointer._x_center: int = x_center
    pointer._y_center: int = y_center
    pointer._length: int = length
    corners = pointer._get_square_coordinates()
    assert corners[0] == result[0]
    assert corners[1] == result[1]
    assert corners[2] == result[2]
    assert corners[3] == result[3]

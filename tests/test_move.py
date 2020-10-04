import pytest
from pytest_mock import MockerFixture

from happyboss.move import Pointer

SCREEN_WIDTH: int = 1000
SCREEN_LENGTH: int = 750

DEFAULT_LENGTH: int = 100


@pytest.fixture()
def pointer(mocker: MockerFixture) -> Pointer:
    mocker.patch("happyboss.move.size", return_value=(SCREEN_WIDTH, SCREEN_LENGTH))
    return Pointer()


def test_get_random_coordinates(pointer:Pointer) -> None:
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
        (
            SCREEN_WIDTH // 2,
            SCREEN_LENGTH // 2,
            DEFAULT_LENGTH,
            (
                (
                    SCREEN_WIDTH // 2 - DEFAULT_LENGTH // 2,
                    SCREEN_LENGTH // 2 - DEFAULT_LENGTH // 2,
                ),
                (
                    SCREEN_WIDTH // 2 + DEFAULT_LENGTH // 2,
                    SCREEN_LENGTH // 2 - DEFAULT_LENGTH // 2,
                ),
                (
                    SCREEN_WIDTH // 2 + DEFAULT_LENGTH // 2,
                    SCREEN_LENGTH // 2 + DEFAULT_LENGTH // 2,
                ),
                (
                    SCREEN_WIDTH // 2 - DEFAULT_LENGTH // 2,
                    SCREEN_LENGTH // 2 + DEFAULT_LENGTH // 2,
                ),
            ),
        ),
    ],
)
def test_get_square_coordinates(x_center: int, y_center: int, length: int, result, pointer) -> None:
    pointer._x_center: int = x_center
    pointer._y_center: int = y_center
    pointer._length: int = length
    corners = pointer._get_square_coordinates()
    assert corners[0] == result[0]
    assert corners[1] == result[1]
    assert corners[2] == result[2]
    assert corners[3] == result[3]


def test_move_pointer(mocker, pointer) -> None:
    mocked_moveTo = mocker.patch("happyboss.move.moveTo")
    pointer._move_pointer(mocker.Mock(), mocker.Mock())
    mocked_moveTo.assert_called_once()


def test_random_movement(mocker, pointer) -> None:
    mocker.patch(
        "happyboss.move.Pointer._get_random_coordinates",
        return_value=(mocker.Mock(), mocker.Mock()),
    )
    side_effects_by_move_pointer = [None, None, None, None, KeyboardInterrupt]
    mocked_move_pointer = mocker.patch(
        "happyboss.move.Pointer._move_pointer",
        side_effect=side_effects_by_move_pointer,
    )
    mocker.patch("happyboss.move.sleep")

    pointer._random_movement()

    assert mocked_move_pointer.call_count == len(side_effects_by_move_pointer)


def test_squared_movement(mocker, pointer) -> None:
    mocker.patch(
        "happyboss.move.Pointer._get_square_coordinates",
        return_value=((mocker.Mock(), mocker.Mock()) for i in range(4)),
    )
    side_effects_by_move_pointer = [None, None, None, KeyboardInterrupt]
    mocked_move_pointer = mocker.patch(
        "happyboss.move.Pointer._move_pointer",
        side_effect=side_effects_by_move_pointer,
    )
    mocker.patch("happyboss.move.sleep")

    pointer._squared_movement()

    assert mocked_move_pointer.call_count == len(side_effects_by_move_pointer)


@pytest.mark.parametrize(
    "movement, movement_method",
    [("random", "_random_movement"), ("square", "_squared_movement")],
)
def test_move_the_mouse_pointer(movement, movement_method, mocker, pointer) -> None:
    mocked_movement_method = mocker.patch(f"happyboss.move.Pointer.{movement_method}")
    pointer._movement = movement
    pointer.move_the_mouse_pointer()
    mocked_movement_method.assert_called_once()


def test_move_the_mouse_pointer_for_new_kind_of_movement(mocker, pointer) -> None:
    with pytest.raises(KeyError):
        pointer._movement = "triangle"
        pointer.move_the_mouse_pointer()

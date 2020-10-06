import pytest
from pytest_mock import MockerFixture
import pyautogui

SCREEN_WIDTH: int = 1000
SCREEN_LENGTH: int = 750

DEFAULT_LENGTH: int = 100

class MockPyautogui:
    @staticmethod
    def size():
        return SCREEN_WIDTH, SCREEN_LENGTH
    
    @staticmethod
    def moveTo():
        return

@pytest.fixture()
def mock_pyautogui(mocker,monkeypatch):
    def mocked_data():
        return SCREEN_WIDTH, SCREEN_LENGTH
    
    def mocked_move():
        return mocker.Mock()
    
    monkeypatch.setattr(pyautogui, "size", mocked_data)
    monkeypatch.setattr(pyautogui, "moveTo", mocked_move)
    
    

@pytest.fixture()
def pointer(mock_pyautogui, mocker: MockerFixture):
    from happyboss.move import Pointer
    return Pointer()


def test_get_random_coordinates(pointer) -> None:
    random_x_coordinate: int
    random_y_coordinate: int
    random_x_coordinate, random_y_coordinate = pointer._get_random_coordinates()
    assert random_x_coordinate in range(SCREEN_WIDTH) and random_y_coordinate in range(
        SCREEN_LENGTH
    )


@pytest.mark.parametrize(
    "x_pixels, y_pixels, length, result",
    [
        (1000, 600, 50, ((475, 275), (525, 275), (525, 325), (475, 325))),
        (2000, 3000, 100, ((950, 1450), (1050, 1450), (1050, 1550), (950, 1550))),
        (
            SCREEN_WIDTH,
            SCREEN_LENGTH,
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
def test_get_square_coordinates(
    x_pixels: int, y_pixels: int, length: int, result, pointer
) -> None:
    pointer._x_pixels: int = x_pixels
    pointer._y_pixels: int = y_pixels
    pointer._length: int = length
    corners = pointer._get_square_coordinates()
    assert corners[0] == result[0]
    assert corners[1] == result[1]
    assert corners[2] == result[2]
    assert corners[3] == result[3]


@pytest.mark.parametrize(
    "x_pixels, y_pixels, length", [(300, 200, 600), (500, 150, 150)]
)
def test_get_square_coordinates_valueerror_out_of_bounds(
    x_pixels: int, y_pixels: int, length: int, pointer
) -> None:
    with pytest.raises(ValueError):
        pointer._x_pixels: int = x_pixels
        pointer._y_pixels: int = y_pixels
        pointer._length: int = length
        pointer._get_square_coordinates()


def test_random_movement(mocker, pointer) -> None:
    mocker.patch(
        "happyboss.move.Pointer._get_random_coordinates",
        return_value=(mocker.Mock(), mocker.Mock()),
    )
    side_effects_by_moveTo = [None, None, None, None, KeyboardInterrupt]
    mocked_moveTo = mocker.patch(
        "happyboss.move.moveTo",
        side_effect=side_effects_by_moveTo,
    )
    mocker.patch("happyboss.move.sleep")

    pointer._random_movement()

    assert mocked_moveTo.call_count == len(side_effects_by_moveTo)


def test_squared_movement(mocker, pointer) -> None:
    mocker.patch(
        "happyboss.move.Pointer._get_square_coordinates",
        return_value=((mocker.Mock(), mocker.Mock()) for i in range(4)),
    )
    side_effects_by_moveTo = [None, None, None, KeyboardInterrupt]
    mocked_moveTo = mocker.patch(
        "happyboss.move.moveTo",
        side_effect=side_effects_by_moveTo,
    )
    mocker.patch("happyboss.move.sleep")

    pointer._squared_movement()

    assert mocked_moveTo.call_count == len(side_effects_by_moveTo)


@pytest.mark.parametrize(
    "movement, movement_method",
    [("random", "_random_movement"), ("square", "_squared_movement")],
)
def test_move_the_mouse_pointer(movement, movement_method, mocker, pointer) -> None:
    mocked_movement_method = mocker.patch(f"happyboss.move.Pointer.{movement_method}")
    pointer._movement = movement
    pointer.move_the_mouse_pointer()
    mocked_movement_method.assert_called_once()


def test_move_the_mouse_pointer_for_new_kind_of_movement(pointer) -> None:
    with pytest.raises(KeyError):
        pointer._movement = "triangle"
        pointer.move_the_mouse_pointer()

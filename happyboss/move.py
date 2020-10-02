"""Interact with Pointer"""

from typing import Tuple
from random import randrange

from pyautogui import size, moveTo


class Pointer:
    def __init__(
        self,
        movement: str = "random",
        length: int = 100,
        sleep_time: int = 30,
        motion_time: int = 0,
    ):
        self._movement: str = movement
        self._length: int = length
        self._sleep_time: int = sleep_time
        self._motion_time: int = motion_time
        self._x_pixels: int
        self._y_pixels: int
        self._x_pixels, self._y_pixels = size()
        self._x_center: int = self._x_pixels // 2
        self._y_center: int = self._y_pixels // 2

    def _get_random_coordinates(self) -> Tuple[int, int]:
        random_x_pixel: int = randrange(start=0, stop=self._x_pixels)
        random_y_pixel: int = randrange(start=0, stop=self._y_pixels)
        return random_x_pixel, random_y_pixel

    def _get_square_coordinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        half_length: int = self._length // 2
        return (
            (self._x_center - half_length, self._y_center - half_length),
            (self._x_center + half_length, self._y_center - half_length),
            (self._x_center + half_length, self._y_center + half_length),
            (self._x_center - half_length, self._y_center + half_length),
        )

    def _move_pointer(self, x_coordinate: int, y_coordinate: int) -> None:
        moveTo(x=x_coordinate, y=y_coordinate, duration=self._motion_time)

    def move_the_mouse_pointer(self) -> None:
        try:
            pass
        except KeyboardInterrupt:
            pass

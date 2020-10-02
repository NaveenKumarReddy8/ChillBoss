"""Interact with Pointer"""

from typing import Tuple, Callable
from random import randrange
from time import sleep

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

    def _random_movement(self) -> None:
        while True:
            try:
                x_move_to: int
                y_move_to: int
                x_move_to, y_move_to = self._get_random_coordinates()
                self._move_pointer(x_coordinate=x_move_to, y_coordinate=y_move_to)
                sleep(self._sleep_time)
            except KeyboardInterrupt:
                break

    def _squared_movement(self):
        corners = self._get_square_coordinates()
        while True:
            try:
                for corner in corners:
                    x_move_to: int
                    y_move_to: int
                    x_move_to, y_move_to = corner
                    self._move_pointer(x_coordinate=x_move_to, y_coordinate=y_move_to)
                    sleep(self._sleep_time)
            except KeyboardInterrupt:
                break

    def move_the_mouse_pointer(self) -> None:
        try:
            movement_method: Callable = {
                "random": self._random_movement,
                "square": self._squared_movement,
            }[self._movement]()
        except KeyError:
            raise

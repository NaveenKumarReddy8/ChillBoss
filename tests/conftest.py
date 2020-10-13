import sys

import pytest

SCREEN_WIDTH: int = 1000
SCREEN_LENGTH: int = 750


class BogusPyautoguiModule:
    @staticmethod
    def size(*args, **kwargs):
        return SCREEN_WIDTH, SCREEN_LENGTH

    @staticmethod
    def moveTo(*args, **kwargs):
        return None


@pytest.fixture(autouse=True)
def mock_pyautogui(monkeypatch):
    monkeypatch.setitem(sys.modules, "pyautogui", BogusPyautoguiModule)

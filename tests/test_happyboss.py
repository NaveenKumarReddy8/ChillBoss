def test_version():
    # Importing happyboss inside the test function to register the bogus
    # pyautogui class before actual pyautogui module gets loaded to sys modules.
    from happyboss import __version__

    assert __version__ == "0.1.0"

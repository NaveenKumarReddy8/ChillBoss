def test_version():
    # Importing chillboss inside the test function to register the bogus
    # pyautogui class before actual pyautogui module gets loaded to sys modules.
    from chillboss import __version__

    assert __version__ == "0.4.0"

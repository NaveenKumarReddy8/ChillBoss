"""Control the execution of program flow."""

import argparse

allowed_movements: tuple = ("random", "square")

parser = argparse.ArgumentParser(
    description="Accept command line arguments for making the boss happy"
)



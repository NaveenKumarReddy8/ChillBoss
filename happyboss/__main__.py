import click

from happyboss.move import Pointer


@click.command()
@click.option(
    "--movement",
    type=click.Choice(["random", "square"], case_sensitive=False),
    default="random",
    help="type of movement of mouse pointer.",
)
@click.option(
    "--length",
    type=int,
    default=None,
    help="custom length of the side of square during square movement.",
)
@click.option(
    "--sleeptime",
    type=int,
    default=30,
    help="amount of sleep time till next movement.",
)
@click.option(
    "--motiontime",
    type=int,
    default=0,
    help="amount of sleep time till next movement.",
)
def chill(motiontime, sleeptime, length, movement):
    if length:
        obj = Pointer(
            movement=movement,
            length=length,
            sleep_time=sleeptime,
            motion_time=motiontime,
        )
    else:
        obj = Pointer(movement=movement, sleep_time=sleeptime, motion_time=motiontime)
    obj.move_the_mouse_pointer()


if __name__ == "__main__":
    chill()

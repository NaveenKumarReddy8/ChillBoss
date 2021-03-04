import logging
import sys

# Using custom logger.
logger: logging.Logger = logging.getLogger("chillboss")

# Creating SteamHandler to log to console.
handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)

# Custom formatter.
formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

# Retaining the log level to Warning.
logger.setLevel(logging.WARNING)

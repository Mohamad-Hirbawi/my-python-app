import logging
import os

def setup_logger(env):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if env == "dev" else logging.ERROR)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG if env == "dev" else logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

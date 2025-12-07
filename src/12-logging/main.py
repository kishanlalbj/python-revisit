from logger import logging


def add(a, b):
    try:
        logging.info(f"Addtion is happening for {a} and {b}")
        return a + b
    except Exception as e:
        logging.error(f"Error performing addition {e}")


add(4, "5")

logging.debug("This is debug message")

logging.info("This is info")

logging.error("This is a error")

logging.warning("This is a warning")

logging.critical("THis is a critical message")
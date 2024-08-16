import logging


def main() -> None:
    """Main entrypoint of package"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.info("Hello World")

    # Do some stuff ..

    return

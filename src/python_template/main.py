import logging

from python_template.models import Config

logger = logging.getLogger(__name__)


def setup_logging(config: Config):
    """Configure logging for the application"""

    # NOTE: For libraries, use default logging config.
    # For applications, customize logging.

    logging.basicConfig(
        level=config.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:
    """Main entrypoint of package"""

    config = Config()

    # setup_logging(config)

    logger.info(config)

    logger.info("Hello World")

    # Do some stuff ..

    return


if __name__ == "__main__":
    main()

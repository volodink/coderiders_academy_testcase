import argparse
from loguru import logger

from app import Application


def main():
    parser = argparse.ArgumentParser(description='code.riders academy test case 3. Elevators, elevators everywhere.')
    parser.add_argument('-v', action='store_true', help='Be more verbose.')
    args = vars(parser.parse_args())
    is_verbose = args['v']

    if is_verbose:
        logger.add("log/task03_{time}.log", format="{time} {level} {message}", rotation="64KB")
        logger.info("Verbosity level increased.")
    else:
        # no argument, so we should remove logger to stop logging at all.
        logger.remove()

    logger.info("Creating application...")
    app = Application()
    logger.success("Creating application... done")

    logger.info("Running application...")
    app.run()

    print("\nHave a nice day :)")
    logger.warning("Have a nice day :)")


if __name__ == "__main__":
    main()

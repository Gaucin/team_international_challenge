from app.capture import DataCapture
from app.log import logger


if __name__ == "__main__":
    capture = DataCapture()
    logger.info("Capturing...")
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    logger.info("Calling build stats")
    capture.build_stats()
    numbers = capture.less(4)
    logger.info(f"{numbers} are less than 4")
    numbers = capture.between(3, 6)
    logger.info(f"{numbers} are between 3 and 6")
    numbers = capture.greater(4)
    logger.info(f"{numbers} are greater than 4")

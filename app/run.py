from app.capture import DataCapture


if __name__ == "__main__":
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()
    capture.less(4)
    capture.between(6, 3)
    capture.greater(4)
